# =========================
# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# =========================

# Pandas é utilizado para carregar, organizar, limpar e analisar os dados
import pandas as pd

# Matplotlib é utilizado para criar gráficos
import matplotlib.pyplot as plt


# =========================
# 2. CARREGAMENTO DOS DADOS
# =========================

# Lê o arquivo CSV e armazena os dados na variável "dados"
# O resultado é um DataFrame (uma estrutura semelhante a uma tabela)
dados = pd.read_csv("vendas_carros.csv")


# =========================
# 3. EXPLORAÇÃO INICIAL DOS DADOS
# =========================

# Exibe os 5 primeiros registros da base
# Isso permite ter uma primeira visão dos dados
print(dados.head())

# Mostra a quantidade de linhas e colunas da base
# Nossa base original possui 4.345 linhas e 9 colunas
print(dados.shape)

# Mostra os nomes de todas as colunas
print(dados.columns)

# Mostra informações sobre:
# - quantidade de registros
# - valores não nulos
# - tipos de dados de cada coluna
dados.info()

# Verifica a quantidade de valores ausentes (nulos)
# em cada coluna da base
print(dados.isnull().sum())

# Calcula o percentual de valores ausentes na coluna Price
# isnull() identifica valores ausentes
# mean() calcula a proporção
# multiplicamos por 100 para transformar em porcentagem
print(
    "Percentual sem preço:",
    dados["Price"].isnull().mean() * 100
)

# Calcula o percentual de valores ausentes na coluna EngineV
print(
    "Percentual sem EngineV:",
    dados["EngineV"].isnull().mean() * 100
)


# =========================
# 4. LIMPEZA DOS DADOS
# =========================

# Remove registros que não possuem Price ou EngineV
# Criamos uma nova base chamada "dados_limpos"
# Assim, a variável "dados" continua contendo os dados originais
dados_limpos = dados.dropna(
    subset=["Price", "EngineV"]
)

# Mostra o tamanho da base após a limpeza
# A base limpa ficou com 4.025 linhas e 9 colunas
print(dados_limpos.shape)


# =========================
# 5. ANÁLISE ESTATÍSTICA
# =========================

# Mostra estatísticas das colunas numéricas:
# count = quantidade de valores
# mean = média
# std = desvio padrão
# min = menor valor
# 25% = primeiro quartil (Q1)
# 50% = mediana (Q2)
# 75% = terceiro quartil (Q3)
# max = maior valor
print(dados_limpos.describe())

# Mostra especificamente as estatísticas da coluna Price
print(dados_limpos["Price"].describe())

# Mostra os 10 veículos com os maiores preços
# nlargest() seleciona os maiores valores da coluna Price
# Depois escolhemos apenas Brand, Model, Year e Price
print(
    dados_limpos.nlargest(10, "Price")[
        ["Brand", "Model", "Year", "Price"]
    ]
)


# =========================
# 6. ANÁLISE DE OUTLIERS
# =========================

# Calcula o primeiro quartil (Q1)
# Q1 representa o ponto de 25% da distribuição dos preços
Q1 = dados_limpos["Price"].quantile(0.25)

# Calcula o terceiro quartil (Q3)
# Q3 representa o ponto de 75% da distribuição dos preços
Q3 = dados_limpos["Price"].quantile(0.75)

# Calcula o intervalo interquartil (IQR)
# IQR = Q3 - Q1
IQR = Q3 - Q1

# Exibe os valores encontrados
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

# Calcula os limites utilizados para identificar
# possíveis valores extremos (outliers)
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print("Limite inferior:", limite_inferior)
print("Limite superior:", limite_superior)

# Filtra somente os veículos cujo preço está
# acima do limite superior calculado pelo IQR
outliers_preco = dados_limpos[
    dados_limpos["Price"] > limite_superior
]

# shape[0] retorna somente a quantidade de linhas
# Encontramos 355 possíveis outliers de preço
print(
    "Quantidade de outliers de preço:",
    outliers_preco.shape[0]
)

# Calcula qual percentual da base limpa
# é formado pelos possíveis outliers
percentual_outliers = (
    outliers_preco.shape[0]
    / dados_limpos.shape[0]
) * 100

# :.2f exibe o resultado com duas casas decimais
print(
    f"Percentual de outliers: {percentual_outliers:.2f}%"
)


# =========================
# 7. VISUALIZAÇÃO DOS DADOS
# =========================

# Cria um histograma da coluna Price
# O histograma ajuda a visualizar como os preços
# estão distribuídos na base
# bins=30 divide os preços em 30 intervalos
plt.hist(
    dados_limpos["Price"],
    bins=30
)

