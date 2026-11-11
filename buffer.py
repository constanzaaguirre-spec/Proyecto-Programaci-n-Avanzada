from collections import deque

class ProcesadorFiltroError:
    """
    Gestiona la memoria histórica de errores usando una cola FIFO optimizada
    y aplica filtrado mediante recursividad matemática.
    """
    def __init__(self, tamano_buffer: int):
        # Implementación de Cola FIFO de tamaño fijo (O(1) en inserción/extracción)
        self.historial = deque(maxlen=tamano_buffer)

    def ver_historial(self):
        return self.historial
        
    def registrar_error(self, error_actual: float):
        self.historial.append(error_actual)
        
    def obtener_error_suavizado(self, alpha: float = 0.5) -> float:
        """
        Inicia el cálculo recursivo del error suavizado.
        """
        if not self.historial:
            return 0.0
        # Se pasa una vista inmutable para proteger el buffer durante la recursión
        valores = tuple(self.historial)
        return self._calcular_ema_recursivo(valores, alpha, len(valores) - 1)
        
    def _calcular_ema_recursivo(self, valores: tuple, alpha: float, idx: int) -> float:
        """
        Cálculo recursivo de Media Móvil Exponencial (EMA).
        Evita el uso de bucles for, protegiendo el tiempo de ejecución.
        """
        # Condición de parada (caso base): elemento más antiguo del buffer
        if idx == 0:
            return valores[0]
        
        # Llamada recursiva: ponderación del valor actual más el histórico suavizado
        return alpha * valores[idx] + (1 - alpha) * self._calcular_ema_recursivo(valores, alpha, idx - 1)