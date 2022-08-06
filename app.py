import pandas as pd


def main():
    # The file name is hardcoded and assigned to fp.
    fp = '/Users/sohamgangopadhyay/Projects/Internal/Bootcamp/Data-Copier/Data/retail_db_json/order_items/part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'

    df = pd.read_json(fp, lines=True)

    df.count()
    # df.describe()
    #
    # df.columns
    # df.dtypes
    #
    # df[['order_item_order_id', 'order_item_subtotal']]
    #
    print(df[df['order_item_order_id'] == 2])


if __name__ == "__main__":
    main()
