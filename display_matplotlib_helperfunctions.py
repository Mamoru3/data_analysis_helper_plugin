# Copyright, Alessandro Loddo, matplotlib helper functions to plot
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Plots a histogram for a given data array or Series, with customizable appearance and optional subplot axis.
def plot_histogram(data, bins=20, title='Histogram', x_label='Value', y_label='Count', size=(8,5), color='skyblue', ax=None, show_decimal = False):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    ax.hist(data, bins=bins, color=color, edgecolor='black')
    ax.set_title(title)
    if not show_decimal:
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if ax is None: plt.tight_layout(); plt.show()

# Plots a vertical bar chart from a Series, with customizable appearance and optional subplot axis.
def plot_bar(series, title='Bar Plot', x_label='Group', y_label='Count', rotation=45, color='cornflowerblue', size=(8,5), ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    series.plot(kind='bar', color=color, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
    if ax is None: plt.tight_layout(); plt.show()

# Plots a horizontal bar chart from a Series, with customizable appearance and optional subplot axis.
def plot_horizontal_bar(series, title='Horizontal Bar Plot', x_label='Count', y_label='Group', color='salmon', size=(8,5), ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    series.plot(kind='barh', color=color, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if ax is None: plt.tight_layout(); plt.show()

def plot_pie(series, title='Pie Chart', autopct='%1.1f%%', startangle=90, size=(6,6), legend=False, ax=None, top_n=None):
    if top_n is not None:
         vc = series.value_counts()
         main_cats = vc[:top_n]
         series = series.apply(lambda x: x if x in main_cats else 'Other')
    counts = series.value_counts()
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    counts.plot(kind='pie', autopct=autopct, startangle=startangle, ax=ax, labels=None)
    ax.set_title(title)
    ax.set_ylabel('')
    if legend:
        ax.legend(counts.index, loc='center left', bbox_to_anchor=(1, 0.5))
    if ax is None: plt.tight_layout(); plt.show()

# Plots a scatter plot for two data arrays or Series, with customizable appearance and optional subplot axis.
def plot_scatter(x, y, title='Scatter Plot', x_label='X', y_label='Y', size=(7,5), color='purple', ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    ax.scatter(x, y, color=color, alpha=0.6)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if ax is None: plt.tight_layout(); plt.show()

def plot_line(data, title='Line Plot', x_label='Value', y_label='Count', size=(7,5), color='skyblue', is_sorted = True, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    if is_sorted is True:
        data = data.value_counts().sort_index()
    data.plot(ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if ax is None: plt.tight_layout(); plt.show()