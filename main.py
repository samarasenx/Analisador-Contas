import pandas as pd
import analisador_excel as analisador

# --- PASSO 0: Criar dados de teste caso o arquivo não exista ---
data_teste = {
    'Data': ['2023-01-10', '2023-01-15', '2023-01-20', '2023-01-25', '2023-02-01'],
    'Categoria': ['Alimentação', 'Transporte', 'Lazer', 'Alimentação', 'Assinaturas'],
    'Valor': [150.00, 50.00, 200.00, 80.00, 45.90]
}
pd.DataFrame(data_teste).to_excel("meu_extrato.xlsx", index=False)

# --- PASSO 1: Execução do Fluxo de Dados ---
try:
    print("\nIniciando análise...")
    
    # Carrega e limpa usando o módulo
    dados = analisador.carregar_e_limpar("meu_extrato.xlsx")
    
    # Processa os gastos por categoria
    resumo = analisador.gastos_por_categoria(dados)

    # Processa os gastos mensais
    mensal = analisador.obter_resumo_mensal(dados)
    
    # Exibe no terminal
    print("\nResumo encontrado por categoria:\n")
    print(resumo.reset_index().to_string(index=False))
    print("\nResumo encontrado por mes:\n")
    print(mensal.reset_index().to_string(index=False))
    
    # PASSO NOVO: Gera a visualização
    print("\nGerando gráfico de visualização...\n")
    analisador.gerar_grafico_gastos(resumo)

except Exception as e:
    print(f"Ocorreu um erro: {e}")