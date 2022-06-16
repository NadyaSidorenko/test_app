"""
Download results.
"""

import base64

import streamlit as st

import pandas as pd
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', None, format1)
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def csv_download_link(df, sidebar=False):
    df_xlsx = to_excel(df)

    st.download_button(label='Скачать таблицу в excel', data=df_xlsx, file_name='Результаты.xlsx')


