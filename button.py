import turtle

class Button:
    def __init__(self, screen, image, position):
        self.button = turtle.Turtle()
        self.screen = screen
        self.button.penup()
        self.button.speed('fastest')
        self.goto(position)
        self.image_path = image
        self.show_button()
    
    def show_button(self):
        self.screen.addshape(self.image_path)
        self.button.shape(self.image_path)
    
    def goto(self, position):
        self.button.goto(position)
    



