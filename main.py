# import the modules
import tkinter
import random

# list of possible tinctures.
tinctures = ['Red', 'Blue', 'Green', 'Pink', 'Black',
             'Yellow', 'Orange', 'White', 'Purple', 'Brown', 'Violet']
points = 0

# the game time left, initially 60 seconds.
timeleft = 60


# function that will start the game.
def startGame(event):
    if timeleft == 60:
        # start the countdown timer.
        countdown()

    # run the function to
    # choose the next tincture.
    afterthisTincture()


# Function to choose and
# display the next tincture.
def afterthisTincture():
    # use the globally declared 'points'
    # and 'play' variables above.
    global points
    global timeleft

    # if a game is currently in play
    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # if the tincture typed is equal
        # to the tincture of the text
        if e.get().lower() == tinctures[1].lower():
            points += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(tinctures)

        # change the tinctures to type, by changing the
        # text _and_ the tinctures to a random tincture value
        label.config(fg=str(tinctures[1]), text=str(tinctures[0]))

        # update the points.
        pointsLabel.config(text="Points: " + str(points))


# Countdown timer function
def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:
        # decrement the timer.
        timeleft -= 1

        # update the time left label
        timeLabel.config(text="Time left: "
                              + str(timeleft))

        # run the function again after 1 second.
        timeLabel.after(1000, countdown)

    # Driver Code


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
