# Ramal inicial
start = 1000

# Ramal final
end = 1005

# Adicionar os parametros para cada ramal
parameters = [
    'outboundproxy=x.x.x.x',
    'qualify=3000',
    'parameter=blablabla'
]

# Definição da função
# verificar o (+), caso não necessitar basta remover no arquivo 
def geradorRange(start : int, end : int, parameters : list):
    for i in range(start,end+1,1):
        print('[{}](+)'.format(i))
        for parameter in parameters:
            print(parameter)
        print()

geradorRange(start,end,parameters)