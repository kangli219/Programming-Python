import numpy as np
import seaborn as sns

def catplot_bar(g, barwidth_ratio, barlabel_round, xlabel, ylabel):
    '''
        The function realizes aesthestics controls for seaborn's bar catplot with one subplot
        - g: a facetgrid with one subplot
        - barwidth_ratio: adjust the original bar width to a shorter one
        - barlabel_round: round barlabel values
        - ylabel, xlabel: label on x-axis and y-axis
    '''
    heights = [p.get_height() for p in g.ax.patches]
    above = np.mean(heights) * 0.02

    for p in g.ax.patches:
        height = p.get_height()
        width = p.get_width()
        width_new = width * barwidth_ratio
        width_diff = width - width_new
        
        # bar width adjustmentand
        p.set_width(width_new)
                
        # new bar center
        p.set_x(p.get_x() + width_diff * 0.5)
                    
        # bar heights labeling
        g.ax.text(p.get_x()+p.get_width() * 0.5,
                 height + above,
                 round(height,1),
                 ha="center") 
        
    g.set_axis_labels(xlabel,ylabel)   
    return g

    
    
def catplot_bar_col(g, barwidth_ratio, barlabel_round, xlabel, ylabel):
    '''
        The function realizes aesthestics controls for seaborn's bar catplot that has col subplots
        - g: a facetgrid with multiple subplot specified by col
        - barwidth_ratio: adjust the original bar width to a shorter one
        - barlabel_round: round barlabel values
        - ylabel, xlabel: label on x-axis and y-axis
    ''' 
    for ax in g.axes:
        # subplot titles
        subtitle = ax.get_title().split(' = ')[1]  # get rid of the " variable name = "
        ax.set_title(subtitle)
        
        # bar heights, widths, and labels
        heights = [p.get_height() for p in ax.patches]
        above = np.mean(heights) * 0.02

        for p in ax.patches:
            height = p.get_height()
            width = p.get_width()
            width_new = width * barwidth_ratio
            width_diff = width - width_new

            p.set_width(width_new)
            p.set_x(p.get_x() + width_diff * 0.5)
            ax.text(p.get_x()+p.get_width() * 0.5,
                     height + above,
                     round(height, barlabel_round),
                     ha="center")
            
    # axis label, legend
    g.set_axis_labels(xlabel,ylabel)    
    return g