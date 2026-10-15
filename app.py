
from flask import Flask, render_template_string

app = Flask(__name__)


   
 
musicas = [   
    ("Smooth Criminal", "Y0pYGmfhaGc"),  
    ("Beat It", "aV4ZFhIUGEU"),    
    ("Billie Jean (Motown 25)", "iQrjmTrVx4Q"),    
    ("Thriller", "CZ4Kf-H_C8o"), 
    ("Bad", "F0FKl0S_pYE"),
    ("Black or White", "_8W4fEaPQh0"),
    ("Remember the Time", "bhLakTP8hu4"),
    ("The Way You Make Me Feel", "dh4VexRyCKE"), 
    ("Don't Stop 'Til You Get Enough", "89NI6FVo8KA"),
    ("Human Nature (1988)", "zN0_6zjba9c"),  
    ("Blame It on the Boogie", "S1ZQkHdXHvQ"),  
    ("Wanna Be Startin' Somethin'", "NSO0QzDCTvI"),
    ("Dirty Diana", "tAFZaJ3w0ng"),
    ("Working Day and Night", "tbljkx981H4"),
]
HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Michael Jackson Para Sempre</title>


}

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    background: linear-gradient(-45deg, #101010, #1b1035, #080808, #251044);
    background-size: 400% 400%;
    animation: luzDoShow 12s ease infinite;
    color: white;
    font-family: Arial, sans-serif;
}

@keyframes luzDoShow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

   

header {
    background: #050505;
    text-align: center;
    padding: 25px 10px;
    border-bottom: 2px solid gold;
}
h1, h2 { color: gold; }
main { max-width: 900px; margin: auto; padding: 20px; }
.player {
    background: #202020;
    padding: 18px;
    border-radius: 12px;
}
iframe {
    width: 100%;
    aspect-ratio: 16 / 9;
    border: none;
    border-radius: 8px;
}
.lista {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 12px;
}
button {
    padding: 16px;
    background: #292929;
    color: white;
    border: 1px solid gold;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
}
button:hover { background: #594500; }
footer {
    text-align: center;
    padding: 25px;
    color: #aaa;
}
</style>
</head>
<body>

<header>
    <h1>👑 Michael Jackson Para Sempre</h1>
    <p>O Rei do Pop vive para sempre! 🎤</p>
</header>

<main>
    <h2>🎬 Player de músicas e videoclipes</h2>

    <div class="player">
        <h3 id="titulo">Billie Jean</h3>
        <iframe id="video"
            
            src="https://www.youtube.com/embed/Zi_XLOBDo_Y"
            title="Videoclipe de Michael Jackson"
            allow="encrypted-media; picture-in-picture"
            allowfullscreen>
        </iframe>
    </div>

    <h2>🎵 Escolha sua música</h2>
    <div class="lista">
        {% for nome, video_id in musicas %}
        
<button onclick="tocar(&quot;{{ video_id }}&quot;, &quot;{{ nome }}&quot;)">
            ▶ {{ nome }}
        </button>
        {% endfor %}
    </div>
</main>

<footer>
    Feito por um fã ❤️ | Michael Jackson Para Sempre
</footer>

<script>



function tocar(id, nome) {
    document.getElementById("titulo").textContent = nome;

    document.getElementById("video").src =
        "https://www.youtube-nocookie.com/embed/" + id +
        "?autoplay=1";
}


</script>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(HTML, musicas=musicas)

if __name__ == "__main__":
    app.run(debug=True)
