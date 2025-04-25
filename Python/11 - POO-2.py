from abc import ABC, abstractmethod
import math

# 1. Abstracción
class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio: float) -> None:
        self.radio = radio
    
    def area(self) -> float:
        return math.pi * self.radio ** 2
    
    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


# 2. Encapsulación
class Empleado:
    def __init__(self, nombre: str, salario: float) -> None:
        self.nombre = nombre
        self.salario = self._validar_salario(salario)  # Usamos el método de validación

    def _validar_salario(self, salario: float) -> float:
        if salario < 0:
            raise ValueError("El salario no puede ser negativo")
        return salario

    def aumentar_salario(self, porcentaje: float) -> None:
        if not 0 < porcentaje <= 1:
            raise ValueError("El porcentaje debe estar entre 0 y 1")
        self.salario *= (1 + porcentaje)

    def obtener_salario(self) -> float:
        return self.salario


# 3. Herencia (Más Ejemplos)
class Persona:
    """Clase base que representa a una persona."""
    
    def __init__(self, nombre: str, edad: int) -> None:
        """
        Inicializa una instancia de Persona.
        
        Args:
            nombre (str): Nombre de la persona.
            edad (int): Edad de la persona.
        """
        self.nombre = nombre.title()  # Capitaliza el nombre
        self.edad = edad
    
    def saludar(self) -> str:
        """Devuelve un saludo personalizado."""
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
    
    def __str__(self) -> str:
        """Representación informal en string."""
        return self.saludar()
    
    def __repr__(self) -> str:
        """Representación oficial para depuración."""
        return f'Persona(nombre="{self.nombre}", edad={self.edad})'


class Estudiante(Persona):
    """Clase que representa a un estudiante, hereda de Persona."""
    
    def __init__(self, nombre: str, edad: int, carrera: str) -> None:
        """
        Inicializa una instancia de Estudiante.
        
        Args:
            carrera (str): Carrera que estudia.
        """
        super().__init__(nombre, edad)
        self.carrera = carrera.title()
    
    def estudiar(self) -> str:
        """Devuelve un mensaje sobre lo que estudia."""
        return f"{self.nombre} está estudiando {self.carrera}."
    
    def __repr__(self) -> str:
        """Representación oficial para depuración."""
        return f'Estudiante(nombre="{self.nombre}", edad={self.edad}, carrera="{self.carrera}")'


class Deportista:
    def entrenar(self) -> str:
        return "Estoy entrenando."

class Musico:
    def tocar_instrumento(self) -> str:
        return "Estoy tocando un instrumento."

class ArtistaDeportista(Persona, Deportista, Musico):  # Herencia múltiple
    def __init__(self, nombre: str, edad: int, deporte: str, instrumento: str) -> None:
        Persona.__init__(self, nombre, edad)
        Deportista.__init__(self)  # No es necesario super() aquí en este caso simple
        Musico.__init__(self)
        self.deporte = deporte
        self.instrumento = instrumento

    def actuar(self) -> str:
        return f"Soy {self.nombre}, hago deporte ({self.deporte}) y toco ({self.instrumento})."


# 4. Polimorfismo
class ListaPersonalizada:
    def __init__(self, *args):
        self.elementos = list(args)

    def __len__(self):
        return len(self.elementos)

class CuentaBancaria:
    """Clase que representa una cuenta bancaria con encapsulamiento."""
    
    def __init__(self, saldo_inicial: float = 0.0) -> None:
        """
        Inicializa una cuenta bancaria.
        
        Args:
            saldo_inicial (float, optional): Saldo inicial. Default 0.0.
        """
        self.__saldo = max(0.0, float(saldo_inicial))  # Atributo privado
    
    def depositar(self, cantidad: float) -> bool:
        """
        Deposita una cantidad en la cuenta.
        
        Args:
            cantidad (float): Cantidad a depositar.
            
        Returns:
            bool: True si el depósito fue exitoso, False si no.
        """
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        return False
    
    def retirar(self, cantidad: float) -> bool:
        """
        Retira una cantidad de la cuenta.
        
        Args:
            cantidad (float): Cantidad a retirar.
            
        Returns:
            bool: True si el retiro fue exitoso, False si no.
        """
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False
    
    @property
    def saldo(self) -> float:
        """Obtiene el saldo actual (propiedad de solo lectura)."""
        return self.__saldo
    
    def __str__(self) -> str:
        """Representación informal del saldo."""
        return f"Saldo actual: ${self.__saldo:.2f}"
    
    def __repr__(self) -> str:
        """Representación oficial para depuración."""
        return f'CuentaBancaria(saldo_inicial={self.__saldo})'


if __name__ == "__main__":
    # Ejemplos de uso
    
    # Abstracción y Polimorfismo (Figuras)
    rectangulo = Rectangulo(5, 10)
    circulo = Circulo(7)
    
    print("--- Figuras ---")
    print(f"Área del rectángulo: {rectangulo.area()}")
    print(f"Perímetro del círculo: {circulo.perimetro()}")

    figuras = [Rectangulo(4, 6), Circulo(3), Rectangulo(2, 8)]
    for figura in figuras:
        print(f"Área: {figura.area()}, Perímetro: {figura.perimetro()}")

    # Encapsulación (Empleado)
    empleado = Empleado("Carlos", 50000)
    empleado.aumentar_salario(0.10)
    print("\n--- Empleado ---")
    print(f"Nuevo salario: {empleado.obtener_salario()}")

    # Herencia (ArtistaDeportista)
    artista_deportista = ArtistaDeportista("Laura", 22, "tenis", "piano")
    print("\n--- Artista Deportista ---")
    print(artista_deportista.saludar())
    print(artista_deportista.entrenar())
    print(artista_deportista.tocar_instrumento())
    print(artista_deportista.actuar())
    print(f"MRO de ArtistaDeportista: {ArtistaDeportista.mro()}")

    # Polimorfismo (ListaPersonalizada y len())
    lista1 = ListaPersonalizada(1, 2, 3, 4, 5)
    print("\n--- Lista Personalizada ---")
    print(len(lista1))
    print(len([10, 20, 30]))

    # Uso de las clases originales
    persona1 = Persona("juan pérez", 25)
    estudiante1 = Estudiante("ana gómez", 20, "ingeniería informática")
    cuenta1 = CuentaBancaria(500)
    
    print("\n--- Ejemplos Originales ---")
    print(persona1)
    print(estudiante1.estudiar())
    
    cuenta1.depositar(250.50)
    print(cuenta1)
    
    if cuenta1.retirar(100):
        print("Retiro exitoso:", cuenta1)
    else:
        print("Fondos insuficientes")
    
    print(f"Saldo mediante propiedad: ${cuenta1.saldo:.2f}")
    
    print("\n--- Representación para depuración ---")
    print(repr(persona1))
    print(repr(estudiante1))
    print(repr(cuenta1))