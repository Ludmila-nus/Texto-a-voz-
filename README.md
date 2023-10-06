# Texto a Voz - Conversión de Artículos a Audio

Este repositorio contiene un proyecto de Python que facilita la conversión de artículos en texto a archivos de audio reproducibles en formato mp3. La herramienta permite a los usuarios descargar artículos de la web y escucharlos en lugar de leerlos.

## Funcionalidades

1. **Descarga y Conversión:** Ingresa la URL del artículo deseado y descárgalo, convirtiendo su contenido completo en un archivo de audio en formato mp3.

2. **Idioma Personalizado:** Elige el idioma en el que prefieres escuchar el artículo. Actualmente compatible con español, inglés, alemán, italiano, japonés, coreano y chino.

3. **Velocidad de Lectura Ajustable:** Selecciona entre lectura lenta, normal o rápida según tus preferencias.

4. **Resumen Opcional:** Genera y reproduce un resumen del artículo como alternativa al texto completo.

## Estructura del Proyecto

- `texto_a_voz.py`: Script principal que maneja la interacción del usuario y la inicialización del proceso de conversión.
- `modulo1.py`: Módulo que contiene las clases `TextoAVoz` e `InteraccionUsuario` que implementan la lógica de descarga, conversión y la interacción con el usuario.
- `README.md`: Este archivo que proporciona información sobre el proyecto, requisitos, instalación y uso.

## Requisitos del Sistema

- Python 3.x
- Bibliotecas Python: `nltk`, `gtts`, `pygame`, `newspaper3k`, `validators`

## Instalación

pip install nltk gtts pygame newspaper3k validators


## Contribuir

Si encuentras algún problema, tienes sugerencias o deseas contribuir al proyecto, ¡no dudes en abrir un problema o enviar una solicitud de extracción!

¡Gracias por utilizar el convertidor de texto a voz! ¡Esperamos que te resulte útil!
