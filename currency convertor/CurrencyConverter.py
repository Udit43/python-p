import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import requests

# # Graph Plot
def get_yearly_rates(amount,currency,converted_currency,amount_of_days):

    today_date = datetime.datetime.now()    # It stores live date and time
    date_1year=(today_date - datetime.timedelta(days = amount_of_days - 1))
    # url='https://api.exchangerate.host/timeseries?start_date=2020-01-01&end_date=2020-01-04'

    url='https://api.exchangerate.host/timeseries'
    payload={'base':currency, 'amount':amount, 'start_date':date_1year.date(), 'end_date':today_date.date()} #
    response = requests.get(url, params=payload)   # It takes live data from url ranging from start date to end date using payload dict.
    data=response.json()

    currency_history= {}        # Creating empty dictionary
    np.rate_history_array=[]    # Creating empty array using numpy


    # Creating a loop ranging from start date to end date

    for item in data['rates']:    # Here item(index) represents date  
        current_date = item       # Current date will get updated for every change in index in loop
        currency_rate=data['rates'][item][converted_currency]   

        currency_history[current_date]=[currency_rate]  
        np.rate_history_array.append(currency_rate)       # appending currency rate for each date in converted currency
    
    # end of loop


    # Pandas
    pd_data = pd.DataFrame(currency_history).transpose()   # .transpose will do transpose of table just like in matrix
    pd_data.columns=['Rate']  # Printing heading of coloumn 2 as Rate in output table
    pd.set_option('display.max_rows',None)
    print(pd_data)            # It prints table of dates and rates in output window


    # Matplotlib
    font1={'family': 'serif', 'color': 'red', 'size':17}       # Creating dictionary named as font1
    font2={'family': 'serif', 'color': 'green', 'size':15}     # Creating dictionary named as font2
    
    plt.plot(np.rate_history_array, label='Current Rate')      # It takes rate_history_array an input and create graph
    plt.legend()                                               # It displays a small box in graph, representing info about graph line
    plt.ylabel(f'{amount} {currency} to {converted_currency}' , fontdict=font2)
    plt.xlabel('Days' ,fontdict=font2)
    plt.title(f'Current rate for {amount} {currency} to {converted_currency} is {np.rate_history_array[-1]}' , fontdict=font1 )
 

# # File Handling Code

# There are two methods to open and read file, but using WITH method we don't have to close the file.
with open("CurrencyCodes.txt") as fo:    
  for line in fo:
    print(line , end=" ")    


# # Output Code

first_currency_code =input("\n\nFROM THE ABOVE DATA, \nEnter the Currency code of a country for which you want to convert \n")
value=int(input('\nEnter '+ first_currency_code +' Amount you want to convert :\n'))

print("\nEnter the Currency code to which you want to convert",value,first_currency_code,": ")
second_currency_code = input()

no_of_days=int(input('\nEnter the number of days you want to see the exchange rate of '+ first_currency_code + ' to ' + second_currency_code+':\n'))
get_yearly_rates(value , first_currency_code , second_currency_code , no_of_days)  # Function call

plt.show()   # It will display graph on screen
