import pandas as pd
import re


# poblacion estimada hasta 2040 -   Fuente: https://www.indec.gob.ar/ftp/cuadros/publicaciones/proyeccionesyestimaciones_nac_2010_2040.pdf
valores = [
    "2010",
    "40.788.453",
    "2011",
    "41.261.490",
    "2012",
    "41.733.271",
    "2013",
    "42.202.935",
    "2014",
    "42.669.500",
    "2015",
    "43.131.966",
    "2016",
    "43.590.368",
    "2017",
    "44.044.811",
    "2018",
    "44.494.502",
    "2019",
    "44.938.712",
    "2020",
    "45.376.763",
    "2021",
    "45.808.747",
    "2022",
    "46.234.830",
    "2023",
    "46.654.581",
    "2024",
    "47.067.641",
    "2025",
    "47.473.760",
    "2026",
    "47.873.268",
    "2027",
    "48.266.524",
    "2028",
    "48.653.385",
    "2029",
    "49.033.678",
    "2030",
    "49.407.265",
    "2031",
    "49.774.276",
    "2032",
    "50.134.861",
    "2033",
    "50.488.930",
    "2034",
    "50.836.373",
    "2035",
    "51.177.087",
    "2036",
    "51.511.042",
    "2037",
    "51.838.245",
    "2038",
    "52.158.610",
    "2039",
    "52.472.054",
    "2040",
    "52.778.477"
]

years = list()
population = list()

for i, v in enumerate(valores):
    if i % 2 == 0:
        years.append(int(v))
    else:
        population.append(int(v.replace('.', '')))

df = pd.DataFrame({'year': years, 'population': population})


df.to_csv(r'./datasets/population-2010-to-2040.csv',
          encoding='utf-8',
          header=True,
          index=False)

# poblacion censo 2001
# Fuente: https://www.indec.gob.ar/ftp/cuadros/poblacion/censo2010_tomo2.pdf
data_2001 = [('Buenos Aires', 13827203),
             ('Catamarca', 334568),
             ('Chaco', 984446),
             ('Chubut', 413237),
             ('Ciudad Autónoma de Buenos Aires', 2776138),
             ('Córdoba', 3066801),
             ('Corrientes', 930991),
             ('Entre Ríos', 1158147),
             ('Formosa', 486559),
             ('Jujuy', 611888),
             ('La Pampa', 299294),
             ('La Rioja', 289983),
             ('Mendoza', 1579651),
             ('Misiones', 965522),
             ('Neuquén', 474155),
             ('Río Negro', 552822),
             ('Salta', 1079051),
             ('San Juan', 620023),
             ('San Luis', 367933),
             ('Santa Cruz', 196958),
             ('Santa Fe', 3000701),
             ('Santiago del Estero', 804457),
             ('Tierra del Fuego, Antártida e Islas del Atlántico Sur', 101079),
             ('Tucumán', 1338523)]

# poblacion censo 2010
# Fuente: https://www.indec.gob.ar/ftp/cuadros/poblacion/censo2010_tomo2.pdf
data_2010 = [('Ciudad Autónoma de Buenos Aires', 2890151),
             ('Buenos Aires', 15625084),
             ('Catamarca', 367828),
             ('Chaco', 1055259),
             ('Chubut', 509108),
             ('Córdoba', 3308876),
             ('Corrientes', 992595),
             ('Entre Ríos', 1235994),
             ('Formosa', 530162),
             ('Jujuy', 673307),
             ('La Pampa', 318951),
             ('La Rioja', 333642),
             ('Mendoza', 1738929),
             ('Misiones', 1101593),
             ('Neuquén', 551266),
             ('Río Negro', 638645),
             ('Salta', 1214441),
             ('San Juan', 681055),
             ('San Luis', 432310),
             ('Santa Cruz', 273964),
             ('Santa Fe', 3194537),
             ('Santiago del Estero', 874006),
             ('Tierra del Fuego, Antártida e Islas del Atlántico Sur', 127205),
             ('Tucumán', 1448188)]

