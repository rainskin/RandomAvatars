from . import Post
from .assets import event
from .controller import Controller


def setup():
    Controller.setup_on(event)
    Post.setup()
