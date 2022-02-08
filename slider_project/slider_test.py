""" Test scenario
1. Move slider tool to location 55
2. Assert slider tool value is equal to form value

3. Click on random place on slider
4. Assert slider tool value is equal to form value

"""


def test_slider(slider_page):
    slider_page.move_to(55)
    assert slider_page.get_location() == '55'

    assert slider_page.get_range_val() == '55'