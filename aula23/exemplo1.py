from datetime import datetime
import pandas as pd
import polars as pl

# Obtendo dados

try:
    ENDERECO_DADOS = r'./../dados/'
    
    hora_inicio = datetime.now()

    print('Carregando...')

    # df_janeiro = pd.read_csv(ENDERECO_DADOS + '202501_NovoBolsaFamilia.CSV', sep=';', encoding='iso-8859-1')
    df_janeiro = pl.read_csv(ENDERECO_DADOS + '202501_NovoBolsaFamilia.CSV', separator=';', encoding='iso-8859-1')
    
    print(df_janeiro.head())

    hora_final = datetime.now()

    print(f'Tempo de execução: {hora_final - hora_inicio}')

except Exception as e:
    print(f'Erro ao obter dados {e}')
