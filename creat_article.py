import os
import datetime
import unicodedata
import re

def format_title(title):
    """Format le titre pour être utilisé dans les noms de fichiers et dossiers."""
    # Normaliser les accents
    title = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode('ascii')
    
    # Remplacer les espaces par des underscores
    title = title.replace(" ", "_")
    
    # Supprimer tous les caractères spéciaux en ne gardant que les lettres, chiffres et underscores
    title = re.sub(r'[^A-Za-z0-9_]', '', title)
    
    return title

def create_article_directory(base_path, title):
    """Crée le dossier de l'article avec la date et un titre formaté."""
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    folder_name = f"{current_date}-{format_title(title)}"
    article_path = os.path.join(base_path, folder_name)
    
    if not os.path.exists(article_path):
        os.makedirs(article_path)
        print(f"Dossier créé: {article_path}")
    else:
        print(f"Le dossier {article_path} existe déjà.")

    return article_path, current_date

def create_metadata_file(article_path, title, current_date):
    """Crée le fichier de métadonnées .yml avec un template."""
    metadata_content = f"""title: "{title}"
author: "yvan"
date: "{current_date}"
image: "template.jpg"
visibility: "no"
categories:
    - Development web
tags:
    - Blog
    """
    metadata_filename = f"{current_date}-{format_title(title)}_metadata.yml"
    metadata_filepath = os.path.join(article_path, metadata_filename)

    with open(metadata_filepath, "w", encoding="utf-8") as file:
        file.write(metadata_content)
    print(f"Fichier metadata créé: {metadata_filepath}")

def create_markdown_file(article_path, title, current_date):
    """Crée le fichier markdown .md avec un template."""
    markdown_content = f"""### **{title}**

ceci est un test
    """
    markdown_filename = f"{current_date}-{format_title(title)}.md"
    markdown_filepath = os.path.join(article_path, markdown_filename)

    with open(markdown_filepath, "w", encoding="utf-8") as file:
        file.write(markdown_content)
    print(f"Fichier Markdown créé: {markdown_filepath}")

if __name__ == "__main__":
    # Chemin de base où les articles seront créés
    base_path = "src/articles"
    
    # Demande du titre
    title = input("Entrez le titre de l'article: ")

    # Création du dossier, des fichiers metadata et markdown
    article_path, current_date = create_article_directory(base_path, title)
    create_metadata_file(article_path, title, current_date)
    create_markdown_file(article_path, title, current_date)
