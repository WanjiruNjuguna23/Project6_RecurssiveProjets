#classMenu
##class Menu:
##    def __init__(self, win, prompt, butn1, butn2, butn3):
##        self.win = win
##        self.prompt = prompt
##        self.butn1 = butn1
##        self.butn2 = butn2
##        self.butn3 = butn3
##
##    def setprompt(self, text):
##        self.prompt.setText(text)
##
##    def butn1_clicked(self, pt):
##        return self.butn1.isClicked(pt)
##
##    def butn2_clicked(self, pt):
##        return self.butn2.isClicked(pt)
##
##    def butn3_clicked(self, pt):
##        return self.butn3.isClicked(pt)
##
##    def button_clicked(self, pt):
##        return self.butn1.isClicked(pt) or self.butn2.isClicked(pt) or self.butn3.isClicked(pt)
##
##    def deactivate_butns(self):
##        self.butn1.deactivate()
##        self.butn2.deactivate()
##        self.butn3.deactivate()
##
##    def getMouse(self):
##        return self.win.getMouse()
##
##    def close(self):
##        return self.win.close()


#classMenu
class Menu:
    def __init__(self, win, prompt, butn1, butn2, butn3, butn4, quitButton):
        self.win = win
        self.prompt = prompt
        self.butn1 = butn1
        self.butn2 = butn2
        self.butn3 = butn3
        self.butn4 = butn4
        self.quitButton = quitButton

    def setprompt(self, text):
        self.prompt.setText(text)

    def butn1_clicked(self, pt):
        return self.butn1.isClicked(pt)

    def butn2_clicked(self, pt):
        return self.butn2.isClicked(pt)

    def butn3_clicked(self, pt):
        return self.butn3.isClicked(pt)

    def butn4_clicked(self, pt):
        return self.butn4.isClicked(pt)

    def quitbutn_clicked(self, pt):
        return self.quitButton.isClicked(pt)

    def button_clicked(self, pt):
        return self.butn1.isClicked(pt) or self.butn2.isClicked(pt) or self.butn3.isClicked(pt) or self.butn4.isClicked(pt) or self.quitButton.isClicked(pt)

    def deactivate_butns(self):
        self.butn1.deactivate()
        self.butn2.deactivate()
        self.butn3.deactivate()

    def getMouse(self):
        return self.win.getMouse()

    def close(self):
        return self.win.close()
if __name__ == "__main__":
    main()
