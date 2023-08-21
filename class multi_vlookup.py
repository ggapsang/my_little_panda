import pandas as pd

class MultiVLookup:
    def __init__(self, source_df):
        """Initialize the MultiVLookup object with a source dataframe."""
        self.source_df = source_df
        
    def lookup(self, lookup_df, on_columns, return_columns, exact_match=True):
        """
        Performs a VLOOKUP-like operation based on multiple criteria.
        
        Args:
        - lookup_df (pd.DataFrame): The dataframe containing the values to lookup.
        - on_columns (list): A list of column names to perform the lookup on.
        - return_columns (list): A list of column names from which to return values.
        - exact_match (bool): If True, performs an exact match. If False, performs an approximate match. Default is True.
        
        Returns:
        - pd.DataFrame: A dataframe with the original columns from lookup_df and the matched values from the specified return_columns.
        """
        merge_how = 'left' if exact_match else 'outer'
        merged_df = lookup_df.merge(self.source_df[on_columns + return_columns], on=on_columns, how=merge_how)
        return merged_df


#################################
# Usage example:
data_source = {
    'Name': ['Alice', 'Bob', 'David', 'Alice'],
    'City': ['NY', 'LA', 'NY', 'LA'],
    'Occupation': ['Engineer', 'Doctor', 'Lawyer', 'Artist']
}
source_df = pd.DataFrame(data_source)

data_lookup = {
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
    'City': ['NY', 'LA', 'LA', 'SF']
}
lookup_df = pd.DataFrame(data_lookup)

multi_vlookup = MultiVLookup(source_df)
result = multi_vlookup.lookup(lookup_df, ['Name', 'City'], ['Occupation'])
print(result)
