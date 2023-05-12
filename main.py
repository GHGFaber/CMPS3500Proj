import pandas as pd
import time
import util
import explore
import describe
import analysis

from rich.console import Console

console = Console()                 # Rich Funct. Displays to Console

# Function to display main menu
def main_menu():
    util.clear_console()
    console.print ("----------------  Main Menu  ------------------- \n\n" +
                    "[1] Load Data       \n" +
                    "[2] Exploring Data  \n" +
                    "[3] Data Analysis   \n" +
                    "[4] Print Data Set  \n\n" +
                    "[Q] Quit            \n")

# Function to load data set
def load_data():
    global df
    while True:
        util.clear_console()
        console.print ("--------------  Load Data Set  ----------------- \n\n" +
                        "\t[1] data.csv                           \n" +
                        "\t[2] Crime_Data_from_2017_to_2019.csv   \n" +
                        "\t[3] nothing.csv                        \n\n" +
                        "\t[R] Return to Main Menu                \n")
        
        file_choice = console.input(f"[{util.current_time()}] Select the number of the file to load from the list above: ").lower()
        if file_choice == "1":
            file_name = "data.csv"
        elif file_choice == "2":
            file_name = "Crime_Data_from_2017_to_2019.csv"
        elif file_choice == "3":
            file_name = "nothing.csv"
        elif file_choice == "r":
            return
        else:
            console.print("Invalid choice.")
            continue

        try:
            start_time = time.time()
            df = pd.read_csv(file_name)
            end_time = time.time()
            df = df.rename(columns=lambda x: x.strip())                         #trim whitespace from headers
            df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)  #trim whitespace from cells
            df = df.drop('Crm Cd 2', axis=1)
            df = df.drop('Crm Cd 3', axis=1)
            df = df.drop('Crm Cd 4', axis=1)
            df = df.drop('Cross Street', axis=1)
            df = df.dropna() 
        except FileNotFoundError:
            console.print("File not found.")
            util.wait_on_user()
            return

        console.print(f"[{util.current_time()}] Total Columns Read: {df.shape[1]}")
        console.print(f"[{util.current_time()}] Total Rows Read: {df.shape[0]}\n")
        console.print("File loaded successfully!")
        console.print(f"Time to load {end_time - start_time} sec.\n")
        util.wait_on_user()
        return

# Function to explore data set
def explore_data():

    global df   # Apparently Necessary to allow other functs to access Dataframe

    while True:
        util.wait_on_user()
        console.print ("-------------  Exploring Data:  ---------------- \n\n" +
                        "\t[1] List all Columns                 \n" +
                        "\t[2] Drop Columns                     \n" +
                        "\t[3] Describe Columns                 \n" +
                        "\t[4] Search Element in Columns        \n" +
                        "\t[5] Sort Column                      \n\n"+
                        "\t[R] Return to Main Menu              \n")
        
        choice = console.input("Enter an option: ").lower()

        if choice == "1":
            util.clear_console()
            console.print("----------  [1] List of all columns:  ---------- \n")
            try:    
                explore.list_all_columns(df)
            except Exception as e:
                console.print("Error occurred:", e)
                util.wait_on_user()
                continue

        elif choice == "2":
            util.clear_console()
            console.print("-------------  [2] Drop Columns:  -------------- \n")
            try:
                explore.drop_column(df)
            except Exception as e:
                console.print("Error occurred:", e)
                util.wait_on_user()
                continue

        elif choice == "3":
            console.print("----------  [3] Describe Columns:  ----------- \n")
            describe_data()

        elif choice == "4":
            util.clear_console()
            console.print("-------  [4] Search Element in Column:  -------- \n")
            try:
                console.print("Select column number to perform a search: ")
                console.print(f"[{util.current_time()}] Enter element to search:\n")
                for i, col_name in enumerate(df.columns):
                    console.print(f"{i}: {col_name}")
                console.print("\n")
                while True:
                    try:
                        column_choice = int(console.input("Enter an option: "))
                        if column_choice < 0 or column_choice >= len(df.columns):
                            console.print("Invalid column number. Please try again.")
                            continue
                        column_name = df.columns[column_choice]
                        element = console.input(f"[{util.current_time()}] Enter element to search: ")
                        try:
                            element = df[column_name].dtype.type(element)
                        except ValueError:
                            console.print("Invalid input for the data type of the selected column. Please try again.")
                        start_time = time.time()
                        rows = explore.search_by_value(df, column_name, element)
                        end_time = time.time()
                        if len(rows) > 0:
                            console.print(f"[{util.current_time()}] Element found in these rows. ")
                            console.print(rows)
                            console.print("\n")
                            console.print(f"[{util.current_time()}] Time to load {end_time - start_time} sec.\n")
                        else:
                            console.print(f"[{util.current_time()}] Element not found. Please select a column.")
                            continue
                        break
                    except ValueError:
                        console.print("Invalid input for the column number. Please try again.")
                    except IndexError:
                        console.print("Invalid input for the column number. Please try again.")
            except Exception as e:
                console.print("Error occurred:", e)
                continue

        elif choice == "5":
            util.clear_console()
            console.print("-------------  [5] Sort Column: ---------------- \n")
            try:
                df = explore.sort_column(df)
            except Exception as e:
                console.print("Error occurred:", e)
                util.wait_on_user()
                continue

        elif choice == "r":
            return 
        
        else:
            console.print("Invalid choice. Please try again.")
            continue

