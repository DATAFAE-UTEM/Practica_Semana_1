from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.chrome.options import Options
import time


# Set options & open server
# Chrome

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Users\\panch\\Desktop\\python\\driver\\chromedriver.exe")

url = "https://www.falabella.com/falabella-cl/category/cat20002/Moda-Mujer?isPLP=1"
driver.get(url)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


try:
    main = WebDriverWait(driver, 10). until(
        Ec.presence_of_element_located((By.XPATH, "//*[@id='testId-searchResults-products']"))
    )

    products = main.find_elements_by_class_name("grid-pod")

    product_list = []

    for product in products:
        name = product.find_element_by_css_selector(".pod-subTitle").text
        price = product.find_element_by_css_selector(".price-0 .cmr-icon-container").text
        brand = product.find_element_by_css_selector(".pod-title").text

        total_items = {
            'Producto' : name,
            'Precio' : price,
            'Marca' : brand
        }
        product_list.append(total_items)
    df =pd.DataFrame(product_list)
    print(df)

finally:
    driver.quit()