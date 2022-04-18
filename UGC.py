import tkinter as tk

gasPrice_Converted = 0
tankLevel_Converted = 0
total = 0

# Window
window = tk.Tk()
window.minsize(300, 300)
window.maxsize(300, 300)
window.title("UGC")
window.iconbitmap("./Assets/Icon.ico")

# Header
header = tk.Label(
    text = "Unturned Gas Calculator",
    fg = "black",
    bg = "#F0F0F0",
    width = "500",
    height = "2"
    ).pack()


# Gas Price
tk.Label(text = "Gas Price:").place(x = 15, y= 50)
gasPrice = tk.StringVar()

tk.Entry(window, textvariable = gasPrice).place(x = 15, y = 80)

# Tank Level
tk.Label(text = "Tank Level:").place(x = 15, y = 110)
tankLevel = tk.StringVar()

tk.Entry(window, textvariable = tankLevel).place(x = 15, y = 140)



# Total Price
tk.Label(text = "Total Price:").place(x = 160, y = 50)
totalPrice = tk.StringVar()

tk.Entry(window, textvariable = totalPrice).place(x = 160, y = 80)


def calculate():

    global gasPrice
    global gasPrice_Converted

    global tankLevel
    global tankLevel_Converted

    global total
        

    gasPrice_Converted = float(gasPrice.get())
    
    tankLevel_Converted = float(tankLevel.get())

    tankLevel_Converted = 100 - tankLevel_Converted

    total = tankLevel_Converted * gasPrice_Converted

    totalPrice.set(total)

# Ok Button
okButton = tk.Button(
    text = "OK",
    fg = "black",
    bg = "white",
    width = "10",
    height = "1",
    command = calculate
    ).place(x = 105, y = 260)


window.mainloop()