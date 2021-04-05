# write a class called Employee that has one attribute called timesheets (set to an empty list) 
# and an __init__function that takes in a first and last name. 

class Employee:
    timesheets = []

    def __init__(self, first, last) :
        self.first = first
        self.last = last
    # write a __str__function that returns the full name
    def __str__(self) :
        return self.first + '' + self.last

    
        # write a testcase
    if __name__ == '__main__' :
        test = Employee('some', 'one')
        print (test)
        assert ( 'some one' == str(test))