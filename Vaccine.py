from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Register:
    """
    Automatically register for excess vaccines in Copenhagen.
    Center selection is done by changing the center argument. 0-7.
    Options are listed in the website.

    Example usage:
        from Vaccine import Register
        bot = Register("Jens L. Bech", "49", "Skolevej 14, 2", "1868 Frederiksberg C", "29291981", 5)
    """    
    def __init__(self, name: str, age: str, address: str, zipcode: str, phone: str, center: int) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.zipcode = zipcode
        self.phone = phone
        self.center = center
        self.apply()

    def apply(self) -> None:
        driver = webdriver.Chrome('./chromedriver')
        driver.get("https://www.regionh.dk/presse-og-nyt/pressemeddelelser-og-nyheder/Sider/Tilmelding-til-at-modtage-overskydende-vaccine-mod-COVID-19.aspx")
        self.find_form(driver)
        for inputText in [self.name, self.age, self.address, self.zipcode, self.phone]:
            driver.find_element_by_class_name("next-button").click()
            driver.find_element_by_tag_name("input[type=text]").send_keys(inputText)
        driver.find_element_by_class_name("next-button").click()
        driver.find_elements_by_tag_name("label")[self.center].click()
        for _ in range(2):
            driver.find_element_by_class_name("next-button").click()

    def find_form(self, driver: webdriver) -> None:
        cookiesButton = driver.find_element_by_class_name("coi-banner__button")
        if(cookiesButton):
            cookiesButton.click()
        driver.find_element_by_tag_name("summary").click()
        driver.find_element_by_class_name("rh-Style-Btn").click()
        driver.switch_to_window(driver.window_handles[1])
