import os
import shutil
import pathlib
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
        sub_dirs_to_create = file.split(os.sep)

        # Create the subdirectory, if needed
        dir_only = ""
        if len(sub_dirs_to_create) > 1:
            # Extract path w/o the original top-level dir (i.e. "static") or the file name
            # ex: "static/file/path/image.png" => "file/path/"
            dir_only = os.path.sep.join(sub_dirs_to_create[1:-1])

            # Append the new top-level directory, i.e. "public"
            new_path = os.path.join(pathlib.Path(dest_dir), pathlib.Path(dir_only))
            
            # Make the subdirectories
            if not os.path.exists(new_path):
                os.makedirs(new_path)

        # Copy file over
        print(f"Copying {os.path.basename(file)} to {os.path.join(dest_dir, dir_only)}")
        shutil.copy(file, os.path.join(dest_dir, dir_only))

"""Returns list of all files in a directory"""
def directory_file_names(dir):
    file_paths = []

    # Recursive function
    if os.path.isfile(dir):
        file_paths.append(dir)
    else:
        dir_contents = os.listdir(path=dir)
        for path in dir_contents:
            if os.path.isfile(path):
                file_paths.append(path)
            else:
                file_paths.extend(directory_file_names(os.path.join(dir, path)))

    return file_paths

"""Converts all Markdown pages at `dir_path_content` to HTML, copies to `dest_dir_path`
Formats HTML with template at `template_path`"""
def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    all_content_files = directory_file_names(dir_path_content)
    md_file_paths = list(filter(lambda file: file.endswith('.md'), all_content_files))

    for md_file_path in md_file_paths:
        generate_page(md_file_path, template_path, dest_dir_path)

"""Converts the Markdown page located at from_path and generates an HTML page at dest_path
Formats using the HTML template at template_path"""
def generate_page(from_path, template_path, dest_path):
    markdown = read_file_text(from_path)
    template = read_file_text(template_path)
    title = extract_title(markdown)

    # Convert to HTML
    markdown_html = markdown_to_html_node(markdown).to_html()

    # Create the HTML file: Split the extension off the end, add the HTML extension
    html_file_name = os.path.basename(from_path).rsplit(os.path.extsep, maxsplit=1)[0] + ".html"

    # Replace the content
    html_page = template.replace('{{ Title }}', title).replace('{{ Content }}', markdown_html)

    
    # Extract path w/o the original top-level dir (i.e. "static") or the file name
    # ex: "static/file/path/image.png" => "file/path/"
    dirs_only = from_path.split(os.sep)
    intermediate_dirs = os.path.sep.join(dirs_only[1:-1])
    final_dest_path = os.path.join(intermediate_dirs, html_file_name)

    # Write the file
    print(f"Creating {html_file_name} in {os.path.join(dest_path, final_dest_path)}")
    write_file_text(html_page, os.path.join(dest_path, final_dest_path))
 

def read_file_text(path):
    text = ""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return text

def write_file_text(text, file_path):
    dir = os.path.dirname(file_path)
    if not os.path.exists(dir):
        os.makedirs(dir)

    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(text)

### Main ###

# Copy static or infrequently changed files to a new folder (ex: CSS, images)
# Recreates the destination directory, i.e. "public"
copy_files_between_directories('static', 'public')

# Expects the 'public' folder to exist from 'copy_files_between_directories()'
generate_pages_recursively('content', 'template.html', 'public')