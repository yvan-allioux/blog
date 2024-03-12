import os
import markdown
import yaml
import json
import re

def read_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def convert_markdown_to_html(directory):
    articles = []

    for foldername, subfolders, filenames in os.walk(directory):
        print(f'Processing folder: {foldername}')
        for filename in filenames:
            if filename.endswith('.md'):
                # Convert markdown to HTML
                file_path = os.path.join(foldername, filename)
                print(f'Processing file: {file_path}')
                with open(file_path, 'r') as f:
                    text = f.read()

                html = markdown.markdown(text)
                # Write HTML to file
                html_file_path = os.path.join(foldername, os.path.splitext(filename)[0] + '.html')
                print(f'Writing file: {html_file_path}')
                with open(html_file_path, 'w') as f:
                    f.write(html)

                # Read metadata from YAML file
                yaml_file_path = os.path.splitext(file_path)[0] + '_metadata.yml'
                metadata = read_yaml(yaml_file_path) if os.path.exists(yaml_file_path) else {}

                #remove the src/ from the path
                print("current html_file_path: ", html_file_path)
                html_file_path = html_file_path.replace("src/","")
                print("new html_file_path: ", html_file_path)

                #path to the folder
                print("current foldername: ", foldername)
                article_folder_path = foldername.replace("src/","")

                # Add HTML path and metadata to the articles list
                articles.append({
                    'html_path': html_file_path,
                    #path to the image
                    'image_path': article_folder_path + metadata['image'],
                    'metadata': metadata
                })

                # Delete the markdown file
                os.remove(file_path)
                print(f'Deleting file: {file_path}')

    # Save articles data to JSON file
    json_file_path = os.path.join(directory, '..', 'articles.json')
    with open(json_file_path, 'w') as f:
        json.dump(articles, f, indent=4)
    print(f'Writing JSON file: {json_file_path}')

print("start build.py")
convert_markdown_to_html('src/articles')
print("end build.py")
