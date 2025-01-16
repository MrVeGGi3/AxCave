import cave

class QuitGameButton(cave.Component):
	def update(self):
		button : cave.UIElementComponent = self.entity.get("UI Element")
		if button.isPressed():
			cave.quitGame()

		
	