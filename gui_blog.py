#블로그 프로그램 만들기
##진행 순서##
#1. 블로그 데이터 관리 모델
#2. GUI 컴포넌트 생성
#3. GUI 컴포넌트 배치
#4. 블로그 관리 함수
#5. 프로그램 실행

#1. 블로그 데이터 관리 모델
#나만의 블로그 프로그램을 만들기 위해서 블로그 데이터를 저장하고, 읽고 쓰고 수정하는 등 관리 기능이 필요
#데이터베이스를 연동해서 사용하면 블로그 데이터를 효율적이고 체계적으로 관리 가능
import sqlite3
import time

# #블로그 목록 조회 함수
# def get_blog_list():
#     conn = sqlite3.connect('blog.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM blog")
#     result = c.fetchall()
#     conn.close()
#     return result
# get_blog_list()
#
# #신규 블로그 작성 함수
# def add_blog(subject, content): #제목 내용
#     conn = sqlite3.connect('blog.db')
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()
#     today = time.strftime('%Y%m%d') #현재 시간
#     c.execute("INSERT INTO blog (subject, content, date) VALUES (?,?,?)",
#               (subject, content, today))
#     conn.commit()
#     conn.close()
#
# #블로그 읽기 함수
# def read_blog(_id):
#     conn = sqlite3.connect('blog.db')
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()
#     c.execute("SELECT * FROM blog WHERE id=?", (_id,))
#     result = c.fetchone()
#     conn.close()
#     return result
#
# #블로그 수정 함수
# def modify_blog(_id, subject, content):
#     conn = sqlite3.connect('blog.db')
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()
#     c.execute("UPDATE blog SET subject=?, content=? WHERE id=?",
#               (subject, content, _id))
#     conn.commit()
#     conn.close()
#
# #블로그 삭제 함수
# def remove_blog(_id):
#     conn = sqlite3.connect('blog.db')
#     conn.row_factory = sqlite3.Row
#     c = conn.cursor()
#     c.execute("DELETE FROM blog WHERE id=?", (_id))
#     conn.commit()
#     conn.close()

#2. GUI 컴포넌트 생성
from tkinter import *
from tkinter.messagebox import *
from blog_data_model import *

root = Tk()                                   # tkinter 객체(창) 생성
root.title('나만의 블로그')

#컴포넌트 생성
listbox = Listbox(root, exportselection=False)    # 블로그 목록을 표시할 리스트 박스
label = Label(root, text='제목')                  # '제목' 문자열을 표시할 라벨
entry = Entry(root)                               # 제목에 해당하는 내용을 표시할 엔트리
text = Text(root)                                 # 블로그 내용을 표시할 텍스트
b1 = Button(root, text='생성')
b2 = Button(root, text='수정')
b3 = Button(root, text='삭제')

#3. GUI 컴포넌트 배치
#grid() 함수의 row는 행을 뜻하고 column은 열을 의미
#columnspan은 열을 병합하는 옵션
#sticky는 할당된 공간에서 고정되는 위치
# 컴포넌트 배치
listbox.grid(row=0, column=0, columnspan=3, sticky='ew')
label.grid(row=1, column=0)

entry.grid(row=1, column=1, columnspan=2, sticky='ew')
text.grid(row=2, column=0, columnspan=3)
b1.grid(row=3, column=0, sticky='ew')
b2.grid(row=3, column=1, sticky='ew')
b3.grid(row=3, column=2, sticky='ew')

root.mainloop() #컴포넌트 확인

#4. 블로그 관리 함수
#블로그 목록 불러오기

#블로그 행 인덱스 저장 리스트
ROW_IDS = []

def load_blog_list():
    listbox.delete(0, END)  # 리스트 박스 초기화
    blog_list = get_blog_list()  # 블로그 리스트 가져오기

    for i, blog in enumerate(blog_list):
        ROW_IDS.append(blog[0])  # 블로그 행 인덱스(ID) 저장
        listbox.insert(i, '[%s/%s/%s] %s' % (
        blog[3][:4], blog[3][4:6], blog[3][6:], blog[2]))  # 리스트 박스에 추가

#블로그 가져오기
def get_blog(event):
    _id = ROW_IDS[listbox.curselection()[0]]  # 마우스 커서가 선택한 요소의 위치(인덱스) 반환
    blog = read_blog(_id)  # 해당 위치 블로그 읽기
    entry.delete(0, END)
    entry.insert(0, blog[2])  # 엔트리에 제목 추가
    text.delete(1.0, END)
    text.insert(1.0, blog[3])  # 텍스트에 내용 추가

listbox.bind('<<ListboxSelect>>', get_blog)  # 리스트 박스에 get_blog 함수 바인딩

#생성 버튼 이벤트 함수
def btn_add(event):
    subject = entry.get().strip()  # 엔트리(제목란)에 입력한 값
    content = text.get(1.0, END).strip()  # 텍스트(내용란)에 입력한 값

    if not subject or not content:  # 제목 또는 내용이 없을 시 오류창 발생
        showerror("오류", "제목 또는 내용을 입력해 주세요")
        return
    add_blog(subject, content)  # 블로그 추가

b1.bind('<Button-1>', btn_add)  # '생성' 버튼에 btn_add 함수 바인딩

#수정 버튼 이벤트 함수
def btn_modify(event):
    sel = listbox.curselection()  # 리스트 박스 선택 값 가져오기
    if not sel:  # 선택 값이 없을 경우
        showerror("오류", "리스트를 먼저 선택해 주세요")
    else:  # 선택 값이 있을 경우
        _id = ROW_IDS[sel[0]]
    subject = entry.get().strip()  # 엔트리(제목란)에 수정한 값
    content = text.get(1.0, END).strip()  # 텍스트(내용란)에 수정한 값

    if not subject or not content:  # 제목 또는 내용이 없을 시 오류창 발생
        showerror("오류", "제목 또는 내용을 입력해 주세요")
        return

    modify_blog(_id, subject, content)  # 블로그 수정

b2.bind('<Button-1>', btn_modify)  # '수정' 버튼에 btn_modify 함수 바인딩

#삭제 버튼 이벤트 함수
def btn_remove(event):
    sel = listbox.curselection()  # 리스트 박스 선택 값 가져오기
    if not sel:
        showerror("오류", "리스트를 먼저 선택해 주세요")
        return
    else:
        _id = ROW_IDS[sel[0]]

    if askyesno("확인", "정말로 삭제하시겠습니까?"):  # 확인 창 발생
        remove_blog(_id)  # 블로그 삭제

b3.bind('<Button-1>', btn_remove)  # '삭제' 버튼에 btn_remove 함수 바인딩

#새로고침 함수
def refresh():
    ROW_IDS.clear()        # 블로그 ID 리스트 삭제
    entry.delete(0, END)   # 제목 삭제
    text.delete(1.0, END)  # 내용 삭제
    load_blog_list()       # 블로그 리스트 불러오기

#5. 프로그램 실행
load_blog_list()
root.mainloop()

