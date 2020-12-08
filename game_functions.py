import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ship, screen, ai_settings, bullets, play_btn, stats):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship, bullets, ai_settings, screen)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)	
		elif event.type == pygame.MOUSEBUTTONDOWN:
			m_x, m_y = pygame.mouse.get_pos()	
			if play_btn.rect.collidepoint(m_x, m_y):
				stats.game_active = True
				stats.set_left_players()
			


def update_screen(ship, screen, ai_settings, bullets, aliens, play_btn, stats):
	screen.fill(ai_settings.bg_color)
		
	ship.blitme()		
	aliens.draw(screen)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	#when game starts, make the play button visible
	if not stats.game_active:
		play_btn.draw_button()
			
	#to make recently drawn screen visible
	pygame.display.flip()
	
	
	
def check_keydown_events(event, ship, bullets, ai_settings, screen):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ship, ai_settings, screen)
			bullets.add(new_bullet)
	elif event.key == pygame.K_q:
		sys.exit()		
							


def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False			
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
		
		
def update_bullets(bullets, aliens, ai_settings, screen, ship):
	bullets.update()
		
	#getting rid of bullets that have disappered
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)		
	
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)	
	#create a new fleet if every alien is destroyed
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(ai_settings, screen, aliens, ship)
	     
			
def	create_fleet(ai_settings, screen, aliens, ship):

	alien = Alien(ai_settings, screen)
	
	#for creating colomns
	alien_width = alien.rect.width
	width = ai_settings.screen_width - (2 * alien_width)
	n_aliens = int(width/(2*alien_width))
	
	#for creating rows
	alien_height = alien.rect.height
	height = ai_settings.screen_height - (2 * alien_height) - (alien_height/2) - ship.rect.height
	n_rows = int(height/(2*alien_height)) 
	
	#creating aliens
	for rows in range(n_rows):
	    for a in range(0, n_aliens):
		    alien = Alien(ai_settings, screen)
		    alien.x = alien_width + 2 * alien_width * a
		    alien.y = alien_height + 2 * alien_height * rows 
		    alien.rect.x = alien.x
		    alien.rect.y = alien.y
		    aliens.add(alien)		

		    
def update_aliens(ai_settings, aliens, ship, stats, bullets, screen):
	check_fleet_direction(ai_settings, aliens)
	aliens.update()
	
	#check if any alien hits the ship
	if pygame.sprite.spritecollideany(ship, aliens):
		create_new_game(ai_settings, ship, stats, aliens, bullets, screen)
		
	#check if any alien reaches the bottom of screen
	if check_reaches_bottom(screen, aliens):
		create_new_game(ai_settings, ship, stats, aliens, bullets, screen)
	

def check_reaches_bottom(screen, aliens):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if(alien.rect.bottom >= screen_rect.bottom):
			return True
	else:
		return False		
			
		
		
def create_new_game(ai_settings, ship, stats, aliens, bullets, screen):
	stats.players_left -= 1
	if stats.players_left > 0:
		aliens.empty()
		bullets.empty()
		
		create_fleet(ai_settings, screen, aliens, ship)
		ship.recenter()
		
		sleep(0.5)
	else:
		stats.game_active = False	
					   
	
	
def check_fleet_direction(ai_settings, aliens):
	for a in aliens.sprites():
		if a.check_edges():
			change_direction(ai_settings, aliens)
			break

def change_direction(ai_settings, aliens):
	for a in aliens.sprites():
		a.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1	
			 	
				
