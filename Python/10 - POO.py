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
    # Ejemplos de uso de las clases
    persona1 = Persona("juan pérez", 25)
    estudiante1 = Estudiante("ana gómez", 20, "ingeniería informática")
    cuenta1 = CuentaBancaria(500)
    
    # Uso de los métodos
    print(persona1)  # Usa __str__
    print(estudiante1.estudiar())
    
    # Operaciones bancarias
    cuenta1.depositar(250.50)
    print(cuenta1)
    
    if cuenta1.retirar(100):
        print("Retiro exitoso:", cuenta1)
    else:
        print("Fondos insuficientes")
    
    # Acceso al saldo (solo lectura)
    print(f"Saldo mediante propiedad: ${cuenta1.saldo:.2f}")
    
    # Representación para depuración
    print("\nRepresentación para depuración:")
    print(repr(persona1))
    print(repr(estudiante1))
    print(repr(cuenta1))