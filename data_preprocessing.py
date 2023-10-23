import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Data\weather_data\weatherstats_toronto_normal_daily.csv')
pollution_data_1 = pd.read_csv('Data\PM2.5\PM2.5_2003_2012.csv')
pollution_data_2 = pd.read_csv('Data\PM2.5\PM2.5_2013_2022.csv')
print(data.head())