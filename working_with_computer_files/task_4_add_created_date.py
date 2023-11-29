from pathlib import Path
from datetime import datetime
from time import mktime


from pathlib import Path


root_dir = Path('task4')

files_path = root_dir.glob('**/*')

for path in files_path:
    if path.is_file():
        date_created = datetime.fromtimestamp(path.stat().st_ctime)
        date_created_str = date_created.strftime('%Y-%m-%d_%H:%M:%S')
        new_filename = date_created_str + path.name
        new_filepath = path.with_name(new_filename)
        print(new_filepath)
        path.rename(new_filepath)


