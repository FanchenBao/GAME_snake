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

def create_food(foods, bodies, head, screen, ai_settings, image_source):
	''' create an extra body for snake to eat'''
	new_food = Body(screen, ai_settings, image_source, (len(bodies) + 1), True)
	# locate the extra body anywhere on the screen except where the snake is
	while True:
		# flag to detect whether the extra body overlaps with the snake
		overlap = False
		# extra body position is random
		new_food.rect.x = ai_settings.x_axis[randint(0, ai_settings.x_ticks - 1)]
		new_food.rect.y = ai_settings.y_axis[randint(0, ai_settings.y_ticks - 1)]
		# check overlap with head
		if head.rect.x == new_food.rect.x and head.rect.y == new_food.rect.y:
			continue
		else:
			# check overlap with body
			for body in bodies.sprites():
				if body.rect.x == new_food.rect.x and body.rect.y == new_food.rect.y:
					overlap = True
					break
			if overlap:
				continue
			# when no overlap occurs, include the extra body in game
			else:
				foods.add(new_food)
				return

def update_head(head, foods, bodies, screen, ai_settings, image_source, stats):
	''' update current head position, consider the situation where head eats an extra body, or head bumps into its own body, or head bumps into obstacle'''
	head.update()
	eaten_body = pygame.sprite.spritecollideany(head, foods)
	eat_self = pygame.sprite.spritecollideany(head, bodies)
	# detect whether head collides with own body
	if eat_self:
		# collide happens, game over
		head.dead = True
		ai_settings.game_active = False
		return

	# detect whether head collide with extra body
	if eaten_body:
		# collide happens, remove extra body from extra bodies group
		foods.remove(eaten_body)
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
				# update score, and keep all scores int
				stats.score += int(ai_settings.point)
				if stats.score > stats.high_score:
					stats.high_score = stats.score

				if len(bodies) >= (ai_settings.threshold * stats.level + 1):
					level_up(ai_settings, stats)

				# create a new extra body
				create_food(foods, bodies, head, screen, ai_settings, image_source)

def level_up(ai_settings, stats):
	''' scale up game settings to increase difficulty'''
	# player earns more point when leveling up
	ai_settings.point *= ai_settings.scale
	# set fps to int
	ai_settings.fps += 1
	
	stats.level += 1

def copy_parameters(new_body, old_body):
	''' copy key parameters to new body from old body'''
	new_body.image = old_body.image.copy()
	new_body.rect.x = old_body.rect.x
	new_body.rect.y = old_body.rect.y
	new_body.dir = old_body.dir
	new_body.pos_change = old_body.pos_change.copy()
	new_body.dir_change = old_body.dir_change.copy()

def check_events(screen, ai_settings, image_source, bodies, head, foods, stats, filename):
	'''monitor user key or mouse input'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_key_down_event(event, screen, ai_settings, image_source, bodies, head, foods, stats, filename)

def check_key_down_event(event, screen, ai_settings, image_source, bodies, head, foods, stats, filename):
	''' determine action based on player keyboard input
	up = 1, right = 2, down = 3, left = 4'''
	if event.key == pygame.K_q:
		# press 'q' to quit game
		save_high_score(filename, stats)
		sys.exit()
	elif event.key == pygame.K_p:
		# press 'p' to start game
		ai_settings.game_active = True
		restart_game(screen, ai_settings, image_source, bodies, head, foods, stats)
	
	if not head.out_of_bound:
		if event.key == pygame.K_LEFT:
			ai_settings.movement = 4
		elif event.key == pygame.K_RIGHT:
			ai_settings.movement = 2
		elif event.key == pygame.K_UP:
			ai_settings.movement = 1
		elif event.key == pygame.K_DOWN:
			ai_settings.movement = 3

def save_high_score(filename, stats):
	with open(filename, 'w') as file_object:
		file_object.write(str(stats.high_score))

def restart_game(screen, ai_settings, image_source, bodies, head, foods, stats):
	''' reset settings and stats when game starts'''
	ai_settings.reset()
	stats.reset_stats()
	head.reset()
	# empty bodies and foods
	bodies.empty()
	foods.empty()

	# create the initial snake
	create_initial_snake(screen, ai_settings, image_source, bodies, head)
	# create the inital extra body
	create_food(foods, bodies, head, screen, ai_settings, image_source)

def create_msgs(msgs, stats):
	msg1 = 'Press "P" to Play'
	msg2 = 'Press "Q" to Quit'
	msg3 = 'Game Over'
	msg4 = 'Your Score: '
	msg5 = "{:,}".format(round(stats.score), -1)
	msg6 = 'High Score: '
	msg7 = "{:,}".format(round(stats.high_score, -1))
	msgs.append(msg1)
	msgs.append(msg2)
	msgs.append(msg3)
	msgs.append(msg4)
	msgs.append(msg5)
	msgs.append(msg6)
	msgs.append(msg7)

def update_msgs(msgs, stats):
	msgs[4] = "{:,}".format(round(stats.score), -1)
	msgs[6] = "{:,}".format(round(stats.high_score), -1)

def update_screen(bodies, foods, ai_settings, screen, head, button):
	''' draw elements onto the screen'''
	screen.fill(ai_settings.background_color)
	# draw snake head
	head.blitme()
	# draw snake body
	bodies.draw(screen)
	# draw extra bodies to be eaten
	foods.draw(screen)

	if not ai_settings.game_active:
		button.draw_button()

	# display the most recently drawn screen
	pygame.display.flip()

