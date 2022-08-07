import pandas as pd
import os

def main():
    # The file name is hardcoded and assigned to fp.
    #fp = '/Users/sohamgangopadhyay/Projects/Internal/Bootcamp/Data-Copier/Data/retail_db_json/order_items/part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'

    BASE_DIR = '/Users/sohamgangopadhyay/Projects/Internal/Bootcamp/Data-Copier/Data/retail_db_json'
    table_name = 'order_items'

    # Lists all the files in the folder.
    # All our folders contain only one file.
    # Hence, we can access it by reading first element in the list as below.

    file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
    fp = f'{BASE_DIR}/{table_name}/{file_name}'

    df = pd.read_json(fp, lines=True)
    # Here is the piece of code to read the content of the file as reader.
    json_reader = pd.read_json(fp, lines=True, chunksize=1000)

    # Here is the piece of code to read each chunk as Dataframe.
    for idx, df in enumerate(json_reader):
        print(f'Number of records in chunk with index {idx} is {df.shape[0]}')


if __name__ == "__main__":
    main()
