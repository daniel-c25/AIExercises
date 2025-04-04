import pandas
import dataImport
import numpy as np

from dataImport import game_sales_raw_data

data_arrays = {
    'Name' : np.array(['John', 'Rosemyne', 'Tuuli']),
    'Role' : np.array(['unknown', 'main character', 'sister'])
}

test_dataframe = pandas.DataFrame(data_arrays)
dataImport.show_raw_data_table(dataImport.game_sales_raw_data)
dataImport.show_raw_data_table(test_dataframe)

dataImport.show_dataframe_table_description(game_sales_raw_data.describe(include='all'))