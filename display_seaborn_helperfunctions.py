# Copyright, Alessandro Loddo, Seaborn helper functions to plot
import seaborn as sns
import matplotlib.pyplot as plt

# Plots a countplot (bar chart of counts for each category in a column) using seaborn.
def plot_countplot(data, column, title=None, rotation=45, palette='pastel', size=(8,5), ax=None, hue = None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    sns.countplot(data=data, x=column, palette=palette, ax=ax, hue=hue)
    ax.set_title(title or f'Countplot of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=rotation)
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

def plot_barplot(data, x, y ,title = 'None',hue = None, ax=None, size=(8,6), palette = None):
    if ax is None:
        fig, ax = plt.subplots(figsize=size)
    sns.barplot(data=data, x=x, y=y, hue=hue, ax=ax, palette=palette, saturation=0.6)
    ax.set_title(title)
    if ax is None: plt.tight_layout(); plt.show()

#Credit to ChatGPT
def plot_100pct_stacked_bar(
    df,
    group_col,
    status_col,
    status_order=None,
    colors=None,
    figsize=(12, 6),
    title=None,
    ax=None
):
    created_fig = False
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        created_fig = True
    # 1. Calculate percentage pivot table
    pivot = (
        df.groupby([group_col, status_col]).size()
        .groupby(level=0).apply(lambda x: 100 * x / x.sum())
        .unstack(fill_value=0)
    )
    # 2. If status_order is provided, reorder the columns (statuses) accordingly
    if status_order is not None:
        pivot = pivot[status_order]
    # 3. Choose colors: if none given, use tab10 colormap
    if colors is None:
        colors = plt.cm.tab10.colors[:pivot.shape[1]]
    # 4. Create the stacked bar chart on the provided ax
    pivot.plot(
        kind='bar',
        stacked=True,
        color=colors,
        ax=ax # <-- plot on the given axis
    )
    # 5. Label axes and set the title
    ax.set_ylabel('Percentage (%)')
    ax.set_xlabel(group_col)
    if title is None:
        ax.set_title(f'Percentage of {status_col} by {group_col} (100% Stacked)')
    else:
        ax.set_title(title)
    # 6. Make x labels readable if there are many groups
    ax.tick_params(axis='x', rotation=45)
    # 7. Add a legend for the status column
    ax.legend(title=status_col)
    # 8. Add percentage labels on each segment of the bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', label_type='center')
    # 9. Only show if you created the figure
    if created_fig:
        plt.tight_layout()
        plt.show()