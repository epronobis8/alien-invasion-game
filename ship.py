import pygame

class Ship:
    """A Class to manage the ship."""

    def __init__(self, ai_game):
        # reference to alien invasion class. gives ship access to the game in alien invasion
        """Initailize the ship and set is starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        
        #update rect object from self.x
        self.rect.x = self.x

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of center of the  screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location."""
        # this function draws the  image at the position specifiedi in rect
        self.screen.blit(self.image, self.rect)
        # pygame lets you treat all game elments like rectangles/rects to move easier
