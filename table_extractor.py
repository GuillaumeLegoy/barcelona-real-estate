import requests

from bs4 import BeautifulSoup

import pandas as pd

links = [
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2013/t0202.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2014/t01.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2014/t0102.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2014/t0202.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2014/t0302.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2014/t0402.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2015/t01.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2015/t0102.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2015/t0202.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2015/t0302.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2015/t0402.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2016/t01.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2016/t0102.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2016/t0202.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2016/t0302.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2016/t0402.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2017/t0101.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2017/t0102.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2017/t0103.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2017/t0104.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2017/t0105.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2018/t02.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2019/t01.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2019/t02.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2019/t03.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2019/t04.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2019/t05.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2020/t0502.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2020/t0102.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2020/t0202.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2020/t0302.htm",
    "https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2020/t0402.htm",
]

df = pd.DataFrame()

for link in links:
    if "0102" in link.rsplit("/", 1)[-1]:
        name = link.rsplit("/", 2)[-2][1:] + "-" + "01-01"
    elif "0202" in link.rsplit("/", 1)[-1]:
        name = link.rsplit("/", 2)[-2][1:] + "-" + "04-01"
    elif "0302" in link.rsplit("/", 1)[-1]:
        name = link.rsplit("/", 2)[-2][1:] + "-" + "07-01"
    elif "0402" in link.rsplit("/", 1)[-1]:
        name = link.rsplit("/", 2)[-2][1:] + "-" + "10-01"

    print(link)
    print(link.rsplit("/", 1)[-1])
    print(link.rsplit("/", 2)[-2][1:])
    print(name)

    URL = link
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    # for row in soup.find_all(class_='WhadsRowVar3'):
    #    print(row.text)

    columns = []
    values = []

    for tr in soup.find_all("tr"):

        for td in tr.find_all("td", {"class": "WhadsRowVar1"}):
            columns.append(td.text.encode("ascii", "ignore"))

        for td in tr.find_all("td", {"class": "WhadsRowVar3"}):
            columns.append(td.text.encode("ascii", "ignore"))

        i = 1
        temp_values = []

        for td in tr.find_all("td", {"class": "WhadsDades"}):

            if i < 17:
                # if td.text.encode("ascii", "ignore").strip() != b'':
                temp_values.append(td.text.encode("ascii", "ignore").decode("utf8"))
                i += 1

            elif i == 17:
                # if td.text.encode("ascii", "ignore").strip() != b'':
                temp_values.append(td.text.encode("ascii", "ignore").decode("utf8"))

                values.append(temp_values)
                i = 1
                temp_values = []

    # for link in soup.findAll('td'):
    #    print(link.text)

    result = pd.DataFrame(values)

    result["bario"] = [
        "empty",
        "Global",
        "empty",
        "1 1. el Raval",
        "1 2. el Barri Gòtic",
        "1 3. la Barceloneta",
        "1 4. Sant Pere, Santa Caterina i la Ribera",
        "2 5. el Fort Pienc",
        "2 6. la Sagrada Família",
        '2 7. la Dreta de l"Eixample',
        '2 8. l"Antiga Esquerra de l"Eixample',
        '2 9. la Nova Esquerra de l"Eixample',
        "2 10. Sant Antoni",
        "3 11. el Poble Sec - AEI Parc Montjuïc",
        "3 12. la Marina del Prat Vermell - AEI Zona Franca",
        "3 13. la Marina de Port",
        "3 14. la Font de la Guatlla",
        "3 15. Hostafrancs",
        "3 16. la Bordeta",
        "3 17. Sants - Badal",
        "3 18. Sants",
        "4 19. les Corts",
        "4 20. la Maternitat i Sant Ramon",
        "4 21. Pedralbes",
        "5 22. Vallvidrera, el Tibidabo i les Planes",
        "5 23. Sarrià",
        "5 24. les Tres Torres",
        "5 25. Sant Gervasi - la Bonanova",
        "5 26. Sant Gervasi - Galvany",
        "5 27. el Putxet i el Farró",
        "6 28. Vallcarca i els Penitents",
        "6 29. el Coll",
        "6 30. la Salut",
        "6 31. la Vila de Gràcia",
        '6 32. el Camp d"en Grassot i Gràcia Nova',
        "7 33. el Baix Guinardó",
        "7 34. Can Baró",
        "7 35. el Guinardó",
        '7 36. la Font d"en Fargues',
        "7 37. el Carmel",
        "7 38. la Teixonera",
        "7 39. Sant Genís dels Agudells",
        "7 40. Montbau",
        '7 41. la Vall d"Hebron',
        "7 42. la Clota",
        "7 43. Horta",
        "8 44. Vilapicina i la Torre Llobeta",
        "8 45. Porta",
        "8 46. el Turó de la Peira",
        "8 47. Can Peguera",
        "8 48. la Guineueta",
        "8 49. Canyelles",
        "8 50. les Roquetes",
        "8 51. Verdun",
        "8 52. la Prosperitat",
        "8 53. la Trinitat Nova",
        "8 54. Torre Baró",
        "8 55. Ciutat Meridiana",
        "8 56. Vallbona",
        "9 57. la Trinitat Vella",
        "9 58. Baró de Viver",
        "9 59. el Bon Pastor",
        "9 60. Sant Andreu",
        "9 61. la Sagrera",
        "9 62. el Congrés i els Indians",
        "9 63. Navas",
        '10 64. el Camp de l"Arpa del Clot',
        "10 65. el Clot",
        "10 66. el Parc i la Llacuna del Poblenou",
        "10 67. la Vila Olímpica del Poblenou",
        "10 68. el Poblenou",
        "10 69. Diagonal Mar i el Front Marítim del Poblenou",
        "10 70. el Besòs i el Maresme",
        "10 71. Provençals del Poblenou",
        "10 72. Sant Martí de Provençals",
        "10 73. la Verneda i la Pau",
        "NC",
    ]
    result["year"] = name

    df = df.append(result, ignore_index=True)


df.to_csv("results_final.csv")
