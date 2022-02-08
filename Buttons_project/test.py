"""Test case
Steps
1. Go to page
2. Click on Double click 2 times.
3. Check if Double click message appeared.

4. Click left on Right click button.
5. Check if Right click message didn't appear.

6.Click right on Right click button.
7. Check if Right click message appeared.

8. Click on Click button.
9. Check if Dynamic click message appeared.
"""


def test_buttons(buttons):
    buttons.double_click()
    assert buttons.check_result('#doubleClickMessage') == 'You have done a double click'
    buttons.click("text='Click Me'")
    assert buttons.check_result('#dynamicClickMessage') == 'You have done a dynamic click'

    buttons.click('#rightClickBtn')
    assert buttons.check_result('#rightClickMessage') is None
    buttons.right_click()
    assert buttons.check_result('#rightClickMessage') == 'You have done a right click'