# Function to describe data set
def describe_data():
    util.clear_console()
    console.print("-----------  [3] Describe Columns: ------------- \n")
    try: 
        for i, column in enumerate(df.columns):
            console.print(f"{i}: {column}")
    except (AttributeError, ValueError):
        console.print("DataFrame is not defined or empty.")
        util.wait_on_user()
        return
    except Exception as e:
        console.print("Error occurred:", e)
        util.wait_on_user()
        return

    col_index = console.input("\nEnter a column number or [L] to list columns:\t")

    try:
        col_name = df.columns[int(col_index)]
    except Exception as e:
        console.print("Error occurred:", e)
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

    console.print(f"\nColumn [{col_name}]:")
    console.print("===========================")
    console.print(f"Count:\t\t\t\t{counts['full']}")
    console.print(f"Unique:\t\t\t\t{counts['unique']}")
    console.print(f"Mean:\t\t\t\t{mean}")
    console.print(f"Median:\t\t\t\t{median}")
    console.print(f"Mode:\t\t\t\t{mode}")
    console.print(f"Standard Deviation (SD):\t{standard_deviation}")
    console.print(f"Variance:\t\t\t{variance}")
    console.print(f"Minimum:\t\t\t{min}")
    console.print(f"Maximum:\t\t\t{max}")

    console.print(f"\nTime to process is {end_time - start_time} sec.\n")
    util.wait_on_user()


# Function for analysis of data set
def data_analysis(df):
    util.clear_console()
    console.print("------------  Data Analysis: --------------- \n")

    console.print(f"[{util.current_time()}] Show the total unique count of crimes per year sorted in descending order.")
    result0 = analysis.analysis_0(df)
    console.print(f"[{util.current_time()}] " + str(result0) + "\n")
 
    console.print(f"[{util.current_time()}] Shot the top 5 areas (AREA NAME) with the mos crime events in all years (Sorted by the number of crime events)")
    result1 = analysis.analysis_1(df)
    console.print(f"[{util.current_time()}] " + str(result1) + "\n")
 
    console.print(f"[{util.current_time()}] Show all months and the unique total count of crimes sorted in increasing order.")
    result2 = analysis.analysis_2(df)
    console.print(f"[{util.current_time()}] " + str(result2) + "\n")
 
    console.print(f"[{util.current_time()}] Show the top 10 streets with the most crimes in LA in 2019. Also display the total amount of crimes in each street.")
    result3 = analysis.analysis_3(df)
    console.print(f"[{util.current_time()}] " + str(result3) + "\n")
  
    console.print(f"[{util.current_time()}] Show the top 5 most dangerous times (in hours) to be in Hollywood. Also display the total amount of crimes in each hour.")
    result4 = analysis.analysis_4(df)
    console.print(f"[{util.current_time()}] " + str(result4) + "\n")
   
    console.print(f"[{util.current_time()}] Print the details of the crime that that took the most time (in hours) to be reported.")
    result5 = analysis.analysis_5(df)
    console.print(f"[{util.current_time()}] " + str(result5) + "\n")
   
    console.print(f"[{util.current_time()}] Show the 10 top most common crime types (Crm Cd Desc) overall across all years.")
    result6 = analysis.analysis_6(df)
    console.print(f"[{util.current_time()}] " + str(result6) + "\n")
   
    console.print(f"[{util.current_time()}] Are woman or men more likely to be the victim of a crime in LA between lunch time (11:00am and 1:00pm)?. Support of your answer.")
    result7 = analysis.analysis_7(df)
    console.print(f"[{util.current_time()}] " + str(result7) + "\n")
    
    console.print(f"[{util.current_time()}] What is the month the has the most major credit card frauds (Crm Cd Desc = 'CREDIT CARDS, FRAUD USE ($950 & UNDER')) in LA in 2019.")
    result8 = analysis.analysis_8(df)
    console.print(f"[{util.current_time()}] " + str(result8) + "\n")

    console.print(f"[{util.current_time()}] List the top 5 more dangerous areas for older man (age from 65 and more) in december of 2018.")
    result9 = analysis.analysis_9(df)
    console.print(f"[{util.current_time()}] " + str(result9) + "\n")
  
    util.wait_on_user()
    return


# fucntion to print data set
def print_data(df):
    util.clear_console()
    console.print ("--------------  Printing Data  ----------------- \n")

    try:
        n = console.input("Enter number of rows:\t")
        pd.set_option('display.max_rows', None)
        #pd.set_option('display.max_columns', None)
        console.print(df.head(int(n)))
    except (AttributeError, ValueError):
        console.print("DataFrame is not defined or empty.")
    except Exception as e:
        console.print("Error occurred:", e)

    util.wait_on_user()


# Main loop
if __name__ == "__main__":
    while True:
        # Display main menu
        main_menu()
        choice = input("Enter an option: ").lower()
        # Call function based on user input
        if choice == "1":
            load_data()
        elif choice == "2":
            explore_data()
        elif choice == "3":
            try:
                data_analysis(df)
            except Exception as e:
                console.print("Error occured:", e)
                util.wait_on_user()
                continue
        elif choice == "4":
            try:
                print_data(df)
            except Exception as e:
                console.print("Error occured:", e)
                util.wait_on_user()
                continue
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")
