from pathlib import Path


root_dir = Path('task1')
files_path = root_dir.iterdir()
print(Path.cwd())

for path in files_path:
    new_file_name = "new_" + path.stem + path.suffix
    new_file_path = path.with_name(new_file_name)
    print(new_file_path)
    path.rename(new_file_path)