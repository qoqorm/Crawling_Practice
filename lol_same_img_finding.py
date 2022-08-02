from email import message
import imghdr
from pydoc import cli
import tkinter as tk
from PIL import ImageTk
from time import sleep, time
import os
from random import sample, shuffle
from tkinter import messagebox

N=4
window = tk.Tk()

window.title("롤 같은 그림 맞추기 게임")
window.geometry("500x500+300+300")
window.resizable(False, True)

champs = os.listdir("롤아이콘") # 롤아이콘 하위의 파일 이름들의 리스트 반환
quizs = sample(champs, N**2//2)*2
quizs[1] = "아리(ahri).png"
quizs[9] = "아리(ahri).png"
shuffle(quizs)

logo = ImageTk.PhotoImage(file="league-of-legends.png")

photo = [None] * N**2
button = [None] * N**2

clicklist = []
correctlist = []

def check(x):
    if not x in clicklist:
        clicklist.append(x)
        button[x]["image"] = photo[x]

    if len(clicklist) == 2:
        if quizs[clicklist[0]] == quizs[clicklist[1]]:
            button[clicklist[0]]["state"] = "disabled"
            button[clicklist[1]]["state"] = "disabled"
            correctlist.append(clicklist[0])
            correctlist.append(clicklist[1])
            if len(correctlist) == N**2:
                t = time() - starttime
                messagebox.showinfo("CLEAR", f"{round(t,2)} 초만에 성공했습니다!")
                exit()
        else:
            window.update()
            sleep(1)
            print("FAIL :(")
            button[clicklist[0]]["image"] = logo
            button[clicklist[1]]["image"] = logo
        clicklist.clear()

def hint_one():
    for i in range(N**2):
        if not i in correctlist:
            button[i]["image"] = photo[i]
    window.update()
    sleep(2)
    for i in range(N**2):
        if not i in correctlist:
            button[i]["image"] = logo
    hint1["state"] = "disabled"

for i in range(N**2):
    photo[i] = ImageTk.PhotoImage(file=f"롤아이콘/{quizs[i]}")
    button[i] = tk.Button(window, image=photo[i], command=lambda x=i:check(x))
    button[i].pack()

for i in range(N):
    for j in range(N):
        button[N*i+j].place(x=i*69, y=j*69)


hint1 = tk.Button(window, text="전체 뒤집기", font=("맑은고딕", 15, "bold"), command=hint_one)
hint1.place(x=N*64 + 50, y=50)

messagebox.showinfo("GAMESTART", "확인을 누르면 게임이 시작됩니다.")

starttime = time()
print(starttime)

for i in range(N**2):
    button[i]["image"] = logo

# garen = ImageTk.PhotoImage(file="롤아이콘/가렌(garen).png")
# la1 = tk.Label(window, image=garen)
# la1.pack()

tk.mainloop()





#- 1 : 32 : 30