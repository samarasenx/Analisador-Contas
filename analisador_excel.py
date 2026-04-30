import pandas as pd
import matplotlib.pyplot as plt

def carregar_e_limpar(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    df['Data'] = pd.to_datetime(df['Data'])
    df['Valor'] = pd.to_numeric(df['Valor'])
    return df

def gastos_por_categoria(df):
    # Retorna os dados agrupados (útil para o gráfico e para o texto)
    return df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)

def gerar_grafico_gastos(resumo_categorias):
    """
    Recebe o resumo agrupado e gera um gráfico de barras.
    """
    plt.figure(figsize=(10, 6)) # Define o tamanho da imagem
    resumo_categorias.plot(kind='bar', color='skyblue', edgecolor='black')
    
    plt.title('Gastos Totais por Categoria', fontsize=14)
    plt.xlabel('Categoria', fontsize=12)
    plt.ylabel('Valor (R$)', fontsize=12)
    plt.xticks(rotation=45) # Rotaciona os nomes para não sobrepor
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout() # Ajusta as margens
    plt.show() # Abre a janela com o gráfico

def obter_resumo_mensal(df):
    # Agrupa pelo mês (extraído da data) e soma os valores
    # O .dt.to_period('M') transforma a data em algo como '2023-05'
    resumo = df.groupby(df['Data'].dt.to_period('M'))['Valor'].sum()
    return resumo