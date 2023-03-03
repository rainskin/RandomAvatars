import os
from pathlib import Path

handlers_folder = Path('..') / 'src' / '_handlers'

for name, dirs, files in os.walk(handlers_folder):
    if 'handler.py' in files:
        path = Path(name)
        new_name = ''.join(i.title() for i in path.name.split('_'))
        new_path = path.parent / new_name
        print(path.rename(new_path))
