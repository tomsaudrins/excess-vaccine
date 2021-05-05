from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Register:
    """
    Example use:
        from Vaccine import Register
        Register(name = "Jens L. Bech", age = "49", address = "Skolevej 14, 2", zipcode = "1868 Frederiksberg C", phone = "29291981", center = "Øksnehallen, Halmtorvet 11, København V")

    List of vaccination centers:

    "Ballerup, Baltorpvej 18"
    "Bella Center, Ørestad Boulevard/Martha Christensens Vej, København S"
    "Bornholm, Ullasvej 39 C, Rønne"
    "Hillerød, Østergade 8"
    "Ishøj, Vejledalen 17"
    "Øksnehallen, Halmtorvet 11, København V"
    "Snekkerstenhallen, Agnetevej 1"
    "Vaccinationscenter Birkerød, Søndervangen 44, 3460 Birkerød"
    """

    def __init__(self, name: str, age: str, address: str, zipcode: str, phone: str, center: str) -> None:
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
        for inputText in [self.name, self.age, self.address, self.zipcode, self.phone]:
            driver.find_element_by_class_name("next-button").click()
            driver.find_element_by_tag_name("input[type=text]").send_keys(inputText)
        driver.find_element_by_class_name("next-button").click()
        driver.find_element_by_xpath(f"//*[text()[contains(., '{self.center}')]]").click()
        for _ in range(3):
            driver.find_element_by_class_name("next-button").click()