# poblacion censo 2022
# Fuente: https://www.censo.gob.ar/wp-content/uploads/2023/01/cnphv2022_resultados_provisionales-.xlsx
data_2022 = [('Buenos Aires', 17569053),
             ('Córdoba', 3978984),
             ('Santa Fe', 3556522),
             ('Ciudad Autónoma de Buenos Aires', 3120612),
             ('Mendoza', 2014533),
             ('Tucumán', 1703186),
             ('Salta', 1440672),
             ('Entre Ríos', 1426426),
             ('Misiones', 1280960),
             ('Corrientes', 1197553),
             ('Chaco', 1142963),
             ('Santiago del Estero', 1054028),
             ('San Juan', 818234),
             ('Jujuy', 797955),
             ('Río Negro', 762067),
             ('Neuquén', 726590),
             ('Formosa', 606041),
             ('Chubut', 603120),
             ('San Luis', 540905),
             ('Catamarca', 429556),
             ('La Rioja', 384607),
             ('La Pampa', 366022),
             ('Santa Cruz', 333473),
             ('Tierra del Fuego, Antártida e Islas del Atlántico Sur', 190641)]


df_2001 = pd.DataFrame(data_2001, columns=['provincia', 'poblacion_2001'])
df_2010 = pd.DataFrame(data_2010, columns=['provincia', 'poblacion_2010'])
df_2022 = pd.DataFrame(data_2022, columns=['provincia', 'poblacion_2022'])


df_2001.set_index('provincia', inplace=True)
df_2010.set_index('provincia', inplace=True)
df_2022.set_index('provincia', inplace=True)

df = pd.concat([df_2001, df_2010, df_2022], axis=1)

df.sort_values(by='poblacion_2022', ascending=False, inplace=True)
df.reset_index(inplace=True)

df.to_csv(r'./datasets/population-provinces-2001-2010-2022.csv',
          encoding='utf-8',
          header=True,
          index=False)

# population in old census
# Fuente: https://censo.gob.ar/index.php/historia/
# Xpath: //div[@class="elementor-widget-wrap elementor-element-populated e-swiper-container"]//section/div[@class="elementor-container elementor-column-gap-default"]/div/div/div/div/h2[@class="elementor-heading-title elementor-size-default"]//text()
hist = [
    "15, 16, 17 de septiembre de 1869",
    "1.877.490 habitantes",
    "262.433 casas",
    "10 de mayo de 1895",
    "4.044.911 habitantes",
    "536.034 casas",
    "1 de junio de 1914",
    "7.903.662 habitantes",
    "No se contabilizaron viviendas",
    "19, 20 y 21 de abril ",
    " 10, 11 y 12 de mayo de 1947",
    "15.893.827 habitantes",
    "3.487.182 viviendas",
    "30 de septiembre de 1960",
    "20.013.793 habitantes",
    "4.681.333 viviendas particulares",
    "30 de septiembre de 1970",
    "23.364.431 habitantes",
    "6.429.482 viviendas",
    "22 de octubre de 1980",
    "27.949.480 habitantes",
    "8.196.120 viviendas particulares",
    "15 de mayo de 1991",
    "32.615.528 habitantes",
    "10.062.731 viviendas particulares",
    "17 y 18 de noviembre de 2001",
    "36.260.130 habitantes",
    "12.041.584 viviendas particulares",
    "27 de octubre de 2010",
    "40.117.096 habitantes",
    "13.812.125 viviendas particulares"
]
    

date_pattern = re.compile('^.* de (\w+) de (\d+)$')
population_pattern = re.compile('^([\.\w]*) habitantes$')

dates = list()
populations = list()

for val in hist:
    date = re.findall(date_pattern, val)
    if date:
        dates.append(int(date[0][-1]))
    population = re.findall(population_pattern, val)
    if population:
        populations.append(int(population[0].replace('.','')))

dates.append(2022)
populations.append(df_2022.sum()[0])

df = pd.DataFrame({'year':dates, 'population':populations})

df.to_csv(r'./datasets/total-population-all-census.csv',
          encoding='utf-8',
          header=True,
          index=False)