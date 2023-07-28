import time

from selenium.webdriver.support.select import Select

from tests.steps_defs.pages.practice_page import PracticePage


def test_select_country_mexico(driver):
    # Given
    page = PracticePage(driver)
    country = 'Mexico'
    # When
    page.enter_country('Me')
    page.select_country(country)
    # Then
    assert country == page.get_country_input().get_attribute('value')


def test_dropdown_option_updates(driver):
    # Given
    page = PracticePage(driver)
    # When
    dropdown = page.get_dropdown()
    select = Select(dropdown)
    # Then
    select.select_by_value('option2')
    time.sleep(5)
    assert 'option2' == dropdown.get_attribute('value')
    select.select_by_value('option3')
    assert 'option3' == dropdown.get_attribute('value')
    time.sleep(5)


def test_alert_pops_up(driver):
    # Given
    page = PracticePage(driver)
    # When
    page.enter_alert_text("Stori Card")
    time.sleep(2)
    page.click_alert_btn()
    time.sleep(2)
    alert = page.get_alert()
    # Then
    assert "Hello Stori Card, share this practice page and share your knowledge" == alert.text
    print(alert.text)
    alert.accept()


def test_alert_pops_up_and_confirm_it(driver):
    # Given
    page = PracticePage(driver)
    # When
    page.enter_alert_text("Stori Card")
    time.sleep(2)
    page.click_confirm_btn()
    time.sleep(2)
    alert = page.get_alert()
    # Then
    print(alert.text)
    assert "Hello Stori Card, Are you sure you want to confirm?" == alert.text
    alert.accept()


def test_print_courses_at_price(driver):
    # Given
    page = PracticePage(driver)
    # Then
    page.print_courses_of_price(25)


def test_print_all_engineer_names(driver):
    # Given
    page = PracticePage(driver)
    # Then
    page.print_engineers_names()


def test_find_text_and_print_it(driver):
    # Given
    page = PracticePage(driver)
    iframe = page.get_courses_iframe()
    driver.switch_to.frame(iframe)
    # When
    text_element = page.get_mentorship_program_text()
    print(text_element.text)
    # Then
    expected_text = 'His mentorship program is most after in the software testing community with long waiting period.'
    assert expected_text == text_element.text
