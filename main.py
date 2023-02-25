
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien invasion")
    play_button = Button(ai_settings,screen,"Play")
    ship=Ship(ai_settings,screen)

    bullets=Group()
    aliens=Group()
    stats = GameStats(ai_settings)
    sb=ScoreBoard(ai_settings,screen,stats)
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        #watch for keyboard and mouse events.
        gf.CheckEvents(ai_settings,screen,stats,ship,aliens,bullets,play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets,aliens,screen,stats,sb, ship,ai_settings)
            gf.update_aliens(ai_settings,ship,screen,stats,aliens,bullets)

        #function for updating evrey surface of the game
        gf.UpdateScreen(ai_settings,screen,stats,sb,ship,bullets,aliens,play_button)

run_game()