import pandas as pd
import time
import util
import explore


def count_all_values(df, column):
    try:
        count = 0
        for value in df[column]:
            count+=1
        print(count)
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

    util.wait_on_user()

def count_unique_values(df, column):
    try:
        unique_values = {}
        for value in df[column]:
            if value in unique_values:
                unique_values[value] += 1
            else:
                unique_values[value] = 1
        print(unique_values)
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

    util.wait_on_user()

def get_mean(df):
    try:
       for i, column in enumerate(df.columns):
            print(f"{i}: {column}")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except Exception as e:
        print("Error occurred:", e)

    col_index = input("\nEnter a column number or [L] to list columns:")

    try:
        col_name = df.columns[int(col_index)]
    except Exception as e:
        print("Error occurred:", e)
        return
    
    try:
        start_time = time.time()
        mean = df[col_name].mean()
        end_time = time.time()
        print(f"The mean of column {col_name} is: {mean}")
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)



def get_median(df):
    try:
       for i, column in enumerate(df.columns):
            print(f"{i}: {column}")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except Exception as e:
        print("Error occurred:", e)

    col_index = input("\nEnter a column number or [L] to list columns:")

    try:
        col_name = df.columns[int(col_index)]
    except Exception as e:
        print("Error occurred:", e)
        return
    
    try:
        start_time = time.time()
        median = df[col_name].median()
        end_time = time.time()
        print(f"The median of column {col_name} is: {median}")
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)


def get_mode(df):
    try:
       for i, column in enumerate(df.columns):
            print(f"{i}: {column}")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except Exception as e:
        print("Error occurred:", e)

    col_index = input("\nEnter a column number or [L] to list columns:")

    try:
        col_name = df.columns[int(col_index)]
    except Exception as e:
        print("Error occurred:", e)
        return
    
    try:
        start_time = time.time()
        mode = df[col_name].mode()
        end_time = time.time()
        print(f"The mode of column {col_name} is: {mode}")
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)
