class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

cruzeiro = City('Cruzeiro', 'Brazil', 85000, ['Santo Cruzeiro', 'Juiz Ladrao'])
taubate = City('Taubaté', 'Brazil', 317000, ['Grávida de taubaté', 'Aulas de Parkour Radicais para Mulheres'])

print(vars(cruzeiro))
print(vars(taubate))