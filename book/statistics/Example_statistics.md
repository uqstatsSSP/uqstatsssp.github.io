# Examples Statistics with Python

Here are some examples of statistics in Python using Python libraries:

**Descriptive Statistics with NumPy**

```python
import numpy as np

# Create an array of data
data = np.array([1, 2, 3, 4, 5])

# Calculate the mean
mean = np.mean(data)
print("Mean:", mean)

# Calculate the median
median = np.median(data)
print("Median:", median)

# Calculate the standard deviation
std_dev = np.std(data)
print("Standard deviation:", std_dev)import numpy as np

# Create an array of data
data = np.array([1, 2, 3, 4, 5])

# Calculate the mean
mean = np.mean(data)
print("Mean:", mean)

# Calculate the median
median = np.median(data)
print("Median:", median)

# Calculate the standard deviation
std_dev = np.std(data)
print("Standard deviation:", std_dev)
```

**Hypothesis Testing with SciPy**

```python
from scipy import stats

# Create two arrays of data
data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([6, 7, 8, 9, 10])

# Perform a t-test to compare the means of the two groups
t_stat, p_value = stats.ttest_ind(data1, data2)
print("T-statistic:", t_stat)
print("P-value:", p_value)
```

**Data Exploration with Pandas**

```python
import pandas as pd

# Read in a dataset
data = pd.read_csv("data.csv")

# Calculate the mean by column
mean_by_column = data.mean()
print("Mean by column:")
print(mean_by_column)

# Calculate the correlation between two columns
corr = data["column1"].corr(data["column2"])
print("Correlation between column1 and column2:", corr)

# Create a histogram of a column
data["column3"].hist()
```

### Probability Distributions with SciPy

The SciPy library provides a variety of functions for working with probability distributions, including generating random samples and calculating probability density functions (PDFs) and cumulative distribution functions (CDFs). Here's an example of generating random samples from a normal distribution:

```python
from scipy.stats import norm

# Generate 1000 random samples from a normal distribution
samples = norm.rvs(loc=0, scale=1, size=1000)

# Calculate the PDF and CDF of the samples
pdf = norm.pdf(samples)
cdf = norm.cdf(samples)
```

**Linear Regression with scikit-Learn:**
The scikit-learn library provides a variety of machine-learning tools, including linear regression. Here's an example of fitting a linear regression model to a dataset:

```python
from sklearn.linear_model import LinearRegression

# Read in a dataset
data = pd.read_csv("data.csv")

# Separate the predictor and target variables
X = data[["predictor1", "predictor2"]]
y = data["target"]

# Fit a linear regression model
model = LinearRegression().fit(X, y)

# Print the coefficients and intercept
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
```

### Time Series Analysis with statsmodels

The statsmodels library provides a variety of tools for time series analysis, including autoregressive integrated moving average (ARIMA) models. Here's an example of fitting an ARIMA model to a time series:

```python
import statsmodels.api as sm

# Read in a time series dataset
data = pd.read_csv("time_series.csv", index_col=0, parse_dates=True)

# Fit an ARIMA model
model = sm.tsa.ARIMA(data, order=(1, 1, 1)).fit()

# Print the summary of the model
print(model.summary())
```

### Nonparametric Statistics with scikit-learn

The scikit-learn library provides a variety of tools for nonparametric statistics, including kernel density estimation (KDE) and k-nearest neighbors (KNN) algorithms. Here's an example of fitting a KDE model to a dataset:

```python
from sklearn.neighbors import KernelDensity

# Generate some random data
data = np.random.normal(size=1000)

# Fit a KDE model
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(data[:, None])

# Evaluate the PDF at some test points
x_test = np.linspace(-5, 5, 100)
log_dens = kde.score_samples(x_test[:, None])
```