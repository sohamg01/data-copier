import pandas as pd


def main():
    # The file name is hardcoded and assigned to fp.
    fp = '/Users/sohamgangopadhyay/Projects/Internal/Bootcamp/Data-Copier/Data/retail_db_json/order_items/part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'

    df = pd.read_json(fp, lines=True)
    # Here is the piece of code to read the content of the file as reader.
    json_reader = pd.read_json(fp, lines=True, chunksize=1000)

    # Here is the piece of code to read each chunk as Dataframe.
    for idx, df in enumerate(json_reader):
        print(f'Number of records in chunk with index {idx} is {df.shape[0]}')


if __name__ == "__main__":
    main()
