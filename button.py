import pygame.font

class Button():
	def __init__(self, ai_settings, screen, msg):
		
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.width, self.height = 200, 50
		self.btn_color = (0, 255, 0)	
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		
		#build the button rectangle and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		#button message to be prepped only once
		self.prep_msg(msg)
		
	def prep_msg(self, msg):
		#Turn message into an image and center it with button
		self.text_image = self.font.render(msg, True, self.text_color, self.btn_color)
		self.image_rect = self.text_image.get_rect()
		self.image_rect.center = self.rect.center
		
	def draw_button(self):
		self.screen.fill(self.btn_color, self.rect)	
		self.screen.blit(self.text_image, self.image_rect)
