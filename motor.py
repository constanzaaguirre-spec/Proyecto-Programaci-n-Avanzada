class PlantaMotor:
    """
    Representa el componente físico del motor, incluyendo la inercia de rotor

    Atributos:
    inercia (float): Constante de tiempo (RPM)
    kv (float): Ganancia (RPM/V)
    v (float): Velocidad actual (RPM)
    """
    def __init__(self, inercia: float, kv: float):
        self.inercia = inercia
        self.ganancia = kv
        self.__vel_act: float = 0.0

    def get_vel(self) -> float:
        # Devuelve la velocidad actual en (RPM)
        return self.__vel_act

    def aplicar_Vol(self, V: float, dt: float):
        """
        Actualiza la velocidad de forma progresiva según la ecuación de inercia
        """
        velocidad_objetivo = V * self.ganancia 

        aceleracion = (velocidad_objetivo - self.__vel_act) / self.inercia

        self.__vel_act += aceleracion * dt