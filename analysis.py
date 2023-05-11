import pandas as pd
import calendar
import re

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

def analysis_0(df):
    # (0)  Show the total unique count of crimes per year sorted in descending order.
    
    return None


def analysis_1(df):
    # (1)  Show the top 5 areas (AREA NAME) with the most crime events in all years (Sorted by the number of crime events)
    
    if 'DATE OCC' not in df.columns:
        print("1: Missing key column 'DATE OCC'")
        return None
    if 'AREA NAME' not in df.columns:
        print("1: Missing key column 'AREA NAME'")
        return None

    # create dictionary of Areas with crime count values
    area_crime_counts = {}
    
    try:
        for value in df['AREA NAME']:
            if value in area_crime_counts:
                area_crime_counts[value] += 1
            else:
                area_crime_counts[value] = 1

    
        sorted_dict = {k: v for k, v in sorted(area_crime_counts.items(), key=lambda item: item[1], reverse=True)}
        # get the top 5 keys from the sorted dictionary
        top_keys = list(sorted_dict.keys())[:5]
        # create a sub-dictionary with the top 5 keys and their values from the parent dictionary
        top_five_areas = {k: v for k, v in area_crime_counts.items() if k in top_keys}
    except Exception as e:
        print("1: Error occurred:", e)
        return None
   
    return sorted(top_five_areas.items(), key=lambda item: item[1], reverse=True)


def analysis_2(df):
    # (2)  Show all months and the unique total count of crimes sorted in increasing order.

    if 'DATE OCC' not in df.columns:
        print("2: Missing key column 'DATE OCC'")
        return None
    
    # create dictionary of Months with crime count values
    month_crime_counts = {}
    
    try:
        df_2 = df
        df_2['DATE OCC'] = pd.to_datetime(df_2['DATE OCC'])
        for value in df_2['DATE OCC']:
            month_name = calendar.month_name[value.month]
            if month_name in month_crime_counts:
                month_crime_counts[month_name] += 1
            else:
                month_crime_counts[month_name] = 1
    except Exception as e:
        print("2: Error occurred:", e)
        return None
   
    return sorted(month_crime_counts.items(), key=lambda item: item[1])


def analysis_3(df):
    # (3)  Show the top 10 streets with the most crimes in LA in 2019. Also display the total amount of crimes in each street.

    return None


def analysis_4(df):
    # (4)  Show the top 5 most dangerous times (in hours) to be in Hollywood. Also display the total amount of crimes in each hour.

    return None


def analysis_5(df):
    # (5)  Print the details of the crime that that took the most time (in hours) to be reported.

    return None


def analysis_6(df):
    # (6)  Show the 10 top most common crime types (Crm Cd Desc) overall across all years.

    if 'DATE OCC' not in df.columns:
        print("6: Missing key column 'DATE OCC'")
        return None
    if 'Crm Cd Desc' not in df.columns:
        print("6: Missing key column 'Crm Cd Desc'")
        return None  
   
    # create dictionary of Months with crime count values
    crime_types = {}
    
    try:
        df_6 = df
        for value in df_6['Crm Cd Desc']:
            if value in crime_types:
                crime_types[value] += 1
            else:
                crime_types[value] = 1

        sorted_dict = {k: v for k, v in sorted(crime_types.items(), key=lambda item: item[1], reverse=True)}
        # get the top 5 keys from the sorted dictionary
        top_keys = list(sorted_dict.keys())[:10]
        # create a sub-dictionary with the top 5 keys and their values from the parent dictionary
        top_ten_crime_types = {k: v for k, v in crime_types.items() if k in top_keys} 
    
    except Exception as e:
        print("2: Error occurred:", e)
        return None
    
    return top_ten_crime_types


