from taipy import Gui
import pandas as pd

#getting started with light mode
Gui(page="# getting started with *taipy*").run(dark_mode=False) # #creates a title, ## creates a subtitle, * for italics, ** for bold

def get_data(path_to_csv: str):
    # pandas.read_csv() returns a pd.DataFrame
    dataset = pd.read_csv(path_to_csv)
    dataset["Date"] = pd.to_datetime(dataset["Date"])
    return dataset

# Read the dataframe
path_to_csv = "dataset.csv"
dataset = get_data(path_to_csv)

# search engine <script async src="https://cse.google.com/cse.js?cx=c6456045664d54b97"> </script> <div class="gcse-search"></div>