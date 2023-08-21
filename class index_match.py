import pandas as pd

class IndexMatch:
    def __init__(self, dataframe):
        self.df = dataframe
        
    def lookup(self, lookup_column, lookup_value, return_column):
        """
        Looks up a value in a given column and returns the corresponding value 
        from another column.
        
        Args:
        - lookup_column (str): Name of the column where the lookup_value should be searched.
        - lookup_value (str/int/float): Value to be searched in the lookup_column.
        - return_column (str): Name of the column from which the result should be fetched.
        
        Returns:
        - result (str/int/float): Resulting value from the return_column. Returns None if not found.
        """
        try:
            result = self.df.loc[self.df[lookup_column] == lookup_value, return_column].values[0]
            return result
        except IndexError:
            return None

########################
# Usage example:
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [28, 32, 25, 30],
    'Occupation': ['Engineer', 'Doctor', 'Designer', 'Lawyer']
}
df = pd.DataFrame(data)
index_match = IndexMatch(df)
charlies_occupation = index_match.lookup('Name', 'Charlie', 'Occupation')
print(charlies_occupation)

"""
This class allows you to specify which column you want to search in (lookup_column), what value you want to search for (lookup_value), and which column you want to retrieve the value from (return_column). This way, you can handle a variety of lookup scenarios with a single class.
"""
