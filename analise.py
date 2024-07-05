import pandas as pd
import numpy as np
from scipy.stats import kendalltau

class Analise:
    
    def __init__(self) -> None:
        self.df_animais = pd.read_csv('./dados/dados_animais.csv')
       
    def buscar_dados_por(self, campo, valor):
        return self.df_animais[self.df_animais[campo] == valor]

    def agrupar_df_por(self, df:pd.DataFrame, campo):
        df_agrupado = df.groupby(campo).size().reset_index(name='Quantidade')
        total_count = df_agrupado['Quantidade'].sum()
        df_agrupado['Porcentagem'] = ((df_agrupado['Quantidade'] / total_count) * 100).round(2)
        return df_agrupado
    
    def agrupar_df_por_avaliacao_ocular(self, df:pd.DataFrame, campo):
        df_bilateral = df[df[campo] == 'BILATERAL']
        df_completo = pd.concat([df, df_bilateral])
        df_agrupado = df_completo.groupby(campo).size().reset_index(name='Quantidade')
        total_count = df_agrupado['Quantidade'].sum()
        df_agrupado['Porcentagem'] = ((df_agrupado['Quantidade'] / total_count) * 100).round(2)
        return df_agrupado
    
    def calcular_media(self, df:pd.DataFrame, campo: str):
        return df[campo].mean().round(2)
    
    def calcular_minimo(self, df:pd.DataFrame, campo: str):
        return df[campo].min()
    
    def calcular_maximo(self, df:pd.DataFrame, campo: str):
        return df[campo].max()
    
    def calcular_std(self, df:pd.DataFrame, campo: str):
        return np.std(df[campo]).round(2)
    
    def calcular_qtd(self, df:pd.DataFrame):
        return len(df)
    
    def buscar_valores_distintos(self, df:pd.DataFrame, campo:str):
        return df[campo].unique()
    
    def count_valores_igual(self, df:pd.DataFrame, campo:str, valor):
        return len(df[df[campo] == valor])
    
    def buscar_dataframe_alteracao(self, df):
        df2 = pd.read_csv('./dados/dados_animais_alteracoes.csv')
        df_merged = pd.merge(df, df2, on='Animal', how='inner')  
        return df_merged[['alteracao', 'LOCALIZAÇÃO','tem_leishmaniose']]
    
    def buscar_colunas(self):
        df2 = pd.read_csv('./dados/dados_animais_alteracoes.csv')
        df_merged = pd.merge(self.df_animais, df2, on='Animal', how='inner')
        return df_merged.columns
    
    def buscar_correlacao(self, colum):
        df2 = pd.read_csv('./dados/dados_animais_alteracoes.csv')
        df_merged = pd.merge(self.df_animais, df2, on='Animal', how='inner') 
        
        correlacoes = []
        coluns = df_merged.columns
        campo_1 = df_merged[colum]
        for colum_2 in coluns:
            campo_2 = df_merged[colum_2]
            if colum != colum_2:
                corr, p_value = kendalltau(campo_1, campo_2)
                correlacoes.append({"coluna_1": colum, "coluna_2": colum_2, "correlcao":corr, "p_valor": p_value})
        return pd.DataFrame(correlacoes)