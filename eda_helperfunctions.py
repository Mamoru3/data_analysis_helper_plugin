# Copyright, Alessandro Loddo, EDA helper functions
import pandas as pd

# Prints a summary of the DataFrame: info, describe, and missing values per column.
def print_summary(df):
    print(df.info())
    print(df.describe(include='all'))
    print('\nMissing values per column:')
    print(df.isnull().sum())

# Returns value counts (with option for percentages) for a specific column.
def column_value_counts(df, column, normalize=False, dropna=False):
    counts = df[column].value_counts(normalize=normalize, dropna=dropna)
    return counts

# Returns a DataFrame with counts and percentages for unique values in a column.
def value_counts_with_percent(df, column, dropna=False):
    counts = df[column].value_counts(dropna=dropna)
    percent = counts / counts.sum() * 100
    return pd.DataFrame({'Count': counts, 'Percent': percent.round(2)})

# Computes the correlation matrix for the whole DataFrame or a list of columns.
def correlation_matrix(df, columns=None):
    if columns:
        return df[columns].corr()
    else:
        return df.corr()

# Groups the DataFrame by a column and aggregates another column with a specified function (mean by default).
def group_and_aggregate(df, group_col, agg_col, agg_func='mean'):
    return df.groupby(group_col)[agg_col].agg(agg_func)