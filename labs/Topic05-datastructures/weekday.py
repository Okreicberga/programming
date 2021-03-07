# program that outputs whether or not today is a weekday
# import pandas function 
import pandas as pd 
  
# 
def check_weekday(date): 
      
    res=len(pd.bdate_range(date,date)) 
      
    if res == 0 : 
        print("It is the weekend, yay!") 
    else: 
        print("Yes, unfortunately today is a weekday.")  
  
date = "2021-02-25"
check_weekday(date) 
  
date = "2021-02-27"
check_weekday(date)