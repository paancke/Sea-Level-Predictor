import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = [float(year) for year in range(df['Year'].min(), 2051)]
    sea_levels_all = [slope * year + intercept for year in years_all]
    plt.plot(years_all, sea_levels_all, 'r')
    
    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_rec, intercept_rec, rvalue_rec, pvalue_rec, stderr_rec = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = [float(year) for year in range(2000, 2051)]
    sea_levels_recent = [slope_rec * year + intercept_rec for year in years_recent]
    plt.plot(years_recent, sea_levels_recent, 'g')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.xlim(1850, 2075)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
