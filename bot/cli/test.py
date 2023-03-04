import os
from pathlib import Path

handlers_folder = Path('..') / 'src' / 'handlers'


def main():
    for name, dirs, files in os.walk(handlers_folder):
        path = Path(name)

        if 'handler.py' in files:
            new_name = ''.join(i[0].upper() + i[1:] for i in path.name.split('_'))
            new_path = path.parent / new_name
            path.rename(new_path)
            (path / 'handler.py').rename(path / 'controller.py')


for i in range(100):
    print(i)
    main()
