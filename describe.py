import pandas as pd
import time
import util
import explore


def get_counts(df,col_name):
    counts = {"full":0, "unique":0}

    try:
        count = 0
        unique_values = {}
        for value in df[col_name]:
            count+=1

            if value in unique_values:
                unique_values[value] += 1
            else:
                unique_values[value] = 1
        counts["full"] = count
        counts["unique"] = len(unique_values)
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)
    
    return counts

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



