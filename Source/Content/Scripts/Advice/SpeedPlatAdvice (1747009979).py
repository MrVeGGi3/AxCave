import cave

class SpeedPlatAdvice(cave.Component):
	def start(self, scene: cave.Scene):
		pass

	def update(self):
		rb : cave.RigidBodyComponent = self.entity.get("RigidBody")
		is_player_collided = rb.collidedWith("Player")

		if is_player_collided:
			cave.UICanvas.add("SpeedPlatformAdvice")
		else:
			cave.UICanvas.remove("SpeedPlatformAdvice")
		
		
	def end(self, scene: cave.Scene):
		pass
	