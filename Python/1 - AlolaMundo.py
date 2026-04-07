"""
CLASE 1: ALOLA MUNDO PYTHON

Esta clase cubre los conceptos fundamentales en Python:
1. Características del lenguaje
2. Tipos de datos básicos
3. Operaciones aritméticas y lógicas
4. Conversión de tipos de datos
5. Métodos útiles para strings
"""

print("=== CLASE 1: ALOLA MUNDO PYTHON ===\n")

# =============================================================================
# 1. ¿QUÉ ES PYTHON Y CARACTERÍSTICAS?
# =============================================================================

print("1. ¿QUÉ ES PYTHON Y CARACTERÍSTICAS?")
print("=" * 40)

print("\n--- ¿Qué es Python? ---")
print("Python es un lenguaje de programación de alto nivel")
print("Características principales:")
print("• Sintaxis simple y legible")
print("• Tipado dinámico")
print("• Interpretado")
print("• Multiplataforma")
print("• Gran cantidad de librerías")

print("\n--- Comentarios en Python ---")
# Los comentarios de una línea se hacen con el símbolo #
print("Los comentarios de una línea usan #")

"""
Los comentarios largos de varias líneas 
se hacen con 3 comillas dobles (docstrings)
También se pueden usar para documentar funciones y clases
"""
print("Los comentarios multilínea usan triple comillas")

print("\n--- Características del lenguaje Python ---")

print("1. Tipado dinámico - las variables pueden cambiar de tipo:")
# Una variable puede cambiar de tipo (tipado dinámico)
A = 2.27
print(f"A cambió de string a: {A}, tipo: {type(A)}")

print("\n2. Verificar tipos con isinstance():")
# Función para saber si una variable pertenece a cierto tipo
print(f"¿A es un float? {isinstance(A, float)}")
print(f"¿A es un string? {isinstance(A, str)}")

print("\n3. Case Sensitive - distingue mayúsculas de minúsculas:")
# Python es Case Sensitive, diferencia mayúsculas de minúsculas
x = 23
X = "73"  #Variable tipo string
print(f"Variable x (minúscula): {x}")
print(f"Variable X (mayúscula): {X}")
print("Son variables diferentes!")

# =============================================================================
# 2. TIPOS DE DATOS BÁSICOS
# =============================================================================

print("\n2. TIPOS DE DATOS BÁSICOS")
print("=" * 40)

print("\n--- Tipos de datos básicos ---")
print("Python maneja varios tipos de datos fundamentales:")

# Tipos de datos, con el signo = asignamos el valor a una variable
x = 23                                                      # Int
y = 2.434                                                   # Float
z = 3 + 5.5j                                                # Complex
A = "Cadena 3"                                              # String
b = True                                                    # Boolean
list = [1, 2, 3, 'a', 'b']                                  # Lista
tuple = (1, 2, 3, 'a', 'b')                                 # Tupla
set = {1, 2, 23, x, 3, 3, 4, y, A, 'A', 'A', 'A', 'a'}      # Conjunto (solo aparecera los elementos 1 sola vez)
dicc = {'Nombre': 'Bob Esponja', 
        'Edad': 25,
        'Cursos': ['Calculo', 'Algebra', 'Ingles']}          # Diccionario
Nulo = None # Esto es un valor nulo

print("\n--- Verificar tipos de variables ---")
print("Usamos type() para ver el tipo de dato de una variable:")
print("Esto es un entero", x, type(x))
print("Esto es un flotante", y, type(y))
print("Esto es un complejo", z, type(z))
print("Esto es un String: " + A, type(A))       # es este caso el signo + se usa para concatenas 2 string
print("Esto es un Booleano", b, type(b))
print("Esto es una lista", list, type(list))
print("Esto es una tupla", tuple, type(tuple))
print("Esto es un conjunto", set, type(set))
print("Esto es un diccionario", dicc, type(dicc))
print("Esto es un nulo", Nulo, type(Nulo))

# =============================================================================
# 3. FORMATEO DE STRINGS Y NÚMEROS
# =============================================================================

print("\n3. FORMATEO DE STRINGS Y NÚMEROS")
print("=" * 40)

