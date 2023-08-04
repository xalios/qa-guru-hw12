from selene import browser, be, have
from qa_guru_hw10_tests.data.users import User
from tests.conftest import RES_DIR
from os.path import join


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    def fill_name(self, firstname, lastname):
        browser.element('#firstName').should(be.blank).click().type(firstname)
        browser.element('#lastName').should(be.blank).click().type(lastname)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).click().type(value)

    def fill_gender(self, value):
        value = value.title()
        browser.all('#genterWrapper .custom-control').element_by(have.exact_text(value)).click()

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).click().type(value)

    def fill_date_of_birth(self, yyyy, month, dd):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(yyyy)
        browser.element(
            f'.react-datepicker__day--0{dd}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbies(self, *values):
        for value in values:
            browser.all('#hobbiesWrapper label').element_by(have.exact_text(value)).click()

    def upload_picture(self, path):
        browser.element("#uploadPicture").send_keys(join(RES_DIR, path))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all("#state div").element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all("#city div").element_by(have.exact_text(value)).click()

    def submit(self):
        browser.element('#submit').click()

    def register(self, user=User):
        self.fill_name(user.first_name, user.last_name)
        self.fill_email(user.email)
        self.fill_user_number(user.phone_number)
        self.fill_gender(user.gender)
        self.fill_date_of_birth(*user.date_of_birth)
        self.fill_subject(user.subjects)
        self.fill_hobbies(*user.hobbies)
        self.upload_picture(user.image)
        self.fill_address(user.current_address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.submit()

    def __assert_registration_success(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def __assert_table_size(self):
        browser.all('.table-responsive>table>tbody>tr').should(have.size(10))
        browser.element('.table-responsive>table>thead>tr').all('th').should(have.size(2))

    def __assert_table_values(self, table_row_title, row_result):
        browser.all('.table-responsive tr').element_by(have.text(table_row_title)).should(have.text(row_result))

    def assert_registration(self, user=User):
        self.__assert_table_size()
        self.__assert_registration_success()

        self.__assert_table_values('Student Name', f'{user.first_name} {user.last_name}')
        self.__assert_table_values('Student Email', user.email)
        self.__assert_table_values('Gender', user.gender)
        self.__assert_table_values('Mobile', user.phone_number)
        self.__assert_table_values(
            'Date of Birth', f'{user.date_of_birth[2]} {user.date_of_birth[1]},{user.date_of_birth[0]}'
        )
        self.__assert_table_values('Subjects', user.subjects)
        self.__assert_table_values('Hobbies', *user.hobbies)
        self.__assert_table_values('Picture', user.image)
        self.__assert_table_values('Address', user.current_address)
        self.__assert_table_values('State and City', f'{user.state} {user.city}')
