import cave

class MyComponent(cave.Component):
	def start(self, scene: cave.Scene):
		self.timer = cave.Timer()
		cave.playSound("Veeegie.ogg", 4.0)

	def update(self):
		if self.timer.get() > 4.0:
			print("Estou mudando de cena")
			cave.setScene("AxCaveStart")
		
	def end(self, scene: cave.Scene):
		pass
	