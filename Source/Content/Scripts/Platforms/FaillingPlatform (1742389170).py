import cave

class FallingPlatform(cave.Component):
	def start(self, scene: cave.Scene):
		pass

	def update(self):
		platform : cave.RigidBodyComponent = self.entity.get("RigidBody")
		is_colliding_player = platform.collidedWith("Player")

		if is_colliding_player:
			platform.setMass(3.0)
		
	def end(self, scene: cave.Scene):
		pass
	