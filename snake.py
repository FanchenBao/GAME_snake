import pygame
from pygame.sprite import Group
from settings import Settings
from image_source import ImageSource
from head import Head
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
	# the bodies already attached to the head
	bodies = Group()
	# the bodies NOT attached to the snake and to be eaten by the snake
	extra_bodies = Group()
	# generate a head
	head = Head(screen, ai_settings, image_source, bodies)
	
	# create the initial snake
	gf.create_initial_snake(screen, ai_settings, image_source, bodies, head)
	# create the inital extra body
	gf.create_extra_body(extra_bodies, bodies, head, screen, ai_settings, image_source)
	# use clock to control fps
	clock = time.Clock()

	# main game loop
	while True:
		gf.check_events(ai_settings)

		gf.update_head(head, extra_bodies, bodies, screen, ai_settings, image_source)
		gf.update_body(bodies)

		gf.update_screen(bodies, extra_bodies, ai_settings, screen, head)

		gf.set_fps(clock)

run_game()