import pandas as pd
import argparse

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="MM2 offset validation summary.")
    parser.add_argument('csv_file', type=str, help="Path to the CSV file containing MM2 offset data")
    args = parser.parse_args()

    # Load the CSV file
    df = pd.read_csv(args.csv_file)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    # pd.set_option('display.show_dimensions', True)
    pd.set_option('display.expand_frame_repr', False)

    # Create a pivot table
    pivot_table = pd.pivot_table(df,
                                 index='MESSAGE',
                                 columns=['GROUP STATE', 'IS OK'],
                                 aggfunc='size',
                                 fill_value=0)

    # Add a column for the total count of messages
    pivot_table['Total messages'] = pivot_table.sum(axis=1)

    # Calculate grand totals
    grand_totals = pivot_table.sum(axis=0).to_frame().T
    grand_totals.index = ['Grand Total']

    # Append the grand totals row to the pivot table
    pivot_table = pd.concat([pivot_table, grand_totals])

    pivot_table.to_csv('pivot_table_summary.csv')

    # Display the pivot table
    print(pivot_table)

if __name__ == "__main__":
    main()
