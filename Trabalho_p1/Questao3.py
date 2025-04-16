def f(x):
    return x**3 - x - 2

def metodo_bissecao(a, b, precisao):
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos em a e b.")
    
    iteracao = 0
    while (b - a) / 2 > precisao:
        m = (a + b) / 2
        if abs(f(m)) < precisao:
            return m, iteracao
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
        iteracao += 1
    
    m = (a + b) / 2
    return m, iteracao

a, b = 1.0, 2.0
precisao = 1e-4

raiz, iteracoes = metodo_bissecao(a, b, precisao)
print(f"Raiz aproximada: {raiz:.6f}")
print(f"Número de iterações: {iteracoes}")
print(f"f(raiz) = {f(raiz):.10f}")