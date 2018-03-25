import pygame
from pygame.sprite import Group
from settings import Settings
from image_source import ImageSource
from head import Head
from button import Button
from game_stats import GameStats
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
	foods = Group()
	# generate a head
	head = Head(screen, ai_settings, image_source, bodies)
	# record game statistics
	filename = 'high_score.txt'
	stats = GameStats(filename)
	# record a list of messages that will be shown at the beginning and end of game
	msgs = []
	gf.create_msgs(msgs, stats)

	# use clock to control fps
	clock = time.Clock()

	# main game loop
	while True:
		gf.check_events(screen, ai_settings, image_source, bodies, head, foods, stats, filename)

		if ai_settings.game_active:
			gf.update_head(head, foods, bodies, screen, ai_settings, image_source, stats)
			# update the location of snake body
			bodies.update()
			# update msgs that will show when game ends
			gf.update_msgs(msgs, stats)
			# snake speed will be controlled by frame rate
			clock.tick(ai_settings.fps)
		
		else:
			if head.dead:
				# show msg when game ends
				button = Button(screen, ai_settings, msgs, True)
			else:
				# show msg before game starts
				button = Button(screen, ai_settings, msgs, False)
		gf.update_screen(bodies, foods, ai_settings, screen, head, button)

run_game()