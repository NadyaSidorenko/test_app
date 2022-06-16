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
import seaborn as sns
import os as os
import pandas as pd
import numpy as np
from pathlib import Path
import tkinter
import _tkinter
#import tkFileDialog
import tkinter.filedialog
from ns_app.download import csv_download_link
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
    titanic=pd.read_csv('ns_app/Titanic.csv')
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
    def mpoint(lat, lon):
        return (np.average(lat), np.average(lon))
    def draw_map_cases():
        # fig_m = px.choropleth(df, locations="iso_code",
        #                  color="NumberOfAccessPoints",
        #                  hover_name="location",
        #                  title="Количество точек доступа",
        #                  color_continuous_scale=px.colors.sequential.Redor)
        fig_m=plt.scatter(x=df['Longitude_WGS84'], y=df['Latitude_WGS84'])
        return fig_m
    m = Map(center=(55.753215, 37.622504), zoom=11)
    fig_m=plt.scatter(x=df['Longitude_WGS84'], y=df['Latitude_WGS84'])
    m.add_layer(fig_m)
