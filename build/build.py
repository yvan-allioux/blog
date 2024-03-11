import os
import markdown

def convert_markdown_to_html(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        print(f'Processing folder: {foldername}')
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(foldername, filename)
                print(f'Processing file: {file_path}')
                with open(file_path, 'r') as f:
                    text = f.read()

                html = markdown.markdown(text)

                html_file_path = os.path.join(foldername, os.path.splitext(filename)[0] + '.html')
                print(f'Writing file: {html_file_path}')
                with open(html_file_path, 'w') as f:
                    f.write(html)
                #delete the markdown file
                os.remove(file_path)
                print(f'Deleting file: {file_path}')

convert_markdown_to_html('articles')

print("start build.py")
convert_markdown_to_html('src/articles')
print("end build.py")

