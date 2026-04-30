# 📊 Financial Insights: Data Analysis & Visualization

Este projeto é uma ferramenta de **ETL (Extract, Transform, Load)** e análise exploratória de dados financeiros desenvolvida em Python. O sistema automatiza a leitura de extratos bancários brutos, realiza o tratamento de tipos de dados e gera visualizações estratégicas para auxiliar na tomada de decisão financeira.

O foco principal aqui foi aplicar **boas práticas de engenharia de dados**, como modularização, tipagem e separação de responsabilidades.

## 🧠 Conceitos de Dados Aplicados

* **Manipulação de DataFrames:** Uso intensivo da biblioteca `Pandas` para estruturar dados tabulares.
* **Time Series Transformation:** Conversão de strings e formatos variados para objetos `datetime`, permitindo análises temporais e extração de períodos (meses/anos).
* **Agregação e Agrupamento:** Implementação de funções de `groupby` e operações de soma para transformar micro-dados em métricas macro.
* **Visualização de Dados:** Geração de gráficos de barras via `Matplotlib` para traduzir números em insights visuais rápidos.
* **Modularização:** Código estruturado em módulos independentes (`analisador_excel.py` e `main.py`), facilitando a manutenção e a reutilização de funções.

## 🛠️ Tecnologias e Bibliotecas

* **Python 3.10+**
* **Pandas:** Motor principal para processamento de dados.
* **Matplotlib:** Biblioteca para visualização gráfica.
* **Openpyxl:** Engine de integração para leitura de arquivos Excel (`.xlsx`).

## 📁 Estrutura do Projeto

```plaintext
├── analisador_excel.py  # Módulo de Processamento (Lógica, Limpeza e Gráficos)
├── main.py              # Script de Execução (Orquestrador do fluxo)
├── meu_extrato.xlsx     # Dataset de entrada (Gerado automaticamente para teste)
└── README.md            # Documentação do projeto