#!/usr/bin/python3

# Option A:
# BTYD Library:
# https://btyd.readthedocs.io/en/latest/index.html
# User Guide:
# https://btyd.readthedocs.io/en/latest/User%20Guide.html

# Option B:
# https://www.kaggle.com/code/mursideyarkin/buy-till-you-die-models-customer-lifetime-value/notebook


from btyd.datasets import load_cdnow_summary


def helloBTYD():
    data = load_cdnow_summary(index_col=[0])
    print(data.head())



