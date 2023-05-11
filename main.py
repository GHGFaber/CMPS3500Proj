import pandas as pd
import time
import util
import explore
import describe
import analysis

# Function to display main menu
def main_menu():
    util.clear_console()
    print("Main Menu:")
    print("**********")
    print("(1) Load Data")
    print("(2) Exploring Data")
    print("(3) Data Analysis")
    print("(4) Print Data Set")
    print("(5) Quit")

# Function to load data set
def load_data():
    util.clear_console()
    global df
    print("Load data set:")
    print("**************")
    print(f"[{util.current_time()}] Select the number of the file to load from the list below:")
    print("\tPlease select an option:")
    print("\t[1] data.csv")
    print("\t[2] Crime_Data_from_2017_to_2019.csv")
    print("\t[3] nothing.csv")
    file_choice = input()
    if file_choice == "1":
        file_name = "data.csv"
    elif file_choice == "2":
        file_name = "Crime_Data_from_2017_to_2019.csv"
    elif file_choice == "3":
        file_name = "nothing.csv"
    else:
        print("Invalid choice. Returning to the main menu.")
        return

    try:
        start_time = time.time()
        df = pd.read_csv(file_name)
        end_time = time.time()
        df = df.rename(columns=lambda x: x.strip()) #trim whitespace from headers
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x) #trim whitespace from cells
        df = df.drop('Crm Cd 2', axis=1)
        df = df.drop('Crm Cd 3', axis=1)
        df = df.drop('Crm Cd 4', axis=1)
        df = df.drop('Cross Street', axis=1)
        df = df.dropna() 
    except FileNotFoundError:
        print("File not found.")
        util.wait_on_user()
        return

    print("")
    print(f"[{util.current_time()}]" + " " + file_choice)
    print(f"[{util.current_time()}] Total Columns Read: {df.shape[1]}")
    print(f"[{util.current_time()}] Total Rows Read: {df.shape[0]}\n")
    print("File loaded successfully!")
    print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    util.wait_on_user()

# Function to explore data set
def explore_data():
    util.clear_console()
    print("Exploring Data:")
    print("***************")
    print("(21) List all Columns:")
    print("(22) Drop Columns:")
    print("(23) Describe Columns:")
    print("(24) Search Element in Column:")
    print("(25) Sort Column:")
    print("(b)  Back to Main Menu:")
    choice = input("Enter an option: ")
    util.clear_console()

    if choice == "21":
        print("(21) List of all columns:")
        print("*************************")
        explore.list_all_columns(df)
    
    elif choice == "22":
        print("(22) Drop Columns:")
        print("******************")
        explore.drop_column(df)

    elif choice == "23":
        print("(23) Describe Columns:")
        print("**********************")
        describe_data()

    elif choice == "24":
        print("(24) Search Element in Column:")
        print("*******************************")
        print("Select column number to perform a search:")
        print(f"[{util.current_time()}] Enter element to search:\n")
        for i, col_name in enumerate(df.columns):
            print(f"{i}: {col_name}")
        print("\n")
        while True:
            try:
                column_choice = int(input("Enter an option: "))
                if column_choice < 0 or column_choice >= len(df.columns):
                    print("Invalid column number. Please try again.")
                    continue
                column_name = df.columns[column_choice]
                element = input(f"[{util.current_time()}] Enter element to search: ")
                try:
                    element = df[column_name].dtype.type(element)
                except ValueError:
                    print("Invalid input for the data type of the selected column. Please try again.")
                    continue
                start_time = time.time()
                rows = explore.search_by_value(df, column_name, element)
                end_time = time.time()
                if len(rows) > 0:
                    print(f"[{util.current_time()}] Element found in these rows. ")
                    print(rows)
                    print(f"\nStats printed succesfully! Time to process is {round(end_time - start_time, 2)} sec.\n ")
                    return explore_data()
                else:
                    print(f"[{util.current_time()}] Element not found.")
                    return explore_data()
            except ValueError:
                print("Invalid input for the column number. Please try again.")
            except IndexError:
                print("Invalid input for the column number. Please try again.")

    elif choice == "25":
        print("(23) Sort Column:")
        print("**********************")
        df = explore.sort_column(df)

    elif choice == "b":
        return 
    
    else:
        print("Invalid choice. Please try again.")
        explore_data()

    # Loop back to current menu
    util.wait_on_user()
    explore_data()


