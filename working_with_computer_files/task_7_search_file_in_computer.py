from pathlib import Path

path = Path('task7')

search_term = "14"

for path in path.rglob('*'):
    if search_term in path.stem:
        print(path.absolute())