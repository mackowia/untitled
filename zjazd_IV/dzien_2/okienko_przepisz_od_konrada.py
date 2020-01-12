import tkinter as tk

#slowa = ("Hi!", "Ha!", "Ho!")
#aktualne_slowo = 0

def zrob_cos():
    if label ['text'] == "Hi!":
        label.configure(text= "Ha!")
    elif label ['text'] == "Ha!":
        label.configure(text="Ho!")
    elif label ['text'] == "Ho!":
        label.configure(text="Hi!")
    tk.Button(root, text=entry.get())
    p.pack()

root = tk.Tk()
label = tk.Label(root, text="Zaraz zaczynamy...")
label.pack()
przycisk = tk.Button(root, text="Kliknij!",
                     command=zrob_cos)
przycisk.pack()
root.mainloop()