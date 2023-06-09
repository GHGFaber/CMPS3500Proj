import pandas as pd
import math

def sort_ascending(arr):
    try:
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = []
            equal = []
            greater = []
            for value in arr:
                if value < pivot:
                    less.append(value)
                elif value == pivot:
                    equal.append(value)
                else:
                    greater.append(value)
            return sort_ascending(less) + sorted(equal) + sort_ascending(greater)
    except Exception as e:
        print("Error occurred:", e)
        
def sort_descending(arr):
    try:
        arr = sort_ascending(arr)
        return arr[::-1]
    except Exception as e:
        print("Error occurred:", e)


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


def get_mean(df, col_name):
    if not pd.api.types.is_numeric_dtype(df[col_name]):
        print("Error: Mean is not of numeric data type.")
        return None

    sum = 0
    count = 0
    try:
        for value in df[col_name]:
            count += 1
            sum += value
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

    return sum/count


def get_median(arr):
    if not isinstance(arr[0], (int, float)):
        print("Error: Median is not of numeric data type.")
        return None
    
    try:
        n = len(arr)
        if n % 2 == 0:
            mid1 = n // 2
            mid2 = mid1 - 1
            median = (arr[mid1] + arr[mid2]) / 2
        else:
            mid = n // 2
            median = arr[mid] 
    except Exception as e:
        print("Error occurred:", e)
    
    return median


def get_mode(df, col_name):
    try:
        unique_values = {}
        max_value = None
        max_key = None

        for value in df[col_name]:
            if value in unique_values:
                unique_values[value] += 1
            else:
                unique_values[value] = 1
        
        for key, value in unique_values.items():
            if max_value is None or value > max_value:
                max_value = value
                max_key = key
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

            
    return max_key

    
def get_standard_deviation(df, col_name, mean):
    if not pd.api.types.is_numeric_dtype(df[col_name]):
        print("Error: Std is not of numeric data type.")
        return None
    
    try:
        differences = [(val-mean)**2 for val in df[col_name]]
        differences_sum = sum(differences)
        stdev = math.sqrt(differences_sum/len(df[col_name]))
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

    return stdev


def get_variance(df, col_name, mean):
    if not pd.api.types.is_numeric_dtype(df[col_name]):
        print("Error: Variance is not of numeric data type.")
        return None
   
    try:
        sq_deviations_sum = sum((x-mean)**2 for x in df[col_name])
        variance = sq_deviations_sum/len(df[col_name])-1
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

    return variance


def get_minimum(df, col_name):
    if not pd.api.types.is_numeric_dtype(df[col_name]):
        print("Error: Minimum is not of numeric data type.")
        return None
    
    try:
        min = None
        for value in df[col_name]:
            if value < min or min is None:
                min = value
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

    return min


def get_maximum(df, col_name):
    if not pd.api.types.is_numeric_dtype(df[col_name]):
        print("Error: Maximum is not of numeric data type.")
        return None
    
    try:
        max = None
        for value in df[col_name]:
            if value > max or max is None:
                max = value
    except (AttributeError, ValueError):
        print("DataFrame is not defined or empty.")
    except IndexError:
        print("Invalid Column Index.")
    except Exception as e:
        print("Error occurred:", e)

    return max



