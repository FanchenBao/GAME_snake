import pygame
from pygame.sprite import Group
from settings import Settings
import game_function as gf

def run_game():
	# initiate game
	pygame.init()

	ai_settings = Settings()
	screen = pygame.display.set_mode(ai_settings.screen_width, ai_settings.screen_height)
	pygame.display.set_caption("Snake")



	# main game loop
	while True:
		gf.check_events()

run_game()