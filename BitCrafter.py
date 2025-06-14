import tkinter as tk
from tkinter import ttk
import webbrowser
import sys
import os

__version__ = "1.0.0"
software = "BitCrafter"
system = "Windows 10/11."
python_version = "Python 3.10."
developer = "Gurraoptimus."
copyright = "© Gurraoptimus Development."
description = "ASCII to Hex Converter"
license = "Apache License 2.0."


def ascii_to_hex(text):
    return ' '.join(format(ord(char), '02x') for char in text)

def convert():
    ascii_input = entry.get()
    hex_output = ascii_to_hex(ascii_input)
    output_var.set(hex_output)

root = tk.Tk()
root.title("BitCrafter - ASCII to Hex Converter")
try:
    root.iconbitmap("BitCrafter (2).ico")
except Exception:
    pass
root.geometry("600x200")
root.resizable(False, False)
root.configure(bg='#23272e')

def open_settings():
    settings_win = tk.Toplevel(root)
    settings_win.title("About BitCrafter")
    settings_win.geometry("300x480")
    settings_win.resizable(False, False)
    settings_win.configure(bg='#23272e')
    try:
        settings_win.iconbitmap("BitCrafter (2).ico")
    except Exception:
        pass
    settings_win.grab_set()
    settings_win.focus_set()
    ttk.Label(settings_win, text=f"{software}", style='Header.TLabel').pack(pady=10)
    ttk.Label(settings_win, text=f"{description}", style='SubHeader.TLabel').pack(pady=(10, 0))
    ttk.Label(settings_win, text=f"Version: {__version__}", style='Bold.TLabel').pack(pady=(10, 0))
    ttk.Label(settings_win, text=f"{python_version}", style='Bold.TLabel').pack(pady=(10, 0))

    ttk.Label(settings_win, text=f"System: {system}", style='Bold.TLabel').pack(pady=(10, 0))
    ttk.Label(settings_win, text=f"Developed: {developer}", style='Bold.TLabel').pack(pady=(10, 0))

    ttk.Label(settings_win, text=f"License: {license}", style='Info.TLabel').pack(pady=(10, 0))
    ttk.Label(settings_win, text="GitHub:", style='Bold.TLabel').pack(pady=(10, 0))
    def open_github():
        webbrowser.open_new("https://gurraoptimus.github.io/BitCrafter")
    ttk.Button(settings_win, text=f"{software}", command=open_github, style='Accent.TButton').pack(pady=(0, 0))
    ttk.Label(settings_win, text=f"{copyright}", style='Bold.TLabel').pack(pady=(10, 0))
    ttk.Label(settings_win, text="For more info, visit at this Website.", style='Info.TLabel').pack(pady=(10, 0))
    ttk.Button(settings_win, text="Close", command=settings_win.destroy, style='Accent.TButton').pack(pady=10)

style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#23272e')
style.configure('Header.TLabel', background='#23272e', foreground='#61afef', font=('Segoe UI', 14, 'bold'))
style.configure('SubHeader.TLabel', background='#23272e', foreground='#98c379', font=('Segoe UI', 11, 'bold'))
style.configure('Info.TLabel', background='#23272e', foreground='#f8f8f2', font=('Segoe UI', 10))
style.configure('Bold.TLabel', background='#23272e', foreground='#e06c75', font=('Segoe UI', 10, 'bold'))
style.configure('Italic.TLabel', background='#23272e', foreground='#f8f8f2', font=('Segoe UI', 9, 'italic'))
style.configure('TLabel', background='#23272e', foreground='#f8f8f2', font=('Segoe UI', 10))
style.configure('TEntry', fieldbackground='#282c34', foreground='#f8f8f2', font=('Consolas', 10))
style.configure('TButton', background='#61afef', foreground='#23272e', font=('Segoe UI', 10, 'bold'), borderwidth=0, focusthickness=3, focuscolor='#61afef')
style.configure('Accent.TButton', background='#98c379', foreground='#23272e', font=('Segoe UI', 10, 'bold'), borderwidth=0)
style.map('TButton',
    background=[('active', '#528bff')],
    foreground=[('active', '#ffffff')]
)
style.map('Accent.TButton',
    background=[('active', '#7ec07e')],
    foreground=[('active', '#23272e')]
)

frame = ttk.Frame(root, padding=20, style='TFrame')
frame.grid()

about_btn = ttk.Button(root, text="About", command=open_settings, style='Accent.TButton')
about_btn.place(relx=1.0, rely=0.0, x=-20, y=20, anchor='ne')

ttk.Label(frame, text="Enter ASCII text:", style='TLabel').grid(column=0, row=0, sticky="w", pady=5, padx=5)
entry = ttk.Entry(frame, width=40, style='TEntry')
entry.grid(column=1, row=0, padx=5, pady=5)

ttk.Button(frame, text="Convert", command=convert, style='TButton').grid(column=0, row=1, pady=10, sticky="w", padx=5)

output_var = tk.StringVar()
ttk.Label(frame, text="Hexadecimal output:", style='TLabel').grid(column=0, row=2, sticky="w", pady=5, padx=5)
ttk.Entry(frame, textvariable=output_var, width=40, state="readonly", style='TEntry').grid(column=1, row=2, padx=5, pady=5)

root.mainloop()