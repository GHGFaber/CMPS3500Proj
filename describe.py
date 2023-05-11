import pandas as pd
import time
import util
import explore


def count_all_values(df):
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
        count = 0
        start_time = time.time()  
        for value in df[col_name]:
            count+=1
        end_time = time.time()
        print(count)
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

def count_unique_values(df):
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
        unique_values = {}
        start_time = time.time() 
        for value in df[col_name]:
            if value in unique_values:
                unique_values[value] += 1
            else:
                unique_values[value] = 1
        end_time = time.time()
        print(unique_values)
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

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

    
def get_standard_deviation(df):
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
        stdev = df[col_name].std()
        end_time = time.time()
        print(f"The standard deviation of column {col_name} is: {stdev}")
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)


def get_variance(df):
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
        variance = df[col_name].var()
        end_time = time.time()
        print(f"The variance of column {col_name} is: {variance}")
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

def get_min(df):
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
        min = df[col_name].min()
        end_time = time.time()
        print(f"The minimum value of column {col_name} is: {min}")
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)


def get_max(df):
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
        max = df[col_name].max()
        end_time = time.time()
        print(f"The maximum value of column {col_name} is: {max}")
        print(f"Time to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)