# Function to describe data set
def describe_data():
    util.clear_console()
    print("Describing Data:")
    print("***************")
    try: 
        for i, column in enumerate(df.columns):
            print(f"{i}: {column}")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
        return
    except Exception as e:
        print("Error occurred:", e)
        return

    col_index = input("\nEnter a column number or [L] to list columns:\t")

    try:
        col_name = df.columns[int(col_index)]
    except Exception as e:
        print("Error occurred:", e)
        return
    
    start_time = time.time()
    sorted_col = describe.sort_descending(df[col_name].tolist())
    counts = describe.get_counts(df, col_name)
    mean = describe.get_mean(df, col_name)
    median = describe.get_median(sorted_col)
    mode = describe.get_mode(df, col_name)
    standard_deviation = describe.get_standard_deviation(df, col_name, mean)
    variance = describe.get_variance(df,col_name, mean)
    min = describe.get_minimum(df, col_name)
    max = describe.get_maximum(df, col_name)
    mean = describe.get_mean(df, col_name)
    end_time = time.time()

    print(f"\nColumn [{col_name}]:")
    print("===========================")
    print(f"Count:\t\t\t\t{counts['full']}")
    print(f"Unique:\t\t\t\t{counts['unique']}")
    print(f"Mean:\t\t\t\t{mean}")
    print(f"Median:\t\t\t\t{median}")
    print(f"Mode:\t\t\t\t{mode}")
    print(f"Standard Deviation (SD):\t{standard_deviation}")
    print(f"Variance:\t\t\t{variance}")
    print(f"Minimum:\t\t\t{min}")
    print(f"Maximum:\t\t\t{max}")

    print(f"\nTime to process is {round(end_time - start_time, 2)} sec.\n")


# Function for analysis of data set
def data_analysis():
    util.clear_console()
    print("\nData Analysis:")
    print("**************")

    print("")
    print(f"[{util.current_time()}] Show the total unique count of crimes per year sorted in descending order.")
    result0 = analysis.analysis_0(df)
    print(f"[{util.current_time()}] " + str(result0) + "\n")
 
    print(f"[{util.current_time()}] Shot the top 5 areas (AREA NAME) with the mos crime events in all years (Sorted by the number of crime events)")
    result1 = analysis.analysis_1(df)
    print(f"[{util.current_time()}] " + str(result1) + "\n")
 
    print(f"[{util.current_time()}] Show all months and the unique total count of crimes sorted in increasing order.")
    result2 = analysis.analysis_2(df)
    print(f"[{util.current_time()}] " + str(result2) + "\n")
 
    print(f"[{util.current_time()}] Show the top 10 streets with the most crimes in LA in 2019. Also display the total amount of crimes in each street.")
    result3 = analysis.analysis_3(df)
    print(f"[{util.current_time()}] " + str(result3) + "\n")
  
    print(f"[{util.current_time()}] Show the top 5 most dangerous times (in hours) to be in Hollywood. Also display the total amount of crimes in each hour.")
    result4 = analysis.analysis_4(df)
    print(f"[{util.current_time()}] " + str(result4) + "\n")
   
    print(f"[{util.current_time()}] Print the details of the crime that that took the most time (in hours) to be reported.")
    result5 = analysis.analysis_5(df)
    print(f"[{util.current_time()}] " + str(result5) + "\n")
   
    print(f"[{util.current_time()}] Show the 10 top most common crime types (Crm Cd Desc) overall across all years.")
    result6 = analysis.analysis_6(df)
    print(f"[{util.current_time()}] " + str(result6) + "\n")
   
    print(f"[{util.current_time()}] Are woman or men more likely to be the victim of a crime in LA between lunch time (11:00am and 1:00pm)?. Support of your answer.")
    result7 = analysis.analysis_7(df)
    print(f"[{util.current_time()}] " + str(result7) + "\n")
    
    print(f"[{util.current_time()}] What is the month the has the most major credit card frauds (Crm Cd Desc = 'CREDIT CARDS, FRAUD USE ($950 & UNDER')) in LA in 2019.")
    result8 = analysis.analysis_8(df)
    print(f"[{util.current_time()}] " + str(result8) + "\n")

    print(f"[{util.current_time()}] List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018.")
    result9 = analysis.analysis_9(df)
    print(f"[{util.current_time()}] " + str(result9) + "\n")
  
    util.wait_on_user()
    return


# fucntion to print data set
def print_data(df):
    util.clear_console()
    print("\nData Analysis:")
    print("**************")

    try:
        n = input("Enter number of rows:\t")
        pd.set_option('display.max_rows', None)
        #pd.set_option('display.max_columns', None)
        print(df.head(int(n)))
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except Exception as e:
        print("Error occurred:", e)

    util.wait_on_user()


# Main loop
if __name__ == "__main__":
    while True:
        # Display main menu
        main_menu()
        choice = input("Enter an option: ")
        # Call function based on user input
        if choice == "1":
            load_data()
        elif choice == "2":
            explore_data()
        elif choice == "3":
            data_analysis()
        elif choice == "4":
            print_data(df)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
