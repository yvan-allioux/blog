import os
import markdown
import yaml
import json
from datetime import datetime

# This function will convert all markdown files in the given directory to HTML
def convert_markdown_to_html(directory):
    articles = []

    for foldername, subfolders, filenames in os.walk(directory):
        print(f'Processing folder: {foldername}')
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(foldername, filename)
                print(f'Processing file: {file_path}')
                with open(file_path, 'r') as f:
                    text = f.read()

                # Extract metadata from YAML frontmatter
                lines = text.split('\n')
                yaml_data = '\n'.join(lines[:lines.index('---') + 1])
                metadata = yaml.safe_load(yaml_data)

                html = markdown.markdown(text)

                html_file_path = os.path.join(foldername, os.path.splitext(filename)[0] + '.html')
                print(f'Writing file: {html_file_path}')
                with open(html_file_path, 'w') as f:
                    f.write(html)

                # Add article metadata and HTML path to the list
                metadata['html_path'] = os.path.relpath(html_file_path, 'src/articles')
                articles.append(metadata)

                # delete the markdown file
                os.remove(file_path)
                print(f'Deleting file: {file_path}')

    # Save articles metadata to a JSON file
    with open('articles.json', 'w') as json_file:
        json.dump(articles, json_file, indent=4, default=str)

print("start build.py")
convert_markdown_to_html('src/articles')
print("end build.py")
