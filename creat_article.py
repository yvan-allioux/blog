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
author: "Yvan"
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


def update_footer_year(footer_path):
    """Met à jour l'année de publication dans le fichier footer.html"""
    current_year = datetime.datetime.now().year

    try:
        # Lire le contenu du fichier footer.html
        with open(footer_path, "r", encoding="utf-8") as file:
            footer_content = file.read()

        # Rechercher l'année et la remplacer
        updated_footer = re.sub(r'©\d{4}', f'©{current_year}', footer_content)

        # Écrire le nouveau contenu dans le fichier
        with open(footer_path, "w", encoding="utf-8") as file:
            file.write(updated_footer)
        
        print(f"L'année du footer a été mise à jour à {current_year}.")
    except Exception as e:
        print(f"Erreur lors de la mise à jour du footer : {e}")

if __name__ == "__main__":
    # Chemin de base où les articles seront créés
    base_path = "src/articles"
    
    # Demande du titre
    title = input("Entrez le titre de l'article: ")

    # Création du dossier, des fichiers metadata et markdown
    article_path, current_date = create_article_directory(base_path, title)
    create_metadata_file(article_path, title, current_date)
    create_markdown_file(article_path, title, current_date)
    update_footer_year("src/articles/footer.html")
