import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar dados
df = pd.read_csv('2015.csv', sep=',')
print('Visualização inicial:')
print(df.head())

# 2. Informações gerais
print('\nInformações gerais:')
df.info()

print('\nEstatísticas descritivas:')
print(df.describe())

# 3. Limpeza de dados (se necessário)
df = df.dropna()

# 4. Correlações com a felicidade
correlacoes = df.corr(numeric_only=True)['Happiness Score'].sort_values(ascending=False)
print('\nCorrelação com a Pontuação de Felicidade:')
print(correlacoes)

# 5. Gráfico PIB per capita vs Felicidade
plt.figure(figsize=(8,5))
plt.scatter(df['Economy (GDP per Capita)'], df['Happiness Score'])
plt.xlabel('PIB per Capita')
plt.ylabel('Happiness Score')
plt.title('PIB per Capita x Felicidade')
plt.show()

# 6. Expectativa de vida vs Felicidade
plt.figure(figsize=(8,5))
plt.scatter(df['Health (Life Expectancy)'], df['Happiness Score'])
plt.xlabel('Expectativa de Vida')
plt.ylabel('Happiness Score')
plt.title('Expectativa de Vida x Felicidade')
plt.show()

# 7. Percepção de corrupção vs Felicidade
plt.figure(figsize=(8,5))
plt.scatter(df['Trust (Government Corruption)'], df['Happiness Score'])
plt.xlabel('Percepção de Corrupção')
plt.ylabel('Happiness Score')
plt.title('Corrupção x Felicidade')
plt.show()

# 8. Média de felicidade por região
media_regiao = df.groupby('Region')['Happiness Score'].mean().sort_values(ascending=False)
print('\nMédia de Felicidade por Região:')
print(media_regiao)

media_regiao.plot(kind='bar', figsize=(10,6))
plt.title('Felicidade Média por Região')
plt.ylabel('Happiness Score')
plt.show()

print(df['Economy (GDP per Capita)'].head(10))