from tkinter import *
from PIL import Image, ImageTk
import AD_InforAccount
import AD_PassWord
import AD_CreateAccount

def ad_home():
    ad_root_homepage = Tk()
    ad_root_homepage.title("Trang chủ")
    ad_root_homepage.state("zoom")

    # Tạo canvas và scrollbar
    canvas = Canvas(ad_root_homepage, borderwidth=0)
    scrollbar = Scrollbar(ad_root_homepage, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Tạo một frame bên trong canvas với kích thước cố định
    frame_hp = Frame(canvas, width=290, height=1000, borderwidth=3, bg="#4682B4")
    canvas.create_window((0, 0), window=frame_hp, anchor='nw')

    # Đặt canvas và scrollbar vào cửa sổ chính
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Ngăn frame điều chỉnh kích thước theo các widget bên trong
    frame_hp.pack_propagate(0)

    # Cập nhật kích thước canvas khi nội dung thay đổi
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_hp.bind("<Configure>", on_frame_configure)

    def create_image(file_name, x, y):
        # Mở ảnh với Pillow
        image = Image.open(file_name)

        # Thay đổi kích thước ảnh
        resized_image = image.resize((x, y))

        # Chuyển đổi ảnh sang định dạng có thể sử dụng bởi Tkinter
        photo = ImageTk.PhotoImage(resized_image)

        return photo

    image_hp = create_image("C://Users//ASUS//Desktop//python-logo.png", 90, 90)
    image_bt = create_image("C://Users//ASUS//Desktop//python-logo.png", 50, 50)

    label_hp = Label(frame_hp, width=200, height=150, image=image_hp, anchor=CENTER,
                     borderwidth=0, bg="#4682B4")
    label_hp.pack()

    def atv_ad_button_tk():
        ad_button_ht.pack_forget()
        ad_button_ht_ctk.pack_forget()
        ad_button_ht_xtk.pack_forget()
        ad_button_ht_clmk.pack_forget()
        ad_button_ht_xlshd.pack_forget()
        ad_button_ht_pq.pack_forget()
        ad_button_dx.pack_forget()
        ad_label_none.pack_forget()

        ad_button_tk_tttk.pack(anchor='w', padx=10, pady=5)
        ad_button_tk_dmk.pack(anchor='w', padx=10, pady=5)
        ad_button_ht.pack(anchor='w', padx=10, pady=5)
        ad_button_dx.pack(anchor='w', padx=10, pady=5)
        ad_label_none.pack()

    ad_button_home = Button(frame_hp, text="    Trang chủ", font=("Arial", 14, "bold"),
                            fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    ad_button_home.pack(anchor='w', padx=10, pady=5)

    ad_button_tk = Button(frame_hp, text="    Tài khoản", font=("Arial", 14, "bold"),
                          fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt,
                          command=atv_ad_button_tk)
    ad_button_tk.pack(anchor='w', padx=10, pady=5)

    def select_ad_button_tk_tttk():
        ad_root_homepage.destroy()
        AD_InforAccount.ad_inforaccount()

    ad_button_tk_tttk = Button(frame_hp, text="    Thông tin tài khoản", font=("Arial", 14, "bold"),
                               fg="white", bg="#4682B4", borderwidth=0, compound="left",
                               image=image_bt, command=select_ad_button_tk_tttk)

    def select_ad_button_tk_dmk():
        ad_root_homepage.destroy()
        AD_PassWord.ad_password()

    ad_button_tk_dmk = Button(frame_hp, text="    Đổi mật khẩu", font=("Arial", 14, "bold"),
                              fg="white", bg="#4682B4", borderwidth=0, compound="left",
                              image=image_bt, command=select_ad_button_tk_dmk)

    def atv_ad_button_ht():
        ad_button_tk_tttk.pack_forget()
        ad_button_tk_dmk.pack_forget()
        ad_button_dx.pack_forget()
        ad_label_none.pack_forget()

        ad_button_ht_ctk.pack(anchor='w', padx=10, pady=5)
        ad_button_ht_xtk.pack(anchor='w', padx=10, pady=5)
        ad_button_ht_clmk.pack(anchor='w', padx=10, pady=5)
        ad_button_ht_xlshd.pack(anchor='w', padx=10, pady=5)
        ad_button_ht_pq.pack(anchor='w', padx=10, pady=5)

        ad_button_dx.pack(anchor='w', padx=10, pady=5)
        ad_label_none.pack()

    ad_button_ht = Button(frame_hp, text="    Hệ thống", font=("Arial", 14, "bold"),
                          fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt,
                          command=atv_ad_button_ht)
    ad_button_ht.pack(anchor='w', padx=10, pady=5)

    def select_ad_button_ht_ctk():
        ad_root_homepage.destroy()
        AD_CreateAccount.ad_createaccount()

    ad_button_ht_ctk = Button(frame_hp, text="    Cấp tài khoản", font=("Arial", 14, "bold"),
                              fg="white", bg="#4682B4", borderwidth=0, compound="left",
                              image=image_bt, command=select_ad_button_ht_ctk)

    ad_button_ht_xtk = Button(frame_hp, text="    Xóa tài khoản", font=("Arial", 14, "bold"),
                              fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)

    ad_button_ht_clmk = Button(frame_hp, text="    Cấp lại mật khẩu", font=("Arial", 14, "bold"),
                               fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)

    ad_button_ht_xlshd = Button(frame_hp, text="    Lịch sử hoạt động", font=("Arial", 14, "bold"),
                                fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)

    ad_button_ht_pq = Button(frame_hp, text="    Phân quyền", font=("Arial", 14, "bold"),
                             fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)

    ad_button_dx = Button(frame_hp, text="    Đăng xuất", font=("Arial", 14, "bold"),
                          fg="white", bg="#4682B4", borderwidth=0, compound="left", image=image_bt)
    ad_button_dx.pack(anchor='w', padx=10, pady=5)

    ad_label_none = Label(frame_hp, bg="#4682B4", borderwidth=0, height=1000)
    ad_label_none.pack()

    ad_label = Label(ad_root_homepage, text="   Trang chủ", fg="white", font=("Arial", 16, "bold"),
                     borderwidth=2, relief=RAISED, width=81, height=2, anchor='w', bg="#4682B4")
    ad_label.place(x=282, y=0)

    ad_label_content = Label(ad_root_homepage, text="  PHẦN MỀM ĐỘC HẠI",
                             fg="blue", font=("Arial", 16, "bold"),
                             borderwidth=2, relief=RAISED, width=81, height=30, anchor=CENTER)
    ad_label_content.place(x=282, y=50)

    ad_root_homepage.mainloop()
