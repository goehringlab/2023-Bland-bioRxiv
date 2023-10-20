import seaborn as sns


def dataplot(data, x, y, ax, order, width=0.4, linewidth=1, transform=None, offset=0, color=None, 
             hue=None, palette=None, marker='o', linewidth_mean=1):
    df_mean = [data[data[x] == o][y].mean() for o in order]
    [ax.hlines(y, i + offset - width/2, i + offset + width/2, zorder=100, color='k', 
               linewidth=linewidth_mean) for i, y in enumerate(df_mean)]
    sns.swarmplot(data=data, x=x, y=y, ax=ax, order=order, linewidth=linewidth, transform=transform, color=color,
                  hue=hue, palette=palette, marker=marker)
    

