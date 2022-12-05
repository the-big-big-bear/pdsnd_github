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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


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
