# todo_app_final.py
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import sys
from datetime import datetime

class SplashScreen:
    """اسپلش اسکرین در ابتدای برنامه"""
    def __init__(self):
        self.splash = tk.Tk()
        self.splash.title("")
        self.splash.geometry("400x300")
        self.splash.overrideredirect(True)
        
        # مرکز صفحه
        screen_width = self.splash.winfo_screenwidth()
        screen_height = self.splash.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 300) // 2
        self.splash.geometry(f"400x300+{x}+{y}")
        
        # پس‌زمینه
        self.canvas = tk.Canvas(self.splash, width=400, height=300, highlightthickness=0)
        self.canvas.pack()
        
        # رنگ‌آمیزی - **تغییر: رنگ ساده**
        self.canvas.create_rectangle(0, 0, 400, 300, fill="#3498db", outline="")
        
        # لوگو و متن
        self.canvas.create_text(200, 100, text="📝", font=("Arial", 64), fill="white")
        self.canvas.create_text(200, 170, text="برنامه مدیریت کارها", 
                               font=("Tahoma", 20, "bold"), fill="white")  # تغییر فونت
        self.canvas.create_text(200, 200, text="در حال بارگذاری...", 
                               font=("Tahoma", 12), fill="white")
        
        # امضای توسعه‌دهنده - **تغییر: رنگ خاکستری روشن**
        self.canvas.create_text(200, 250, 
                               text="توسعه‌دهنده: مهزیار رضایی یزدی", 
                               font=("Tahoma", 10), fill="#e0e0e0")  # تغییر: رنگ ساده
        
        self.splash.update()
    
    def close(self):
        """بستن اسپلش اسکرین"""
        self.splash.destroy()

