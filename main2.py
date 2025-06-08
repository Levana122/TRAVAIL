from bs4 import BeautifulSoup

# Ouvre le fichier HTML avec encodage UTF-8 pour éviter les problèmes de caractères
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

# Extraction du titre de la page
title = soup.title.string
print("Titre de la page:", title)

# Extraction du texte de la balise h1
h1_text = soup.find("h1").string
print("Texte de la balise h1:", h1_text)

# Dictionnaire pour stocker les produits
all_products = dict()

# Extraction des noms et des prix des produits
products = soup.find_all("li")
for product in products:
    name = product.find("h2").string
    price_str = product.find("p", class_="price").string
    price_list = price_str.split(" ")
    price = price_list[1]

    # Nettoyage du prix (enlève caractères spéciaux, remplace la virgule)
    price = price.replace('€', '').replace('â‚¬', '').replace(',', '.').strip()
    all_products[name] = {"prix": price}

    # Description
    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description

# Affichage des informations extraites
print("Produits:", all_products)

# Transformation des prix en dollars
for name in all_products.keys():
    price_str = all_products[name]["prix"]
    price = float(price_str)
    dollar_price = price * 1.2
    all_products[name]["prix_dollar"] = f"{dollar_price:.2f}$"

# Affichage avec les prix en dollars
print("Tous les produits:", all_products)

