class GameStats():
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.set_left_players()
		self.game_active = False
		
	def set_left_players(self):
		self.players_left = self.ai_settings.no_of_ships
		
			
