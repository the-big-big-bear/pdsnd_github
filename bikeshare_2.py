import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_MAPPING = {
            'all': 'all',
            'january': '1',
            'february': '2',
            'march': '3',
            'april': '4',
            'may': '5',
            'june': '6',
        }


def get_key_from_value(dict, value):
    '''
    Return key of a provided value within a dictionary
    '''
    for k, v in dict.items():
        if v == value or v == str(value):
            return k
 
    return "key does not exist"


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        input_city = input("Would you like to see data for Chicago, New York, or Washington: ").lower()
        if input_city in ['chicago', 'new york', 'washington']:
            city = CITY_DATA[input_city.lower()]
            break
        else:
            print("Please input among available options")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        input_month = input("Which month? January, February, March, April, May, or June?. Type 'all' if you want to skip filter: ").lower()
        if input_month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            month = MONTH_MAPPING[input_month]
            break
        else:
            print("Please input among available options")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day? Please type your response as a day name such as Monday, Tuesday, Wednesdays...? Or type 'all' if you want to skip filter: ").lower()
        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print("Please input a valid day name")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load csv file as dataframe
    df = pd.read_csv(city)
    
    # Create new columns for filter later
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')

    df['Month'] = df['Start Time'].dt.month
    df['Weekday Name'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        df = df.loc[df['Month']==int(month)]

    # filter by day of week if applicable
    if day != 'all':
        df = df.loc[df['Weekday Name']==day.title()]

    # Prompt user if they want to see the data
    iter = 0
    step = 5
    number_of_rows = len(df)
    maximum_iter = np.ceil(number_of_rows / step)
    while True:
        if iter == 0:
            view_data = input("Do you want to take a look at the data. Type 'y' or 'yes' to see first 5 rows. Type 'n' to quit: ")
        elif iter > 0:
            view_data = input("Do you want to continue view next 5 rows?. Type 'y' or 'yes' to see first 5 rows. Type 'n' to quit: ")
        
        if view_data in ['y', 'yes']:
            if iter == maximum_iter:
                print(df.iloc[iter*step:])
            else:
                print(df.iloc[iter*step:(iter+1)*step])
            iter += 1
        elif view_data == 'n':
            break
        else:
            print("Please type valid answer")
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    print("Most common month: ", get_key_from_value(MONTH_MAPPING, most_common_month).title())

    # TO DO: display the most common day of week
    most_common_weekday = df['Weekday Name'].mode()[0]
    print("Most common weekday: ", most_common_weekday)

    # TO DO: display the most common start hour
    most_common_hour = df['Start Hour'].mode()[0]
    print("Most common hour: ", most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most common start station: ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most common end station: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = df['Start Station'] + ' --- ' + df['End Station']
    most_common_start_end_station = start_end_station.mode()[0]
    print("Most common start-end station: ", most_common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_h, total_m = divmod(total_travel_time, 60)
    print(f'Total Travel Time: {total_travel_time} seconds ~ {int(total_h):,} hour and {int(total_m)} minutes')

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    avg_h, avg_m = divmod(avg_travel_time, 60)
    print(f'Average Travel Time: {avg_travel_time} seconds ~ {int(avg_h):,} hour and {int(avg_m)} minutes')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Counts of user types: \n', user_type_count)
    print('-'*40)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Counts of gender: \n', gender_count)
        print('-'*40)
    except KeyError:
        print('This file does not have column Gender, skip checking count of gender!')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        df['Birth Year']
    except KeyError:
        print("This file does not have column Birth Year, skip finding statistics for birth year")
    else: 
        earliest_yob = int(df['Birth Year'].min())
        print('Earliest year of birth:', earliest_yob)

        most_recent_yob = int(df['Birth Year'].max())
        print('Most recent year of birth: ', most_recent_yob)

        most_common_yob = int(df['Birth Year'].mode()[0])
        print('Most common year of birth: ', most_common_yob)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
