## TODO: import all necessary packages and functions
import csv
import datetime
import calendar
import time
from datetime import date
from collections import Counter
import random
from random import choice

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    # TODO: handle raw input and complete function
    if city == 'Chicago' or city == 'chicago':
        return "C:\kdacity\data analyst\python\chicago.csv"
    elif city == 'New York'or city == 'new york':
        return "C:\\kdacity\\data analyst\\python\\new_york_city.csv"
    elif city == 'Washington'or city == 'washington':
        return "C:\kdacity\data analyst\python\Washington.csv"

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function
    return time_period
    #if time_period == month:
        #return 'month'
    #if time_period == day:
        #return 'day'
    #if time_period == none:
        #return 'month'




def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    city_file = get_city()
    #time_period = get_time_period()
    # TODO: handle raw input and complete function
    if month == 'January':
        d = 1
    if month == 'February':
        d=2
    if month == 'March':
        d=3
    if month == 'April':
        d=4
    if month == 'May':
        d=5
    if month == 'June':
        d=6
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        v=[]
        l=[]
        t=[]
        month_list=[]
        for row in j:
            v,l = row['Start Time'].split(" ")
            for x in v:
                year,month,day = v.split('-')
                s= int(year)
                m = int(month)
                z= int(day)
                t = datetime.date(s,m,z).month
                month_list.append(t)
        c= month_list.count(d)
            #print(c)
        print(" The total number of trips taken in the month is",c)



def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function
    city_file = get_city()
    #time_period = get_time_period()
    day_new = int(day)
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        v=[]
        day_list=[]
        for row in j:
            v,l = row['Start Time'].split(" ")
            for x in v:
                year, month, day = v.split('-')
                l = datetime.date(int(year), int(month), int(day)).weekday()
                day_list.append(l)
        print(day_list)
        day_count= day_list.count(day_new)
        print("the no of trips taken on this day of the week is", day_count)


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    city_file = get_city()
    time_period = get_time_period()
    #f = open(city_file,'r')
    '''DicReader reads the file to the function and maps the first row as the fieldname, similar to Excel/csv'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        v=[]
        l=[]
        month_list=[]
        for row in j:
            v,l = row['Start Time'].split(" ")
            for x in v:
                year, month, day = v.split('-')
                t = datetime.date(int(year), int(month), int(day)).month
                month_list.append(t)
        c= Counter(month_list).most_common(1)
        day,number =zip(*c)
        if day[0] == 1:
            print ('January')
            return number
        elif day[0] == 2:
            print('February')
            print( number[0])
        elif day[0] == 3:
            return 'March'
            return number
        elif day[0] == 4:
            return 'April'
            return number
        elif day[0] == 5:
            return 'May'
            return number
        elif day[0] == 6:
            return 'June'
            return number
        elif day[0] == 7:
            return 'July'
            return number
        if day[0] == 8:
            print ('August')
            return number
        elif day[0] == 9:
            print('September')
            print( number[0])
        elif day[0] == 10:
            return 'October'
            return number
        elif day[0] == 11:
            return 'November'
            return number
        elif day[0] == 12:
            return 'December'
            return number



def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    city_file = get_city()
    time_period = get_time_period()


    '''DicReader reads the file to the function and maps the first row as the fieldname, similar to Excel/csv'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        v=[]
        day_list=[]
        for row in j:
            v,l = row['Start Time'].split(" ")
            for x in v:
                year, month, day = v.split('-')
                l = datetime.date(int(year), int(month), int(day)).weekday()
                day_list.append(l)
        c= Counter(day_list).most_common(1)
        day,number =zip(*c)

        if day[0] == 0:
            return 'Monday'

        elif day[0] == 1:
            return 'Tuesday'

        elif day[0] == 2:
            return 'Wednesday'
            return number[0]
        elif day == 3:
            return 'Thursday'

        elif day == 4:
            return 'Friday'

        elif day == 5:
            return 'Saturday'

        elif day[0] == 6:
            return 'Sunday'



def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    city_file = get_city()
    time_period = get_time_period()

    '''DicReader reads the file to the function and maps the first row as the fieldname, similar to Excel/csv'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        v=[]
        hr_list=[]
        for row in j:
            v,l = row['Start Time'].split(" ")
            for x in l:
                hour, minute, second = l.split(':')
                n = hour
                hr_list.append(n)

        c= Counter(hr_list).most_common(1)
        #print(c)
        popular_hr,number =zip(*c)

        return popular_hr[0]




def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    city_file = get_city()
    time_period = get_time_period()

    '''DicReader reads the file to the function and maps the first row as the fieldname, similar to Excel/csv'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        v=[]
        trip_list=[]
        sum=0
        for row in j:
            w = row['Trip Duration']
            trip_list.append(w)
        results = list(map(int,trip_list))
        for row in results:
            sum = sum + row

        avg = sum/len(list(trip_list))
        print(" The total trip duration and average trip duration are", sum,avg)





