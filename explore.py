import pandas as pd
import time
import util

def list_all_columns(df):
    try:
        start_time = time.time()
        for i, column in enumerate(df.columns):
            print(f"{i}: {column}")
        end_time = time.time()
        print(f"\nTime to load {round(end_time - start_time, 2)} sec.\n")
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except Exception as e:
            print("Error occurred:", e)
    
    util.wait_on_user()


def drop_column(df):
    index_to_drop = input("Select a column number to drop or [L] to list columns:")

    if index_to_drop == "L":
        try:
            for i, column in enumerate(df.columns):
                print(f"{i}: {column}")
        except (AttributeError, ValueError):
            print("DataFrame is not defined or empty.")
        except Exception as e:
            print("Error occurred:", e)

        index_to_drop = input("\nSelect a column number to drop or [L] to list columns:")

    try:
        df.drop(df.columns[int(index_to_drop)], axis=1, inplace=True)
        print(df.head())
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

    util.wait_on_user()

    
def search_by_value(df, column_name, value):
    try:
        # Check if column_name is in df
        if column_name not in df.columns:
            raise ValueError(f"{column_name} is not a column in the DataFrame")
        
        rows = df[df[column_name] == value]
        return rows[column_name]

    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

    util.wait_on_user()

