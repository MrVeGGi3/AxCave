import cave

class AxoMovement(cave.Component):
	
	def start(self, scene: cave.Scene):
		pass

	def update(self):
		character : cave.CharacterComponent = self.entity.get("Character")
		is_ground_colliding : bool = character.collidedWith("Ground")
		is_water_colliding : bool = character.collidedWith("Water")
		is_speed_ground_colliding : bool = character.collidedWith("SpeedGround")

		if is_ground_colliding:
			character.jump()
		
		elif is_water_colliding:
			cave.restartCurrentScene()
		
		elif is_speed_ground_colliding:
			character.jumpSpeed += 10.0
			character.jump()
		else: 
			character.jumpSpeed = 10.0


	def end(self, scene: cave.Scene):
		pass
	