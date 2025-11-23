# import
import tkinter as tk
import sys
import io
import requests as ftech

def run_code():
    code = teks.get("1.0", tk.END)

    code_file = open("code.py", "w")
    code_file.write(code)
    
    terminal.delete("1.0", tk.END)

    sys.stdout = mystdout = io.StringIO()

    try:
        exec(code, globals())
    except Exception as eror:
        print(f"Error: {eror}")

    output = mystdout.getvalue()
    terminal.insert(tk.END, output)

# head
window = tk.Tk()
window.config(bg="#444343")
window.title("pyCharm bajakan")
window.geometry("600x600")

# r = ftech.get("http://192.168.1.29")
# print(r.text)

# body
teks = tk.Text(window, height=15, width=70, bg="dimgray", fg="white")
teks.pack()

run = tk.Button(window, text="Run", width=20, command=run_code, bg="dimgray")
run.pack()

terminal = tk.Text(window, height=15, width=70, bg="dimgray", fg="white")
terminal.pack()

window.mainloop()
