import sys
import pygame
from body import Body

def create_body(screen, ai_settings, bodies):
	''' create a new snake body'''
	new_body = Body(screen, ai_settings)
	bodies.add(new_body)

def create_initial_snake(screen, ai_settings, image_source, bodies):
	new_head = Body(screen, ai_settings, image_source, 1)
	bodies.add(new_head)
	new_body = Body(screen, ai_settings, image_source, 2)
	new_body.rect.x = new_head.rect.x - ai_settings.unit
	bodies.add(new_body)

def update_body(bodies):
	''' update the location of snake body'''
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
			body.movement = 'left'
	elif event.key == pygame.K_RIGHT:
		for body in bodies.sprites():
			body.movement = 'right'
	elif event.key == pygame.K_UP:
		for body in bodies.sprites():
			body.movement = 'up'
	elif event.key == pygame.K_DOWN:
		for body in bodies.sprites():
			body.movement = 'down'
	elif event.key == pygame.K_q:
		# press 'q' to quit game
		sys.exit()

def set_fps(clock):
	''' sake speed will be controlled by frame rate'''
	clock.tick(1)

def update_screen(bodies, ai_settings, screen):
	''' draw elements onto the screen'''
	screen.fill(ai_settings.background_color)

	# draw snake body
	bodies.draw(screen)
	# for body in bodies.sprites():
	# 	body.draw()

	# display the most recently drawn screen
	pygame.display.flip()

