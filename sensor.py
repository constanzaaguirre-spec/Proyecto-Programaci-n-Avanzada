from motor import PlantaMotor

class Sensor:
    def __init__(self, id_sensor: str, motor: PlantaMotor):
        self.id_sensor = id_sensor
        self.motor = motor
        self.vel = 0.0

    def medir_vel(self) -> float:
        # Lee la velocidad real del motor
        vel_real = self.motor.get_vel()
        self.vel = vel_real
        return self.vel