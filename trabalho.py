camisa_a = {'P': 3, 'G': 6}
camisa_b = {'P': 1, 'G': 5}
camisa_c = {'P': 3, 'G': 5}

fabricacao_maio = {'A': 100, 'B': 50, 'C': 50}
fabricacao_junho = {'A': 50, 'B': 100, 'C': 50}

total_botao_maio = 0
for modelo, quantidade in fabricacao_maio.items():
    if modelo == 'A':
        total_botao_maio += camisa_a['P']*quantidade + camisa_a['G']*quantidade
    elif modelo == 'B':
        total_botao_maio += camisa_b['P']*quantidade + camisa_b['G']*quantidade
    elif modelo == 'C':
        total_botao_maio += camisa_c['P']*quantidade + camisa_c['G']*quantidade

total_botao_junho = 0
for modelo, quantidade in fabricacao_junho.items():
    if modelo == 'A':
        total_botao_junho += camisa_a['P']*quantidade + camisa_a['G']*quantidade
    elif modelo == 'B':
        total_botao_junho += camisa_b['P']*quantidade + camisa_b['G']*quantidade
    elif modelo == 'C':
        total_botao_junho += camisa_c['P']*quantidade + camisa_c['G']*quantidade

print("Total de botões usados em maio: ", total_botao_maio)
print("Total de botões usados em junho: ", total_botao_junho)