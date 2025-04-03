import random as rand

# fazer um sistema de diagnostico de pacientes:
# -o paciente ira colocar os sintomas que ele esta sentindo
# -quanto mais sintomas ele der, menos doenças vão ser sugeridas
# -sugerir possíveis doenças baseado nos sintomas
# -pedir onde o paciente mora
# -definir médicos especialistas para cada área
# -algumas áreas podem ter surtos de doenças, esses surtos vão aumentar as chances do paciente ter essa doença
# -histórico familiar, apenas vai ser útil se a doença for genética, ou ter uma maior chance de pegar uma doença
# -ter mais consultas dependendo do caso, casos leves são apenas uma, casos graves vai ter que ter um retorno, e emergências serão mandados diretamente ao hospital
# -a simulação vai durar 1 mês(30 dias) e terá 5-10 pacientes por dia
# -doenças que tiveram sintomas parecidos com a outra ira ser necessário pedir uma outra consulta ou histórico familiar

identificação = [
    "nome da doença",
    "sintoma1",
    "sintoma2",
    "sintoma3",
    "sintoma4",
    "precisa de revisita",
    "vem da familia",
    "região epidemica"
]

cidades =[
    'SBO',
    'Americana',
    'Campinas'
    
]

cidades = [
    SBO :={
    'nome da cidade': 'SBO',
    'medica1':'ISABELA',
    'medico2':'PROTIOLI',
    'medica3':'ANAFOLIO',
    },
    Campinas := {
    'nome da cidade':'Campinas',
    'medica1':'IsAbElA',
    'medico2':'PoRtIoLi',
    'medico3':'anofilo1', 
    },
    Americana :={
    'nome da cidade': 'Americana',
    'medica1':'isabela',
    'medico2':'portioli',
    'medica3':'anafilo',    
    }
    
]

doenças = [
    pneumonia := {
    "nome da doença": "pneumonia",
    "sintoma1": "falta de ar",
    "sintoma2": "dor no corpo",
    "sintoma3": "indisposição fisica",
    "sintoma4": "N/A",
    "precisa de revisita": "SIM",
    "vem da familia": "NÃO",
    "influencia da região": "NÃO",
    "região epidemica": "nenhuma"

    },
    dengue := {
    "nome da doença": "dengue",
    "sintoma1": "dor no corpo",
    "sintoma2": "dor no corp",
    "sintoma3": "indisposição fisica",
    "sintoma4": "N/A",
    "precisa de revisita": "NÃO",
    "vem da familia": "NÃO",
    "influencia da região": "SIM",
    "região epidemica": cidades[rand.randint(0,len(cidades)-1)]['nome da cidade']
    }

]

nomes = [
    "Isabela", "Caio", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Kleber", "Laura", "Marcelo", "Natália", "Otávio", "Patrícia", "Quintino", "Rafaela", "Samuel", "Tatiane",
    "Ubiratan", "Vitor", "William", "Xavier", "Yasmin", "Zuleica",
    "Adriana", "Breno", "Camila", "Diego", "Eliane", "Fábio", "Giovana", "Henrique", "Isabela", "João",
    "Karen", "Luciana", "Mariana", "Nelson", "Olívia", "Paulo", "Quésia", "Rodrigo", "Simone", "Thaís",
    "Ursula", "Vanessa", "Wagner", "Ximena", "Yago", "Zilda",
    "Alex", "Beatriz", "Cristiano", "Debora", "Emerson", "Felipe", "Gustavo", "Heloísa", "Ícaro", "Jéssica",
    "Kaio", "Luan", "Milena", "Nícolas", "Orlando", "Priscila", "Quirino", "Renata", "Sandro", "Tamires",
    "Uriel", "Valéria", "Ana", "Bruno", "Yuri", "Zenaide"
]



ID = 0

class paciente:
    
    def __init__(self,nome):
        global ID
        self.nome = nome
        self.id = ID
        ID += 1
        self.consultado = False
        self.visitas = 0
        self.dia_da_consulta = 0
        self.dia_do_retorno = None
        self.cidade = cidades[rand.randint(0,len(cidades)-1)]
        
        self.problema = doenças[rand.randint(0,len(doenças)-1)]
        for i in range(2):
            print(self.cidade['nome da cidade'])
            print(self.problema['região epidemica'])
            if self.problema['influencia da região'] == 'SIM' and self.problema['região epidemica'] != self.cidade['nome da cidade']:
                self.cidade = cidades[rand.randint(0,len(cidades)-1)]
        print()
        
    def show_doença(self):
        print(self.nome)
        self.visitas += 1
        for j in range(len(identificação)):
            print(f'{identificação[j]}: {self.problema[identificação[j]]}') 
        print(' ')
        if self.problema['região epidemica'] == self.cidade['nome da cidade']:
            print(f'{self.nome} pode ir ao seguintes medicos em sua cidade({self.problema['região epidemica']}):')
            #print(f'{self.nome} pode ir ao seguintes medicos em sua cidade({self.cidade['nome da cidade']}):')
            for medico,pessoa in self.cidade.items():
                if medico != 'nome da cidade':
                    print(f'{medico}:{pessoa}')
            print()
        print(f'a cidade de {self.nome} é {self.cidade['nome da cidade']}')
        print('')
    def voltar_ao_medico(self):
        self.retorno = 7
        
class cidade:
    def __init__(self):
        pass
pacientes_gerais = []
ids_validos = []

pacientes_para_voltar = []




def main():
    
    dia_max = 10
    dia = 0
    log = []
    pacientes = []
    calma = True
    pacientes_buffer =  []
    
    for i in range(dia_max):
        print(' ')
        calma = True
        for i in range(len(doenças)):
            print(11111111111)
            if dia % 7 == 0:
                print(8888888888888888)
                if doenças[i]['influencia da região'] == 'SIM':
                    doenças[i]['região epidemica'] = cidades[rand.randint(0,len(cidades)-1)]['nome da cidade']
                    print(f'a região epidemica de {doenças[i]['nome da doença']} mudou para {doenças[i]['região epidemica']}')
                    print()
        pacientes = []
        rand.shuffle(nomes)
        for i in range(2):
            pacientes_gerais.append(paciente(nomes[i]))
            
        for i,p1 in enumerate(pacientes_gerais):
            
            if p1.visitas == 0:
                p1.show_doença()
                p1.visitas += 1
                if p1.problema['precisa de revisita'] == 'SIM':
                    log.append(f'{p1.nome} precisa voltar daqui a 7 dias, retorne no dia {dia+7}')
                    p1.dia_da_consulta = dia
                    p1.dia_do_retorno = dia+7
            else:
                if p1.dia_do_retorno == dia:
                    print(f'o paciente {p1.nome} voltou para tratar {p1.problema['nome da doença']}')
                    p1.problema['precisa de revisita'] = 'NÃO'
                    p1.show_doença()
                    print('--------------------')    
        print(ids_validos)
        for i in range(len(log)):
            print(log[i])
        log = []
        print(F'DIA {dia}')
        
        while calma:
            print('responda com Y ou N')
            escolha = str(input("você quer ir ao proximo dia?"))
            if escolha.upper() == "Y":
                if dia < dia_max:
                    dia += 1
                calma = False
            else:
                calma = True
main()
        


