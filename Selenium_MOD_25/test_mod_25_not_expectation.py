import pytest
from selenium import webdriver
from config import *





def test_show_my_pets():

    # Вводим email "берем из файла config"
    pytest.driver.find_element_by_id('email').send_keys(valid_email)
    # Вводим пароль "берем из файла config"
    pytest.driver.find_element_by_id('pass').send_keys(valid_pass)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"



    # находим все карточки питомцев
    # фото
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    # имена
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    # описание
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    # print(names[0].text)
    # print
    # print(len(names))
    # print
    # print(descriptions[0].text)

    for i in range(len(names)):
       assert images[i].get_attribute('src') != ''
       assert names[i].text != ''
       assert descriptions[i].text != ''
       assert ',' in descriptions[i].text
       parts = descriptions[i].text.split(",")
       assert len(parts[0]) > 0
       assert len(parts[1]) > 0


    # string = ""
    #
    # for i in range(1):
    #     assert (images[i].get_attribute('src')) != string
    #     assert (names[i].text) != string
    #     assert (descriptions[i].text) != string
    #     assert ',' in descriptions[i].text
    #     parts = descriptions[i].text.split(",")
    #     assert len(parts[0]) > 0
    #     assert len(parts[1]) > 0
