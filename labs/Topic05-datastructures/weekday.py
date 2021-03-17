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
  
date =  (input("Enter the date: "))
check_weekday(date) 
  
