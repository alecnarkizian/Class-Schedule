#Narkizian, Alec 
#5/14/16
#Intro CS
#Lab 5.05
#unit5/lab5.05.py
import os.path
# name of file:
iofile = 'studentdb.txt'
#catalog contains the classes and thier descriptions, [descption, Unites, Days of the week (m = Monday, tu = tuesday, w = wednesday, th = Thursday, f = Friday), hours of the class in military time]
catalog = {
    'dids1': ['designing information devices and systems i', 4, ['tu', 'f'], 1530, 1700],
    'fs': ['freshman seminar', 2, ['w'], 1600, 1700],
    'opt1': ['hands-on optics', 1, ['m'], 1700, 1900],
    'math1b': ['Calculus', 4, ['m', 'w', 'f'], 1400, 1459],
    'chem1a': ['general chemistry', 3, ['m','w','f'], 900, 1000],
    'ee106a': ['introduction to robotics', 4, ['tu','th'], 930, 1100],
    'cs61a': ['The Structure and Interpretation of Computer Programs', 4, ['m', 'w', 'w'], 1400, 1459],
    'e92': ['Perspectives in Engineering', 1, ['w'], 1600, 1650],
    'cs9e': ['Productive Use of the UNIX Environment', 2, ['M', 'Tu'], 830, 959],
    'psych2': ['Principles of Psychology', 3, ['m', 'w', 'f'], 1500, 1559]
        
    }
#schedule contains the useres schedule, will stay even if code ended 
schedule = {}
#available commands for the user 
commands = ["all courses", "schedule", "add", "drop", "help", "quit"]
#classes offered for the major
available_classes = ['dids1', 'fs', 'opt1', 'math1b', 'chem1a', 'ee106a', 'cs61a', 'e92', 'cs9e', 'psych2']
currentunitcount = 0   # global variable
MAX_UNITS_ALLOWED = 22 # global variable
#input: none
#output: writes the schedule into iofile
def write_studentinfo():
    f = open(iofile, 'a')
    for course in schedule:
        line = course + ': ' + str(schedule[course]) + ' \n'
        f.write(line)
    f.close()
#input: none
#output: reads the schedule from the iofile
def load_existing_studentinfo():
    print(schedule)
    if os.path.exists(iofile):
        f = open(iofile, 'r')
        lines = f.readlines()
        print(lines)
        for line in lines:
            line = line.rstrip(' \n')
            student, studentdata = line.split(':')
            catalog[student] = studentdata
        f.close()
#input: the catalog
#output: corrclty formats the classes and their needed info for the all courses command
def all_course(iteration):
    for word in iteration:
        print(word)
        print(iteration[word])
# program running:
while True:
    answer = input("What would you like to do? ").lower()
    if answer == 'add':
        #input: None
        #output: adds class to schedule 
        def add_class_to_schedule():
            classes_time = 0
            global catalog
            global currentunitcount
            global MAX_UNITS_ALLOWED
            classtoadd= input("What class would you like to add? ").lower()
            if classtoadd not in available_classes:   
                print(classtoadd + " isnt in catalog")
            else:
                if classtoadd in schedule:
                    print(classtoadd +" is already in schedule")
                else:
                    units_whole = catalog[classtoadd]
                    #unites_whole grabs the list of the class you selected
                    true_unites = units_whole[1]
                    #true_unites is the unites in the class you selected
                    MAX_UNITS_ALLOWED = MAX_UNITS_ALLOWED - true_unites
                    if MAX_UNITS_ALLOWED > 0: 
                        if not classes_time > 1:
                            for course in schedule:
                                for day in schedule[course][2]:
                                    if day in catalog[classtoadd][2]:
                                        classtoaddSTART = catalog[classtoadd][3]
                                        classtoaddEND = catalog[classtoadd][4]
                                        existingclassSTART = schedule[course][3]
                                        existingclassSTOP = schedule[course][4]
                                        if (classtoaddSTART > existingclassSTART and \
                                        classtoaddSTART < existingclassSTOP) \
                                        or (classtoaddEND > existingclassSTART and \
                                        classtoaddEND < existingclassSTOP) \
                                        or (existingclassSTART > classtoaddSTART and \
                                        existingclassSTART < classtoaddEND) \
                                        or (existingclassSTOP > classtoaddSTART and \
                                        existingclassSTOP < classtoaddEND) \
                                        or classtoaddSTART == existingclassSTART \
                                        or classtoaddEND == existingclassSTOP:
                                            print("Sorry, there is a conflict, cannot add course.")
                                            return None
                            schedule[classtoadd] = catalog[classtoadd]
                            currentunitcount = currentunitcount + schedule[classtoadd][1]
                            print(classtoadd + " has been added to your schedule")
                        else:
                            print("You already have a course at this time")
                    else:
                        print("no more credits are needed")
        add_class_to_schedule()
    #prints the courses
    if answer=='all courses':
        print(all_course(catalog))
    #prints the user-made schedule
    if answer=='schedule':
        load_existing_studentinfo()
        if len(schedule) == 0:
            print("You haven't added any courses to you schedule")
        else:
            print(schedule)
    #prints the help command
    if answer=='help':
            print(commands)
    #lets the user know they put in a wrong command
    if answer not in commands:
        print("that is not a command")
    
    if answer=='drop':
        def drop():
            global catalog
            classtodrop= input("what class would you like to drop: ").lower()
            if classtodrop in schedule:
                global MAX_UNITS_ALLOWED
                schedule.pop(classtodrop)
                print(classtodrop + " has been dropped from your schedule")
                class_for_credits = catalog[classtodrop]
                total_credits = class_for_credits[1]
                MAX_UNITS_ALLOWED = MAX_UNITS_ALLOWED + total_credits
            else:
                print("This class is not in your schedule")
                return
        drop()   
    if answer=='quit':
        write_studentinfo()
        break