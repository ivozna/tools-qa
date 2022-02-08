"""Test case
Steps
1. Go to page
2. Click Add button
2. Click on full name bar and enter a name.
3. Click on last name bar and enter a name.
4. Click on email bar and enter an email.
5. Click on age bar and enter a data.
6. Click on salary bar and enter a data.
7. Click on department bar and enter a data.
6. Click submit button.


Expected result:
Check if email ira.vozna is in the result.
"""
user_info = {
    "name": "Ira",
    "last_name": "Vozna",
    "email": "ira.vozna@gmail.com",
    "age": "29",
    "salary": "2000",
    "department": "QA"
}


def test_web_tables(web_tables_page):
    web_tables_page.add_user(user_info)
    assert web_tables_page.check_new_record(user_info["email"])
    web_tables_page.delete_record(user_info["email"])
    assert web_tables_page.check_delete_record(user_info["email"])
    web_tables_page.close()


def test_web_tables_search(web_tables_page):
    web_tables_page.fill_search("Alden")
    assert web_tables_page.check_search_result("Alden") == True
    web_tables_page.fill_search("Oleh")
    assert web_tables_page.check_search_result("Oleh") == False
    web_tables_page.close()