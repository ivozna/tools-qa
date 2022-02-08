def test_menu(menu_page):
    menu_page.hover_on("Main Item 2")
    menu_page.hover_on('SUB SUB LIST »')
    assert menu_page.is_visible('Sub Sub Item 1') == True
    assert menu_page.is_visible('Sub Sub Item 2') == True


