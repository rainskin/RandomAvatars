from botty import Answer

import assets.answers as a
import assets.kbs as k

from .samples import STARTGROUP_URL, USER
from .samples import texts as t


def test():
    assert a.menu(USER) == Answer(t.greet.strip(), k.menu(STARTGROUP_URL))
