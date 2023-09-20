from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

# Global lists to store smartphone names and prices
smartphone_names = []
smartphone_prices = []


def open_in_new_tab(driver, url):
    """
        Opens a new browser tab and navigates to the specified URL.

        Args:
        - driver: Selenium WebDriver instance.
        - url: String representing the URL to navigate to.
    """
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)

def get_data_morele(driver):
    """
        Fetch smartphone names and prices from the Morele website.

        Args:
        - driver: Selenium WebDriver instance.
    """
    open_in_new_tab(driver,"https://www.morele.net/wyszukiwarka/0/0/,9397.00,,,,,,,0,,,,/1/?q=iphone%2014")
    name_elements = driver.find_elements(By.XPATH, "//a[@class='productLink']")
    # Extract names
    for element in name_elements:
        name = element.text.replace('Smartfon ', '')
        smartphone_names.append(name)
    price_elements = driver.find_elements(By.XPATH, "//div[@class='price-new']")
    # Extract prices
    for element in price_elements:
        price = element.text.replace(" zł", '').replace(' ', '').replace(',', '.')
        smartphone_prices.append(float(price))



def get_data_xcom(driver):
    """
    Fetch smartphone names and prices from the Xcom website.

    Args:
    - driver: Selenium WebDriver instance.
    """
    open_in_new_tab(driver,"https://www.x-kom.pl/szukaj?q=iphone%2014")
    name_elements = driver.find_elements(By.XPATH, "//h3[@class='sc-16zrtke-0 kGLNun sc-1yu46qn-9 feSnpB']/span")
    #Extract names and append to the list
    for element in name_elements:
        smartphone_names.append(element.text)
    price_elements = driver.find_elements(By.XPATH, "//span[@data-name='productPrice']")
    # Extract prices and append to the list
    for element in price_elements:
        price = element.text.replace(" zł", '').replace(' ', '').replace(',', '.')
        smartphone_prices.append(float(price))

def get_data_mediamarkt(driver):
    """
    Fetch smartphone names and prices from the MediaMarkt website. Also, manages cookie acceptance.

    Args:
    - driver: Selenium WebDriver instance.
    """
    open_in_new_tab(driver,"https://mediamarkt.pl/telefony-i-smartfony/smartfony/iphone./model=iphone-14,iphone-14-plus,iphone-14-pro,iphone-14-pro-max")
    time.sleep(2)
    #accept cookies
    try:
        cookie_accept = driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")
        cookie_accept.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Cookie button not found. Continuing without clicking.")
    name_elements = driver.find_elements(By.XPATH, "//h2[@class='title']")
    for element in name_elements:
        name = element.text.replace("Smartfon ", '')
        smartphone_names.append(name)

    price_elements = driver.find_elements(By.XPATH, "//div[@class='main-price is-big']/span")
    for element in price_elements:
        price = element.text.replace(' ', '').replace('\n', '').strip()
        if price:  # This ensures that only non-empty prices are considered

            smartphone_prices.append(float(price))






def main():
    """
    Main driver function. Fetches data from all the sources and displays it.
    """
    chrome_options = Options()
    driver_path = ChromeDriverManager().install()

    # Using ChromeService to define the executable path
    s = ChromeService(driver_path)
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.implicitly_wait(5)
    get_data_morele(driver)
    get_data_xcom(driver)
    get_data_mediamarkt(driver)
    # print("Smartphone Names", smartphone_names)
    # print("Smartphone Prices: ", smartphone_prices)
    smartphones_data = list(zip(smartphone_names, smartphone_prices))
    for item in smartphones_data:
        for j in item:
            print(j ,end=' ')
        print()
    input("please click enter to continue: ")


if __name__ == "__main__":
    main()
