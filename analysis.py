import pandas as pd
import math

# (0)  Show the total unique count of crimes per year sorted in descending order.
# (1)  Shot the top 5 areas (AREA NAME) with the mos crime events in all years (Sorted by the number of crime events)
# (2)  Show all months and the unique total count of crimes sorted in increasing order.
# (3)  Show the top 10 streets with the most crimes in LA in 2019. Also display the total amount of crimes in each street.
# (4)  Show the top 5 most dangerous times (in hours) to be in Hollywood. Also display the total amount of crimes in each hour.
# (5)  Print the details of the crime that that took the most time (in hours) to be reported.
# (6)  Show the 10 top most common crime types (Crm Cd Desc) overall across all years.
# (7)  Are woman or men more likely to be the victim of a crime in LA between lunch time (11:00am and 1:00pm)?. Support of your answer.
# (8)  What is the month the has the most major credit card frauds (Crm Cd Desc = 'CREDIT CARDS, FRAUD USE ($950 & UNDER')) in LA in 2019.
# (9)  List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018.

def analysis_7(df):
    if 'TIME OCC' not in df.columns:
        print("Missing key column 'TIME OCC")
        return None
    if 'LOCATION' not in df.columns:
        print("Missing key column 'LOCATION")
        return None
    if 'Vict Sex' not in df.columns:
        print("Missing key column 'Vict Sex")
        return None
   
    start_time = 1100
    end_time = 1300
    location_name = 'LOS ANGELES'
    df_7 = df.loc[(df['TIME OCC'] >= start_time) & (df['TIME OCC'] <= end_time)]
    df_7 = df_7[df_7['LOCATION'].str.contains(location_name, case=False, na=False)]
    df_7 = df_7[(df_7['Vict Sex'] == 'F') | (df_7['Vict Sex'] == 'M')]

    vict_sex_counts = {}
    for value in df['Vict Sex']:
        if value in vict_sex_counts:
            vict_sex_counts[value] += 1
        else:
            vict_sex_counts[value] = 1

    key = max(vict_sex_counts, key=vict_sex_counts.get)
    value = vict_sex_counts[key]
    
    result = {}
    if key == 'M':
        result = {'Men': value}
    else:
        result = {'Women': value}

    return result