# Define o título do gráfico
plt.title(
    "Distribuição dos preços dos veículos"
)

# Define o nome do eixo horizontal (X)
plt.xlabel("Preço")

# Define o nome do eixo vertical (Y)
plt.ylabel("Quantidade de veículos")

# O comando abaixo está temporariamente comentado
# para o gráfico não abrir toda vez que executamos
# o programa durante os testes
# plt.show()


# =========================
# 8. ANÁLISE POR MARCA
# =========================

# Conta quantos veículos existem de cada marca
# value_counts() conta quantas vezes cada valor
# aparece na coluna Brand
quantidade_marcas = (
    dados_limpos["Brand"].value_counts()
)

# Exibe a quantidade de veículos por marca
print(quantidade_marcas)

# CONCLUSÃO:
# A Volkswagen possui a maior quantidade de registros
# na base limpa, com 880 veículos.
# Em seguida aparecem:
# Mercedes-Benz = 823
# BMW = 640
# Toyota = 510
#
# Importante:
# Não afirmamos que são as marcas "mais vendidas".
# Os dados mostram a quantidade de registros presentes
# na base analisada.


# Calcula a participação percentual de cada marca
#
# normalize=True:
# transforma a contagem em proporção
#
# mul(100):
# multiplica a proporção por 100,
# transformando-a em porcentagem
#
# round(2):
# arredonda o resultado para duas casas decimais
percentual_marcas = (
    dados_limpos["Brand"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

# Exibe o percentual de cada marca na base limpa
print(percentual_marcas)

# Exemplo de interpretação:
# Volkswagen = 21,86%
# Isso significa que aproximadamente 21,86%
# dos veículos da base limpa são Volkswagen.
# =========================
# 9. PREÇO MÉDIO POR MARCA
# =========================


# Agrupa os veículos por marca, calcula o preço médio
# e organiza o resultado do maior para o menor
preco_medio_marca = (
    dados_limpos.groupby("Brand")["Price"]
    .mean()
    .sort_values(ascending=False)
)

# Exibe o preço médio de cada marca
print(preco_medio_marca)
preco_medio_marca = (
    dados_limpos.groupby("Brand")["Price"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# Exibe o preço médio de cada marca
print(preco_medio_marca)
# =========================
# 10. QUILOMETRAGEM MÉDIA POR MARCA
# =========================

# Agrupa os veículos por marca e calcula
# a quilometragem média de cada uma
quilometragem_media = (
    dados_limpos.groupby("Brand")["Mileage"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

# Exibe a quilometragem média por marca
print(quilometragem_media)
# =========================
# 11. CORRELAÇÃO ENTRE QUILOMETRAGEM E PREÇO
# =========================

# Calcula a correlação entre Mileage e Price
# O resultado ajuda a verificar se existe relação
# entre a quilometragem do veículo e seu preço
correlacao = dados_limpos["Mileage"].corr(
    dados_limpos["Price"]
)

# Exibe a correlação arredondada para duas casas decimais
print("Correlação entre Mileage e Price:", round(correlacao, 2))
# CONCLUSÃO:
# A correlação entre Mileage e Price foi de -0.47.
# Isso indica uma correlação negativa moderada:
# na base analisada, veículos com maior quilometragem
# tendem a apresentar preços menores.
#
# Importante: correlação não significa causalidade.
# Outros fatores, como marca, modelo, ano e motor,
# também podem influenciar o preço do veículo.
# =========================
# 12. GRÁFICO: QUILOMETRAGEM X PREÇO
# =========================

# Cria um gráfico de dispersão (scatter)
# Cada ponto representa um veículo da base
# Eixo X = quilometragem
# Eixo Y = preço
plt.scatter(
    dados_limpos["Mileage"],
    dados_limpos["Price"]
)

# Define o título do gráfico
plt.title("Relação entre Quilometragem e Preço")

# Define o nome do eixo X
plt.xlabel("Quilometragem")

# Define o nome do eixo Y
plt.ylabel("Preço")

# Exibe o gráfico na tela
plt.show()
# =========================
# 13. INVESTIGAÇÃO DE VALORES EXTREMOS DE QUILOMETRAGEM
# =========================

# Mostra os 10 veículos com os maiores valores de Mileage
# para verificar possíveis valores extremos na base
maiores_quilometragens = dados_limpos.nlargest(
    10,
    "Mileage"
)

# Exibe apenas as colunas mais importantes para a análise
print(
    maiores_quilometragens[
        ["Brand", "Model", "Year", "Mileage", "Price"]
    ]
)
