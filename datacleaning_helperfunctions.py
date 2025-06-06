# Copyright, Alessandro Loddo, data cleaning helper functions to clean dataset
import pandas as pd
import numpy as np

    #Drops columns from the DataFrame that have a higher proportion of missing values
    #than the specified threshold (default 50%)
def drop_high_missing_columns(df, threshold=0.5):    
    missing_ratio = df.isnull().mean()  # Calculate fraction of missing values per column
    cols_to_drop = missing_ratio[missing_ratio > threshold].index  # Find columns exceeding threshold
    return df.drop(columns=cols_to_drop)  # Drop those columns and return new DataFrame

    #Fills missing values in a specified column with a given value.
def fill_missing_with_value(df, column, value):
    df[column] = df[column].fillna(value)  # Fill NaNs in column with the specified value
    return df
    
    #Fills missing values in a specified column with the mode (most common value) of that column.
def fill_missing_with_mode(df, column):
    mode = df[column].mode()[0]  # Find the mode (most frequent value)
    df[column] = df[column].fillna(mode)  # Fill NaNs with mode
    return df

    #Fills missing values in a specified column with the median value of that column.
    #Useful for numerical columns.
def fill_missing_with_median(df, column):
    median = df[column].median()  # Find the median
    df[column] = df[column].fillna(median)  # Fill NaNs with median
    return df

    #Converts one or more columns to pandas datetime type.
    #Any values that cannot be converted will become NaT (Not a Time).
def convert_columns_to_datetime(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')  # Convert each column to datetime
    return df

    #Removes duplicate rows from the DataFrame.
    #If subset is given, considers only those columns for identifying duplicates.
def remove_duplicates(df, subset=None):
    return df.drop_duplicates(subset=subset)

    #Converts a specified column to pandas 'category' type (useful for memory savings and categorical data).
    #df[column] = df[column].astype('category')
def convert_column_to_category(df, column):
    return df

    #Encodes a categorical column as integer codes.
    #Each unique value will be assigned a unique integer.
def encode_categorical_column(df, column):
    df[column] = df[column].astype('category').cat.codes
    return df