# funwithmathv2 , includes word jumble solver
# this is funwithmath

from graphics import *
from random import randrange
from buttonclass import *
from classMenu import Menu
from computations import Math

def drawMenu():
    win = GraphWin("Fun with math!", 600, 500)
    win.setCoords(0,0,12,2) #sets coordinates
    intro = Text(Point(3.5,1.60), "This program compues a \n\
the exponential form of a user\n desired base and exponent\n\
along with printing out its binary form or \n\
the number of ways k items\n \
can be selected by a pool of n items.")
    intro.setSize(11)
    intro.draw(win)
    
    baseText = Text(Point(8.5,1.75), "Enter a positive integer:")
    baseText.setSize(11)
    baseText.draw(win)

    baseInput = Entry(Point(11,1.75), 6)
    baseInput.draw(win)
    
    expText = Text(Point(8.5, 1.5), "Enter an integer\ngreater than 1:")
    expText.setSize(11)
    expText.draw(win)

    expInput = Entry(Point(11,1.5), 6)
    expInput.draw(win)

    butn1 = Button(win, Point(1.5, 1), 2, 0.3, "Calculate\nexponent")
    butn1.activate()
    butn2 = Button(win, Point(4, 1), 2, 0.3, "Find\nbinary")
    butn2.activate()
    butn3 = Button(win, Point(7, 1), 2, 0.3, "Find\nfactorial")
    butn3.activate()
    butn4 = Button(win, Point(10,1), 2, 0.3, "Combination")
    butn4.activate()
    quitbutn= Button(win, Point(10,0.4),2,0.3,"Quit")
    quitbutn.activate()
    menu = Menu(win, intro, butn1, butn2, butn3, butn4, quitbutn)
    return menu, baseInput, expInput    #returns to be able to solve computations after while loop
    

def chooseButtn(menu, baseInput, expInput):
    

    funMath = Math()

    pt = menu.win.getMouse()

    result = Text(Point(6, 0.3), "")    # creates an empty string to reset the wording later in  for loops
    result.setSize(11)
    
    while not menu.quitbutn_clicked(pt):
        
        if menu.butn1_clicked(pt):
            result.undraw()
            base = int(baseInput.getText())
            exp = int(expInput.getText())
            funMath = Math()
            notValid = True
            while notValid:
                if base<0:
                    nValid = Text(Point(6,0.3),"Not valid input")
                    nValid.setSize(11)
                    nValid.draw(menu.win)
                else:
                    if 2<=exp:
                        notValid = False

            output_exp = "Base raised to the exp(power) is: "+ str(funMath.power(base,exp))
            result.setText(output_exp)  # variable created to reset everything
            result.draw(menu.win)
            

        elif menu.butn2_clicked(pt):
            result.undraw() # undraw everytime user clicks each button and doesn't glitch
            base = int(baseInput.getText())
            exp = int(expInput.getText())
            funMath = Math()
            notValid = True
            while notValid:
                if base<0:
                    nValid = Text(Point(6,0.3),"Not valid input")
                    nValid.setSize(11)
                    nValid.draw(menu.win)
                else:
                    if 2<=exp:
                        notValid = False

            output_exp = str(base) + " in binary form is " + str(funMath.baseConversion(base, exp))

            result.setText(output_exp)
            result.draw(menu.win)

        elif menu.butn3_clicked(pt):
            result.undraw()
            base = int(baseInput.getText())
            exp = int(expInput.getText())
            funMath = Math()
            notValid = True
            while notValid:
                if base<0:
                    nValid = Text(Point(6,0.3),"Not valid input")
                    nValid.setSize(11)
                    nValid.draw(menu.win)
                else:
                    if 2<=exp:
                        notValid = False

            if base<0:
                notExist = Text(Point(6,0.3), "Factorial does not exist for\n negative numbers")
                notExist.setSize(11)
                notExist.draw(menu.win)
                notExist.undraw()

            elif base == 0:
                zeroFac = Text(Point(6,0.3), "The factorial of 0 is 1")
                zeroFac.setSize(11)
                zeroFac.draw(menu.win)
                zeroFac.undraw()

            else:
                output_Factorial = "The factorial of "+ str(base)+ " is "+ str(funMath.recur_factorial(base))
                result.setText(output_Factorial)
                result.draw(menu.win)
        elif menu.butn4_clicked(pt):
            result.undraw()
            base = int(baseInput.getText())
            exp = int(expInput.getText())
            funMath = Math()
            notValid = True
            while notValid:
                if base<0:
                    nValid = Text(Point(6,0.3),"Not valid input")
                    nValid.setSize(11)
                    nValid.draw(menu.win)
                else:
                    if 2<=exp:
                        notValid = False

            output_exp = str(funMath.combination(base, exp))
            result.setText(output_exp)
            result.draw(menu.win)
        pt = menu.win.getMouse()
    # If the Quit button is clicked
    menu.win.close()

if __name__ == "__main__":
    main()
