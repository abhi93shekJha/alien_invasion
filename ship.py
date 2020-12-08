import pygame

class Ship():
	"""this class is for positioning ship on the screen"""
	
	def __init__(self, screen, ai_settings):
		"""this function will align the ship with screen"""
		self.screen = screen
		self.ai_settings = ai_settings
		
		#load ship image and get rectangle of ship and screen surfaces
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		#start new ship at the bottom center of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#parameter for moving the ship to right or left
		self.moving_right = False
		self.moving_left = False
		
		self.center = float(self.rect.centerx)
		
	
	def blitme(self):
		"""Draw the ship at it's current location"""
		self.screen.blit(self.image, self.rect)	
		
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if(self.moving_left and self.rect.left > 0):
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center		
		
	def recenter(self):
		self.center = self.screen_rect.centerx
			 	


