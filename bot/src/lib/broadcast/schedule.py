from core.constants import *
from .broadcast import Broadcast


def schedule(post: MESSAGE):
    Broadcast(post).schedule()
