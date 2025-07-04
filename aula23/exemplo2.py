from datetime import datetime
import pandas as pd
import polars as pl

# Obtendo dados

try:
    ENDERECO_DADOS = r'./../dados/'
    
    hora_inicio = datetime.now()

    print('Carregando...')
    print(hora_inicio)

    lista_arquivos = ['202501_NovoBolsaFamilia.CSV',
                      '202502_NovoBolsaFamilia.CSV',
                      '202503_NovoBolsaFamilia.CSV',
                      '202504_NovoBolsaFamilia.CSV',
                      '202505_NovoBolsaFamilia.CSV']
    
    df_bolsa_familia = None
      
    for arquivo in lista_arquivos:
        print(f'Processando o arquivo {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat((df_bolsa_familia, df))
        
        print(df)
        print(df.shape)

        del df

    print('Bolsa família concatenado')
    print(df_bolsa_familia.head())
    print(df_bolsa_familia.shape)
    
    hora_final = datetime.now()

    print(f'Tempo de execução: {hora_final - hora_inicio}')

except Exception as e:
    print(f'Erro ao obter dados {e}')
