# Importacion de modulos
import modulo1

if __name__ == "__main__":
    # Saludo e interacción con el usuario
    print("¡Bienvenido al programa de conversión de texto a voz!")

continuar_otro_texto = True
while continuar_otro_texto:

    # Crea una instancia de la clase InteraccionUsuario
    interaccion = modulo1.InteraccionUsuario()
        
    # Llama a los métodos para obtener la URL, idioma y velocidad
    interaccion.obtener_url_valida()
    interaccion.obtener_idioma()
    interaccion.obtener_velocidad()
    interaccion.obtener_texto()

    # Llama al método para iniciar la conversión
    interaccion.iniciar_conversion()
    
    otro_texto = input("¿Usted desea convertir otro texto? Responda 'si' / 'no': ")

    if otro_texto.lower() != 'si':
        print('Gracias por usar nuestro programa de conversión de texto a voz! Hasta la próxima')  
        continuar_otro_texto = False






        