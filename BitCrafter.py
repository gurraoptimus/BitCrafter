import tkinter as tk
from tkinter import ttk
import webbrowser

def ascii_to_hex(text):
    return ' '.join(format(ord(char), '02x') for char in text)

def convert():
    ascii_input = entry.get()
    hex_output = ascii_to_hex(ascii_input)
    output_var.set(hex_output)

root = tk.Tk()
root.title("BitCrafter - ASCII to Hex Converter")
root.iconbitmap("icon.ico")
root.geometry("600x200")
root.resizable(False, False)

# Setting up the theme and styles
# root.tk.call("source", "azure.tcl")  # Assuming you have an azure.tcl theme file
# If you don't have the azure.tcl theme, you can use the default theme or create your own styles

# Settings button and dialog
def open_settings():
    settings_win = tk.Toplevel(root)
    settings_win.title("About BitCrafter")
    settings_win.geometry("300x380")
    settings_win.resizable(False, False)
    settings_win.configure(bg='#23272e')
    try:
        settings_win.iconbitmap("icon.ico")
    except Exception:
        pass

    ttk.Label(settings_win, text="About BitCrafter", style='TLabel', font=('Segoe UI', 12, 'bold')).pack(pady=10)
    ttk.Label(settings_win, text="ASCII to Hex Converter", style='TLabel', font=('Segoe UI', 10)).pack(pady=(5, 0))
    ttk.Label(settings_win, text="Version: 1.0.0", style='TLabel', font=('Segoe UI', 9)).pack(pady=(10, 0))
    ttk.Label(settings_win, text="Author: Gurraoptimus", style='TLabel', font=('Segoe UI', 9)).pack(pady=(10, 0))
    ttk.Label(settings_win, text="License: MIT", style='TLabel', font=('Segoe UI', 9)).pack(pady=(10, 0))
    ttk.Label(settings_win, text="GitHub:", style='TLabel', font=('Segoe UI', 9, 'bold')).pack(pady=(10, 0))
    def open_github():
        webbrowser.open_new("https://github.com/gurraoptimus/BitCrafter")

    ttk.Button(settings_win, text="BitCrafter", command=open_github, style='TButton').pack(pady=(0, 0))
    ttk.Label(settings_win, text="Built by Gurraoptimus Development", style='TLabel', font=('Segoe UI', 9, 'italic')).pack(pady=(10, 0))
    ttk.Label(settings_win, text="For more information, visit the GitHub page.", style='TLabel', font=('Segoe UI', 9)).pack(pady=(10, 0))
    ttk.Button(settings_win, text="Close", command=settings_win.destroy, style='TButton').pack(pady=10)

style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='#23272e')
style.configure('TLabel', background='#23272e', foreground='#f8f8f2', font=('Segoe UI', 10))
style.configure('TEntry', fieldbackground='#282c34', foreground='#f8f8f2', font=('Consolas', 10))
style.configure('TButton', background='#61afef', foreground='#23272e', font=('Segoe UI', 10, 'bold'))

frame = ttk.Frame(root, padding=20, style='TFrame')
frame.grid()

# Place the About button at the top right corner
about_btn = ttk.Button(root, text="About", command=open_settings, style='TButton')
about_btn.place(relx=1.0, rely=0.0, x=-20, y=20, anchor='ne')

ttk.Label(frame, text="Enter ASCII text:", style='TLabel').grid(column=0, row=0, sticky="w", pady=5)
entry = ttk.Entry(frame, width=40, style='TEntry')
entry.grid(column=1, row=0, padx=5, pady=5)

ttk.Button(frame, text="Convert", command=convert, style='TButton').grid(column=0, row=1, pady=10, sticky="w")

output_var = tk.StringVar()
ttk.Label(frame, text="Hexadecimal output:", style='TLabel').grid(column=0, row=2, sticky="w", pady=5)
ttk.Entry(frame, textvariable=output_var, width=40, state="readonly", style='TEntry').grid(column=1, row=2, padx=5, pady=5)

root.configure(bg='#23272e')
root.mainloop()