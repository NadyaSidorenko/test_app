"""
Main application.
"""
from distutils.command.install import install
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
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
st.title('Визуализация датасетов')
from ns_app.test import test_v
# Настройка боковой панели
st.sidebar.title("Справка")
st.sidebar.info(
    """
    1. Выбор варианта "свой датасет"
        1.1 Загрузите файл в формате csv
        1.2 Выберите тип графика и оси
        1.3 Наслаждайтесь полученным графиком :)
    2. Выбор варианта "Titanic"
        Демонстрационный вариант без загрузки своего датасета. 
        2.1 Выберите тип графика и оси
        2.2 Наслаждайтесь полученным графиком :)
    """
)

experiment={'names':['свой датасет','Titanic']}#, 'Iris']}
df_e = pd.DataFrame(experiment)
option_e = st.selectbox(
   'Список датасетов',
    df_e['names'].unique())
if option_e=='свой датасет':
    uploaded_file = st.file_uploader("Выберете CSV файл", accept_multiple_files=False)
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe.head())
        graph_name={'names':['линейный','столбчатая диаграмма', 'точечный график']}
        df_g = pd.DataFrame(graph_name)
        option_g = st.selectbox(
           'Выбор графика',
            df_g['names'].unique())
        x_name={'names':list(dataframe.columns)}
        df_x = pd.DataFrame(x_name)
        option_x = st.selectbox(
           'Выбор оси Х',
            df_x['names'].unique())
        y_name={'names':list(dataframe.columns)}
        df_y = pd.DataFrame(y_name)
        option_y = st.selectbox(
           'Выбор оси Y',
            df_y['names'].unique())
        if option_g=='линейный':
            fig1=go.Figure()
            fig1 = px.line(dataframe, x=str(option_x), y=str(option_y))
            st.write(fig1)
        if option_g=='точечный график':
            fig1=go.Figure()
            fig1 = px.scatter(dataframe, x=str(option_x), y=str(option_y))
            st.write(fig1)
        if option_g=='столбчатая диаграмма':
            fig1=go.Figure()
            fig1 = px.bar(dataframe, x=str(option_x), y=str(option_y))
            st.write(fig1)
if option_e=='Titanic':
    titanic=pd.read_csv('titanic.csv')
    st.write(titanic)
    graph_name={'names':['линейный','столбчатая диаграмма', 'точечный график']}
    df_g = pd.DataFrame(graph_name)
    option_g = st.selectbox(
       'Выбор графика',
        df_g['names'].unique())
    x_name={'names':list(titanic.columns)}
    df_x = pd.DataFrame(x_name)
    option_x = st.selectbox(
       'Выбор оси Х',
        df_x['names'].unique())
    y_name={'names':list(titanic.columns)}
    df_y = pd.DataFrame(y_name)
    option_y = st.selectbox(
       'Выбор оси Y',
        df_y['names'].unique())
    if option_g=='линейный':
        fig1=go.Figure()
        fig1 = px.line(titanic, x=str(option_x), y=str(option_y))
        st.write(fig1)
    if option_g=='точечный график':
        fig1=go.Figure()
        fig1 = px.scatter(titanic, x=str(option_x), y=str(option_y))
        st.write(fig1)
    if option_g=='столбчатая диаграмма':
        fig1=go.Figure()
        fig1 = px.bar(titanic, x=str(option_x), y=str(option_y))
        st.write(fig1)
    if st.button('Статистический анализ'):
        pval_amb=test_v(titanic.query('Sex=="male"')['PassengerId'].nunique(),
                           titanic['PassengerId'].nunique(),
                           titanic.query('Sex=="female"')['PassengerId'].nunique(),
                           titanic['PassengerId'].nunique())
        if pval_amb<0.01:
            st.write('Доля женщин и мужчин различна')
        else:
            st.write('Статистически значимых различий между долями женщин и мужчин не найдено')        
        fig_t=titanic.pivot_table(index=['Sex'], values='PassengerId', aggfunc='nunique').reset_index()
        fig_t['sex, %']=100*fig_t['PassengerId']/fig_t['PassengerId'].sum()
        fig = px.bar(fig_t, y=["sex, %"], x= "Sex",
                        labels=dict(Sex="пол", value="Доля уникальных пассажиров, %", variable="обозначения"))
        st.write(fig)
        st.write('Распределение возрастов пассажиров')
        fig2=np.histogram(titanic['Age'], bins=100, range=(0,titanic['Age'].max() ))[0]
        st.bar_chart(fig2)
# if option_e=='Iris':
#     file_name = 'https://raw.githubusercontent.com/tttdddnet/Python-Jupyter-Geo/main/data-9776-2020-12-21.csv'
#     df = pd.read_csv('test_iris.csv')
#     st.write(df)
