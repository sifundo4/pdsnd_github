import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('which city? chicago, new york city or washington?').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Error, invalid input")
 
    # get user input for month (all, january, february, ... , june)
    while True:    
        month = input('which month? all, january, february, ... , june?').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Error, invalid input")
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('which day of the week? all, monday, tuesday, ... sunday?').lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Error, Invalid input")
    
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    df = pd.read_csv(CITY_DATA[city])
    
    #converting start time to date-time and adding month and day of week columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Extracting month
    df['month'] = df['Start Time'].dt.month
    
    #Extracting day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # get user input for month (all, january, february, ... , june)
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        #getting months index
        month = months.index(month) + 1
        
        #filtering by month to create new dataframe
        df = df[df['month'] == month]

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if day != 'all':
        #filtering by dat to create new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    frequent_month = df['month'].mode()[0]
    print('The most frequent month is:', frequent_month)

    # display the most common day of week
    frequent_day = df['day_of_week'].mode()[0]
    print('The most frequent day is:', frequent_day)

    #create hour column in dataframe
    df['hour'] = df['Start Time'].dt.hour
    
    # display the most common start hour
    frequent_hour = df['hour'].mode()[0]
    print('The most frequent hour is:', frequent_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    frequent_start_station = df['Start Station'].mode()[0]
    print('{} is the most frequently used start station'.format(frequent_start_station))

    # display most commonly used end station
    frequent_end_station = df['End Station'].mode()[0]
    print('{} is the most frequently used end station'.format(frequent_end_station))


    # display most frequent combination of start station and end station trip
    df['combined'] = df['Start Station'] + 'up to' + df['End Station']
    frequent_combination = df['combined'].mode()[0]
    print('{} is the most frequently used station combination'.format(frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(user_type_count)

    # Display counts of gender ------- if statement used due to no genders in washington data
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("No gender in this data")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_by = df['Birth Year'].min()
        print(earliest_by)
        recent_by = df['Birth Year'].max()
        print(recent_by)
        frequent_by = df['Birth Year'].mode()[0]
        print(frequent_by)
    else:
        print("No birth year in this data.")

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





