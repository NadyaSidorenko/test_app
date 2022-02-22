"""
Main application.
"""
from distutils.command.install import install

import pandas as pd
import streamlit as st

import pandas as pd
import numpy as np

# Настройка боковой панели
st.sidebar.title("Справка")
st.sidebar.info(
    """
    Здесь будет располагаться инструкция по работе с приложением.
    """
)

lst={'names':['1-тест МП', 'Другой']}
df = pd.DataFrame(lst)
option = st.selectbox(
   'Тип теста',
    df['names'].unique())
'Вы выбрали: ', option

experiment={'names':['1-Эксперименты добавления товаров', 'Другой']}
df_e = pd.DataFrame(experiment)
option_e = st.selectbox(
   'Список экспериментов',
    df_e['names'].unique())
'Вы выбрали: ', option_e

df_group=pd.DataFrame(np.random.randint(1000,10000,size=(100, 1)))
df_group=df_group.rename(columns={0:'cartnumber'})


df_test = pd.DataFrame({'list_n':[0,1,2,3,4,5,6,7,8,9]})
options_t = st.multiselect(
    'Выбор тестовой группы', 
    df_test['list_n'].unique())

options_k = st.multiselect(
    'Выбор контрольной группы', 
    df_test['list_n'].unique())

st.title('Сервис экспериментов и тестов на Streamlit')
x = st.slider('x')
st.write('выбор периода', x, 'дней')

st.sidebar.radio('кнопка', options=['Сформировать', 'Сохранить результаты'])
st.write(option, option_e, options_k, options_t)