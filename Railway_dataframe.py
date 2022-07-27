import pandas as pd

data = {
    "Train_name": ["LOKAMANYA EXPRESS", "HOWRAH EXPRESS", "HAMPI EXPRESS", "AMARVATHI EXPRESS", "KANYAKUMARI EXPRESS",
                   "RAJDHANI EXPRESS"],
    "Train_number": [221922, 973149, 938010, 221944, 661922, 226722],
    "Train_platform": [5, 4, 7, 2, 3, 9],
    "Train_arrival": ['18:30', '22:15', '22:30', '13:00', '10:30', '18:35'],
    "Train_depature": ['18:45', '22:30', '18:50', '18:15', '11:00', '18:55']

}


df = pd.DataFrame(data)
print(df)
