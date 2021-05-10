link = 'https://ajuntament.barcelona.cat/estadistica/angles/Estadistiques_per_territori/Barris/Habitatge_i_mercat_immobiliari/Mercat_immobiliari/Compravenda_habitatges/a2013/t0202.htm'

if '0102' in link.rsplit('/', 1)[-1]:
    name = link.rsplit('/', 2)[-2][1:] + '-' + '01-01'
elif '0202' in link.rsplit('/', 1)[-1]:
    name = link.rsplit('/', 2)[-2][1:] + '-' + '04-01'
elif '0302' in link.rsplit('/', 1)[-1]:
    name = link.rsplit('/', 2)[-2][1:] + '-' + '07-01'
elif '0402' in link.rsplit('/', 1)[-1]:
    name = link.rsplit('/', 2)[-2][1:] + '-' + '10-01'

print(name)