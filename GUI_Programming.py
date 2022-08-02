from mimetypes import common_types
import tkinter as tk

window = tk.Tk()  # 창 생성
window.title("TKINTER TEST")
window.geometry("500x500+100+100")
window.resizable(False, False)

rainbow = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]

la_rain = [None]*7

def check(st):
    print(f"{st} CLICK!")

for i in range(7):
    la_rain[i] = tk.Button(window, background=rainbow[i], width=30, command=lambda x=rainbow[i]:check(x))
    la_rain[i].pack()



# def change():
#     if la1["text"] == "Hello World":
#         la1["text"] = "Goodbye World"
#         la1["fg"] = "blue"
#     else:
#         la1["text"] = "Hello World"
#         la1["fg"] = "red"

# 위젯 : 어떤 시스템을 이루는 소형 부품!
# 요소 생성 -> 창에 붙임

# la1 = tk.Label(window, text="Hello World", font=("맑은고딕", 30, "bold"), fg="red")
# la1.place(x=100, y=200)
# bu1 = tk.Button(window, text="CLICK", command=change)
# bu1.place(x=100, y=200)

tk.mainloop()  # 창 유지