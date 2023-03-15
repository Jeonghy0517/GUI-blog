#블로그 데이터 DB 연결
#sqlite3 : 개발용이나 소규모 프로젝트에서 사용하는 파일 기반의 가벼운 데이터베이스 모듈
#블로그 데이터를 관리(저장, 조회, 수정, 삭제)하기 위한 목적으로 데이터베이스를 활용

#DB 생성
import sqlite3
conn = sqlite3.connect('blog.db')

#테이블 생성
c = conn.cursor() #커서 생성
c.execute('''CREATE TABLE blog (id integer PRIMARY KEY, subject text, content text, date text)''')

#데이터 입력
c.execute("INSERT INTO blog VALUES (1, '첫 번째 블로그','첫 번째 작성글입니다.','20230315')")
conn.commit()

c.execute("INSERT INTO blog VALUES (2, '두 번째 블로그','두 번째 작성글입니다.','20230315')")
conn.commit()

c.execute("INSERT INTO blog VALUES (3, '세 번째 블로그','세 번째 작성글입니다.','20230315')")
conn.commit()

#데이터 조회
c.execute('SELECT * FROM blog')
all = c.fetchall()
print(all)

#데이터베이스 접속 종료
conn.close()

#------------------------------------------------------------------------------------------------------------------
#그래픽 사용자 인터페이스 (GUI)
#tkinter : 파이썬으로 GUI 프로그램을 만들 때 사용하는 대표적인 내장 라이브러리
#PyQt5와 같은 완성도 높은 외장 라이브러리도 있지만, 간단한 수준에서 기능 구현을 위해 먼저 시도할 수 있는 라이브러리

#창 띄우기
from tkinter import *

root = Tk() #tkinter 객체(창) 생성
label = Label(root, text='Hello World!') #root 창에 lable 컴포넌트(위젯) 추가
label.pack() #label 객체를 창에 표시

root.mainloop() #root 창을 메인 루프에 태우기
                #종료되지 않고 이벤트 수신 등의 역할을 수행

#창 크기 조절
from tkinter import *

root = Tk() #tkinter 객체(창) 생성
root.geometry('300x200')
label = Label(root, text='Hello World !') #root창에 Label 컴포넌트(위젯) 추가
label.pack() #label 객체를 창에 표시

root.mainloop() #root 창을 메인 루프에 태우기
                #종료되지 않고 이벤트 수신 등의 역할을 수행

#------------------------------------------------------------------------------------------------------------------
#tkinter에서 자주 사용되는 컴포넌트
'''
리스트박스(ListBox) : 선택 가능한 사용자 선택 목록
라벨(Label) : 한 행짜리 문자열을 출력할 수 있는 컴포넌트
엔트리(Entry) : 사용자 데이터를 받을 수 있는 한 행짜리 입력 창
텍스트(Text) : 사용자 데이터를 받을 수 있는 여러 행짜리 입력 창
버튼(Button) : 클릭할 수 있는 버튼
'''

#리스트 박스 (ListBox) : 정해진 순서가 있는 여러개의 데이터를 표시하는 컴포넌트
from tkinter import *

root = Tk() #tkinter 객체(창) 생성
root.geometry('200x200')
listbox = Listbox(root) #root 창에 Listbox 컴포넌트(위젯) 추가
listbox.pack() #Listbox 객체를 창에 표시

for i in ['첫번째 요소', '두번째 요소', '세번째 요소', '네번째 요소']:
    listbox.insert(END, i) #Listbox 마지막 위치에 새로운 데이터 추가
root.mainloop() #root 창을 메인 루프에 태우기
                #종료되지 않고 이벤트 수신 등의 역할을 수행

#사용자의 선택에 따른 이벤트 생성
def event_for_listbox(event):
    print("선택되었습니다 !")

root = Tk()
root.geometry('200x200')
listbox = Listbox(root)
listbox.pack()

for i in ['첫번째 요소', '두번째 요소', '세번째 요소', '네번째 요소']:
    listbox.insert(END, i)

listbox.bind('<<ListboxSelect>>', event_for_listbox) #리스트박스 선택 시 event_for_listbox 함수 호출

root.mainloop()

#엔트리 (Entry) : 사용자 데이터를 입력 받을 수 있는 한 행짜리 입력 창
root = Tk()
root.geometry('200x200')

entry = Entry(root) #root 창에 Listbox 컴포넌트(위젯) 추가
entry.insert(0, "데이터를 입력해 주세요") #첫번째 데이터에 엔트리 입력값 저장
entry.pack() #엔트리 객체를 창에 표시

root.mainloop()

#사용자 입력에 따른 이벤트 생성 버전
def event_for_entry(event):
    print(f"사용자 입력 값은 {entry.get()} 입니다!")

root = Tk()
root.geometry('200x200')

entry = Entry(root)
entry.insert(0, "데이터를 입력해 주세요")
entry.bind("<Return>", event_for_entry) #엔트리 값 Return시 함수 호출
entry.pack()

root.mainloop()

#텍스트 (Text) : 사용자 데이터를 받을 수 있는 여러 행 짜리 입력 창
data = '''첫번째 데이터
두번째 데이터
세번쨰 데이터'''

root = Tk()
root.geometry('200x200')

text = Text(root) #root 창에 Text 컴포넌트(위젯) 추가
text.insert(1.0, data) #첫번째 데이터에 Text 입력값 저장
text.pack() #Text 객체를 창에 표시