def analysis_7(df):
    # (7)  Are woman or men more likely to be the victim of a crime in LA between lunch time (11:00am and 1:00pm)?. Support of your answer.

    if 'TIME OCC' not in df.columns:
        print("7: Missing key column 'TIME OCC'")
        return None
    if 'LOCATION' not in df.columns:
        print("7: Missing key column 'LOCATION'")
        return None
    if 'Vict Sex' not in df.columns:
        print("7: Missing key column 'Vict Sex'")
        return None
   
   
    start_time = 1100
    end_time = 1300
    location_name = 'LOS ANGELES'

    try:
        df_7 = df.loc[(df['TIME OCC'] >= start_time) & (df['TIME OCC'] <= end_time)]
        df_7 = df_7[df_7['LOCATION'].str.contains(location_name, case=False, na=False)]
        df_7 = df_7[(df_7['Vict Sex'] == 'F') | (df_7['Vict Sex'] == 'M')]
    except Exception as e:
        print("7: Error occurred:", e)
        return None

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


def analysis_8(df):
    # (8)  What is the month the has the most major credit card frauds (Crm Cd Desc = 'CREDIT CARDS, FRAUD USE ($950 & UNDER')) in LA in 2019.
    
    # if 'DATE OCC' not in df.columns:
    #     print("8: Missing key column 'DATE OCC'")
    #     return None
    # if 'LOCATION' not in df.columns:
    #     print("8: Missing key column 'LOCATION'")
    #     return None
    # if 'Crm Cd' not in df.columns:
    #     print("8: Missing key column 'Crm Cd'")
    #     return None
    # if 'Crm Cd Desc' not in df.columns:
    #     print("8: Missing key column 'Crm Cd Desc'")
    #     return None
    
    # target_desc = 'CREDIT CARDS, FRAUD USE ($950.01 & OVER)'
    # location_name = 'LOS ANGELES'
    # target_year = 2013

    # try:
    #     df_8 = df
    #     df_8['DATE OCC'] = pd.to_datetime(df_8['DATE OCC'])
    #     df_8 = df_8[df_8['Crm Cd Desc'].str.extract(target_desc, flags=re.IGNORECASE).notnull().any(1)]
    #     #df_8 = df_8[df_8['LOCATION'].str.contains(location_name, case=False, na=False)]
    #     #df_8 = df_8.loc[df_8['DATE OCC'].dt.year == target_year]

    #     fraudct_by_month = {}
    #     for value in df_8['DATE OCC']:
    #         month_name = calendar.month_name[value.month]
    #         if month_name in fraudct_by_month:
    #             fraudct_by_month[month_name] += 1
    #         else:
    #             fraudct_by_month[month_name] = 1

    #     if not fraudct_by_month:
    #         return "No major credit card frauds in {} in {}".format(location_name, target_year)
    # except Exception as e:
    #     print("8: Error occurred:", e)
    #     return None
 
    # return max(fraudct_by_month.items(), key=lambda x: x[1])
    return None


def analysis_9(df):
    # (9)  List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018.
    if 'DATE OCC' not in df.columns:
        print("9: Missing key column 'DATE OCC'")
        return None
    if 'AREA NAME' not in df.columns:
        print("9: Missing key column 'AREA NAME'")
        return None
    if 'Vict Age' not in df.columns:
        print("9: Missing key column 'Vict Age'")
        return None
    if 'Vict Sex' not in df.columns:
        print("9: Missing key column 'Vict Sex'")
        return None
    
    target_month = 12
    target_year = 2018
    target_age = 65
    target_gender = 'M'
    
    try:
        df_9 = df
        df_9['DATE OCC'] = pd.to_datetime(df_9['DATE OCC'])
        df_9 = df_9.loc[(df_9['DATE OCC'].dt.month == target_month) & (df_9['DATE OCC'].dt.year == target_year)]
        df_9 = df_9[df_9['Vict Sex'] == target_gender]
        df_9 = df_9[df_9['Vict Age'] >= target_age]
    except Exception as e:
        print("9: Error occurred:", e)
        return None

    # create dictionary of Areas with crime count values
    area_crime_counts = {}
    for value in df_9['AREA NAME']:
        if value in area_crime_counts:
            area_crime_counts[value] += 1
        else:
            area_crime_counts[value] = 1

    sorted_dict = {k: v for k, v in sorted(area_crime_counts.items(), key=lambda item: item[1], reverse=True)}
    # get the top 5 keys from the sorted dictionary
    top_keys = list(sorted_dict.keys())[:5]
    # create a sub-dictionary with the top 5 keys and their values from the parent dictionary
    top_five_areas = {k: v for k, v in area_crime_counts.items() if k in top_keys} 
   
    return top_five_areas