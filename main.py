import os
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Client:
    r = 572

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationController")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-notifications')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--disable-gpu")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument(f"user-data-dir={os.getcwd()}/cookie")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(5)
        self.driver.set_window_size(1920, 1080)
        # self.driver.maximize_window()

    def draw_circle(self):
        self.driver.get("https://neal.fun/perfect-circle/")
        time.sleep(1)
        self.driver.find_element(By.TAG_NAME, 'button').click()
        body = self.driver.find_element(By.TAG_NAME, 'section')
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(body, self.r, 0).click_and_hold().perform()
        # Вычисление координат точек круга
        # step = 180  # Шаг угла в градусах
        # for angle in range(0, 361, step):
        #     # Вычисление координат точки на окружности
        #     radians = math.radians(angle)
        #     x = int(self.r * math.cos(radians))
        #     y = int(self.r * math.sin(radians))
        #     # Перемещение курсора на следующую точку и рисование линии
        #     action.move_to_element_with_offset(body, x, y).perform()
        radians = math.radians(180)
        x = int(self.r * math.cos(radians))
        y = int(self.r * math.sin(radians))
        action.move_to_element_with_offset(body, x, y).perform()
        radians = math.radians(355)
        x = int(self.r * math.cos(radians))
        y = int(self.r * math.sin(radians))
        action.move_to_element_with_offset(body, x, y).perform()
        radians = math.radians(360)
        x = int(self.r * math.cos(radians))
        y = int(self.r * math.sin(radians))
        action.move_to_element_with_offset(body, x, y).perform()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    a = Client()
    a.draw_circle()
    input('Идеальный круг нарисован!')
    a.quit()
