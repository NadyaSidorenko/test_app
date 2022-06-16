"""
Main application.
"""
from distutils.command.install import install
#pip install pandas
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import scipy.stats as stats
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import os as os
import pandas as pd
import numpy as np
from pathlib import Path
from download import csv_download_link
#название приложения
st.title('Сервис для работы с датасетами')
from ns_app.test import test_v
# Настройка боковой панели
st.sidebar.title("Справка")
st.sidebar.info(
    """
    Здесь будет располагаться инструкция по работе с приложением.
    """
)

# lst={'names':['Titanic', 'Iris']}
# df = pd.DataFrame(lst)
# option = st.selectbox(
#    'Выбор датасета',
#     df['names'].unique())

experiment={'names':['Titanic', 'map']}
df_e = pd.DataFrame(experiment)
option_e = st.selectbox(
   'Список датасетов',
    df_e['names'].unique())
if option_e=='Titanic':
    titanic=pd.read_csv('titanic.csv')
    st.write(titanic)
    if st.button('Статистический анализ'):
        pval_amb=test_v(titanic.query('Sex=="male"')['PassengerId'].nunique(),
                           titanic['PassengerId'].nunique(),
                           titanic.query('Sex=="female"')['PassengerId'].nunique(),
                           titanic['PassengerId'].nunique())
        if pval_amb<0.01:
            st.write('Доля женщин и мужчин различна')
        else:
            st.write('Статистически значимых различий между долями женщин и мужчин не найдено')
        #fig=sns.histplot(data=titanic, x="Sex", multiple="dodge", shrink=.8)
        
        fig_t=titanic.pivot_table(index=['Sex'], values='PassengerId', aggfunc='nunique').reset_index()
        fig_t['sex, %']=100*fig_t['PassengerId']/fig_t['PassengerId'].sum()
        fig = px.bar(fig_t, y=["sex, %"], x= "Sex",
                        labels=dict(Sex="пол", value="Доля уникальных пассажиров, %", variable="обозначения"))
        st.write(fig)
        #fig2=sns.histplot(data=titanic, x="Age", hue="Sex")
        fig2=np.histogram(titanic['Age'], bins=100, range=(0,titanic['Age'].max() ))[0]
        st.bar_chart(fig2)
if option_e=='map':
    file_name = 'https://raw.githubusercontent.com/tttdddnet/Python-Jupyter-Geo/main/data-9776-2020-12-21.csv'
    df = pd.read_csv(file_name, sep=';', encoding='cp1251')
    gmaps.configure(api_key='...')

    wifi_points = []
    i = 0
    while i < len(df.index):
        wifi_points.append({'Coordinates': [df['Latitude_WGS84'][i], df['Longitude_WGS84'][i]], 'Location': df['Location'][i], 'NumberOfAccessPoints': df['NumberOfAccessPoints'][i]})
        i += 1

    marker_coordinates = [wifi['Coordinates'] for wifi in wifi_points]
    marker_coordinates = [[float(x) for x in y] for y in marker_coordinates] # здесь мы проходимся по элементами вложенных списков и меняем их типы со str на float

    info_box_template = """
    <dl>
    <dt>Адрес:</dt><dd>{Location}</dd>
    <dt>Количество точек доступа:</dt><dd>{NumberOfAccessPoints}</dd>
    </dl>
    """

    marker_info  = [info_box_template.format(**points) for points in wifi_points]
    marker_layer = gmaps.marker_layer(marker_coordinates, info_box_content=marker_info )

    fig = gmaps.figure()
    fig.add_layer(marker_layer)
    fig
