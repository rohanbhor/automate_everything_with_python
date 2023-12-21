from pathlib import Path

root_dir = Path('images')

files_path = root_dir.glob('**/*')

for path in files_path:
    print(path.parts)
    print(path)