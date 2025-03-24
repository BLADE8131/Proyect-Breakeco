from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_article(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.93 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return None, None, [f"Error al obtener el contenido: {e}"]
    soup = BeautifulSoup(response.content, "html.parser")
    
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Sin título"
    subtitle_tag = soup.find("h2")
    subtitle = subtitle_tag.get_text(strip=True) if subtitle_tag else ""
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    
    return title, subtitle, paragraphs

    # Extraer todas las imágenes (obtener URLs)
    """
    images = []
    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            images.append(src)
    """



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        title, subtitle, paragraphs = scrape_article(url)
        return render_template("article.html", title=title, subtitle=subtitle, paragraphs=paragraphs)
    return render_template("index.html")

app.run(debug=True)
