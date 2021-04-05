#  Program that create a class called Timesheetentry that has three attributes that are all set by an_init_function
# Project
# startTime (a datime object)
# duration (in minutes)
import datetime as dt 

class Timesheetentry: 
    
    
    def __init__(self, project, start, duration):
        self.project = project
        self.start = start
        self.duration = duration

# write a_str_function for this class that returns the project and the duration
    def __str__(self):
        return self.project +':' + str(self.duration)
# write a test case for this class that creates an instance and prints it out


# class code

if __name__ == '__main__':
    ts = dt.datetime(2021,3,19,16,20)
    test = Timesheetentry('test', ts, 60)
    print (test)

