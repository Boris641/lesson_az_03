from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import matplotlib.pyplot as plt



driver = webdriver.Chrome()

try:
    # Открыть страницу https://www.divan.ru/
    driver.get("https://www.divan.ru/")

    # Небольшая задержка, чтобы страница успела загрузиться
    time.sleep(5)
# Найти и кликнуть на раздел "Диваны"
    sofas_section = driver.find_element(By.CLASS_NAME, 'popmechanic-desktop')
    sofas_section.click()

    # Небольшая задержка, чтобы страница успела загрузиться
    time.sleep(5)

    # Прокрутка страницы для загрузки всех товаров (можно настроить количество прокруток)
    for _ in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    # Извлечение цен на диваны
    prices = driver.find_elements(By.CLASS_NAME, 'pY3d2')
    price_list = []
    for price in prices:
        price_text = price.text.replace(' ', '').replace('₽', '')
        if price_text.isdigit():
            price_list.append(int(price_text))

    # Сохранение данных в CSV файл
    df = pd.DataFrame(price_list, columns=['Price'])
    df.to_csv('sofa_prices.csv', index=False)

    # Нахождение средней цены
    average_price = df['Price'].mean()
    print(f'Средняя цена на диваны: {average_price:.2f} ₽')

    # Построение гистограммы цен
    plt.hist(df['Price'], bins=20, edgecolor='black')
    plt.title('Распределение цен на диваны')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество')
    plt.show()

finally:
    # Закрыть браузер
    driver.quit()