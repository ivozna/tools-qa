from playwright.sync_api import Playwright


class PracticeFormPage:
    GENDER_OPTIONS = {
        'male': '1',
        'female': '2',
        'other': '3'
    }

    HOBBIES = {
        'Sports': 1,
        'Reading': 2,
        'Music': 3
    }

    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, slow_mo=700)
        self.context = self.browser.new_context(ignore_https_errors=True)
        self.page = self.context.new_page()
        self.page.goto("https://demoqa.com/automation-practice-form")

    def submit_form(self, form):
        self.page.fill("#firstName", form['firstName'])
        self.page.fill("#lastName", form["lastName"])

        if 'userEmail' in form:
            self.page.fill("#userEmail", form["userEmail"])

        gender = PracticeFormPage.GENDER_OPTIONS[form['gender']]
        self.page.click(f"label[for='gender-radio-{gender}']")

        self.page.fill("#userNumber", form["userNumber"])

        if 'dateOfBirthInput' in form:
            self.page.click("#dateOfBirthInput")
            day = form["dateOfBirthInput"].split()[0]
            self.page.click(f".react-datepicker__month >> text={day}")

        if 'subjectsInput' in form:
            self.page.click("#subjectsContainer")
            for subj in form["subjectsInput"]:
                self.page.fill('#subjectsInput', subj)
                self.page.click(f'.subjects-auto-complete__menu >> text="{subj}"')

        if 'hobbies' in form:
            for item in form['hobbies']:
                hobby = PracticeFormPage.HOBBIES[item]
                self.page.click(f'label[for="hobbies-checkbox-{hobby}"]')

        if 'file' in form:
            self.page.click("input[type=\"file\"]")
            self.page.set_input_files("input[type=\"file\"]", form["file"])

        if 'currentAddress' in form:
            self.page.fill("#currentAddress", form["currentAddress"])

        if 'state' in form:
            self.page.click("#state")
            self.page.click(f'#state >> text="{form["state"]}"')

        if 'city' in form:
            self.page.click("#city")
            self.page.click(f'#city >> text="{form["city"]}"')

        self.page.click("#submit")

    def check_confirmation(self, label, value):
        return self.page.query_selector(f'.modal-body >> :text("{value}"):right-of(:text("{label}"))') is not None

    def close_modal(self):
        self.page.click("img[alt=\"adplus-dvertising\"]")

        self.page.click("#closeLargeModal")

    def is_empty(self):
        return self.page.input_value("#firstName") == ''
        # return self.page.query_selector("#firstName").input_value()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
