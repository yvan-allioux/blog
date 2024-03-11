
import os
import markdown

def convert_markdown_to_html(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'r') as f:
                    text = f.read()

                html = markdown.markdown(text)

                html_file_path = os.path.join(foldername, os.path.splitext(filename)[0] + '.html')
                with open(html_file_path, 'w') as f:
                    f.write(html)

print("start build.py")
convert_markdown_to_html('articles')
print("end build.py")

