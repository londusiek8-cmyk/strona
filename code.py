import tkinter as tk
import random
import os

punkty = 0

poziom = input("Jaki chcesz poziom (latwy/sredni/trudny/mieszany)? ")

okno = tk.Tk()

if poziom == "latwy":
    r = random.randint(40, 50)
elif poziom == "sredni":
    r = random.randint(30, 40)
elif poziom == "trudny":
    r = random.randint(20, 30)
elif poziom == "mieszany":
    r = random.randint(20, 50)
else:
    print("Niepoprawny poziom!")
    okno.destroy()
    exit()

okno.title("Aim Trainer")
okno.geometry("800x600")

canvas = tk.Canvas(okno, width=800, height=600)
canvas.pack()

x = random.randint(r, 800 - r)
y = random.randint(r, 600 - r)

kolor = random.choice(["red", "yellow", "green", "purple"])

kolo = canvas.create_oval(
    x - r, y - r,
    x + r, y + r,
    fill=kolor
)


def nowy_rozmiar():
    global r

    if poziom == "latwy":
        r = random.randint(40, 50)
    elif poziom == "sredni":
        r = random.randint(30, 40)
    elif poziom == "trudny":
        r = random.randint(20, 30)
    elif poziom == "mieszany":
        r = random.randint(20, 50)


def klik(event):
    global punkty, x, y, r, kolor, kolo

    odleglosc = ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5

    if odleglosc <= r:
        punkty += 1
        print(punkty)
    else:
        punkty -= 1
        print(punkty)

    if punkty >= 20:
        print("Wygrales!")
        os.startfile("read.bat")
        okno.destroy()
        return

    if punkty < 0:
        print("Przegrales!")
        os.startfile("read.bat")
        okno.destroy()
        return

    canvas.delete(kolo)

    nowy_rozmiar()

    x = random.randint(r, 800 - r)
    y = random.randint(r, 600 - r)

    kolor = random.choice(["red", "yellow", "green", "purple"])

    kolo = canvas.create_oval(
        x - r, y - r,
        x + r, y + r,
        fill=kolor
    )


canvas.bind("<Button-1>", klik)

okno.mainloop()