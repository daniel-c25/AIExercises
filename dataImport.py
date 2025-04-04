import pandas
import plotly.graph_objects as go

game_sales_raw_data = pandas.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
def show_dash_table_raw_game_sales(dataframe):
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(dataframe.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[dataframe[col] for col in dataframe.columns],
                   fill_color='lavender',
                   align='left'))
    ])
    fig.show()