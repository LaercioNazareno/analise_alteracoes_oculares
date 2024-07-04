import altair as alt
import streamlit as st
from analise import Analise

analise = Analise()

st.title('Análise estatistica dos dados')

analise_txt = f'''
    Análise comparativa dos grupos de animas que contrariam e não contrairam a leishmaniose 
'''
st.write(analise_txt)
########################################################################################################################
st.header('Análise Populacional')
########################################################################################################################
df = analise.df_animais
qtd_total = analise.calcular_qtd(df)
df_agrupado = analise.agrupar_df_por(df, 'RAÇA')

analise_txt = f'''
    A base de dados contém {qtd_total} avaliações de animais, distribuido da seguinte maneira:\n
'''
st.write(analise_txt)

bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('RAÇA', title='RAÇA', sort='-x'),
    color='RAÇA'
).properties(
    title=f'Quantidade de animais'
)
st.altair_chart(bar_chart, use_container_width=True)
########################################################################################################################
st.subheader('Idade')
df_agrupado = analise.agrupar_df_por(df, 'IDADE')
media = analise.calcular_media(df, 'IDADE')
maxima = analise.calcular_maximo(df, 'IDADE')
minima = analise.calcular_minimo(df, 'IDADE')
dv = analise.calcular_std(df, 'IDADE')

analise_txt = f'''
    O animal mais novo tem {minima} anos, \n
    o animal mais velho tem {maxima} anos,\n
    a média de idade da populção é de {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('TLS OD')
media = analise.calcular_media(df, 'TLS OD')
maxima = analise.calcular_maximo(df, 'TLS OD')
minima = analise.calcular_minimo(df, 'TLS OD')
dv = analise.calcular_std(df, 'TLS OD')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('TLS OE')
media = analise.calcular_media(df, 'TLS OE')
maxima = analise.calcular_maximo(df, 'TLS OE')
minima = analise.calcular_minimo(df, 'TLS OE')
dv = analise.calcular_std(df, 'TLS OE')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('PIO OD')
media = analise.calcular_media(df, 'PIO OD')
maxima = analise.calcular_maximo(df, 'PIO OD')
minima = analise.calcular_minimo(df, 'PIO OD')
dv = analise.calcular_std(df, 'PIO OD')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('PIO OE')
media = analise.calcular_media(df, 'PIO OE')
maxima = analise.calcular_maximo(df, 'PIO OE')
minima = analise.calcular_minimo(df, 'PIO OE')
dv = analise.calcular_std(df, 'PIO OE')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('Teste de fluorosceína')
qtd_positivo = analise.count_valores_igual(df, 'Teste de fluorosceína', 1)
qtd_negativo = analise.count_valores_igual(df, 'Teste de fluorosceína', 0)
analise_txt = f'''
    valores positivos:\n
    \tquantidade: {qtd_positivo}
    \tporcentagem: {round((qtd_positivo/qtd_total)*100, 2)} %
    \n
    valores negativos:\n
    \tquantidade: {qtd_negativo}
    \tporcentagem: {round((qtd_negativo/qtd_total)*100, 2)} %
    \n
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('DIAGNÓSTICOS')

diagnosticos_distintos = analise.buscar_valores_distintos(df, 'DIAGNÓSTICO')
df_agrupado = analise.agrupar_df_por(df, ['DIAGNÓSTICO', 'LOCALIZAÇÃO'])

analise_txt = f'''
    A base de dados contém {len(diagnosticos_distintos)} direfentes tipos DIAGNÓSTICOS que são distribuidos daseguinte maneira:\n
'''
st.write(analise_txt)

st.dataframe(df_agrupado)
bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('DIAGNÓSTICO', title='DIAGNÓSTICO', sort='-x'),
    color='DIAGNÓSTICO'
).properties(
    title=f'Quantidade de DIAGNÓSTICO'
)
st.altair_chart(bar_chart, use_container_width=True)
########################################################################################################################
st.subheader('DIAGNÓSTICOS')

diagnosticos_distintos = analise.buscar_valores_distintos(df, 'DIAGNÓSTICO')
df_agrupado = analise.agrupar_df_por(df, ['DIAGNÓSTICO', 'LOCALIZAÇÃO'])

analise_txt = f'''
    A base de dados contém {len(diagnosticos_distintos)} direfentes tipos DIAGNÓSTICOS que são distribuidos daseguinte maneira:\n
'''
st.write(analise_txt)

st.dataframe(df_agrupado)
bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('DIAGNÓSTICO', title='DIAGNÓSTICO', sort='-x'),
    color='DIAGNÓSTICO'
).properties(
    title=f'Quantidade de DIAGNÓSTICO'
)
st.altair_chart(bar_chart, use_container_width=True)
########################################################################################################################
st.subheader('Alterações')

