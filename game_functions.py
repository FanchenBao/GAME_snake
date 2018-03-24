import sys
import pygame
from body import Body
from random import randint

def create_initial_snake(screen, ai_settings, image_source, bodies, head):
	new_body = Body(screen, ai_settings, image_source, 1)
	new_body.rect.x = head.rect.x - ai_settings.unit
	new_body.rect.y = head.rect.y
	# default starting dir = 2 (snake going to the right at beginning)
	new_body.dir = 2
	bodies.add(new_body)

def create_extra_body(extra_bodies, bodies, head, screen, ai_settings, image_source):
	''' create an extra body for snake to eat'''
	extra_body = Body(screen, ai_settings, image_source, (len(bodies) + 1))
	# locate the extra body anywhere on the screen except where the snake is
	while True:
		# flag to detect whether the extra body overlaps with the snake
		overlap = False
		# extra body position is random
		extra_body.rect.x = ai_settings.x_axis[randint(0, ai_settings.x_ticks - 1)]
		extra_body.rect.y = ai_settings.y_axis[randint(0, ai_settings.y_ticks - 1)]
		# check overlap with head
		if head.rect.x == extra_body.rect.x and head.rect.y == extra_body.rect.y:
			continue
		else:
			# check overlap with body
			for body in bodies.sprites():
				if body.rect.x == extra_body.rect.x and body.rect.y == extra_body.rect.y:
					overlap = True
					break
			if overlap:
				continue
			# when no overlap occurs, include the extra body in game
			else:
				extra_bodies.add(extra_body)
				return

def update_head(head, extra_bodies, bodies, screen, ai_settings, image_source):
	''' update current head position, consider the situation where head eats an extra body, or head bumps into its own body, or head bumps into obstacle'''
	head.update()
	eaten_body = pygame.sprite.spritecollideany(head, extra_bodies)
	# detect whether head collide with extra body
	if eaten_body:
		# collide happens, remove extra body from extra bodies group
		extra_bodies.remove(eaten_body)
		for body in bodies.sprites():
			# find the last body of snake
			if body.index == len(bodies):
				# copy key parameters from last body to the newly eaten body
				copy_parameters(eaten_body, body)
				# depending on the last body's current dir, set eaten body's coordinate
				if body.dir == 1:
					eaten_body.rect.y = body.rect.y + ai_settings.unit
				if body.dir == 3:
					eaten_body.rect.y = body.rect.y - ai_settings.unit
				if body.dir == 4:
					eaten_body.rect.x = body.rect.x + ai_settings.unit
				if body.dir == 2:
					eaten_body.rect.x = body.rect.x - ai_settings.unit
				# add eaten body to the bodies group (snake gets longer)
				bodies.add(eaten_body)
				# create a new extra body
				create_extra_body(extra_bodies, bodies, head, screen, ai_settings, image_source)
				return

def copy_parameters(new_body, old_body):
	''' copy key parameters to new body from old body'''
	new_body.image = old_body.image.copy()
	new_body.rect.x = old_body.rect.x
	new_body.rect.y = old_body.rect.y
	new_body.dir = old_body.dir
	new_body.pos_change = old_body.pos_change.copy()
	new_body.dir_change = old_body.dir_change.copy()

def update_body(bodies):
	''' update the location of snake body'''
	bodies.update()

def check_events(ai_settings):
	'''monitor user key or mouse input'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_key_down_event(event, ai_settings)

def check_key_down_event(event, ai_settings):
	''' determine action based on player keyboard input
	up = 1, right = 2, down = 3, left = 4'''
	if event.key == pygame.K_LEFT:
		ai_settings.movement = 4
	elif event.key == pygame.K_RIGHT:
		ai_settings.movement = 2
	elif event.key == pygame.K_UP:
		ai_settings.movement = 1
	elif event.key == pygame.K_DOWN:
		ai_settings.movement = 3
	elif event.key == pygame.K_q:
		# press 'q' to quit game
		sys.exit()

def set_fps(clock):
	''' sake speed will be controlled by frame rate'''
	clock.tick(5)

def update_screen(bodies, extra_bodies, ai_settings, screen, head):
	''' draw elements onto the screen'''
	screen.fill(ai_settings.background_color)
	# draw snake head
	head.blitme()
	# draw snake body
	bodies.draw(screen)
	# draw extra bodies to be eaten
	extra_bodies.draw(screen)
	# for body in bodies.sprites():
	# 	body.draw()

	# display the most recently drawn screen
	pygame.display.flip()

