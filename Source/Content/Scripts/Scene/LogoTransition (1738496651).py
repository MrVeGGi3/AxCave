import cave

class LogoComponent(cave.Component):
	def start(self, scene: cave.Scene):
		self.timer = cave.Timer()
		cave.playSound("Veeegie.ogg", 4.0)

	def update(self):
		is_playing = False
		if not is_playing:
			if self.timer.get() > 4.0:
				print("Estou mudando de cena")
				cave.setScene("AxCaveStart")
				is_playing = True
			
		
	def end(self, scene: cave.Scene):
		pass
	