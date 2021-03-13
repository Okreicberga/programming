# Program that prints out a menu of commands
# The program return what the user chose. 

def displayMenu () :
    print ( "What would you like to do?")
    print ("\t (a) Add new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip ()
    return choice

def doAdd (students):
    print ("do add")
def doView (students):
    print ("Do View")
def doNothing (dumby):
    pass

choiceMap = {
    'a': doAdd,
    'v': doView,
    'q': doNothing
}
   



# main program    
students = []

choice = displayMenu ()
while (choice != 'q'):
    #we could do it with lamda function
    if choice in choiceMap:
        choiceMap[choice] (students)
    else: 
        print ("\n\n please select either a, v or q")
    choise=displayMenu ()

