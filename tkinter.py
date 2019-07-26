
    # Driver Code

import tkinter
# create a GUI window
root = tkinter.Tk()

# set the title
root.title("Tincture Challange")

# set the size
root.geometry("375x200")

# add an instructions label
instructions = tkinter.Label(root, text="Type in the Tincture "
                                        "of the words, and not the word text!",
                             font=('Acumina', 12))
instructions.pack()

# add a points label
pointsLabel = tkinter.Label(root, text="Press enter to start",
                            font=('Acumina', 12))
pointsLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text="Seconds left: " +
                                     str(timeleft), font=('Acumina', 12))

timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font=('Acumina', 60))
label.pack()

# add a text entry box for
# typing in tinctures
e = tkinter.Entry(root)

# run the 'startGame' function
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
