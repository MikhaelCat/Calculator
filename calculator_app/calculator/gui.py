import tkinter as tk
from tkinter import ttk, messagebox
from .safe_eval import safe_eval
from .utils import format_result
import os

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор (Python)")
        self.icon_path = os.path.join(os.path.dirname(__file__), "..", "resources", "icon.ico")
        if os.path.exists(self.icon_path):
            self.iconbitmap(self.icon_path)
        self.resizable(False, False)
        self.history = []
        self._create_widgets()

    def _create_widgets(self):
        frm = ttk.Frame(self, padding=6)
        frm.grid(row=0, column=0)

        self.expr_var = tk.StringVar()
        self.result_var = tk.StringVar(value="")

        entry = ttk.Entry(frm, textvariable=self.expr_var, font=("Segoe UI", 18), justify='right', width=18)
        entry.grid(row=0, column=0, columnspan=4, pady=(0,8))
        entry.focus_set()

        result_label = ttk.Label(frm, textvariable=self.result_var, font=("Segoe UI", 12), anchor='e')
        result_label.grid(row=1, column=0, columnspan=4, sticky="we", pady=(0,8))

        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('%',4,2), ('+',4,3),
            ('(',5,0), (')',5,1), ('**',5,2), ('=',5,3),
        ]
        for (text,r,c) in buttons:
            btn = ttk.Button(frm, text=text, command=lambda t=text: self.on_button(t))
            btn.grid(row=r+1, column=c, ipadx=8, ipady=8, padx=4, pady=4)

        clear_btn = ttk.Button(frm, text="C", command=self.clear_all)
        clear_btn.grid(row=7, column=0, columnspan=2, padx=4, pady=4, ipadx=8, ipady=8)

        back_btn = ttk.Button(frm, text="←", command=self.backspace)
        back_btn.grid(row=7, column=2, padx=4, pady=4, ipadx=8, ipady=8)

        copy_btn = ttk.Button(frm, text="Copy", command=self.copy_result)
        copy_btn.grid(row=7, column=3, padx=4, pady=4, ipadx=4, ipady=8)

        self.bind_all('<Return>', lambda e: self.calculate())
        self.bind_all('<KP_Enter>', lambda e: self.calculate())

    def on_button(self, token):
        if token == '=':
            self.calculate()
            return
        self.expr_var.set(self.expr_var.get() + token)

    def calculate(self):
        expr = self.expr_var.get().strip()
        if not expr:
            return
        try:
            result = safe_eval(expr)
            result_str = format_result(result)
            self.result_var.set(f"= {result_str}")
            self.history.insert(0, f"{expr} = {result_str}")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def clear_all(self):
        self.expr_var.set("")
        self.result_var.set("")

    def backspace(self):
        self.expr_var.set(self.expr_var.get()[:-1])

    def copy_result(self):
        res = self.result_var.get()
        if res.startswith('= '):
            res = res[2:]
        self.clipboard_clear()
        self.clipboard_append(res)
