import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("برنامه مدیریت کارها")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        #فایل ذخیره سازی
        self.filename = "todos.json"

        #لیست کارها
        self.todos = []

        #بارگذاری کارهای ذخیره شده
        self.load_todos()

        #المان های رابط کاربری
        self.setup_ui()

    def setup_ui(self):
        """المان های رابط کاربری"""
        #عنوان برنامه
        title_label = tk.Label(
            self.root,
            text="برنامه مدیریت کار های روزانه",
            font=("B nazanin", 20, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        title_label.pack(pady=20)

        print("بخش 1 کامل شد : پنجره اصلی ساخته شد")
        print("دستور بعدی : ساختن فرم اضافه کردن کار")

#اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
