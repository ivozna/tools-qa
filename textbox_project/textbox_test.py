"""Test case
Steps
1. Go to page
2. Click on full name bar and enter a name.
3. Click on email bar and enter an email.
4. Click on current address bar and enter a text.
5. Click on permanent address bar and enter a text.
6. Click submit button.
Expected result:
- Name ira and email ira.vozna@gmail.com are in results bar.
"""


def test_textbox_basic(textbox_page):
    textbox_page.fill_name("Ira")
    textbox_page.fill_email("ira.vozna@gmail.com")
    textbox_page.fill_current_address("Liska 7")
    textbox_page.fill_permanent_address("Dnisterska 13")
    textbox_page.submit()
    assert textbox_page.get_info("#name") == 'Name:Ira'
    assert textbox_page.get_info("#email") == 'Email:ira.vozna@gmail.com'
    textbox_page.close()


def test_textbox_name(textbox_page):
    textbox_page.fill_name("Ira")
    textbox_page.submit()
    assert textbox_page.get_info("#name") == 'Name:Ira'
    assert textbox_page.get_info("#email") is None
    assert textbox_page.get_info("#currentAddress") is None
    assert textbox_page.get_info("#permanentAddress") is None
    textbox_page.close()


