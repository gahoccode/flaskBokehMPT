"""
Bokeh plot generation helpers for portfolio optimization results.
"""
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColorBar, LinearColorMapper, BasicTicker
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256


def efficient_frontier_plot(df, optimal):
    """
    Create efficient frontier scatter plot with Sharpe ratio coloring and optimal points highlighted.
    Args:
        df (pd.DataFrame): Portfolio metrics DataFrame
        optimal (dict): Dict of optimal portfolios
    Returns:
        bokeh.plotting.Figure
    """
    mapper = linear_cmap(field_name='Sharpe', palette=Viridis256,
                        low=df['Sharpe'].min(), high=df['Sharpe'].max())
    p = figure(title="Efficient Frontier", x_axis_label="Risk (Volatility)", y_axis_label="Return",
               width=600, height=400, tools="pan,wheel_zoom,box_zoom,reset,save")
    p.scatter('Risk', 'Return', source=df, color=mapper, size=6, legend_label="Portfolios", alpha=0.6)

    # Highlight optimal portfolios
    for label, color in zip(['max_sharpe', 'min_variance', 'max_return'], ['red', 'blue', 'green']):
        pt = optimal[label]
        p.scatter([pt['Risk']], [pt['Return']], color=color, size=16, marker="star",
                  legend_label=label.replace('_', ' ').title())

    color_bar = ColorBar(color_mapper=mapper['transform'], ticker=BasicTicker(), label_standoff=12, location=(0,0))
    p.add_layout(color_bar, 'right')
    p.legend.click_policy = "hide"
    return p

def weights_bar_plot(optimal, asset_names):
    """
    Create bar plot of asset weights for the max Sharpe ratio portfolio.
    Args:
        optimal (dict): Dict of optimal portfolios
        asset_names (list): List of asset names
    Returns:
        bokeh.plotting.Figure
    """
    weights = [optimal['max_sharpe'][name] for name in asset_names]
    p = figure(x_range=asset_names, title="Max Sharpe Portfolio Weights",
               width=600, height=400, y_axis_label="Weight")
    p.vbar(x=asset_names, top=weights, width=0.6, color="orange")
    return p

def combined_layout(df, optimal):
    """
    Combine all plots into a single layout for output.
    Args:
        df (pd.DataFrame): Portfolio metrics DataFrame
        optimal (dict): Dict of optimal portfolios
    Returns:
        bokeh.layouts.LayoutDOM
    """
    asset_names = [name for name in df.columns if name not in ['Return', 'Risk', 'Sharpe']]
    frontier = efficient_frontier_plot(df, optimal)
    weights = weights_bar_plot(optimal, asset_names)
    return column(frontier, weights)
