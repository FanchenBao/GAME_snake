import sys
import pygame
from body import Body

def create_body(screen, ai_settings, bodies):
	''' create a new snake body'''
	new_body = Body(screen, ai_settings)
	bodies.add(new_body)

def create_initial_snake(screen, ai_settings, image_source, bodies, head):
	for i in range(4):
		new_body = Body(screen, ai_settings, image_source, i + 2)
		new_body.rect.x = head.rect.x - ai_settings.unit * (i + 1)
		new_body.rect.y = head.rect.y
		bodies.add(new_body)

def update_head(head):
	head.update()

def update_body(bodies):
	''' update the location of snake body'''
	bodies.update()

def check_events(head):
	'''monitor user key or mouse input'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_key_down_event(event, head)

def check_key_down_event(event, head):
	''' determine action based on player keyboard input
	up = 1, right = 2, down = 3, left = 4'''
	if event.key == pygame.K_LEFT:
		head.movement = 4
	elif event.key == pygame.K_RIGHT:
		head.movement = 2
	elif event.key == pygame.K_UP:
		head.movement = 1
	elif event.key == pygame.K_DOWN:
		head.movement = 3
	elif event.key == pygame.K_q:
		# press 'q' to quit game
		sys.exit()

def set_fps(clock):
	''' sake speed will be controlled by frame rate'''
	clock.tick(4)

def update_screen(bodies, ai_settings, screen, head):
	''' draw elements onto the screen'''
	screen.fill(ai_settings.background_color)
	# draw snake head
	head.blitme()
	# draw snake body
	bodies.draw(screen)
	# for body in bodies.sprites():
	# 	body.draw()

	# display the most recently drawn screen
	pygame.display.flip()

