import pandas
from dash import Dash, dash_table, html

game_sales_raw_data = pandas.read_csv("Video_Games_Sales_as_at_22_Dec_2016.csv")

def show_dash_table_raw_game_sales():
    app = Dash(__name__)
    app.layout = html.Div([
        dash_table.DataTable(
            id='my-table',  # A unique identifier for your table
            columns=[{"name": i, "id": i} for i in game_sales_raw_data.columns],
            data=game_sales_raw_data.to_dict('records'),
            # Add other DataTable properties as needed (e.g., sort_action, filter_action)
        )
    ])
    if __name__ == '__main__':
        app.run(debug=True)