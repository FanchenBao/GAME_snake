import sys
import pygame
from body import Body

def create_body(bodies, screen, ai_settings):
	new_body = Body(screen, ai_settings)
	bodies.add(new_body)

def update_body(bodies):
	bodies.update()

def check_events(bodies):
	'''monitor user key or mouse input'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_key_down_event(event, bodies)

def check_key_down_event(event, bodies):
	''' determine action based on player keyboard input'''
	if event.key == pygame.K_LEFT:
		for body in bodies.sprites():
			body.move_left = True
			body.move_right = False
			body.move_up = False
			body.move_down = False
	elif event.key == pygame.K_RIGHT:
		for body in bodies.sprites():
			body.move_left = False
			body.move_right = True
			body.move_up = False
			body.move_down = False
	elif event.key == pygame.K_UP:
		for body in bodies.sprites():
			body.move_left = False
			body.move_right = False
			body.move_up = True
			body.move_down = False
	elif event.key == pygame.K_DOWN:
		for body in bodies.sprites():
			body.move_left = False
			body.move_right = False
			body.move_up = False
			body.move_down = True
	elif event.key == pygame.K_q:
		# press 'q' to quit game
		sys.exit()

def set_fps(clock):
	''' sake speed will be controlled by frame rate'''
	clock.tick(10)

def update_screen(bodies, ai_settings, screen):
	''' draw elements onto the screen'''
	screen.fill(ai_settings.background_color)

	# draw snake body
	bodies.draw(screen)

	# display the most recently drawn screen
	pygame.display.flip()