class TodoApp:
    def __init__(self, root):
        self.root = root
        
        # نمایش اسپلش اسکرین اول
        splash = SplashScreen()
        
        # تنظیم پنجره اصلی
        self.root.title("📝karGOO")
        self.root.geometry("800x600")
        
        # چاپ اطلاعات توسعه‌دهنده در کنسول
        self.print_developer_info()
        
        # بارگذاری داده‌ها
        self.todos = []
        self.selected_todo = None
        self.filename = "todos.json"
        self.load_todos()
        
        # مخفی کردن پنجره اصلی تا اسپلش بسته بشه
        self.root.withdraw()
        
        # ایجاد رابط کاربری
        self.create_widgets()
        
        # بستن اسپلش بعد از 2 ثانیه و نمایش پنجره اصلی
        self.root.after(2000, splash.close)
        self.root.after(2100, self.show_main_window)
    
    def print_developer_info(self):
        """نمایش اطلاعات توسعه‌دهنده در کنسول"""
        print("\n" + "="*60)
        print("🎯 برنامه مدیریت کارها - نسخه 1.0")
        print("👨‍💻 توسعه‌دهنده: مهزیار رضایی یزدی")
        print("📧 ایمیل: takecare661283@gmail.com")
        print("📅 تاریخ: ۱۴۰۳")
        print("="*60 + "\n")
    
    def show_main_window(self):
        """نمایش پنجره اصلی"""
        self.root.deiconify()
    
    def load_todos(self):
        """بارگذاری کارها"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.todos = json.load(f)
                print(f"✅ {len(self.todos)} کار بارگذاری شد")
            except:
                print("⚠️ خطا در خواندن فایل")
                self.todos = []
        else:
            print("📁 فایل جدید ایجاد می‌شود")
            self.todos = []
    
    def save_todos(self):
        """ذخیره کارها"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.todos, f, ensure_ascii=False, indent=2)
            print("💾 داده‌ها ذخیره شد")
            return True
        except Exception as e:
            print(f"❌ خطا در ذخیره‌سازی: {e}")
            return False
    
    def create_widgets(self):
        """ایجاد المان‌های رابط کاربری"""
        # منو
        self.create_menu()
        
        # عنوان
        title = tk.Label(
            self.root,
            text="📋 برنامه مدیریت کارهای روزانه",
            font=("Tahoma", 18, "bold"),
            fg='#2c3e50'
        )
        title.pack(pady=20)
        
        # جدول
        self.create_table()
        
        # دکمه هوشمند
        self.create_smart_button()
        
        # دکمه‌های دیگر
        self.create_other_buttons()
        
        # فوتر با امضای توسعه‌دهنده
        self.create_developer_footer()
    
    def create_menu(self):
        """ایجاد منو"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # منوی فایل
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="فایل", menu=file_menu)
        file_menu.add_command(label="خروج", command=self.root.quit)
        
        # منوی راهنما
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="راهنما", menu=help_menu)
        help_menu.add_command(label="درباره برنامه", command=self.show_about)
    
    def show_about(self):
        """نمایش پنجره درباره برنامه"""
        about_window = tk.Toplevel(self.root)
        about_window.title("درباره برنامه")
        about_window.geometry("500x350")
        about_window.resizable(False, False)
        
        tk.Label(
            about_window,
            text="📝 برنامه مدیریت کارها",
            font=("Tahoma", 18, "bold"),
            fg='#2c3e50'
        ).pack(pady=20)
        
        tk.Label(
            about_window,
            text="نسخه 1.0.0",
            font=("Tahoma", 12),
            fg='#7f8c8d'
        ).pack(pady=10)
        
        info_text = """
        یک ابزار ساده و کاربردی برای مدیریت کارهای روزانه
        
        ✨ ویژگی‌ها:
        • مدیریت کارها با اولویت‌بندی
        • دکمه هوشمند تغییر وضعیت
        • ذخیره‌سازی خودکار
        • رابط کاربری فارسی
        
        👨‍💻 توسعه‌دهنده:
        مهزیار رضایی یزدی
        
        📧 ایمیل:
        takecare661283@gmail.com
        
        ⭐ لطفاً در گیت‌هاب ستاره دهید!
        """
        
        tk.Label(
            about_window,
            text=info_text,
            font=("Tahoma", 11),
            justify=tk.LEFT,
            padx=20
        ).pack(pady=10)
        
        tk.Button(
            about_window,
            text="باشه",
            font=("Tahoma", 11),
            command=about_window.destroy
        ).pack(pady=20)
    
    def create_table(self):
        """ایجاد جدول کارها"""
        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(table_frame, columns=('id', 'task', 'status'), show='headings', height=10)
        
        self.tree.heading('id', text='شناسه')
        self.tree.heading('task', text='کار')
        self.tree.heading('status', text='وضعیت')
        
        self.tree.column('id', width=60, anchor='center')
        self.tree.column('task', width=400)
        self.tree.column('status', width=100, anchor='center')
        
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.bind('<<TreeviewSelect>>', self.on_item_selected)
        
        self.fill_table()
    
    def fill_table(self):
        """پر کردن جدول"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for todo in self.todos:
            status = "✅ انجام شده" if todo['completed'] else "⏳ در انتظار"
            self.tree.insert('', tk.END, values=(todo['id'], todo['task'], status))
    
    def on_item_selected(self, event):
        """وقتی کار انتخاب شد"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            todo_id = item['values'][0]
            
            for todo in self.todos:
                if todo['id'] == todo_id:
                    self.selected_todo = todo
                    break
            
            self.update_smart_button()
        else:
            self.selected_todo = None
            self.update_smart_button()
    
    def create_smart_button(self):
        """ایجاد دکمه هوشمند"""
        self.smart_btn = tk.Button(
            self.root,
            text="⬇️ ابتدا یک کار انتخاب کنید",
            font=("Tahoma", 12),
            bg="#95a5a6",
            fg="white",
            width=25,
            height=2,
            state="disabled",
            command=self.toggle_todo_status
        )
        self.smart_btn.pack(pady=10)
    
    def update_smart_button(self):
        """به‌روزرسانی دکمه هوشمند"""
        if self.selected_todo is None:
            self.smart_btn.config(
                text="⬇️ ابتدا یک کار انتخاب کنید",
                bg="#95a5a6",
                state="disabled"
            )
        elif self.selected_todo['completed']:
            self.smart_btn.config(
                text="↩️ لغو تکمیل این کار",
                bg="#e67e22",
                state="normal"
            )
        else:
            self.smart_btn.config(
                text="✅ تکمیل این کار",
                bg="#2ecc71",
                state="normal"
            )
    
    def toggle_todo_status(self):
        """تغییر وضعیت کار"""
        if self.selected_todo is None:
            return
        
        todo = self.selected_todo
        
        if todo['completed']:
            confirm = messagebox.askyesno("لغو تکمیل", f"آیا می‌خواهید کار '{todo['task']}' را لغو تکمیل کنید؟")
            if confirm:
                todo['completed'] = False
                message = f"کار '{todo['task']}' به وضعیت 'در انتظار' برگشت"
        else:
            confirm = messagebox.askyesno("تکمیل کار", f"آیا کار '{todo['task']}' را انجام داده‌اید؟")
            if confirm:
                todo['completed'] = True
                message = f"کار '{todo['task']}' انجام شد!"
        
        if confirm:
            self.fill_table()
            self.update_smart_button()
            self.save_todos()
            messagebox.showinfo("موفق", message)
    
    def create_other_buttons(self):
        """ایجاد دکمه‌های دیگر"""
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        tk.Button(
            button_frame,
            text="➕ اضافه کردن کار",
            font=("Tahoma", 10),
            bg="#3498db",
            fg="white",
            padx=15,
            pady=8,
            command=self.add_todo
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="🗑️ حذف کار",
            font=("Tahoma", 10),
            bg="#e74c3c",
            fg="white",
            padx=15,
            pady=8,
            command=self.delete_todo
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="📊 آمار",
            font=("Tahoma", 10),
            bg="#9b59b6",
            fg="white",
            padx=15,
            pady=8,
            command=self.show_stats
        ).pack(side=tk.LEFT, padx=5)
    
    def add_todo(self):
        """اضافه کردن کار جدید"""
        dialog = tk.Toplevel(self.root)
        dialog.title("کار جدید")
        dialog.geometry("400x200")
        
        tk.Label(dialog, text="عنوان کار:", font=("Tahoma", 12)).pack(pady=10)
        
        task_entry = tk.Entry(dialog, width=40, font=("Tahoma", 12))
        task_entry.pack(pady=10)
        
        def save_task():
            task = task_entry.get().strip()
            if task:
                new_todo = {
                    "id": len(self.todos) + 1,
                    "task": task,
                    "completed": False
                }
                self.todos.append(new_todo)
                self.fill_table()
                self.save_todos()
                dialog.destroy()
                messagebox.showinfo("موفق", "کار اضافه شد!")
        
        tk.Button(dialog, text="ذخیره", command=save_task, font=("Tahoma", 12)).pack(pady=20)
    
    def delete_todo(self):
        """حذف کار انتخاب شده"""
        if self.selected_todo is None:
            messagebox.showwarning("هشدار", "لطفاً کار مورد نظر را انتخاب کنید")
            return
        
        todo = self.selected_todo
        
        confirm = messagebox.askyesno("تأیید حذف", f"آیا مطمئنید می‌خواهید کار '{todo['task']}' را حذف کنید؟")
        
        if confirm:
            self.todos = [t for t in self.todos if t['id'] != todo['id']]
            self.selected_todo = None
            self.fill_table()
            self.update_smart_button()
            self.save_todos()
            messagebox.showinfo("موفق", "کار حذف شد!")
    
    def show_stats(self):
        """نمایش آمار"""
        total = len(self.todos)
        completed = len([t for t in self.todos if t['completed']])
        pending = total - completed
        
        if total > 0:
            progress = (completed / total) * 100
        else:
            progress = 0
        
        stats = f"""
📊 آمار کارها:
✅ کل کارها: {total}
✅ انجام شده: {completed}
⏳ در انتظار: {pending}
📈 پیشرفت: {progress:.1f}%
        """
        
        messagebox.showinfo("آمار", stats)
    
    def create_developer_footer(self):
        """ایجاد فوتر با امضای توسعه‌دهنده"""
        footer = tk.Frame(self.root, bg='#f8f9fa', relief=tk.GROOVE, bd=1)
        footer.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        
        signature = "👨‍💻 توسعه‌دهنده: مهزیار رضایی یزدی | 📧 takecare661283@gmail.com | 🎯 پروژه مدیریت کارها"
        
        tk.Label(
            footer,
            text=signature,
            font=("Tahoma", 9),
            bg='#f8f9fa',
            fg='#2c3e50',
            padx=10,
            pady=5
        ).pack()

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()