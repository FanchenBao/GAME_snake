import pygame
from pygame.sprite import Group
from settings import Settings
from image_source import ImageSource
import game_functions as gf
from pygame import time

def run_game():
	# initiate game
	pygame.init()

	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Snake")

	# set up the original images of all necessary body parts
	image_source = ImageSource()
	bodies = Group()
	# create the initial body, i.e. head of snake
	gf.create_initial_snake(screen, ai_settings, image_source, bodies)
	# use clock to control fps
	clock = time.Clock()

	# main game loop
	while True:
		gf.check_events(bodies)

		gf.update_body(bodies)

		gf.update_screen(bodies, ai_settings, screen)

		gf.set_fps(clock)

run_game()