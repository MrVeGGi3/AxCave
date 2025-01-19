import cave

class TestComponent(cave.Component):
	def start(self, scene: cave.Scene):
		cave.playSound("SeaWaves.ogg", 2.0, 1)

	def update(self):
		pass
		
	def end(self, scene: cave.Scene):
		pass
	