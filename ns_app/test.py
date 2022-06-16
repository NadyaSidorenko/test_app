from scipy import stats as sts 
import math as mth
import pandas as pd
import numpy as np

#функции для проверки гипотез
def test_v(purchases1,leads1, purchases2,leads2):
    # пропорция успехов в группе group1:
    p1 = purchases1/leads1
    # пропорция успехов в группе group2:
    p2 = purchases2/leads2
    # пропорция успехов в комбинированном датасете:
    p_combined = (purchases1+purchases2)/(leads1+leads2)
    # разница пропорций в датасетах
    difference = p1 - p2 
    # считаем статистику в ст.отклонениях стандартного нормального распределения
    z_value = difference / mth.sqrt(p_combined * (1 - p_combined) * (1/leads1 + 1/leads2))
    #задаем стандартное нормальное распределение (среднее 0, ст.отклонение 1)
    distr = sts.norm(0, 1) 
    p_value = (1 - distr.cdf(abs(z_value))) * 2
    return p_value