def test_register(register_page):
    register_page.goto('/register')
    register_page.fill_info('#firstname', 'Ira1')
    register_page.fill_info('#lastname', 'Vozn2a')
    register_page.fill_info('#userName', 'ivozna3')
    register_page.fill_info('#password', 'Kozako4za123#')
    register_page.click_captcha()

    def handle_dialog(dialog):
        assert dialog.message == 'hello'
        dialog.accept()

    register_page.register(lambda: handle_dialog)


def test_login(login_page):
    login_page.fill_info('#userName', "Ira")
    login_page.fill_info('#password', "kozakoza")
    login_page.login()
    assert login_page.invalid_result() == 'Invalid username or password!'


def test_login2(login_page):
    login_page.fill_info('#userName', "")
    login_page.fill_info('#password', "")
    login_page.login()
    assert login_page.is_empty('#userName')
    assert login_page.is_empty('#password')
    assert login_page.invalid_result() == ''


def test_login3(login_page):
    login_page.fill_info('#userName', "ivozna")
    login_page.fill_info('#password', "Kozakoza123#")
    login_page.login()
    login_page.goto('/profile')
    assert login_page.valid_result() == 'ivozna'


def test_add_books(profile_page_auth):
    profile_page_auth.go_to_store()
    profile_page_auth.click_book('9781449325862')
    profile_page_auth.add_book()
    profile_page_auth.back_to_store()
    profile_page_auth.click_book('9781449365035')
    profile_page_auth.add_book()
    profile_page_auth.back_to_store()
    profile_page_auth.click_book('9781593277574')
    profile_page_auth.add_book()
    profile_page_auth.goto('/profile')
    assert profile_page_auth.get_books() == ['Git Pocket Guide', 'Speaking JavaScript', 'Understanding ECMAScript 6']
    profile_page_auth.delete_all_books()
    assert profile_page_auth.is_profile_empty()

