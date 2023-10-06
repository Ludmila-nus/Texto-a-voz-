# Importacion de bibliotecas
""" se importan: newspaper se usa para descargar y analizar el contenido de la página web, 
nltk para la tokenización del texto, gtts para convertir el texto en voz, y pygame para reproducir el archivo de audio,
validators para validar si una cadena ingresada por el usuario es una URL válida"""

import nltk
from nltk.tokenize import word_tokenize
from gtts import gTTS
import pygame
import pygame.mixer
from newspaper import Article
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import validators



"""pip install scikit-learn
 tengo que importar esta libreria"""

nltk.download('punkt')


class TextoAVoz:
    def __init__(self, url):
        """Inicializa la instancia con la URL a traducir."""
        self.url = url

    def limpiar_texto(self, texto):
        # Paso 1: Tokenizar el texto en palabras
        tokens = word_tokenize(texto)
        
        # Paso 2: Convertir las palabras a minúsculas y filtrar palabras no alfabéticas
        tokens = [word.lower() for word in tokens if word.isalpha()]
        
        # Paso 3: Unir las palabras en una cadena
        texto_limpiado = ' '.join(tokens)
        
        # Paso 4: Devolver el texto limpiado
        return texto_limpiado
    

    def descargar_url(self, idioma, velocidad, resumen=False):
        """Descarga y convierte el contenido de la URL en audio."""
        try:
            # Se utiliza la biblioteca Newspaper3k para descargar y analizar el contenido de la página web del artículo a partir de la URL proporcionada.
            article = Article(self.url)
            
            # descargamos el articulo
            article.download()
            # parseo
            article.parse()
            
            # se extrae el titulo y el contenido del artículo
            titulo = article.title
            contenido = article.text

            # Si se solicita un resumen, se genera
            if resumen:
                contenido = self.generar_resumen(contenido)
            
            # Combinar título y contenido en una sola cadena para tokenización
            texto_completo = f"{titulo} {contenido}"
            
            # Tokenización para la velocidad de lectura
            tokens = word_tokenize(texto_completo)
            
            # Ajustar la velocidad para lectura
            velocidad_lectura = 1.0
            if velocidad.lower() == 'lenta':
                velocidad_lectura = 0.8  
            elif velocidad.lower() == 'rapida':
                velocidad_lectura = 1.4  
            elif velocidad.lower() == 'normal':
                velocidad_lectura = 1.0

            # Crear un objeto gTTS (Google Text-to-Speech) con el contenido del artículo.
            tts = gTTS(texto_completo, lang=idioma, slow=velocidad_lectura)

            # Guarda el archivo de audio en formato mp3
            tts.save("articulo.mp3")


        # Si se produce una excepción, este bloque se ejecutará y imprimirá un mensaje de error que incluye información
        # sobre la excepción. {e} 
        except Exception as e:
            print(f"Error durante la descarga y conversión: {e}")     
   
    def reproducir_audio(self):
        # reproducir el archivo de audio mp3 generado
        
        # Desactiva la inicialización del sistema de video
        # configura algunos parámetros antes de inicializar pygame. Estos parámetros se refieren a la 
        # frecuencia de muestreo (44100 Hz), el tamaño de bits (-16 bits, que significa bits firmados de 16 bits), 
        # el número de canales (2 para estéreo), y el tamaño del búfer (2048).
        try:
            pygame.mixer.pre_init(44100, -16, 2, 2048)  # Ajusta los parámetros de audio
            pygame.init()  # Inicializa pygame
            
            pygame.mixer.init()  # Inicializa el módulo de mezcla de sonido de Pygame
            
            pygame.mixer.music.load("articulo.mp3") #  Carga el archivo de audio "articulo.mp3" en el reproductor de música de Pygame.
            pygame.mixer.music.play() # Inicia la reproducción del archivo de audio. En este caso, comienza a reproducir el artículo convertido en voz.
            pygame.event.wait()  # Espera hasta que se termine de reproducir el audio

        # Si se produce una excepción, este bloque se ejecutará y imprimirá un mensaje de error que incluye información
        # sobre la excepción. {e} 
        except Exception as e:
            print(f"Error durante la reproducción de audio: {e}")
    
    def generar_resumen(self, texto, cantidad_oraciones=5):
        # Paso 1: Limpiar el texto
        texto_limpiado = self.limpiar_texto(texto)
        
        # Paso 2: Tokenizar el texto en oraciones
        oraciones = nltk.sent_tokenize(texto)
        
        # Paso 3: Calcular la matriz TF-IDF
        vectorizador = TfidfVectorizer()
        matriz_tfidf = vectorizador.fit_transform([texto_limpiado] + oraciones)
        
        # Paso 4: Calcular similitud coseno entre la primera oración (documento original) y las demás oraciones
        similitudes = cosine_similarity(matriz_tfidf[0], matriz_tfidf[1:])
        
        # Paso 5: Obtener las oraciones más similares (resumen)
        oraciones_similares = [oraciones[i] for i in similitudes.argsort(axis=1).flatten()[-cantidad_oraciones:]]
        
        # Paso 6: Unir las oraciones para formar el resumen
        resumen = ' '.join(oraciones_similares)
        
        # Paso 7: Devolver el resumen generado
        return resumen


