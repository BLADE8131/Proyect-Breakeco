# News Reader - Lector de Noticias Limpio

News Reader es una aplicación web desarrollada en Python que permite al usuario ingresar la URL de un artículo de noticia y, mediante técnicas de web scraping (usando BeautifulSoup), extrae y muestra únicamente el contenido esencial: título, subtítulo y párrafos. Esto genera una experiencia de lectura libre de distracciones.

## Características

- **Interfaz sencilla:** El usuario ingresa la URL del artículo a través de un formulario limpio.
- **Scraping de contenido:** Se extraen los elementos principales (título, subtítulo y párrafos) para mostrar únicamente la información relevante.
- **Diseño minimalista:** Una interfaz limpia que mejora la legibilidad y reduce el "ruido" visual que pueden tener las páginas web tradicionales.
- **Personalización:** Fácil de adaptar para soportar estructuras de diferentes portales de noticias.

## Beneficios

- **Lectura sin distracciones:** Al eliminar elementos innecesarios, el lector puede concentrarse únicamente en el contenido del artículo.
- **Ahorro de tiempo:** Evita tener que desplazarse por páginas recargadas de anuncios o secciones secundarias.
- **Accesibilidad:** Una interfaz simplificada que mejora la experiencia para personas que prefieren una lectura más directa y clara.
- **Aprendizaje y personalización:** Sirve como proyecto base para aprender sobre web scraping, Flask y la integración de bibliotecas en Python, permitiendo ampliar sus funcionalidades según las necesidades del usuario.

## Estructura del Proyecto

```
news_reader/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── article.html
└── static/
    └── css/
        └── style.css
```

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/news_reader.git
   cd news_reader
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```

2. **Accede a la aplicación:**
   Abre tu navegador y dirígete a `http://127.0.0.1:5000/`.

3. **Ingresa la URL del artículo:**
   Introduce la dirección del artículo en el campo de texto y presiona el botón para obtener una lectura limpia del contenido.

## Consideraciones

- Algunos sitios web pueden bloquear solicitudes de scraping. Si recibes un error (por ejemplo, 403 Forbidden), considera agregar o ajustar los encabezados HTTP (como el `User-Agent`) para simular una petición realizada desde un navegador real.
- La estructura HTML de cada sitio puede variar, por lo que podrías necesitar adaptar la lógica de extracción de contenido (títulos, subtítulos y párrafos) según el portal de noticias.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar la funcionalidad o agregar nuevas características, por favor abre un _issue_ o envía un _pull request_.