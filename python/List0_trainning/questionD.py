#inputs
A = int(input())
L = int(input())
P = int(input())
horas = int(input())

#cálculo
AxL = int((A + L + abs(A - L)) / 2)
AxL_P = int(((AxL + P) + abs(AxL - P)) / 2)
resultado = AxL_P * horas

print(resultado)

