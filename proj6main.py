# main menu
#Danna and Marta(Wanjiru)
# Programming assignment 6 due May 3
from graphics import *
from buttonclass import *
from wordJumblesolver import *
from random import randrange
from classMenu import Menu
from computations import Math
from gwindowMath import *


def mainMenu():
    win = GraphWin("Main", 600, 600)
    win.setCoords(0, 0, 12, 2)

    startText = Text(Point(6,1.5), "Hello, this program allows the user to\n choose between\n two activities to \
either do a word jumble solver\n or do math calculations.\n\
Click on either word solver or fun math\n to run the activities :):")
    startText.setFill("purple")
    startText.draw(win)

    buttn1 = Button(win, Point(2, 1), 2, 0.3, "Word\nSolver")

    buttn2 = Button(win, Point(10, 1), 2, 0.3, "Fun\nMath")
    
    quitButtn = Button(win, Point(10, .3), 2, 0.3, "Quit")
    quitButtn.activate()

    pt = win.getMouse()

    while not quitButtn.isClicked(pt):
        if buttn1.isClicked(pt):
            win2 = GraphWin("wordJumbleSolver!", 600, 500)
            win2.setCoords(0,0,12,2)
            intro = Text(Point(3.5,1.60), "This program generates all\n\
anagrams of a word found \n in the dictionary being used as \na reference in this program\
and prints\n out all the words generated.")
            intro.setSize(11)
            intro.draw(win2)
            wordText = Text(Point(8.5,1.75), "Enter a word:")
            wordText.setSize(11)
            wordText.draw(win2)
            wordInput = Entry(Point(11,1.75), 6)
            wordInput.draw(win2)

            words = Text(Point(5, 0.4), "")
            words.setFill("dark green")
            words.setSize(14)
            words.draw(win2)
            butn4 = Button(win2, Point(2, 1), 2, 0.3, "anagrams")
            quitButton = Button(win2, Point(6, 1), 2, 0.3, "quit")
            pt = win2.getMouse()
            while not quitButton.isClicked(pt):
                if butn4.isClicked(pt):
                    ans = wordSolver(wordInput.getText())
                    if len(ans) == 0:#check if the anagram is not found in the dictionary
                        words.setText("Anagram not in ditctionary")

                    else:
                        words.setText(str(ans))#returns the anagrams 

            
                pt = win2.getMouse()
            win2.close()
            

        elif buttn2.isClicked(pt):
            menu, baseInput, expInput = drawMenu()
            option = chooseButtn(menu, baseInput, expInput)

        else:
            err = Text(Point(6,.5), "Please click one of the buttons above.")
            err.setSize(13)
            err.setFill("red")  # Warning to user to click on one of the two options
            err.draw(win)
            
        pt = win.getMouse()

    win.close()


mainMenu()
