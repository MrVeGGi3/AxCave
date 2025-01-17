import cave # type: ignore

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
			character.gravity = 10.0
		
		elif is_water_colliding:
			cave.restartCurrentScene()
		
		elif is_speed_ground_colliding:
			character.jumpSpeed += 10.0
			character.gravity = 5.0
			character.jump()
			cave.playSound("Weee.ogg", 2.0)
		else: 
			character.jumpSpeed = 10.0


	def end(self, scene: cave.Scene):
		pass
	