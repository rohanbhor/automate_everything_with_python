from pathlib import Path


root_dir = Path('task2')
files_path = root_dir.glob('**/*')

for path in files_path:
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = parent_folder + '-' + path.name
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)  # new_filepath is path object