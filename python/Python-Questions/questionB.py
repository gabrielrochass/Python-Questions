#variáveis curtas -> significado nos comentários

x_steve = int(input())
z_steve = int(input())

x_hogsmeade = int(34)
z_hogsmeade = int(220)

x_kakariko = int(0)
z_kakariko = int(0)

x_solitude = int(140)
z_solitude = int(456)

dsh = ((x_steve - x_hogsmeade)**2 + (z_steve - z_hogsmeade)**2)**0.5 
dsk = ((x_steve - x_kakariko)**2 + (z_steve - z_kakariko)**2)**0.5
dss = ((x_steve - x_solitude)**2 + (z_steve - z_solitude)**2)**0.5

print (f'Distancia para Hogsmeade: {dsh:.2f}')
print (f'Distancia para Kakariko: {dsk:.2f}')
print (f'Distancia para Solitude: {dss:.2f}')