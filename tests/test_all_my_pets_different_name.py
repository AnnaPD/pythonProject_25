from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()


# Задание 25.3.1. Написать тест, который проверяет, что на странице со списком питомцев пользователя:
#
# 1. Присутствуют все питомцы.
# 2. Хотя бы у половины питомцев есть фото.
# 3. У всех питомцев есть имя, возраст и порода.
# 4. У всех питомцев разные имена. В списке нет повторяющихся питомцев.(Сложное задание).

# 4. У всех питомцев разные имена. В списке нет повторяющихся питомцев.(Сложное задание).

def test_all_my_pets_different_name(test_show_my_pets):
    # Добавляем явное ожидание
    WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr'))
    )
    # Получаем список всех строк таблицы (данные всех питомцев)
    pets_info = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Перебираем данные из pets_info, оставляем имя, породу и возраст, оставшиеся данные меняем на пустую строку
    # и разделяем по пробелу. Выбираем имена и добавляем их в список pets_name.
    name_pets = []
    for i in range(len(pets_info)):
        petsinfo = pets_info[i].text.replace('\n', '').replace('×', '')
        split_petsinfo = petsinfo.split(' ')
        name_pets.append(split_petsinfo[0])

    # Перебираем имена, если имя повторяется, то прибавляем к счетчику n единицу.
    # Проверяем, если n == 0, то повторяющихся имен нет.
    n = 0
    for i in range(len(name_pets)):
        if name_pets.count(name_pets[i]) > 1:
            n += 1
    assert n == 0
    print('\n')
    print(n)
    print(name_pets)

# Вторую часть вопроса пока не смогла решить.

# Запускаем в терминале команду:
# pytest -v --driver Chrome --driver-path /chromedriver.exe tests/test_all_my_pets_different_name.py