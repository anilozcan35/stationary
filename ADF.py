import pandas as pd
import seaborn as sns
import numpy as np
from statsmodels.tsa.stattools import adfuller

# import data
df = sns.load_dataset("flights")
# map
df["month"].unique().tolist()
month_map = {"Jan" : 1,
             "Feb": 2,
             "Mar": 3,
             "Apr": 4,
             "May": 5,
             "Jun": 6,
             "Jul": 7,
             "Aug": 8,
             "Sep": 9,
             "Oct": 10,
             "Nov": 11,
             "Dec": 12
             }

df["month"] = df["month"].replace(month_map)

# proper date
df["date"] = pd.to_datetime(df[["year","month"]].assign(day = 1))

# drop unnecce columns
df.drop(columns = ["year","month"],axis = 1, inplace = True)
# fix dataframe order
df = df[["date","passengers"]]

import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.ion()
plt.show()

# index
df.index = df["date"]
df.drop(columns = "date", axis = 1, inplace= True)

# difference and log to make data stationary
df["passengers"] = np.log(df["passengers"])
df["passengers"] = df["passengers"].diff()
# plot
df["passengers"].plot()
# drop null values
df.dropna(inplace= True)
# check if data is stationary
results = adfuller(df["passengers"])
df["passengers"].plot()

df.describe().T

# Turkey energy consumption - ADF analysis

# read excel
df_consumption = pd.read_excel(r"C:\Users\aozcan\Downloads\electric_consumption.xlsx",sheet_name='Book1',header=None)

# columns
df_consumption.columns = ["tarih","tuketim"]

# proper date format
df_consumption.tarih = pd.to_datetime(df_consumption.tarih)
# date to index
df_consumption.index = df_consumption.tarih
# drop unneccesary date column
df_consumption.drop(columns= "tarih", inplace= True)
# replace unneccesarry , to convert data to int64
df_consumption.tuketim = df_consumption.tuketim.str.replace(",", "")
# tuketim date to numeric
df_consumption.tuketim = pd.to_numeric(df_consumption.tuketim)
# info
df_consumption.info()

df_consumption.plot(color = "pink")

results = adfuller(df_consumption["tuketim"])
