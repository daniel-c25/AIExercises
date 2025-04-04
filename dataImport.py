import pandas
import plotly.graph_objects as go

game_sales_raw_data = pandas.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")
def show_raw_data_table(dataframe):
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(dataframe.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[dataframe[col] for col in dataframe.columns],
                   fill_color='lavender',
                   align='left'))
    ])
    fig.show()

def show_dataframe_table_description(dataframe):
    dataframe = dataframe.reset_index()
    dataframe = dataframe.rename(columns={'index': 'Statistic'})
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(dataframe.columns),
                    fill_color='lightgray',
                    align='left'),
        cells=dict(values=[dataframe[col].astype(str) for col in dataframe.columns],
                   fill_color='white',
                   align='left'))
    ])

    fig.update_layout(title='DataFrame Description')
    fig.show()