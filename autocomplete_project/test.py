"""Test scenario
1.Write letter "W" in first container
2. Assert autocomplete options appeared

3. Click outside the container
4. Assert autocomplete options have disappeared

5. Write down 3 colors.
6. Delete 1 of them.
7. Assert the color is deleted.

8. Delete all colors with 1 button.
9. Assert all colors are deleted.
"""


def test_autocomplete(autocomplete_page):
    autocomplete_page.type_color("w")
    assert autocomplete_page.get_options() == ['Yellow', 'White']
    autocomplete_page.click_outside()
    assert autocomplete_page.get_options() == []


def test_color_deleted(autocomplete_page):
    autocomplete_page.fill_color('White')
    autocomplete_page.fill_color('Red')
    autocomplete_page.fill_color('Black')
    autocomplete_page.delete_color('Black')
    assert autocomplete_page.get_results() == ['White', 'Red']


def test_all_colors_deleted(autocomplete_page):
    autocomplete_page.fill_color('White')
    autocomplete_page.fill_color('Red')
    autocomplete_page.fill_color('Black')
    autocomplete_page.delete_all_colors()
    assert autocomplete_page.get_results() == []