class InteraccionUsuario:

    def __init__(self):
        self.url_usuario = None
        self.idioma_usuario = None
        self.velocidad_usuario = None
        self.accion_usuario = None
     # validar si una cadena ingresada por el usuario es una URL válida
    def obtener_url_valida(self):
        while True:
            # Pregunta al usuario por la URL
            url_usuario = input("Por favor, ingrese la URL del artículo que desea convertir a voz: ")
    
            # Validar la URL
            if validators.url(url_usuario):
                # La URL es válida, puedes salir del bucle
                self.url_usuario = url_usuario
                return self.url_usuario
            else:
                print("¡La URL ingresada no es válida! Por favor, ingrese una URL válida.")
    
    def obtener_idioma(self):
        while True:
            # Pregunta al usuario por el idioma
            idioma_usuario = input('¿A qué idioma desea traducir el texto? Listado de idiomas:\n "es": Español\n "en": Inglés\n"de": Alemán\
                                   \n"it": Italiano\n"ja": Japonés\n"ko": Coreano\n"zh": Chino" Escriba las iniciales: ')
    
            # corrobora que el ingreso del idioma sea correcto
            if idioma_usuario.lower() in ['es', 'en', 'de', 'it', 'ja', 'ko', 'zh']:
                self.idioma_usuario = idioma_usuario
                return self.idioma_usuario
            else:
                print ('¡Ingrese un idioma valido!')
    
    def obtener_velocidad(self):  
        while True:
             # Pregunta al usuario por ela velocidad de lectura
            velocidad_usuario = input("¿Desea una lectura lenta, normal o rapida? Responda 'lenta' / 'normal' / 'rapida': ")
            # corrobora que el ingreso de la velocidad sea correcta
            if velocidad_usuario.lower() in ['lenta', 'normal', 'rapida']:
                self.velocidad_usuario = velocidad_usuario
                return self.velocidad_usuario
            else:
                print ('¡Ingrese una velocidad valida!')
     

    def obtener_texto(self):
        while True:
            # pregunta al usuario si desea escuchar el texto completo o un resumen
            accion_usuario = input("¿Usted desea escuchar el texto completo o un resumen? \n Responda 'texto completo' / 'resumen': ")


            if accion_usuario.lower() in ['texto completo', 'resumen']:
                self.accion_usuario = accion_usuario     
                return self.accion_usuario
            # devuelve un mensaje de error si se ingresa una palabra erronea y reinicia el bucle 
            else:
                print(f'Su respuesta fue "{accion_usuario}" esta palabra no es valida, ingrese "texto completo" o "resumen"')

    def iniciar_conversion(self):
        # Crea una instancia de la clase TextoAVoz
        texto = TextoAVoz(self.url_usuario)

        if self.accion_usuario.lower() == 'texto completo':
            # Descarga y convierte el contenido total en audio
            texto.descargar_url(self.idioma_usuario, self.velocidad_usuario)
            # Reproduce el audio
            texto.reproducir_audio()
     
        
        # Si el usuario desea un resumen, lo genera y lo reproduce
        if self.accion_usuario.lower() == 'resumen':
            texto.descargar_url(self.idioma_usuario, self.velocidad_usuario, resumen=True)
            # Reproduce el audio
            texto.reproducir_audio()
  

            

 
