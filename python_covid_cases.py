import requests
from IPython.display import clear_output as clear

print("Casos de Covid-19 por pais \n")

pais=[]

n=int(input("Quantos países você quer verificar? \n"))
clear()

#Define os paises
for i in range(n):
  pais.append(str(input("Digite o " + str(i+1) + "° país para ser verificado: \n")))
clear()

#Trás a info de casa país
for i in range(len(pais)):
  escolha_pais = pais[i]
  print(f"------- {i+1}° pais -------")
  url = f'https://disease.sh/v3/covid-19/countries/{escolha_pais}'
  casos = requests.get(url)

  #Caso o país esteja na DataBase:
  if casos.status_code == 200:
    print(f'As informações do {escolha_pais} são: ')
    print()
    # População Total
    population = format(casos.json()['population'],',')
    population = population.replace(',', '.')
    print(f"População total: {population}")
    print()
    # Casos Totais
    cases=format(casos.json()['cases'],',')
    cases=cases.replace(',', '.')
    print(f"Números de casos de Covid-19: {cases}")
    # % de casos do Total
    porcentagem=(round((casos.json()['cases']*100)/casos.json()['population'],2))
    print(f"Cerca de {porcentagem}%  da população total do pais")
    print()
    # Mortes Totais
    deaths = format(casos.json()['deaths'],',')
    deaths = deaths.replace(',', '.')
    print(f"Números de mortes por Covid-19: {deaths}")
    # % de mortes do Total
    porcentagem=(round((casos.json()['deaths']*100)/casos.json()['population'],2))
    print(f"Cerca de {porcentagem}% da população total do pais")
    print('')

  #Caso não tenha valor válido retorna o erro
  else:
    print(f'O pais: {escolha_pais} É inválido')
    print(f'Erro: {casos.status_code} \n')
    print('')