import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# paste in the full cells for each of the 6 Google Colaboratory cells that include problems

# Problem 1) write your first function here
def rows_and_columns(dataframe):

    rowsandcols = dataframe.shape
    totalsize = dataframe.size
    
    row = rowsandcols[0]
    col = rowsandcols[1]
    
    finalnumber = "The data has " + str(row) + " rows and " + str(col) + " columns."
    return finalnumber

    
# Problem 1) write your second function here
def get_min_max(dataframe, colname):
    min_max = ()
    minval = dataframe[::1][colname].min()
    maxval = dataframe[::1][colname].max()

    min_max = min_max + (minval,)
    min_max = min_max + (maxval,)
    return min_max

# Problem 1) write your third function here
def odd_get_min_max(dataframe, col_name):

    odd_rows = dataframe[col_name].iloc[1::2]

    minval = odd_rows.min()

    maxval = odd_rows.max()

    return minval, maxval
  
# Problem 2) write your function here
def get_uniq(dataframe, colname):
  return dataframe[colname].unique()

# Problem 3) write your function here
def unique_nonNaN_cnt(dataframe, colname):
  return sum(dataframe[colname].value_counts())


# distribution of cases by age and sex
# Problem 4) Complete where we have indicated below
def create_bar_plot_by_sex(covid19_data, age_ranges):
  age_range_labels = [str(x[0])+"-"+str(x[1]) for x in age_ranges]
  # from the covid19_data, select the age_range for female rows 
  female_age_ranges = covid19_data[covid19_data['sex']=='female']['age_range'] # problem 4, fill this in
  counts_female = female_age_ranges.value_counts()[age_range_labels]
  
  # from the covid19_data, select the age_range for male rows 
  male_age_ranges = covid19_data[covid19_data['sex']=='male']['age_range'] # problem 4, fill this in
  counts_male = male_age_ranges.value_counts()[age_range_labels]

  # create plot
  fig, ax = plt.subplots(figsize=(20, 10))
  index = np.arange(len(age_ranges))
  bar_width = 0.35
  opacity = 0.8

  # the bar function draws a bar plot, the first two arugments are the x position of the bar, and its height
  rects1 = plt.bar(index,counts_male , bar_width, # problem 4, fill in first two arguments
                  alpha=opacity,color='b',label='Male')

  rects2 = plt.bar(index,counts_female , bar_width, # problem 4, fill in first two arguments hint: you have to use the bar_width in the first argument
                  alpha=opacity,color='g',label='Female')

  plt.xlabel('Age Range')
  plt.ylabel('Count')
  plt.title('Corona Cases per Age Group')
  #plt.xticks(index + bar_width, age_ranges)
  plt.xticks(index, ["["+str(x[0])+","+str(x[1])+")" for x in age_ranges])
  plt.legend()

  plt.tight_layout()
  return counts_female, counts_male


# distribution of cases by country with >1000 cases
# Problem 5) Complete where we have indicated below
def create_bar_plot_by_country(covid19_data):
  country_cnts = covid19_data.country.value_counts()

  # get the counts for countries with >1000 cases, this should be a data series
  counts =   country_cnts[country_cnts > 1000]
  # get number of countries with >1000 cases, this should be an integer
  n_groups = len(country_cnts[country_cnts > 1000])

  # create plot
  fig, ax = plt.subplots(figsize=(20, 10))
  index = np.arange(n_groups)
  bar_width = 0.35
  opacity = 0.8

  rects1 = plt.bar(index, counts, bar_width,
                  alpha=opacity,color='b')

  plt.xlabel('Country')
  plt.ylabel('Count')
  plt.title('Corona Cases per Country')
  plt.xticks(index, country_cnts.index.values ) # Problem 5, fill this in
  plt.legend()

  plt.tight_layout()
  return n_groups, counts
  
  # Problem 6) Complete where we have indicated below
def create_bar_plot_for_derek(covid19_data):
  # first we subset the data by the appropriate age bracket and do a bit of cleaning
  prof_age_data = covid19_data[covid19_data['age_range'] =="30-40"]
  prof_age_data=prof_age_data.replace(to_replace='25.02.2020 - 26.02.2020',value='25.02.2020')

  # and we convert the column to a date-time
  prof_age_data['date_confirmation']=pd.to_datetime(prof_age_data['date_confirmation'],dayfirst=True)

  outcomes_over_time = prof_age_data[['date_confirmation', 'outcome_class']].groupby(['date_confirmation']).agg(['mean','count','std']).reset_index()

  outcomes_over_time = outcomes_over_time.dropna() # we should drop the rows with missing values

  x = outcomes_over_time.date_confirmation
  y =  outcomes_over_time.outcome_class['mean']
  error =  outcomes_over_time.outcome_class['std']

  fig, ax = plt.subplots(figsize=(20, 10))
  ax.errorbar(x, y, yerr=error, fmt='-o')
  plt.ylabel('Relative Frequency', fontsize=14)
  plt.xlabel('Date', fontsize=14)
  return x, y, error



   


