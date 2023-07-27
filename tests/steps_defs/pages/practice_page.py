from selenium.webdriver.common.by import By

from tests.steps_defs.pages.base_page import BasePage


class PracticePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    COUNTRIES_INPUT = (By.ID, 'autocomplete')
    DROPDOWN = (By.ID, 'dropdown-class-example')
    OPEN_WINDOW_BTN = (By.ID, 'openwindow')
    NAME_INPUT = (By.ID, 'name')
    ALERT_BTN = (By.ID, 'alertbtn')
    CONFIRM_BTN = (By.ID, 'confirmbtn')
    COURSES_TABLE = (By.NAME, 'courses')
    ENGINEERS_TABLE = (By.CSS_SELECTOR, 'div.tableFixHead > table')
    COURSES_IFRAME = (By.ID, 'courses-iframe')
    MENTORSHIP_TEXT = (By.XPATH, "//li[contains(.,'His mentorship program')]")

    def enter_country(self, country):
        country_input = self.get_country_input()
        country_input.click()
        country_input.send_keys(country)

    def select_country(self, country):
        option = self.get_country_option(country)
        option.click()

    def enter_alert_text(self, text):
        alert_input = self.get_alert_input()
        alert_input.click()
        alert_input.send_keys(text)

    def click_alert_btn(self):
        self.get_alert_btn().click()

    def click_confirm_btn(self):
        self.get_confirm_btn().click()

    def get_alert(self):
        return self.driver.switch_to.alert

    def print_courses_of_price(self, price):
        # Get the table
        table = self.get_courses_table()
        # Get all rows in the table (excluding the header)
        rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
        # Initialize an empty list to store the names of the courses
        courses = []
        # Go through each row
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')  # get the columns in the row
            # Check if the price matches
            if cols[2].text == str(price):
                # If the price matches, add the course name to the list
                courses.append(cols[1].text)
        # Print the number of courses and their names
        print(f"There are {len(courses)} courses that cost ${price}:")
        for course in courses:
            print(course)

    def print_engineers_names(self):
        # Get the table
        table = self.get_engineers_table()
        # Get all rows in the table (excluding the header)
        rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
        # Go through each row
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')  # get the columns in the row
            # Check if the position is "Engineer"
            if cols[1].text == "Engineer":
                # If the position is "Engineer", print the name
                print(cols[0].text)

    def get_country_input(self):
        return self.driver.find_element(*self.COUNTRIES_INPUT)

    def get_dropdown(self):
        return self.driver.find_element(*self.DROPDOWN)

    def get_alert_input(self):
        return self.driver.find_element(*self.NAME_INPUT)

    def get_alert_btn(self):
        return self.driver.find_element(*self.ALERT_BTN)

    def get_confirm_btn(self):
        return self.driver.find_element(*self.CONFIRM_BTN)

    def get_courses_table(self):
        return self.driver.find_element(*self.COURSES_TABLE)

    def get_engineers_table(self):
        return self.driver.find_element(*self.ENGINEERS_TABLE)

    def get_courses_iframe(self):
        return self.driver.find_element(*self.COURSES_IFRAME)

    def get_mentorship_program_text(self):
        return self.driver.find_element(*self.MENTORSHIP_TEXT)

    def get_country_option(self, country):
        locator = (By.XPATH, '//li/div[text()="{}"]'.format(country))
        return self.find_visible_element(locator)
