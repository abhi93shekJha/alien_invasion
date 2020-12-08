import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button

def run_game():
	
	#Initialize game and create a screen object,
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	
	#get Ship
	ship = Ship(screen, ai_settings)
	
	#create bullets
	bullets = Group()
	
	#create aliens
	aliens= Group()
	
	#create stats
	stats = GameStats(ai_settings)
	
	#create play button
	play_btn = Button(ai_settings, screen, "Play")
	
	gf.create_fleet(ai_settings, screen, aliens, ship)
	
	pygame.display.set_caption("Alien Invasion")
    
	#start the main loop for the game
	while True:
		#watch for keyboard and mouse events
		gf.check_events(ship, screen, ai_settings, bullets, play_btn, stats)
		
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, ai_settings, screen, ship)	
			gf.update_aliens(ai_settings, aliens, ship, stats, bullets, screen)
			
		gf.update_screen(ship, screen, ai_settings, bullets, aliens, play_btn, stats)

run_game()
