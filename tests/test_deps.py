from deps import mention


def test_mention():
    link = '<a href="tg://user?id=724477101">Dmitriy</a>'
    assert mention("Dmitriy", 724477101) == link
