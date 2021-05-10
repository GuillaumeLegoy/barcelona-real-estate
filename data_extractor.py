import time

from selenium import webdriver


driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/index.htm')

time.sleep(5) # Let the user actually see something!

elems = driver.find_elements_by_css_selector(".WhadsMenuNivell [href]")
links = [elem.get_attribute('href') for elem in elems]

all_links = []

for page in links:
    driver.get(page)

    elems2 = driver.find_elements_by_css_selector(".WhadsMenuNivell [href]")
    links2 = [elem.get_attribute('href') for elem in elems2]

    print(page)

    for i in links2:
        all_links.append(i)

    elems2 = driver.find_elements_by_css_selector(".WhadsTitVar1 [href]")
    links2 = [elem.get_attribute('href') for elem in elems2]

    for i in links2:
        all_links.append(i)





compravenda_habitatges = []

for i in all_links:
    if "Compravenda_habitatges" in i:
        driver.get(i)

        elems2 = driver.find_elements_by_css_selector(".WhadsTitVar1 [href]")
        links2 = [elem.get_attribute('href') for elem in elems2]

        for i in links2:
            compravenda_habitatges.append(i)

print(compravenda_habitatges)

driver.quit()