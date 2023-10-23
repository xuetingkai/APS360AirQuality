import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Data\weather_data\weatherstats_toronto_normal_daily.csv')
pollution_data = pd.read_csv('Data\PM2.5\pollution_data.csv')

print(data.head())