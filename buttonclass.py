
from graphics import *

class Button:

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button in a graphical window (win) with the words (label) in it
    located in Point centerPt and with height being how tall the button is and
    width being how wide the button is. e.g. myButton = Button(myWin, "quit", Point(300,300), 50, 100)"""
        x, y  = center.getX(), center.getY()
        self.xmin = x - width / 2
        self.xmax = x + width / 2
        self.ymin = y - height / 2
        self.ymax = y + height / 2
        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(pt1, pt2)
        self.rect.draw(win)
        self.words = Text(center, label)
        self.words.draw(win)
        self.rect.setFill("lightgray")
        self.activate()

    def activate(self):
        """ Set This button to be enabled/active"""
        self.words.setFill("black")
        self.rect.setWidth(2)
        self.active =  True

    def deactivate(self):
        """Sets this button to 'inactive' """
        ## color the text dark gray
        self.words.setFill("darkgrey")
        ## set the outline of button to be thinner
        self.rect.setWidth(1)
        ## set the boolean active flag to be false
        self.active = False

    def isClicked(self, pt):
        """Returns True of button active and Point is inside, else returns False"""
        if self.active and \
           self.xmin <= pt.getX() <= self.xmax and \
           self.ymin <= pt.getY() <= self.ymax:
            return True
        else:
            return False

if __name__ == "__main__":
    main()
