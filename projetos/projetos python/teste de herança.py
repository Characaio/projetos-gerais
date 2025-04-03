


baguio =[
        ['isa', 13],
        ['caio',20],
        ['chagas',15],
        ['peixoto',26],
        ['robertin',43],
        ['carlin',100],
        ['soroso',23],
        ['cardoso',72],
        ['carlasso',4],
        ['robertasso',9]
    ]

class renderables:
    def __init__(self):
        pass
    def render(self):
        print('im rendering')
    def update(self):
        print('im moving')


class particle(renderables):
    def __init__(self,name,movement):
        self.name = name
        self.movement = movement

coisos = []
for i in range(len(baguio)):
    coisos.append(particle(baguio[i][0],baguio[i][1]))

for p1,i in enumerate(coisos):
    p1.render()
