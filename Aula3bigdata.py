import pandas as pd #importa a biblioteca pandas
import numpy as np #importa a biblioteca numpy
import matplotlib.pyplot as plt #importa a biblioteca matplotlib

Dados_x= np.linspace(0,10,10) # gera dados em x de 10
# em 10 valores
Dados_y = Dados_x * Dados_x # multiplica os dados de x 
# e armazena em y

plt.figure(figsize=(10,8),facecolor='gray') #Cria uma figura