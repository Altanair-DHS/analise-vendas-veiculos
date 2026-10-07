# 📊 Análise de Vendas de Veículos

Projeto de análise de dados desenvolvido com **Python, Pandas, Matplotlib e Power BI**, com o objetivo de explorar uma base de dados de veículos e transformar os dados em informações úteis para análise.

## 🎯 Objetivo do projeto

Analisar uma base de dados de veículos, realizando etapas de:

- exploração dos dados;
- identificação de valores ausentes;
- limpeza da base;
- análise estatística;
- identificação de possíveis outliers;
- análise da quantidade de veículos por marca;
- análise de preços;
- criação de visualizações;
- desenvolvimento de dashboard no Power BI.

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Power BI
- Visual Studio Code
- Git e GitHub

## 🧹 Tratamento dos dados

A base original possui **4.345 registros**.

Durante a análise foram identificados valores ausentes nas colunas `Price` e `EngineV`.

Após a remoção dos registros sem essas informações, a base utilizada na análise ficou com:

**4.025 veículos**

## 📈 Algumas análises realizadas

A quantidade de veículos por marca encontrada na base tratada foi:

| Marca | Quantidade |
|---|---:|
| Volkswagen | 880 |
| Mercedes-Benz | 823 |
| BMW | 640 |
| Toyota | 510 |
| Renault | 445 |
| Audi | 420 |
| Mitsubishi | 307 |

A Volkswagen é a marca com maior quantidade de veículos na base analisada, representando aproximadamente **21,86%** dos registros após a limpeza.

## 📊 Dashboard Power BI

Foi desenvolvido um dashboard no Power BI para visualizar os principais resultados da análise, incluindo:

- quantidade de veículos por marca;
- preço médio por marca.

## 🔎 Análise de outliers

Utilizando o método do intervalo interquartil (IQR), foram identificados **355 possíveis outliers de preço**, correspondentes a aproximadamente **8,82%** da base tratada.

Esses registros não foram automaticamente excluídos, pois preços elevados podem representar veículos de maior valor e não necessariamente erros nos dados.

## 🚀 Próximas melhorias

Como evolução do projeto, poderão ser adicionados:

- novas visualizações;
- análises de preço por ano e quilometragem;
- correlação entre as variáveis;
- modelo de regressão para estimativa de preços.

## 👨‍💻 Autor

**Altanair da Hora Silva**

Projeto desenvolvido para aprendizado e construção de portfólio em **Análise de Dados e Ciência de Dados**.