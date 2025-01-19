import cave

class FallGrounAdvice(cave.Component):
	def start(self, scene: cave.Scene):
		pass

	def update(self):
		rb : cave.RigidBodyComponent = self.entity.get("RigidBody")
		is_player_collided = rb.collidedWith("Player")

		if is_player_collided:
			cave.UICanvas.add("FallGroundAdvice")
		else:
			cave.UICanvas.remove("FallGroundAdvice")
		
	def end(self, scene: cave.Scene):
		pass
	