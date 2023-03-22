from main import Motor

class MotorController:

    def __init__(self,list_of_motors):
        self.motor=list_of_motors

    def set_speed(self,speed):
        for motor in self.motor:
            motor.set_speed(speed)

    def speed_up(self):
        for bob in self.motor:
            bob.speed_up()

    def slow_down(self):
        for jill in self.motor:
            jill.slow_down()

    def add_Motor(self, motor:Motor): #typehint
        self.motor.append(motor)


if __name__ == " __init__":
    motor1 = Motor()
    motor2 = Motor()
    motor3 = Motor()
    motor_group=MotorController([motor1,motor2,motor3])
