import os
import shutil

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

# copy_files_between_directories('static', 'public')
