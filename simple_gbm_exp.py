#%%
import warnings
from datetime import datetime
import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt
import mplfinance        as mpf
warnings.filterwarnings('ignore')


#%%


#%%
mu          = 0.025
sigma       = 0.123
start_price = 1000
size        = 300
timeframe   = 5

returns = np.random.normal(loc=mu, scale=sigma, size=size)
prices  = start_price*(1+returns).cumprod()

df = pd.DataFrame()
df['price'] = prices

start_dt = datetime.strptime("12/1/2020 11:12:00.000000", "%d/%m/%Y %H:%M:%S.%f")
df['datetime'] = [pd.to_datetime(start_dt+pd.DateOffset(minutes=offset)) for offset in range(0, len(df))]

df = df.set_index(pd.DatetimeIndex(df['datetime']))
df = df.drop(['datetime'], axis=1)

df_xm = df['price'].resample(f"{timeframe}Min").ohlc()
df_xm['Volume'] = 1.0 + np.random.sample(len(df_xm)) * 15
df_xm = df_xm.rename(columns={"open": "Open", "high": "High", "low":"Low", "close":"Close"})

mpf.plot(df_xm, type='candle', style='yahoo', volume=True)


#%%

#%%
df_xm['Close'].hist(bins=160)

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%


#%%

#%%

