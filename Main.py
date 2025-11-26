import tkinter as tk

def hitung():
    nama = e_nama.get()
    try:
        qty = int(e_qty.get())
        harga = int(e_harga.get())
    except:
        label_total.config(text="Input salah")
        return

    total = qty * harga
    label_total.config(text=f"TOTAL : Rp {total}")
    text.insert(tk.END, f"{nama} : {qty}, total Harga : {total}\n")

root = tk.Tk()
root.title("Mini Kasir")

tk.Label(root, text="Nama Barang:").pack()
e_nama = tk.Entry(root)
e_nama.pack()

tk.Label(root, text="Jumlah:").pack()
e_qty = tk.Entry(root)
e_qty.pack()

tk.Label(root, text="Harga:").pack()
e_harga = tk.Entry(root)
e_harga.pack()

tk.Button(root, text="TOTAL HARGA", command=hitung).pack(pady=5)

label_total = tk.Label(root, text="TOTAL : Rp 0")
label_total.pack(pady=5)

text = tk.Text(root, height=10, width=40)
text.pack(pady=5)

root.mainloop()
