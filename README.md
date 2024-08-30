# Chat con IA para Entrenamiento en Entrevistas Técnicas

Este proyecto consiste en una aplicación web desarrollada con Flask que interactúa con un modelo de inteligencia artificial de Google para proporcionar respuestas a preguntas técnicas. La aplicación está diseñada para ayudar a los usuarios a prepararse para entrevistas técnicas, ofreciendo una interfaz donde pueden seleccionar temas, ver preguntas comunes y recibir retroalimentación generada por IA.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)

## Características

- Selección de temas relacionados con entrevistas técnicas (Java, Spring Boot, SQL).
- Preguntas comunes predefinidas que se cargan dinámicamente en función del tema seleccionado.
- Posibilidad de que los usuarios escriban sus respuestas y reciban retroalimentación de un modelo de inteligencia artificial.
- Respuestas generadas utilizando un modelo de IA de Google configurado a través de una clave de API.

## Tecnologías Utilizadas

- **Backend:**
  - Python
  - Flask
  - Librería de IA generativa de Google (`google.generativeai`)

- **Frontend:**
  - HTML5
  - CSS (Bootstrap 4.5.2)
  - JavaScript (jQuery)

## Requisitos Previos

- Python 3.x instalado en tu sistema.
- Clave de API de Google para interactuar con su servicio de IA generativa.
- Bibliotecas necesarias instaladas en tu entorno de Python.

## Instalación

1. **Clonar el Repositorio:**
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
2. **Ejecutar la Aplicación:**
   pip install -r requeriments.txt
3. **Configurar api key:**
   GOOGLE_API_KEY = 'TU_CLAVE_API'

## Uso
1. **Ejecutar la Aplicación:**
	python main.py o py main.py
2. **Acceder a la aplicacion:**
	http://localhost:5000

## Interaccion
Selecciona un tema del menú desplegable.
Carga preguntas relacionadas con el tema.
Selecciona una pregunta o escribe tu propia pregunta.
Escribe una respuesta y envíala para recibir retroalimentación de la IA.