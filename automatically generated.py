import tkinter as tk
import tkinter.messagebox as msgbox


program = tk.Tk()
program.title("生成reg檔")
program.geometry("300x300")

label = tk.Label(program, text="請輸入一個介於1到128的數字：")
label.pack()

input_num = tk.Entry(program, width=20)
input_num.pack()

def generate_reg_file():
    num = input_num.get()
    if not num.isdigit():
        msgbox.showerror("錯誤", "請輸入一個正整數！")
        return
    num = int(num)
    if num < 1 or num > 128:
        msgbox.showerror("錯誤", "請輸入介於1到128的數字！")
        return

 
    with open("windows_mobile_hotspot.reg", "w") as f:
        f.write('Windows Registry Editor Version 5.00\n\n')
        f.write('[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\icssvc\Settings]\n')
        f.write('"WifiMaxPeers"=dword:{:10X}'.format(num))

    msgbox.showinfo("success!","success!")

button = tk.Button(program, text="生成檔案", command=generate_reg_file)
button.pack()
program.mainloop()
