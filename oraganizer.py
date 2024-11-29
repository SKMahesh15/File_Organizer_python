from os import *
import shutil

folders = ['Documents', 'Images', 'Python', 'C++ and C', 'HTML and CSS', 'JavaScript', 'Java', 'Videos']

parent_dir = input("Please input a directory: ")
parent_dir = path.join(parent_dir)

documents = ('.txt', '.docx', '.doc', '.odt', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx', '.rtf')
images = ('.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.apng', '.avif', '.gif', '.png', '.webp')
videos = ('.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.ogg', '.divx', '.3gp')
html_css = ('.html', '.css')
cpp_c = ('.c', '.cpp')


for folder in folders:
    folder_path = path.join(parent_dir, folder)
    mkdir(folder_path)
    print(folder_path)


listed_path = listdir(parent_dir)

for files in listed_path:
    if files.endswith(documents):
        shutil.move(path.join(parent_dir, files), path.join(parent_dir, 'Documents', files))
    elif files.endswith(images):
        shutil.move(path.join(parent_dir, files), path.join(parent_dir, 'Images', files))
    elif files.endswith(videos):
        shutil.move(path.join(parent_dir, files), path.join(parent_dir, 'Videos', files))
    elif files.endswith('.py'):
        shutil.move(path.join(parent_dir, files), path.join(parent_dir, 'Python', files))
    elif files.endswith('.java'):
        shutil.move(path.join(parent_dir, files), path.join(parent_dir, 'Java', files))
    elif files.endswith('.js'):
        shutil.move(path.join(parent_dir, files), path.join(parent_dir, 'JavaScript', files))
    elif files.endswith(html_css):
        shutil.move(path.join(parent_dir, files), path.join(parent_dir, 'HTML and CSS', files))
    elif files.endswith(cpp_c):
        shutil.move(path.join(parent_dir, files), path.join(parent_dir, 'C++ and C', files))
