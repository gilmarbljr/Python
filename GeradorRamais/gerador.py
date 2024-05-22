start = 4001
end = 4044
parameters = [
    'outboundproxy=192.168.1.35',
    'qualify=3000'
]

def geradorRange(start : int, end : int, parameters : list):
    for i in range(start,end+1,1):
        print('[{}](+)'.format(i))
        for parameter in parameters:
            print(parameter)
        print()

geradorRange(start,end,parameters)