import cave

class StartGameButton(cave.Component):
	def start(self, scene: cave.Scene):
		pass

	def update(self):
		button : cave.UIElementComponent = self.entity.get("UI Element")
		if button.isPressed():
			cave.setScene("Change Level Scene")
		
	def end(self, scene: cave.Scene):
		pass
	