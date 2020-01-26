#numeric_column: The target that you want to forecast
#iterations: The number of forecast you want to make
#t_intervals: how many forecast you want to make. it can be number of day for a time series data.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
def monte_carlo_simulation(numeric_column, iterations, t_intervals):
    log_returns = np.log(1 + numeric_column.pct_change())
    u = log_returns.mean() #Mean of the logarithmich return
    var = log_returns.var() #Variance of the logarithic return
    drift = u - (0.5 * var) #drift / trend of the logarithmic return
    stdev = log_returns.std() #Standard deviation of the log return
    daily_returns = np.exp(drift + stdev * norm.ppf(np.random.rand(t_intervals, iterations)))
    S0 = numeric_column.iloc[-1]
    price_list = np.zeros_like(daily_returns)
    price_list[0] = S0
    for t in range(1, t_intervals):
        price_list[t] = price_list[t - 1] * daily_returns[t]
    price_list = pd.DataFrame(price_list)
    price_list['close'] = price_list[0]
    close = numeric_column
    close = pd.DataFrame(close)
    frames = [close, price_list]
    monte_carlo_forecast = pd.concat(frames)
    monte_carlo = monte_carlo_forecast.iloc[:,:].values
    import matplotlib.pyplot as plt
    plt.figure(figsize=(17,8))
    plt.plot(monte_carlo)
    plt.show()
    return plt
    
