import pygame


class Ship():
    def __init__(self,ai_settigns,screen):
        self.screen=screen
        self.ai_settings=ai_settigns
        #load the image,return an surface representing the ship
        self.image=pygame.image.load('image\ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
       # self.centery=float(self.rect.centery)
        #movement flags
        self.moving_right = False
        self.moving_left =False
        #self.moving_forward= False
        #self.moving_backward= False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        elif self.moving_left and self.rect.left > 0:
            self.center -=self.ai_settings.ship_speed_factor
       # elif self.moving_forward and self.rect.top >self.screen_rect.top:
          #  self.centery -= self.ai_settings.ship_speed_factor
            #print(self.screen_rect.top)
        #elif self.moving_backward and self.rect.bottom<self.screen_rect.bottom:
          #  self.centery +=self.ai_settings.ship_speed_factor
           # print(self.screen_rect.bottom)
        self.rect.centerx=self.center
       # self.rect.centery=self.centery
    def center_ship(self):
        self.center= self.screen_rect.centerx