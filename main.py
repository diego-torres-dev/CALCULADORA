def somar(n1: float, n2: float) -> float:
    '''Recebe dois números reais e retorna a soma deles'''
    return n1 + n2


def subtrair(n1: float, n2: float) -> float:
    '''Recebe dois números reais e retorna a diferença entre eles'''
    return n1 - n2


def multiplicar(n1: float, n2: float) -> float:
    '''Recebe dois números reais e retorna produto deles'''
    return n1 * n2


def dividir(n1: float, n2: float) -> float:
    '''Recebe dois números reais e retorna quociente deles'''
    return n1 / n2


def efetuar(operacao, n1: float, n2: float) -> float:
    '''Recebe dois números reais e retorna o resultado da operação entre eles'''
    return operacao(n1, n2)


print('Soma: {}'.format(somar(3, 5)))
print('Diferença: {}'.format(subtrair(3, 5)))
print('Produto: {}'.format(multiplicar(3, 5)))
print('Quociente: {}'.format(dividir(3, 5)))

print('Soma: {}'.format(efetuar(somar, 3, 5)))
print('Diferença: {}'.format(efetuar(subtrair, 3, 5)))
print('Produto: {}'.format(efetuar(multiplicar, 3, 5)))
print('Quociente: {}'.format(efetuar(dividir, 3, 5)))
