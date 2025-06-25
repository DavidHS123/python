# En este programa, usaremos un bucle `while` para iniciar una sesión de usuario. El bucle continuará ejecutándose hasta que el usuario ponga bien las credenciales o decida salir.

# Definimos las credenciales de usuario
username = "admin"
password = "1234"

# Iniciamos el bucle while
print("Bienvenido al sistema de inicio de sesión.")
while True:
    # Pedimos al usuario que introduzca su nombre de usuario
    # Si el usuario introduce Ctrl+C, el programa se detendrá
    user_input = input("Introduce tu nombre de usuario (o pulsa Ctrl+C para terminar): ")
    
    # Comprobamos si el nombre de usuario es correcto
    if user_input == username:
        # Si el nombre de usuario es correcto, pedimos la contraseña
        pass_input = input("Introduce tu contraseña: ")
        
        # Comprobamos si la contraseña es correcta
        if pass_input == password:
            print("¡Bienvenido!")
            # Si las credenciales son correctas, salimos del bucle
            break
        else:
            # Si la contraseña es incorrecta, informamos al usuario
            print("Contraseña incorrecta. Inténtalo de nuevo.")
    else:
        # Si el nombre de usuario es incorrecto, informamos al usuario
        print("Usuario no encontrado. Inténtalo de nuevo.")

# Si el usuario decide salir, puede hacerlo con Ctrl+C
print("Gracias por usar el sistema. ¡Hasta luego!")

# Nota: Este programa no maneja excepciones de forma avanzada, como el caso de Ctrl+C. En un entorno real, sería recomendable implementar un manejo de excepciones para mejorar la experiencia del usuario.