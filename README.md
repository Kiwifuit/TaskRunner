Project Documentation? I dunno
----------------------------------

So, apparently, I forgot about this project, and I decided to give it another run.<sup>(note: I left this project in the shelves of my hard drive's memory for days by now)</sup>

Day One
--------
So, first off, I have to import tkinter, do some blah-blah-blah, this is what the code looks like rn:
```py
from tkinter import *

root = Tk()

startProgram = tkinter.messagebox.askyesno("Start Program", "Start Program?")

root.mainloop()
```
ngl that seems unimpressive. Also, I have no fucking idea wether or not this shit will work. <sup>Epic forshadowing</sup>

well fuck...<br>
<img src="markdown images/nice.png"><br>
and...<br>
<img src="markdown images/double nice.png">

If your weenie 'lil brainy there tryna scratchy scratchy,
tryna wonder wtf is wrong with this shit, VS Code is making me scratch my head by slapping me with an error
then just say tell me that the error is both wrong and right, `True` or `False`. Either I'm stupid bc I'm a noob, or something's going on with this thing. But for now, I think I *miiiiiiiiiiiight* need Turtle...

So I turned my tkinter project into a turtle one...
-----------------------------------------------------
Yes, you fucking seen the title right, I wiped the sript clean for the **third time** yay to me.

I actually have a reason for doing this.

1) All this shit i have tried only with both the `Turtle` and `Tkinter` modules present.
2) Makes the prank more convincing, and takes a long time for ppl to realize that this shit was a prank lmfao

So I did the basic code:
```py
import tkinter
import turtle

cursor = turtle.Turtle()
screen = turtle.Screen()


turtle.done()
```
Then add the `root` variable:
```py
import tkinter
import turtle

cursor = turtle.Turtle()
screen = turtle.Screen()
root = tkinter.Tk()


turtle.done()
```
Then add both the turtle (`cursor` here) and the screen customizations<br>(i.e. window title, background color, turtle color, etc.):
```py
import tkinter
import turtle

cursor = turtle.Turtle()
screen = turtle.Screen()
root = tkinter.Tk()

cursor.color("white")
screen.bgcolor("black")
screen.title("SUPER DUPER MEGA COOL SPIRALS AND DRAWINGS by Kiwifruit")

turtle.done()
```
and when we run it...<br>
<img src="markdown images/YES.png">

YES, WE FUCKING DID IT &nbsp;&nbsp;<sup>or at least *I* did, you are just reading this shit on GitHub</sup>

So, I did it (in what looks like) first try...
----------------------------------------------------
So, Yay to me I guess.

Continuing on, all I have to do next is `withdraw()` the parent variable (`root` here), so it won't show up and shit<br>
(side note: I renamed the file from `what-the.md` to `documentation.md`, this , might be the final name for this file I dunno):
```py
import tkinter
import turtle

cursor = turtle.Turtle()
screen = turtle.Screen()
root = tkinter.Tk()
root.withdraw()

cursor.color("white")
screen.bgcolor("black")
screen.title("SUPER DUPER MEGA COOL SPIRALS AND DRAWINGS by Kiwifruit")

turtle.done()
```
If you are wondering, I placed the `root.withdraw()` function right below `root = tkinter.Tk()` so that you can't see the tk window, since it makes it then hides it a few lines later, you would be able to see it. Putting the `root.withdraw()` was a quick fix to that disease

And we have another problem: I wanted to make the hidden window close after the turtle window closes, but that doesnt happen, instead, only the turtle window closes. And I need to find a fix for that...


Anyways, I added the prompt thingy and now the code looks like this:
```py
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

turtle.done()
```

Since `tkinter.messagebox.askyesno()` returns a bool (a `True` or `False` thingy), I can just add `if` satements, since we do not have that much uncertainty, and now the code looks like this:
```py
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
```
For the non-nerds/people who don't understand code:

starting from the `startProgram` variable, the program makes a prompt, asking the user wether or not to start the program, if the user clicks on "yes", which returns `True` in Python, it will make an error message, as a sort of "prank" or something, if the user clicks on "no" for some reason, which returns `False`, it will make a prompt that says "Bye Bye" and if the prompt returns an `"ok"`, which means the user either clicked the `x` on the corner or clicked the "Ok" button, the program will close. Same goes for the `if errorMessage == "ok"` thing, except more comedy points for me.


Also, remember this earlier?

>And we have another problem: I wanted to make the hidden window close after the turtle window closes, but that doesnt happen, instead, only the turtle window closes. And I need to find a fix for that...

Apparently, this problem got fixed when I wrote the final lines of code, but I do not know what line exactly fixed this, since I did not test my code after I did the explanaition above. Maybe it has to do with the `exit()` function. I dunno. But hey, at least it is now fixed, which is better


And so is the end of my documentation...
-----------------------------------------
To be honest, I never thought I'd be able to finish this project without standing up for a break, it's very hot here, as I am typing this shit out, at least...

Anyways, thank you so much for going to this GitHub repo and take your time to read this shit. Should I keep the "Day One" thing on the file? Yeah, I should, just because I want to.

This whole file is about 176 lines long, so I really am happy that you checked this repo out...

You can also run the script for yourself, or download the final product at both [my website](e3.mahkiwi123.repl.co/downloads.html) or at this repo, I will put up the executable when I am done with everything

Oh yeah, If you are wondering how I made these markdown files or pretty much any file that ends with .md, it's as easy as [Discord's formatting system for messages](), with some modifications...

Again, tysm for visiting this repo, and even reading the whole `documentation.md` file. Have a great day!
