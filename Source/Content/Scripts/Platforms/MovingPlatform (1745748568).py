import cave  # type: ignore

class MovingPlatform(cave.Component):
	def start(self, scene: cave.Scene):
		self.timer = cave.Timer()

	def update(self):
		goingRight : bool = False
		_rb : cave.RigidBodyComponent = self.entity.get("Dynamic Body")

		if self.timer.get() > 3.0:
			self.timer.reset()
			goingRight = not goingRight
		

		if goingRight:
			_rb.setLinearVelocity(5.0, 0.0, 0.0)
		else:
			_rb.setLinearVelocity(-5.0, 0.0, 0.0)

	
	def end(self, scene: cave.Scene):
		pass
	