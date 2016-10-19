"""
Name: Chris Cook
Email: c.w.cook@live.com
Assignment: Homework 4 - Fraction Class
Due: 24 Oct @ 1:00 p.m.
"""

#Answer #1

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives
    def talk(self):
        """A cat says meow! when asked to talk."""
        print('meow!')
    def lose_life(self):
        """A cat can only lose a life if they have at least
        one life. When lives reach zero, the ’is_alive’
        variable becomes False.
        """
        if(self.lives >1 and self.is_alive):
        	self.lives -= self.lives
        else:
        	is_alive = false

#Answer #2
4
3
4
3
9
16