print("\n--- Formateo de strings ---")
print("Diferentes formas de insertar variables en strings:")

# Forma alternativa para imprimir y/o insertar un valor numérico dentro de un string
nombre = 'Bob Toronja'
Edad = 32
print(f"f-strings: El alumno {nombre} tiene {Edad} años")
print("Concatenación: El alumno " + nombre + " tiene " + str(Edad) + " años")

print("\n--- Formateo de números ---")
# Representación de miles
Millonada = 6_325_412.32563215 # Se pueden escribir _ para separar los miles, el número se imprimirá normal
Millonada_formateado = "{:,}".format(Millonada)
print(f'Número original: {Millonada}')
print(f'Con separador de miles: {Millonada_formateado}')

print("\n--- Trabajar con diccionarios ---")
print("Formas de acceder a datos en diccionarios:")

# Extraer datos del diccionario
edad = dicc['Edad'] # Extraer el valor de la clave 'Edad'
print(f"Acceso directo: La edad de {dicc['Nombre']} es {edad} años.")

edad = dicc.get('Edad') # Usar .get() para extraer la edad
print(f"Con .get(): La edad de {dicc['Nombre']} es {edad} años.")

# Intentar acceder a una clave que no existe
altura = dicc.get('Altura', 'No especificada')  # 'No especificada' es un valor por defecto
print(f"Clave inexistente: La altura de {dicc['Nombre']} es {altura}.")


# =============================================================================
# 4. OPERACIONES ARITMÉTICAS Y LÓGICAS
# =============================================================================

print("\n4. OPERACIONES ARITMÉTICAS Y LÓGICAS")
print("=" * 40)

print("\n--- Operaciones aritméticas básicas ---")
print("Python soporta todas las operaciones matemáticas básicas:")

print("\nSuma (+):")
print(f"6 + 5 = {6 + 5}, tipo: {type(6 + 5)}")              # Int + Int = Int
print(f"{x} + 33 = {x + 33}, tipo: {type(x + 33)}")
print(f"{x} + {y} = {x + y}, tipo: {type(x + y)}")              # Int + Float = Float
print(f"2.8 + 1.4 = {2.8 + 1.4}, tipo: {type(2.8 + 1.4)}")      # Float + Float = Float

print("\nResta (-):")
print(f"6 - 5 = {6 - 5}, tipo: {type(6 - 5)}")              # Int - Int = Int
print(f"{x} - 33 = {x - 33}, tipo: {type(x - 33)}")
print(f"{x} - {y} = {x - y}, tipo: {type(x - y)}")              # Int - Float = Float
print(f"2.8 - 1.4 = {2.8 - 1.4}, tipo: {type(2.8 - 1.4)}")      # Float - Float = Float

print("\nMultiplicación (*):")
print(f"6 * 5 = {6 * 5}, tipo: {type(6 * 5)}")              # Int * Int = Int
print(f"{x} * 33 = {x * 33}, tipo: {type(x * 33)}")
print(f"{x} * {y} = {x * y}, tipo: {type(x * y)}")              # Int * Float = Float
print(f"2.8 * 1.4 = {2.8 * 1.4}, tipo: {type(2.8 * 1.4)}")      # Float * Float = Float

print("\nDivisión (/) - siempre devuelve float:")
print(f"5 / 6 = {5 / 6}, tipo: {type(5 / 6)}")              # Int / Int = Float
print(f"{x} / 33 = {x / 33}, tipo: {type(x / 33)}")
print(f"{x} / {y} = {x / y}, tipo: {type(x / y)}")              # Int / Float = Float
print(f"2.8 / 1.4 = {2.8 / 1.4}, tipo: {type(2.8 / 1.4)}")      # Float / Float = Float

print("\nDivisión entera (//) - sin decimales:")
print(f"5 // 6 = {5 // 6}, tipo: {type(5 // 6)}")            # Int // Int = Int
print(f"{x} // 33 = {x // 33}, tipo: {type(x // 33)}")
print(f"{x} // {y} = {x // y}, tipo: {type(x // y)}")            # Int // Float = Float
print(f"2.8 // 1.4 = {2.8 // 1.4}, tipo: {type(2.8 // 1.4)}")    # Float // Float = Float

