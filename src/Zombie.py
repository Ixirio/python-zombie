import random

class Zombie:

    body : dict
    head : dict
    leftArm : dict
    rightArm : dict
    leftLeg : dict
    rightLeg : dict

    def __init__(self, fullBody: bool) -> None:
        self.body = self.getZombiePart('body', True)
        self.head = self.getZombiePart('head', fullBody)
        self.leftArm = self.getZombiePart('left_arm', fullBody)
        self.rightArm = self.getZombiePart('right_arm', fullBody)
        self.leftLeg = self.getZombiePart('left_leg', fullBody)
        self.rightLeg = self.getZombiePart('right_leg', fullBody)

    def getRandomBool(self) -> bool:
        return bool(random.getrandbits(1))

    def getZombiePart(self, element: str, required: bool = False) -> dict:
        return {
            'has' : True if required else self.getRandomBool(),
            'path': f'/static/zombie/{element}.png'
        }
