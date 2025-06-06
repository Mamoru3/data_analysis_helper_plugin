# Copyright, Alessandro Loddo, Seaborn helper functions to plot
import seaborn as sns
import matplotlib.pyplot as plt


# Plots a countplot (bar chart of counts for each category in a column) using seaborn.
def plot_countplot(data, column, title=None, rotation=45, palette='pastel', size=(8,5), ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    sns.countplot(data=data, x=column, palette=palette, ax=ax)
    ax.set_title(title or f'Countplot of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=rotation)
    if ax is None: plt.tight_layout(); plt.show()

# Plots a boxplot for the distribution of a numerical variable by categories using seaborn.
def plot_boxplot(data, x, y, title=None, palette='Set2', size=(8,5), ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    sns.boxplot(data=data, x=x, y=y, palette=palette, ax=ax)
    ax.set_title(title or f'Boxplot of {y} by {x}')
    if ax is None: plt.tight_layout(); plt.show()

# Plots a violin plot for the distribution of a numerical variable by categories using seaborn.
def plot_violinplot(data, x, y, title=None, palette='muted', size=(8,5), ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    sns.violinplot(data=data, x=x, y=y, palette=palette, ax=ax)
    ax.set_title(title or f'Violin Plot: {y} by {x}')
    if ax is None: plt.tight_layout(); plt.show()

# Plots a heatmap from a DataFrame or 2D array using seaborn.
def plot_heatmap(data, annot=True, cmap='Blues', size=(8,6), title='Heatmap', ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    sns.heatmap(data, annot=annot, cmap=cmap, ax=ax)
    ax.set_title(title)
    if ax is None: plt.tight_layout(); plt.show()

# Plots pairwise relationships in a dataset using seaborn's pairplot.
def plot_pairplot(data, vars=None, hue=None, palette='husl'):
    # pairplot always creates its own figure
    sns.pairplot(data, vars=vars, hue=hue, palette=palette)
    plt.tight_layout()
    plt.show()