print("\nMódulo (%) - resto de la división:")
print(f"5 % 6 = {5 % 6}, tipo: {type(5 % 6)}")            # Int % Int = Int
print(f"{x} % 33 = {x % 33}, tipo: {type(x % 33)}")
print(f"{x} % {y} = {x % y}, tipo: {type(x % y)}")            # Int % Float = Float
print(f"2.8 % 1.4 = {2.8 % 1.4}, tipo: {type(2.8 % 1.4)}")    # Float % Float = Float

print("\nOperador + dual - suma números, concatena strings:")
print(f"1 + 2 = {1 + 2} (suma de números)")
print(f"'1' + '2' = {'1' + '2'} (concatenación de strings)")

print("\n--- Operadores de comparación ---")
print("Los operadores de comparación devuelven True o False:")

Op1 = 23
Op2 = 57

print(f"¿{Op1} > {Op2}? {Op1 > Op2} (mayor estricto)")
print(f"¿{Op1} < {Op2}? {Op1 < Op2} (menor estricto)")
print(f"¿{Op1} >= 23? {Op1 >= 23} (mayor o igual)")
print(f"¿44 <= {Op2}? {44 <= Op2} (menor o igual)")
print(f"¿{Op1} == {Op2}? {Op1 == Op2} (igual a)")
print(f"¿{Op2} == 57? {Op2 == 57} (igual a)")
print(f"¿{Op1} != {Op2}? {Op1 != Op2} (distinto a)")

print(f"\nOperadores de identidad:")
print(f"¿{Op1} es de tipo int? {type(Op1) is int}")
print(f"¿{Op1} NO es de tipo int? {type(Op1) is not int}")

# Algebra Booleana
print("\n--- Operaciones lógicas ---")
print("Los operadores lógicos trabajan con valores booleanos:")

t = True
f = False
t2 = True

print(f"Valor de t: {t}")
print(f"Negación de t (not t): {not t}")             # Negación Lógica
print(f"t AND f: {t and f}")        # Conjunción Lógica (y)
print(f"t AND t2: {t and t2}")
print(f"t OR f: {t or f}")         # Disyunción Lógica (o)
print(f"f OR f: {f or f}")

print("\n--- Operadores de asignación ---")
print("Python tiene operadores que combinan operación y asignación:")

# Incrementar valores
x = x + 1 # Forma larga
print(f"x = x + 1, ahora x = {x}")
x += 1  # Forma corta equivalente
print(f"x += 1, ahora x = {x}")

print("\nTodos los operadores de asignación:")
x_asig = 30
print(f"x inicial: {x_asig}")
x_asig += 5  # x = x + 5
print(f"x += 5: {x_asig}")
x_asig -= 3  # x = x - 3  
print(f"x -= 3: {x_asig}")
x_asig *= 2  # x = x * 2
print(f"x *= 2: {x_asig}")
x_asig /= 4  # x = x / 4
print(f"x /= 4: {x_asig}")
x_asig //= 3 # x = x // 3
print(f"x //= 3: {x_asig}")
x_asig %= 3  # x = x % 3
print(f"x %= 3: {x_asig}")
x_asig **= 3 # x = x ** 3 (potencia)
print(f"x **= 3: {x_asig}")

# =============================================================================
# 5. CONVERSIÓN DE TIPOS Y ENTRADA DE DATOS
# =============================================================================

print("\n5. CONVERSIÓN DE TIPOS Y ENTRADA DE DATOS")
print("=" * 40)

print("\n--- Conversión de tipos de datos (Type Casting) ---")
print("Python permite convertir entre diferentes tipos de datos:")

# Transformar una variable a Int
print("\nConversión a entero (int):")
print(f"X era: {X} (tipo: {type(X)})")
X = int(X)
print(f"X ahora es: {X} (tipo: {type(X)})")
print(f"y era: {y} (tipo: {type(y)})")
print(f"int(y) = {int(y)} (se pierde la parte decimal)")

# Transformar una variable a String
print("\nConversión a string (str):")
print(f"y era: {y} (tipo: {type(y)})")
y = str(y)
print(f"y ahora es: {y} (tipo: {type(y)})")

