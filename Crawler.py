from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.chrome.options import Options


# Set options & open server
# Chrome

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Program Files (x86)\\chromedriver.exe")

url = "https://www.falabella.com/falabella-cl/category/cat20002/Moda-Mujer?isPLP=1"
driver.get(url)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


try:
    main = WebDriverWait(driver, 10). until(
        Ec.presence_of_element_located((By.XPATH, "//*[@id='testId-searchResults-products']"))
    )

    products = main.find_elements_by_class_name("grid-pod")
    for product in products:
        name = product.find_element_by_class_name("pod-subTitle")
        price = product.find_element_by_css_selector(".price-0 .cmr-icon-container")
        brand = product.find_element_by_class_name("pod-title")
        print(name.text, price.text, brand.text)

finally:
    driver.quit()