import plotly.express as px
from plotly.graph_objects import Figure
from download import download_data

def plot_ts(ticker:str) -> Figure:
    """
    Plot historical closing prices of a stock using Plotly.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol.
    Returns
    -------
    Figure
        A Plotly graph.
    ---
    """
    df = download_data(ticker)
    fig = px.line(
            df, x='Date', 
            y='Close', 
            title= f'{ticker} Stack Prices'
        )
    return fig