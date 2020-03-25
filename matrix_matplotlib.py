# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# %%
apl_price = [93.95, 112.15, 104.05, 144.85, 169.49]
ms_price = [39.01, 50.29, 57.05, 69.98, 94.39]
year = [2014, 2015, 2016, 2017, 2018]


# %%
plt.plot(
    year, apl_price, 'ok',
    year, ms_price, 'g',
)

plt.xlabel('Year')
plt.xlabel('Stock Price')

plt.axis([2013, 2019, 20, 180])

plt.show()

