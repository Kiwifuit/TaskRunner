import tkinter
import turtle

cursor = turtle.Turtle()
screen = turtle.Screen()
root = tkinter.Tk()
root.withdraw()

cursor.color("white")
screen.bgcolor("black")
screen.title("SUPER DUPER MEGA COOL SPIRALS AND DRAWINGS by Kiwifruit")

startProgram = tkinter.messagebox.askyesno("Start program?", "Start program?")
if startProgram == True:
    errorMessage = tkinter.messagebox.showerror("Error", "Task Failed Successfully")
    if errorMessage == "ok":
        exit()
if startProgram == False:
    byeBye = tkinter.messagebox.showinfo("Bye Bye", "Bye Bye!")
    if byeBye == "ok":
        exit()


turtle.done()