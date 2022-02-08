"""Test scenario:
1. Go to page
2. Click on all bars and fill in the info
3. Click submit
4. Check if email is in the "Thank you window"
"""

form = {
    "firstName": "ira",
    "lastName": "vozna",
    "userEmail": "ira.vozna@gmail.com",
    "gender": "male",
    "userNumber": "0635712531",
    "dateOfBirthInput": "17 Jan 2022",
    "subjectsInput": ["Maths", "Economics"],
    "hobbies": ["Sports", "Music"],
    "file": "image.jfif",
    "currentAddress": "liska 7",
    "state": "Haryana",
    "city": "Panipat",
}


def test_practice_form(practice_form):
    practice_form.submit_form(form)
    assert practice_form.check_confirmation('Student Email', 'ira.vozna@gmail.com')
    assert practice_form.check_confirmation('Mobile', '0635712531')
    assert practice_form.check_confirmation('State and City', 'Haryana Panipat')
    practice_form.close_modal()
    assert practice_form.is_empty()


def test_minimal(practice_form):
    practice_form.submit_form({
        "firstName": "Vasyl",
        "lastName": "Romanchak",
        "gender": 'male',
        "userNumber": "0679343020"
    })
    assert practice_form.check_confirmation('Mobile', '0679343020')
    practice_form.close_modal()
    assert practice_form.is_empty()

#
# def test_practiceform(practiceform_page):
#     practiceform_page.submit_form()
#     assert practiceform_page.data_submited()
#     assert practiceform_page.check_confirmation('Address', 'liska 7')
#
