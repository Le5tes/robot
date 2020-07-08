import gpiozero

class RobotController:
    def __init__(self):
        self.robot = gpiozero.Robot(left=(17,18), right=(27,22))

    def giveCommand(self, command):
        print(command)
        if command == "forward":
            self.robot.forward()
        elif command == "back":
            self.robot.backward()
        elif command == "right":
            self.robot.right()
        elif command == "left":
            self.robot.left()
        elif command == "stop":
            self.robot.stop()
        else:
            return "Command not recognised"
        return command
