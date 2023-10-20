import seaborn as sns


def dataplot(data, x, y, ax, order, width=0.4, linewidth=1, transform=None, offset=0, color=None, 
             hue=None, palette=None, marker='o', linewidth_mean=1):
    """

    Main function for swarmplots in the paper

    Args:
        data (_type_): pandas dataframe
        x (_type_): name of x axis variable (categorical variable)
        y (_type_): name of y axis variable (continuous variable)
        ax (_type_): axis
        order (_type_): order of categorical values
        width (float, optional): width of mean line. Defaults to 0.4.
        linewidth (int, optional): linewidth for points. Defaults to 1.
        transform (_type_, optional): for moving the points left or right. Defaults to None.
        offset (int, optional): offset value for the mean line. Defaults to 0.
        color (_type_, optional): color of points (if using single color). Defaults to None.
        hue (_type_, optional): categorical variable for hue. Defaults to None.
        palette (_type_, optional): dictionary for hue. Defaults to None.
        marker (str, optional): marker style for points. Defaults to 'o'.
        linewidth_mean (int, optional): thickness of mean line. Defaults to 1.
    """

    # Calculate means
    df_mean = [data[data[x] == o][y].mean() for o in order]
    
    # Draw mean lines
    [ax.hlines(y, i + offset - width/2, i + offset + width/2, zorder=100, color='k', 
               linewidth=linewidth_mean) for i, y in enumerate(df_mean)]
    
    # Draw points
    sns.swarmplot(data=data, x=x, y=y, ax=ax, order=order, linewidth=linewidth, transform=transform, color=color,
                  hue=hue, palette=palette, marker=marker)
    