df = analise.buscar_dataframe_alteracao(df)
diagnosticos_distintos = analise.buscar_valores_distintos(df, 'alteracao')
df_agrupado = analise.agrupar_df_por(df, 'alteracao')

analise_txt = f'''
    A base de dados contém {len(diagnosticos_distintos)} direfentes tipos alterações que são distribuidos daseguinte maneira:\n
'''
st.write(analise_txt)

st.dataframe(df_agrupado)
bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('alteracao', title='alterações', sort='-x'),
    color='alteracao'
).properties(
    title=f'Quantidade de alterações'
)
st.altair_chart(bar_chart, use_container_width=True)
########################################################################################################################
st.header('Análise dos animais sem leishmaniose')
########################################################################################################################

df = analise.buscar_dados_por(campo='tem_leishmaniose', valor=0)
qtd_total = analise.calcular_qtd(df)
df_agrupado = analise.agrupar_df_por(df, 'RAÇA')

analise_txt = f'''
    A base de dados contém {qtd_total} avaliações de animais, distribuido da seguinte maneira:\n
'''
st.write(analise_txt)

bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('RAÇA', title='RAÇA', sort='-x'),
    color='RAÇA'
).properties(
    title=f'Quantidade de animais'
)
st.altair_chart(bar_chart, use_container_width=True)
########################################################################################################################
st.subheader('Idade')
df_agrupado = analise.agrupar_df_por(df, 'IDADE')
media = analise.calcular_media(df, 'IDADE')
maxima = analise.calcular_maximo(df, 'IDADE')
minima = analise.calcular_minimo(df, 'IDADE')
dv = analise.calcular_std(df, 'IDADE')

analise_txt = f'''
    O animal mais novo tem {minima} anos, \n
    o animal mais velho tem {maxima} anos,\n
    a média de idade da populção é de {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('TLS OD')
media = analise.calcular_media(df, 'TLS OD')
maxima = analise.calcular_maximo(df, 'TLS OD')
minima = analise.calcular_minimo(df, 'TLS OD')
dv = analise.calcular_std(df, 'TLS OD')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('TLS OE')
media = analise.calcular_media(df, 'TLS OE')
maxima = analise.calcular_maximo(df, 'TLS OE')
minima = analise.calcular_minimo(df, 'TLS OE')
dv = analise.calcular_std(df, 'TLS OE')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('PIO OD')
media = analise.calcular_media(df, 'PIO OD')
maxima = analise.calcular_maximo(df, 'PIO OD')
minima = analise.calcular_minimo(df, 'PIO OD')
dv = analise.calcular_std(df, 'PIO OD')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('PIO OE')
media = analise.calcular_media(df, 'PIO OE')
maxima = analise.calcular_maximo(df, 'PIO OE')
minima = analise.calcular_minimo(df, 'PIO OE')
dv = analise.calcular_std(df, 'PIO OE')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('Teste de fluorosceína')
qtd_positivo = analise.count_valores_igual(df, 'Teste de fluorosceína', 1)
qtd_negativo = analise.count_valores_igual(df, 'Teste de fluorosceína', 0)
analise_txt = f'''
    valores positivos:\n
    \tquantidade: {qtd_positivo}
    \tporcentagem: {round((qtd_positivo/qtd_total)*100, 2)} %
    \n
    valores negativos:\n
    \tquantidade: {qtd_negativo}
    \tporcentagem: {round((qtd_negativo/qtd_total)*100, 2)} %
    \n
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('DIAGNÓSTICOS')

diagnosticos_distintos = analise.buscar_valores_distintos(df, 'DIAGNÓSTICO')
df_agrupado = analise.agrupar_df_por(df, ['DIAGNÓSTICO', 'LOCALIZAÇÃO'])

analise_txt = f'''
    A base de dados contém {len(diagnosticos_distintos)} direfentes tipos DIAGNÓSTICOS que são distribuidos daseguinte maneira:\n
'''
st.write(analise_txt)

st.dataframe(df_agrupado)
bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('DIAGNÓSTICO', title='DIAGNÓSTICO', sort='-x'),
    color='DIAGNÓSTICO'
).properties(
    title=f'Quantidade de DIAGNÓSTICO'
)
st.altair_chart(bar_chart, use_container_width=True)
########################################################################################################################
st.subheader('Alterações')

df = analise.buscar_dataframe_alteracao(df)
diagnosticos_distintos = analise.buscar_valores_distintos(df, 'alteracao')
df_agrupado = analise.agrupar_df_por(df, 'alteracao')

analise_txt = f'''
    A base de dados contém {len(diagnosticos_distintos)} direfentes tipos alterações que são distribuidos daseguinte maneira:\n
'''
st.write(analise_txt)

st.dataframe(df_agrupado)
bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('alteracao', title='alterações', sort='-x'),
    color='alteracao'
).properties(
    title=f'Quantidade de alterações'
)
st.altair_chart(bar_chart, use_container_width=True)
########################################################################################################################
st.header('Análise dos animais com leishmaniose')
########################################################################################################################

