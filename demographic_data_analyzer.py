import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race']).value_counts()

    # What is the average age of men?
    avv= df.loc[df['sex'] == 'Male','age']
    average_age_men =round(avv.mean() , 1)
    
    # What is the percentage of people who have a Bachelor's degree?
    per = df['education'].value_counts(normalize=True)*100
    percentage_bachelors = round(per.Bachelors,1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
  
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education =df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    high_edu = higher_education['salary'].value_counts(normalize = True) * 100
    lower_education = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    low_edu = lower_education['salary'].value_counts(normalize = True) * 100
    
    # percentage with salary >50K
    higher_education_rich = round(high_edu.loc['>50K'],1)
    lower_education_rich = round(low_edu.loc['>50K'],1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours =df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minu = df[df['hours-per-week'] == min_work_hours ]
    num_min_workers = minu['salary'].value_counts(normalize = True)*100
    rich_percentage = num_min_workers.loc['>50K']

    # What country has the highest percentage of people that earn >50K?
    hi =df.groupby('native-country')
    tot =round(hi['salary'].value_counts(normalize = True)*100 , 2)
    country3 = tot.reset_index(name='percentage')
    too = country3[country3['salary'] == '>50K'].sort_values(by=['percentage'],ascending = False)
    highest_earning_country =too['native-country'].values[0]
    highest_earning_country_percentage = round(too['percentage'].max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    top = df[(df['salary'] == '>50K') & (df['native-country' ]=='India')]
    top1 =top['occupation'].value_counts().index[0]
    top_IN_occupation = top1



    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
