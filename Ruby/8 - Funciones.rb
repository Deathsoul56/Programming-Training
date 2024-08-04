def saludar(nombre)
    puts "¡Hola, #{nombre}!"
  end

# Definir funciones
def funcion (x)
    return x + 5
end
  
  if __FILE__ == $0
    saludar("Ana")

    puts "#{funcion(2)}"
  end
  