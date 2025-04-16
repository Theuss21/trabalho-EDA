import numpy as np

dias_total = 30
ciclos_hora = 60
ciclos_dia = ciclos_hora * 24
ciclos_total = dias_total * ciclos_dia

temperatura = np.random.uniform(10, 30, ciclos_total)
umidade = np.random.uniform(5, 100, ciclos_total)
pressoes = np.random.uniform(1010, 1025)

dia20_0 = 19 * dias_total
dias2_1 = 20 * dias_total

temp_dia20 = temperatura[dia20_0:dias2_1]
umid_dia20 = temperatura[dia20_0:dias2_1]
pres_dia20 = temperatura[dia20_0:dias2_1]

temp_min = np.min(temp_dia20)
temp_max = np.max(temp_dia20)
temp_med = np.mean(temp_dia20)

umid_min = np.min(umid_dia20)
umid_max = np.max(umid_dia20)
umid_med = np.mean(umid_dia20)

pres_min = np.min(pres_dia20)
pres_max = np.min(pres_dia20)
pres_med = np.mean(pres_dia20)

print('Estatísticas do dia 20:')
print(f'Temperatura mínima {temp_min:.1f}, máxima {temp_max:.1f} e a média foi de {temp_med:.1f}')
print(f'Umidade mínima {umid_min:.1f}, máxima {umid_max:.1f} e a média foi de {umid_med:.1f}')
print(f'Pressão mínima {pres_min:.1f}, máxima {pres_max:.1f} e a média foi de {pres_med:.1f}')