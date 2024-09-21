from tkinter import *
import AD_Home
import Homepage2


def run_program():
    user_input = text_tentk.get("1.0", "end-1c")
    if user_input == "A":
        root_login.destroy()
        AD_Home.ad_home()
    elif user_input == "2":
        root_login.destroy()
        Homepage2.homepage2()


root_login = Tk()
root_login.title("Đăng nhập")

root_login.state('zoomed')

label_dn = Label(root_login, text="ĐĂNG NHẬP BẰNG TÀI KHOẢN", font=("Arial", 25, "bold"), fg="blue")
label_dn.place(relx=0.5, rely=0.16, anchor=CENTER)  # Đặt ở phía trên cửa sổ

frame = Frame(root_login, height=350, width=450, borderwidth=3, bg="white")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Đặt khung ở giữa màn hình

label_tentk = Label(frame, text="Tài khoản", font=("Arial", 12, "bold"), fg="blue")
label_tentk.place(relx=0.1, rely=0.1)

text_tentk = Text(frame, width=44, height=1.5, borderwidth=2)
text_tentk.place(relx=0.1, rely=0.2)

label_mk = Label(frame, text="Mật khẩu", font=("Arial", 12, "bold"), fg="blue")
label_mk.place(relx=0.1, rely=0.37)

text_mk = Text(frame, width=44, height=1.5, borderwidth=2)
text_mk.place(relx=0.1, rely=0.47)

button_quenmk = Button(frame, width=12, height=1, text="Quên mật khẩu?", fg="blue")
button_quenmk.place(relx=0.693, rely=0.64)

button_dn = Button(frame, width=29, height=1, text="ĐĂNG NHẬP", font=("Arial", 14, "bold"), bg="#4682B4", fg="white",
                   command=run_program)
button_dn.place(relx=0.1, rely=0.78)

root_login.mainloop()
