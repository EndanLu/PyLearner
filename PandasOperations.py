#!/usr/bin/python3

import pandas
from sklearn import linear_model

def testPandasLinearRegression():
    df = pandas.read_csv("cars.csv")

    X = df[['Weight', 'Volume']]
    y = df['CO2']

    regr = linear_model.LinearRegression()
    regr.fit(X.values, y.values)

    # 打印重量相对于 CO2 的系数值，以及体积相对于 CO2 的系数值。
    print(regr.coef_)

    # 预测重量为 2300kg、排量为 1300ccm 的汽车的二氧化碳排放量：
    predictedCO2 = regr.predict([[2300, 1300]])
    print(predictedCO2)


