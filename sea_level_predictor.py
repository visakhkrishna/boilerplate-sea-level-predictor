import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig1, ax1 = plt.subplots(figsize=(5, 5))
    ax1 = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(min(df['Year']), 2051, 10)
    y1= res.intercept + res.slope*x1
    ax1 = plt.plot(x1, res.intercept + res.slope * x1, 'r', label='fitted line')

    # Create second line of best fit
    df_recent= df[df['Year'] > 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000, 2051, 2)
    y2 = res_recent.intercept + res_recent.slope * x2
    ax1 = plt.plot(x2, y2, 'g', label='fitted line')

    # Add labels and title
    #ax1.set(xlabel='Year', ylabel='Sea Level (inches)', title='Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel("Sea Level (inches)")
    plt.title('Rise in Sea Level')
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()