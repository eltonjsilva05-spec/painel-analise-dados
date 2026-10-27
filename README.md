# 📊 DataFlow Studio: Mini Pipeline ETL & ELT em Streamlit

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg)](https://www.sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Sobre o Projeto

O **DataFlow Studio** é uma aplicação web interativa desenvolvida em Python com **Streamlit**, projetada para demonstrar e comparar de forma prática dois dos principais paradigmas de engenharia de dados: **ETL (Extract, Transform, Load)** e **ELT (Extract, Load, Transform)**.

A ferramenta permite que o usuário faça o upload de arquivos brutos (CSV ou Excel), escolha a estratégia de processamento desejada, aplique transformações dinâmicas e visualize os resultados instantaneamente por meio de tabelas interativas e gráficos gerados em tempo real.

---

## 🛠️ Arquitetura e Abordagens Implementadas

1. **ETL (Extract, Transform, Load):**
   * **Extração:** Leitura direta do arquivo bruto carregado pelo usuário.
   * **Transformação:** Processamento, limpeza e agregação dos dados em memória utilizando a biblioteca **Pandas**.
   * **Carga/Exibição:** Exibição imediata dos dados tratados na interface visual e plotagem do gráfico.

2. **ELT (Extract, Load, Transform):**
   * **Extração & Carga (EL):** Ingestão imediata dos dados brutos diretamente em um banco de dados relacional **SQLite** em memória (`:memory:`).
   * **Transformação (T):** Execução de consultas analíticas utilizando **SQL** (`GROUP BY`, `SUM`, `ORDER BY`) para transformar os dados direto no banco.
   * **Exibição:** Recuperação do resultado via SQL e renderização no painel visual.

---

## 🚀 Funcionalidades

* **Upload Dinâmico:** Suporte para arquivos nos formatos `.csv` e `.xlsx` (Excel).
* **Seletor de Estratégia:** Alternância em tempo de execução entre os fluxos ETL e ELT.
* **Mapeamento Flexível:** Seleção automática de colunas textuais para agrupamento e colunas numéricas para métricas.
* **Visualização Analítica:** Renderização automática de tabelas responsivas e gráficos de barras interativos.

---

## 📋 Pré-requisitos

Certifique-se de ter o **Python** instalado em sua máquina. As principais bibliotecas utilizadas no projeto são:
* `streamlit`
* `pandas`
* `openpyxl` (para leitura de arquivos Excel)

---

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/eltonjsilva05-spec/painel-analise-dados.git](https://github.com/eltonjsilva05-spec/painel-analise-dados.git)
   cd painel-analise-dados
