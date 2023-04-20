import json

#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na
#linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias
#devem ser ignorados no cálculo da média;

with open('dados.json', 'r') as file:
    dados = json.load(file)

menor_valor = float('inf')
maior_valor = float('-inf')
soma_valores = 0
dias_com_faturamento = 0
for dia in dados:
    if dia['valor'] > 0:
        soma_valores += dia['valor']
        dias_com_faturamento += 1
        if dia['valor'] < menor_valor:
            menor_valor = dia['valor']
        if dia['valor'] > maior_valor:
            maior_valor = dia['valor']
media_mensal = soma_valores / dias_com_faturamento

dias_acima_da_media = 0
for dia in dados:
    if dia['valor'] > media_mensal:
        dias_acima_da_media += 1

print(f'Menor valor do faturamento: R$ {menor_valor:.2f}')
print(f'Maior valor do faturamento: R$ {maior_valor:.2f}')
print(f'Quantos dias o faturamento ficou acima da média: {dias_acima_da_media}')