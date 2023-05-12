import pandas as pd
import time
import util

from rich.console import Console

console = Console()

def list_all_columns(df):
    try:
        start_time = time.time()
        for i, column in enumerate(df.columns):
            console.print(f"{i}: {column}")
        end_time = time.time()
        console.print(f"\nTime to load {end_time - start_time} sec.\n")
    except (AttributeError, ValueError):
        console.print("DataFrame is not defined or empty.")
    except Exception as e:
            console.print("Error occurred:", e)
    
    util.wait_on_user()


def drop_column(df):
    index_to_drop = console.input("Select a column number to drop or [L] to list columns: ").upper()

    if index_to_drop == "L":
        try:
            for i, column in enumerate(df.columns):
                console.print(f"{i}: {column}")
        except (AttributeError, ValueError):
            console.print("DataFrame is not defined or empty.")
        except Exception as e:
            console.print("Error occurred:", e)

        index_to_drop = console.input("\nSelect a column number to drop or [L] to list columns:")

    try:
        df.drop(df.columns[int(index_to_drop)], axis=1, inplace=True)
        console.print(df.head())
    except (AttributeError, ValueError):
        console.print("DataFrame is not defined or empty.")
    except IndexError:
        console.print("Invalid Column Index.")
    except Exception as e:
        console.print("Error occurred:", e)

    util.wait_on_user()

    
def search_by_value(df, column_name, value):
    try:
        # Check if column_name is in df
        if column_name not in df.columns:
            raise ValueError(f"{column_name} is not a column in the DataFrame")
        
        rows = df[df[column_name] == value]
        return rows[column_name]

    except ValueError as ve:
        console.print("ValueError:", ve)
    except Exception as e:
        console.print("An unexpected error occurred:", e)

    util.wait_on_user()

def sort_column(df):
    try:
       for i, column in enumerate(df.columns):
            console.print(f"{i}: {column}")
    except (AttributeError, ValueError):
        console.print("DataFrame is not defined or empty.")
    except Exception as e:
        console.print("Error occurred:", e)

    col_index = console.input("\nEnter a column number or [L] to list columns: ")

    try:
        col_name = df.columns[int(col_index)]
    except Exception as e:
        console.print("Error occurred:", e)
        return
    
    choice = input("\n[a] for ascending or [d] for descending:\t")

    if choice == "a":
        try:
            start_time = time.time()
            df = df.sort_values(col_name, ascending=True)
            end_time = time.time()
            console.print(f"Time to sort {end_time - start_time} sec.\n")
        except (AttributeError, ValueError):
            console.print("DataFrame is not defined or empty.")
        except IndexError:
            console.print("Invalid Column Index.")
        except Exception as e:
            console.print("Error occurred:", e)

    elif choice == "d":
        try:
            start_time = time.time()
            df = df.sort_values(col_name, ascending=False)
            end_time = time.time()
            console.print(f"Time to sort {end_time - start_time} sec.\n")
        except (AttributeError, ValueError):
            console.print("DataFrame is not defined or empty.")
        except IndexError:
            console.print("Invalid Column Index.")
        except Exception as e:
            console.print("Error occurred:", e)

    else:
        console.print("Invalid choice. Please try again.")

    console.print(df[col_name])
    util.wait_on_user()
    return df