root.mainloop()

#버튼 (Button) : 사용자의 클릭 이벤트에 따라 동작을 처리할 수 있는 버튼
def btn_click(event):
    print(f"버튼이 클릭되었습니다 !")

root = Tk()
root.geometry('200x100')

b1 = Button(root, text = '나의 첫번째 버튼') #root 창에 Text 컴포넌트(위젯) 추가
b1.bind("<Button-1>",btn_click) #버튼 클릭 시 함수 호출
b1.pack() #버튼 객체 창에 표시

root.mainloop()

#버튼 & 텍스트
def btn_click(event):
    print(f"사용자 입력 값은 : \n{text.get(1.0, END)} 입니다!")

data = '''여러줄의 데이터를 입력하고 버튼을 클릭해주세요 '''

root = Tk()
root.geometry('500x500')

text = Text(root)
text.insert(1.0, data)
text.pack()

b1 = Button(root, text = '결과값 확인')
b1.bind("<Button-1>",btn_click) #버튼 클릭 시 함수 호출
b1.pack()

root.mainloop()

#------------------------------------------------------------------------------------------------------------------
#컴포넌트 배치, 다이얼로그 창

#컴포넌트 배치
#Geometry Manager  : tkinter에서 컴포넌트를 화면에 배치하는 방식
'''
Pack : 컴포넌트들을 부모 컴포넌트에 자동 패킹하여 불필요한 공간을 자동으로 없앰
Place : 컴포넌트 위치를 절대 좌표로 위치 시킴 (창 크기와 상관 없이 위치 고정)
Grid : 컴포넌트를 테이블 레이아웃으로 배치 (엑셀처럼), 행(row),열(column) 정보 사용
'''

#방법1. Pack (상대위치) 방식으로 컴포넌트 배치
#가장 처음 선언한 pack()부터 배치
#side 파라미터로 정렬 위치 지정 (left, right, top, bottom)
#place()와 병행 사용 가능
from tkinter import *

root = Tk()
root.geometry('300x300')

#좌측 배치
buttonLeft = Button(root, width=10, text='1')
buttonLeft.pack(side='left')
#우측 배치
buttonRight = Button(root, width=10, text='2')
buttonRight.pack(side='right')
#상단 배치
buttonTop = Button(root, width=10, text='3')
buttonTop.pack(side='top')
#하단 배치
buttonBottom = Button(root, width=10, text='4')
buttonBottom.pack(side='bottom')
#중앙 배치
buttonCenter = Button(root, width=10, text='5')
buttonCenter.pack(expand=True)

root.mainloop()

#방법2. Place(절대위치) 방식으로 컴포넌트 배치
root = Tk()
root.geometry('300x300')

button1 = Button(root, width=10, text='1')
button1.place(x=30, y=30)

button2 = Button(root, width=10, text='2')
button2.place(x=50, y=50)

button3 = Button(root, width=10, text='3')
button3.place(x=100, y=100)

button4 = Button(root, width=10, text='4')
button4.place(x=200, y=100)

button5 = Button(root, width=10, text='5')
button5.place(x=200, y=150)

root.mainloop()

#방법3. Grid 방식으로 컴포넌트 배치
root = Tk()
root.geometry('300x300')

button1 = Button(root, width=10, text='1')
button1.grid(row=0,column=0)

button2 = Button(root, width=10, text='2')
button2.grid(row=0,column=1)

button3 = Button(root, width=10, text='3')
button3.grid(row=0,column=2)

button4 = Button(root, width=10, text='4')
button4.grid(row=1,column=0)

button5 = Button(root, width=10, text='5')
button5.grid(row=1,column=1)

button6 = Button(root, width=10, text='6')
button6.grid(row=1,column=2)

root.mainloop()

#다이얼로그 창
#사용자가 버튼을 클릭해서 데이터를 삭제하려할 때 메세지를 띄워 확인하거나 특정 오류가 발생 했을 때 팝업되는 알림창
#이러한 확인 창, 오류 창을 다이얼로그 창이라고 함

#확인 창
from tkinter.messagebox import *

if askyesno("확인", "정말 삭제 하시겠습니까?"):
    #Yes : True값 반환
    print('삭제되었습니다.')
else:
    #No : False값 반환
    print('삭제되지 않았습니다.')

#오류 창
from tkinter.messagebox import *
showerror("오류","오류가 발생했습니다.")

#------------------------------------------------------------------------------------------------------------------
#실행 파일 (exe) 만들기
#pyInstaller : 파이썬으로 개발한 프로그램을 실행 파일 (exe)로 만드는 외장 라이브러리
#작성한 파이썬 프로그램을 다른 사용자가 사용하려면?
'''
1. 파이썬 설치
2. 가상환경 세팅 및 관련 라이브러리 설치
3. 작성한 프로그램 전달
4. 프로그램 사용법 설명
'''

#실행파일 (exe) 형태로 프로그램을 전달 할 경우, 바로 실행 가능
#실행 절차
'''
1. CMD 접속
2. 가상 환경 활성화
3. pip install pyInstaller
4. 파이썬 파일 위치로 이동
5. pyinstaller 파이썬파일명.py 입력
6. 새롭게 만들어진 dist 폴더 안에 exe 파일 실행 확인
'''