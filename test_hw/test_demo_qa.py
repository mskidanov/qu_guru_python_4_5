import pytest
import os
from selene import browser, be, have, command


    #  Заполнение формы регистрации нового пользователя
def test_hw(browser_options):
    first_name = 'Ivan'
    last_name = 'Petrov'
    user_email = 'test@test.qa'
    user_number = '9112223344'
    adress = 'Green street'
    state = 'NCR'
    city = 'Delhi'
    file = '555.jpg'
    path_to_file = '/img/555.jpg'
    browser.element('#adplus-anchor').perform(command.js.remove)  # Удаление рекламного банера
    browser.element('#firstName').should(be.blank).type(first_name)
    browser.element('#lastName').should(be.blank).type(last_name)
    browser.element('#userEmail').should(be.blank).type(user_email)
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type(user_number)
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1987"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="9"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--015"]').click()
    browser.element('#subjectsInput').perform(command.js.scroll_into_view)  # Скролл страницы
    browser.element('#subjectsInput').set_value('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + path_to_file)
    browser.element('#currentAddress').set_value(adress)
    browser.element('#react-select-3-input').type(state).press_enter()
    browser.element('#react-select-4-input').type(city).press_enter()
    browser.element('#submit').perform(command.js.click)

    #  Проверка корректности заполнения формы регистрации
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('//table/tbody/tr[1]/td[2]').should(have.text(f'{first_name} {last_name}'))
    browser.element('//table/tbody/tr[2]/td[2]').should(have.text(user_email))
    browser.element('//table/tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//table/tbody/tr[4]/td[2]').should(have.text(user_number))
    browser.element('//table/tbody/tr[5]/td[2]').perform(command.js.scroll_into_view)
    browser.element('//table/tbody/tr[5]/td[2]').should(have.text('15 October,1987'))
    browser.element('//table/tbody/tr[6]/td[2]').should(have.text('Computer Science'))
    browser.element('//table/tbody/tr[7]/td[2]').should(have.text('Sports'))
    browser.element('//table/tbody/tr[8]/td[2]').should(have.text(file))
    browser.element('//table/tbody/tr[9]/td[2]').should(have.text('Green street'))
    browser.element('//table/tbody/tr[10]/td[2]').should(have.text(f'{state} {city}'))

    # Закрытие формы
    browser.element('#closeLargeModal').perform(command.js.click)