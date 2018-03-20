import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf
from pygame import time

def run_game():
	# initiate game
	pygame.init()

	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Snake")

	bodies = Group()
	# create the initial body, i.e. head of snake
	gf.create_body(bodies, screen, ai_settings)
	# use clock to control fps
	clock = time.Clock()

	# main game loop
	while True:
		gf.check_events(bodies)

		gf.update_body(bodies)

		gf.update_screen(bodies, ai_settings, screen)

		gf.set_fps(clock)

run_game()