df = analise.buscar_dados_por(campo='tem_leishmaniose', valor=1)
qtd_total = analise.calcular_qtd(df)
df_agrupado = analise.agrupar_df_por(df, 'RAÇA')

analise_txt = f'''
    A base de dados contém {qtd_total} avaliações de animais, distribuido da seguinte maneira:\n
'''
st.write(analise_txt)

bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('RAÇA', title='RAÇA', sort='-x'),
    color='RAÇA'
).properties(
    title=f'Quantidade de animais'
)
st.altair_chart(bar_chart, use_container_width=True)
########################################################################################################################
st.subheader('Idade')
df_agrupado = analise.agrupar_df_por(df, 'IDADE')
media = analise.calcular_media(df, 'IDADE')
maxima = analise.calcular_maximo(df, 'IDADE')
minima = analise.calcular_minimo(df, 'IDADE')
dv = analise.calcular_std(df, 'IDADE')

analise_txt = f'''
    O animal mais novo tem {minima} anos, \n
    o animal mais velho tem {maxima} anos,\n
    a média de idade da populção é de {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('TLS OD')
media = analise.calcular_media(df, 'TLS OD')
maxima = analise.calcular_maximo(df, 'TLS OD')
minima = analise.calcular_minimo(df, 'TLS OD')
dv = analise.calcular_std(df, 'TLS OD')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('TLS OE')
media = analise.calcular_media(df, 'TLS OE')
maxima = analise.calcular_maximo(df, 'TLS OE')
minima = analise.calcular_minimo(df, 'TLS OE')
dv = analise.calcular_std(df, 'TLS OE')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('PIO OD')
media = analise.calcular_media(df, 'PIO OD')
maxima = analise.calcular_maximo(df, 'PIO OD')
minima = analise.calcular_minimo(df, 'PIO OD')
dv = analise.calcular_std(df, 'PIO OD')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('PIO OE')
media = analise.calcular_media(df, 'PIO OE')
maxima = analise.calcular_maximo(df, 'PIO OE')
minima = analise.calcular_minimo(df, 'PIO OE')
dv = analise.calcular_std(df, 'PIO OE')

analise_txt = f'''
    O menor valor encontrado {minima}, \n
    o maior valor encontrado {maxima},\n
    a média de valores é {media} com um desvio padrão de {dv}
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('Teste de fluorosceína')
qtd_positivo = analise.count_valores_igual(df, 'Teste de fluorosceína', 1)
qtd_negativo = analise.count_valores_igual(df, 'Teste de fluorosceína', 0)
analise_txt = f'''
    valores positivos:\n
    \tquantidade: {qtd_positivo}
    \tporcentagem: {round((qtd_positivo/qtd_total)*100, 2)} %
    \n
    valores negativos:\n
    \tquantidade: {qtd_negativo}
    \tporcentagem: {round((qtd_negativo/qtd_total)*100, 2)} %
    \n
'''
st.write(analise_txt)
########################################################################################################################
st.subheader('DIAGNÓSTICOS')

diagnosticos_distintos = analise.buscar_valores_distintos(df, 'DIAGNÓSTICO')
df_agrupado = analise.agrupar_df_por(df, ['DIAGNÓSTICO', 'LOCALIZAÇÃO'])

analise_txt = f'''
    A base de dados contém {len(diagnosticos_distintos)} direfentes tipos DIAGNÓSTICOS que são distribuidos daseguinte maneira:\n
'''
st.write(analise_txt)

st.dataframe(df_agrupado)
bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('DIAGNÓSTICO', title='DIAGNÓSTICO', sort='-x'),
    color='DIAGNÓSTICO'
).properties(
    title=f'Quantidade de DIAGNÓSTICO'
)
st.altair_chart(bar_chart, use_container_width=True)
########################################################################################################################
st.subheader('Alterações')

df = analise.buscar_dataframe_alteracao(df)
diagnosticos_distintos = analise.buscar_valores_distintos(df, 'alteracao')
df_agrupado = analise.agrupar_df_por(df, 'alteracao')

analise_txt = f'''
    A base de dados contém {len(diagnosticos_distintos)} direfentes tipos alterações que são distribuidos daseguinte maneira:\n
'''
st.write(analise_txt)

st.dataframe(df_agrupado)
bar_chart = alt.Chart(df_agrupado).mark_bar().encode(
    x=alt.X('Quantidade', title='Quantidade'),
    y=alt.Y('alteracao', title='alterações', sort='-x'),
    color='alteracao'
).properties(
    title=f'Quantidade de alterações'
)
st.altair_chart(bar_chart, use_container_width=True)

########################################################################################################################
st.header('Correlação')
########################################################################################################################

campo = st.selectbox("Selecione um campo", analise.buscar_colunas())
dados = analise.buscar_correlacao([campo])
st.dataframe(dados)