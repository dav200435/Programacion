from tkinter import *
from tkinter import messagebox

def readFromFile():
    try:
        with open("fichero.txt", "r") as file:
            content = file.read()
            txt.delete(1.0, END)
            txt.insert(END, content)
    except FileNotFoundError:
        messagebox.showinfo("Error", "File not found!")

def writeToFile():
    content_to_write = escribir.get("1.0", END)
    with open("fichero.txt", "w") as file:
        file.write(content_to_write)
        messagebox.showinfo("Success", "Content written to file!")

def main():
    global root
    global txt
    global escribir

    root = Tk()
    root.geometry("700x350")
    root.title("File Viewer and Writer")

    # Label
    w = Label(root, text="Vista de fichero")
    w.pack()

    # Text widget for viewing
    txt = Text(root, height=5, width=52)
    txt.pack()

    # Button to read from file
    read_button = Button(root, text="Leer", command=readFromFile)
    read_button.pack()

    # Text widget for writing
    escribir = Text(root, height=5, width=52)
    escribir.pack()

    # Button to write to file
    write_button = Button(root, text="Escribir", command=writeToFile)
    write_button.pack()

    root.mainloop()

main()