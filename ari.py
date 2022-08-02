from bs4 import BeautifulSoup

st = """<!-- test.html -->
<html>
    <body>
        <div id="champ">
            <span class="name">AHRI</span>
            <span class="hp">600</span>
            <span class="mp">450</span>
        </div>
        
        <div id="champ">
            <span class="name">VEIGAR</span>
            <span class="hp">550</span>
            <span class="mp">420</span>
        </div>
        
        <div id="champ">
            <span class="name">VICTOR</span>
            <span class="hp">630</span>
            <span class="mp">480</span>
        </div>
    </body>
</html>"""

soup = BeautifulSoup(st, "html.parser")

champs = []
for i in soup.select("#champ"):
    chname = i.select_one(".name").text
    chhp = i.select_one(".hp").text
    chmp = i.select_one(".mp").text

    champs.append([chname, chhp, chmp])

print(champs)