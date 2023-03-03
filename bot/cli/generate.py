import shutil

import typer

from .config import *

TEMPLATE_FOLDER = TEMPLATES_FOLDER / 'handler'


def main():
    typer.run(generate)


def generate(handler_name: str, subhandler_names: list[str] = typer.Argument(None)):
    dest_folder = HANDLERS_FOLDER / handler_name

    if not subhandler_names:
        return copy_template(dest_folder)

    if dest_folder.exists():
        handler_file = dest_folder / 'handler.py'
        handler_file.unlink(missing_ok=True)
        init_file = dest_folder / '__init__.py'
        init_file.write_text('from .handlers import setup\n\nsetup()\n')

    for i in subhandler_names:
        dest_subfolder = dest_folder / 'handlers' / i
        copy_template(dest_subfolder)

    template_file = TEMPLATES_FOLDER / '__init__.txt'
    dest_file = dest_folder / 'handlers' / '__init__.py'

    template_text = template_file.read_text()
    subhandlers_strings = [f'from . import {name}' for name in subhandler_names]
    subhandlers_text = '\n    '.join(subhandlers_strings)
    text = template_text.format(subhandlers=subhandlers_text)

    dest_file.write_text(text)


def copy_template(path: str):
    shutil.copytree(TEMPLATE_FOLDER, path, dirs_exist_ok=True)
