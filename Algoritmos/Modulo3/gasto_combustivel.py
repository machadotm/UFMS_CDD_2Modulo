#!/usr/bin/env python
# coding: utf-8

# In[4]:

# Solicita ao usuário o tempo gasto, a velocidade média e o combustível utilizado para a viagem
tempo_gasto = float(input("Informe o tempo gasto na viagem (horas): "))
velocidade_media = float(input("Informe a velocidade média do percurso (km/h): "))
combustivel_utilizado = int(input("Informe a quantidade de combustível utilizado para a viagem (litro): "))

# Definindo a função que vai calcular o combustível gasto na viagem
def calcular_combustivel(tempo_gasto, velocidade_media, combustivel_utilizado):
    distancia = velocidade_media * tempo_gasto
    combustivel_gasto = distancia/combustivel_utilizado
    return combustivel_gasto

# Chama a função para calcular a quantidade de combustível gasto
quantidade_combustivel = calcular_combustivel(tempo_gasto, velocidade_media, combustivel_utilizado)

# Exibe o resultado
print(f"Quantidade de combustível gasto na viagem: {quantidade_combustivel} litros")





