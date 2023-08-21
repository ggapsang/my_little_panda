import pandas as pd

class VLookup :
    def __init__(self, source_df) :
        self.source.df = source_df

    def lookup(self, lookup_df, lookup_value, return_column, exact_match=True) :
        """
        Performs a VLOOKUP-like operation.
        
        Args:
        - lookup_df (pd.DataFrame): The dataframe containing the values to lookup.
        - lookup_value (str): The column name to perform the lookup on (equivalent to the column containing the lookup_value in VLOOKUP).
        - return_column (str): The column name from which to return the value (equivalent to col_index_num in VLOOKUP).
        - exact_match (bool): If True, performs an exact match. If False, performs an approximate match. Default is True.
        
        Returns:
        - pd.DataFrame: A dataframe with the original columns from lookup_df and the matched values from the specified return_column.
        """

        merge_how = 'left' if exact_match else 'outer'
        merged_df = lookup_df.merge(self.source_df[[lookup_value, return_column]], on=lookup_value, how=merge_how)
        
        return merged_df


################################3
# Usage example:
data_source = {
    'Name': ['Alice', 'Bob', 'David'],
    'Occupation': ['Engineer', 'Doctor', 'Lawyer']
}
source_df = pd.DataFrame(data_source)

data_lookup = {
    'Name': ['Alice', 'Bob', 'Charlie']
}
lookup_df = pd.DataFrame(data_lookup)

vlookup = VLookup(source_df)
result = vlookup.lookup(lookup_df, 'Name', 'Occupation')
print(result)

"""In this class:

The __init__ method initializes the VLookup object with a source dataframe (source_df), which is equivalent to the table array in the VLOOKUP function.

The lookup method takes in a dataframe (lookup_df) containing the values to be looked up, the name of the column to perform the lookup on (on_column), the name of the column from which to return the value (return_column), and whether to perform an exact match (exact_match). It then uses the merge method to perform the lookup and returns the result.
"""
