from pathlib import Path


root_dir = Path('task3')

files_path = root_dir.glob('**/*')

for path in files_path:
    if path.is_file():
        parent = path.parts[-2]
        new_filename = parent + '_new_' + path.name
        new_filepath = path.with_name(new_filename)
        print(new_filepath)
        path.rename(new_filepath)