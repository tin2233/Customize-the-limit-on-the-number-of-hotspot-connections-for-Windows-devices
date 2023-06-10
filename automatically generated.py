import tkinter as tk
from tkinter import messagebox
import requests
import webbrowser

def check_for_update(repo_owner, repo_name, current_version):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        release_data = response.json()
        latest_version = release_data["tag_name"]
        release_url = release_data["html_url"]
        if latest_version != current_version:
            choice = messagebox.askyesno("更新提示", f"發現新版本 ({latest_version})！是否前往 GitHub 更新？")
            if choice:
                webbrowser.open_new_tab(release_url)
        else:
            messagebox.showinfo("更新提示", "你已經是最新版本。")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("更新提示", f"檢查更新時出現錯誤: {e}")

def generate_reg_file():
    num = input_num.get()
    if not num.isdigit():
        messagebox.showerror("錯誤", "請輸入一個正整數！")
        return
    num = int(num)
    if num < 1 or num > 128:
        messagebox.showerror("錯誤", "請輸入介於1到128的數字！")
        return

    with open("windows_mobile_hotspot.reg", "w") as f:
        f.write('Windows Registry Editor Version 5.00\n')
        f.write('[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\icssvc\Settings]\n')
        f.write('"WifiMaxPeers"=dword:{:10X}'.format(num))

    messagebox.showinfo("成功!", "成功生成檔案！")

def check_update():
    check_for_update("tin2233", "Customize-the-limit-on-the-number-of-hotspot-connections-for-Windows-devices", "V1.0.1")

def show_about():
    messagebox.showinfo("關於", "版本號：V1.0.1")

program = tk.Tk()
program.title("生成reg檔")
program.geometry("300x300")

menu_bar = tk.Menu(program)
program.config(menu=menu_bar)


file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="說明", menu=file_menu)


file_menu.add_command(label="檢查更新", command=check_update)

file_menu.add_command(label="關於", command=show_about)

label = tk.Label(program, text="請輸入一個介於1到128的數字：")
label.pack()

input_num = tk.Entry(program, width=20)
input_num.pack()

button_generate = tk.Button(program, text="生成檔案", command=generate_reg_file)
button_generate.pack()

program.mainloop()
