""" Test scenario
1. Move drag me to Drop me box.
2. Assert drag me is on Drop me box.

3. Assert Drop me box became blue.
4. Assert "Drop me" changed to "Dropped!"
5. Take Drag me from Dropped!
6. Assert Dropped stayed blue.
"""


def test_simple_dropped(simple_page):
    simple_page.move_to()
    assert simple_page.get_text() == 'Dropped!'
    # assert simple_page.get_color() == True
    # simple_page.move_back()
    # assert simple_page.get_color() == True