# Transformar una variable a Float
print("\nConversión a float:")
print(f"X era: {X} (tipo: {type(X)})")
X = float(X)
print(f"X ahora es: {X} (tipo: {type(X)})")

print("\n--- Entrada de datos del usuario ---")
print("La función input() permite obtener datos del usuario:")

# Ingresar un valor de forma manual
valor = input("Ingrese su valor aqui: ")
print(f"El valor ingresado es: {valor} (tipo: {type(valor)})")  # Siempre será un string
print("Nota: input() SIEMPRE devuelve un string")

# =============================================================================
# 6. MÉTODOS ÚTILES PARA STRINGS Y DESPEDIDA
# =============================================================================

print("\n6. MÉTODOS ÚTILES PARA STRINGS Y DESPEDIDA")
print("=" * 40)

print("\n--- Métodos útiles para strings ---")
print("Los strings tienen muchos métodos incorporados:")

# Funciones para string
mi_string = 'cazuEla'
print(f"String de ejemplo: '{mi_string}'")

print(f"\nMétodos informativos:")
print(f"len('{mi_string}'): {len(mi_string)} caracteres")
print(f"find('z'): posición {mi_string.find('z')} (primera ocurrencia)")
print(f"count('a'): {mi_string.count('a')} veces aparece la 'a'")

print(f"\nMétodos de formato:")
print(f"capitalize(): '{mi_string.capitalize()}' (primera letra mayúscula)")
print(f"upper(): '{mi_string.upper()}' (todo en mayúsculas)")  
print(f"lower(): '{mi_string.lower()}' (todo en minúsculas)")

print(f"\nMétodos de validación:")
print(f"isdigit(): {mi_string.isdigit()} (¿solo dígitos?)")
print(f"isalpha(): {mi_string.isalpha()} (¿solo letras?)")
print(f"isalnum(): {mi_string.isalnum()} (¿solo alfanumérico?)")

print(f"\nMétodos de transformación:")
print(f"replace('z', 'ss'): '{mi_string.replace('z', 'ss')}' (reemplaza z por ss)")
print(f"Repetición con *: '{mi_string}' * 3 = '{mi_string * 3}'")

print("\n--- Despedida ---")
print("Creando un marco decorativo con strings:")

linea1 = "**********************"
linea2 = "*                    *"
linea3 = "*       Adios!       *"
print(linea1)
print(linea2)
print(linea3)
print(linea2)
print("*" * 22)  # Alternativa usando repetición

print("\n--- Resumen ---")
print("En esta lección aprendiste:")
print("✓ Tipos de datos básicos de Python")
print("✓ Operaciones aritméticas y lógicas")
print("✓ Comparaciones y conversiones de tipo")
print("✓ Entrada de datos del usuario")
print("✓ Métodos útiles para strings")
print("✓ Características del lenguaje Python")

# =============================================================================
# CONCLUSIONES
# =============================================================================

print("\n" + "=" * 50)
print("CONCLUSIONES SOBRE ALOLA MUNDO Y CONCEPTOS BÁSICOS")
print("=" * 50)

print("\n1. TIPOS DE DATOS Y VARIABLES:")
print("   • Tipado dinámico: no es necesario declarar el tipo de variable")
print("   • Tipos básicos: int, float, complex, str, bool, list, tuple, set, dict")

print("\n2. OPERADORES Y EXPRESIONES:")
print("   • Python soporta operaciones aritméticas completas incluida división entera (//) y módulo (%)")
print("   • Los operadores lógicos son palabras reservadas: and, or, not")

print("\n3. MÉTODOS Y FUNCIONES INTEGRADAS:")
print("   • input() siempre captura strings")
print("   • type() y isinstance() para verificar tipos de datos")
print("   • Strings tienen muchos métodos útiles (upper, lower, replace, find)")

print("\n4. BUENAS PRÁCTICAS:")
print("   • Usar f-strings para formateo claro y seguro de strings")
print("   • Nombrar variables de forma clara considerando que Python distingue mayúsculas (Case Sensitive)")

print("\n=== FIN DE LA CLASE 1 ===\n")