def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    city_file = get_city()
    time_period = get_time_period()

    '''DicReader reads the file to the function and maps the first row as the fieldname'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        start_stat_list =[]
        end_stat_list = []
        for i in j:
            l = i['Start Station']
            p = i['End Station']
            start_stat_list.append(l)
            end_stat_list.append(p)
        count_of_start_stat= Counter(start_stat_list).most_common(1)
        count_of_end_stat = Counter(end_stat_list).most_common(1)
        pop_start,count_pop_start = zip(*count_of_start_stat)
        pop_end,count_pop_end = zip(*count_of_end_stat)
    print(" The most popular start and end stations are", pop_start, pop_end)


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    city_file = get_city()
    time_period = get_time_period()

    '''DicReader reads the file to the function and maps the first row as the fieldname, similar to Excel/csv'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        start_end=[]
        start=[]
        n =[]
        m=[]
        end =[]
        for row in j:
            n = row['Start Station']
            m = row['End Station']
            start.append(n)
            end.append(m)
        start_end = list(zip(start,end))
        c= Counter(start_end).most_common(1)
        pop_trip,number =zip(*c)
        print(" The most popular trip is", pop_trip)
        # pop_trip


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    city_file = get_city()
    time_period = get_time_period()

    '''DicReader reads the file to the function and maps the first row as the fieldname, similar to Excel/csv'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        user_list=[]
        for row in j:
            l = row['User Type']
            user_list.append(l)
        i=0
        f=0
        for row in user_list:
            if row == 'Customer':
                i = i+1
            if row == 'Subscriber':
                f = f+1
        print(" The count of customer and subscriber is", i,f)
        #return i
        #return f



def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    city_file = get_city()
    time_period = get_time_period()
    if city_file == "C:\kdacity\data analyst\python\Washington.csv":
        return ' No gender column'

    '''DicReader reads the file to the function and maps the first row as the fieldname, similar to Excel/csv'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        gender_list=[]
        for row in j:
            l = row['Gender']
            gender_list.append(l)
        i=0
        f=0
        for row in gender_list:
            if row == 'Male':
                i = i+1
            if row == 'Female':
                f = f+1
        print(" The count of male and female are", i,f)
        #return i
        #return f

def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''

    # TODO: complete function
    city_file = get_city()
    time_period = get_time_period()
    if city_file == "C:\kdacity\data analyst\python\Washington.csv":
        return ' No birth years column'

    '''DicReader reads the file to the function and maps the first row as the fieldname, similar to Excel/csv'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        birth_list=[]
        for row in j:
            if row['Birth Year'] > '10':
                l = row['Birth Year']
                birth_list.append(l)
                #k =' '.join(k).split()
        #print(k)
        earliest = min(birth_list)
        recent = max(birth_list)
        c = Counter(birth_list).most_common(1)
        #print(c)
        pop_year,number =zip(*c)
        print(" The earliest, most recent and most popular birth years are", earliest,recent, pop_year[0])
        #return pop_year[0]
        #return earliest
        #return recent

def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')

    # TODO: handle raw input and complete function
    city_file = get_city()
    #time_period = get_time_period()

    '''DicReader reads the file to the function and maps the first row as the fieldname, similar to Excel/csv'''
    with open(city_file,'r') as table:
        j = csv.DictReader(table)
        i=0
        t=[]
        def display_check():
            display_ = input('\nWould you like to view five more lines of individual trip data?'
                        'Type \'yes\' or \'no\'.\n')
            if display_ == 'yes':
                return display_fn()
            elif display_ == 'no':
                restart()

        def display_fn():
            u=0#m = m +1
            for row in j:
                t.append(row)
                a = random.choice(t)
                print(a)
                u = u+1
                if u>5:
                    break
            display_check()

        k=0
        if display == 'yes':
            for row in j:
                print(row)
                i = i+1
                if i>5:
                    display='no'
                    display_check()
        elif display == 'no':
            restart()






def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    #print(" The no of trips in the month is",get_month())
    get_day(get_month())

    print('Calculating the first statistic...')
    #get_month()
    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        print("The most popular month is ",popular_month(city,time_period))#TODO: call popular_month function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        print(" The most popular day of the week is\n",popular_day(city, time_period))# TODO: call popular_day function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    print(" The most popular hour is",popular_hour(city,time_period))# TODO: call popular_hour function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    print( trip_duration(city,time_period))# TODO: call trip_duration function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    popular_stations(city,time_period)# TODO: call popular_stations function and print the results
    #print(popular_stations(city,time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    popular_trip(city,time_period)# TODO: call popular_trip function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    users(city,time_period)# TODO: call users function and print the result
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    print(gender(city,time_period))# TODO: call gender function and print the results

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    #birth_years(city,time_period)
    print(birth_years(city,time_period))
    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()
def restart():
    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()
    if restart.lower() == 'no':
        quit()


if __name__ == "__main__":
	statistics()
