import os
import shutil
from markdown_to_html_node import *

"""Copies all files and directories from the `source_dir` to the `dest_dir`
Creates the dest_dir if it does not exist and deletes all content within
"""
def copy_files_between_directories(source_dir, dest_dir):
    # See if source_dir exists
    if not os.path.exists(source_dir):
        raise Exception(f"Source dir {source_dir} does not exist")
    if not os.path.isdir(source_dir):
        raise Exception(f"Source {source_dir} is not a dir")
    
    # Delete existing dest, create new
    if os.path.isdir(dest_dir):
        print(f"Deleting dest_dir {dest_dir}...")
        shutil.rmtree(dest_dir)
    print(f"Creating new dest_dir {dest_dir}...")
    os.mkdir(dest_dir)

    # Recursive copy from source_dir to dest_dir
    # Could just use sh.utils.copytree(), but doing it manually as an exercise
    files_to_copy = directory_file_names(source_dir)
    for file in files_to_copy:
        sub_dirs_to_create = file.split("/")

        # Create the subdirectory, if needed
        dir_only = ""
        if len(sub_dirs_to_create) > 1:
            # Extract path w/o top-level dir or file name
            # ex: "static/file/path/image.png" => "file/path/"
            dir_only = "/".join(sub_dirs_to_create[1:-1])
            if not os.path.exists(dest_dir + "/" + dir_only):
                os.makedirs(dest_dir + "/" + dir_only)

        # Copy file over
        print(f"Copying {file} to {dest_dir}")
        shutil.copy(file, dest_dir + "/" + dir_only)

"""Returns list of all files in a directory
"""
def directory_file_names(dir):
    file_paths = []

    if os.path.isfile(dir):
        file_paths.append(dir)
    else:
        dir_contents = os.listdir(path=dir)
        for path in dir_contents:
            if os.path.isfile(path):
                file_paths.append(path)
            else:
                file_paths.extend(directory_file_names(dir + "/" + path))

    return file_paths

"""Converts the Markdown page located at from_path and generates an HTML page at dest_path
Formats using the  HTML template at template_path"""
def generate_page(from_path, template_path, dest_path):
    markdown = read_file_text(from_path)
    title = extract_title(markdown)
    markdown_html = markdown_to_html_node(markdown).to_html()

    template = read_file_text(template_path)
    html_page = template.replace('{{ Title }}', title).replace('{{ Content }}', markdown_html)

    write_file_text(html_page, dest_path)
 

def read_file_text(path):
    text = ""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return text

def write_file_text(text, path):
    with open(path, 'w', encoding="utf-8") as f:
        f.write(text)


### Generate page ###

copy_files_between_directories('static', 'public')
generate_page('content/index.md', 'template.html', 'public/index.html')