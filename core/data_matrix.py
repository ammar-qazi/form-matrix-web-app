class DataMatrix:
    """Replacement for Pandas DataFrame functionality"""
    def __init__(self, data_dict):
        self.data = data_dict
        self.columns = list(data_dict.keys())
        self._length = len(next(iter(data_dict.values())))
    
    def copy(self):
        return DataMatrix({k: v.copy() for k, v in self.data.items()})
    
    def __getitem__(self, column):
        return self.data[column]
    
    def unique(self, column):
        values = set()
        for value in self.data[column]:
            if value is not None:  # Skip None values
                values.add(value)
        return sorted(list(values))  # Return sorted list for consistency
    
    def get_rows(self):
        """Return all rows as a list of dictionaries"""
        return [
            {col: self.data[col][i] for col in self.columns}
            for i in range(self._length)
        ]
    
    @property
    def empty(self):
        return self._length == 0
    
    def filter(self, column, value):
        """Filter the data to keep only rows where the column matches the value"""
        indices = [i for i, v in enumerate(self.data[column]) if v == value]
        new_data = {col: [self.data[col][i] for i in indices] for col in self.columns}
        return DataMatrix(new_data)
    
    def filter_multiple(self, conditions):
        """
        Filter the data based on multiple column-value pairs
        
        Args:
            conditions: dict of {column: value} pairs to filter by
        """
        indices = []
        for i in range(self._length):
            matches = True
            for col, val in conditions.items():
                if val is not None and self.data[col][i] != val:
                    matches = False
                    break
            if matches:
                indices.append(i)
        
        new_data = {col: [self.data[col][i] for i in indices] for col in self.columns}
        return DataMatrix(new_data)
    
    def get_row(self, line):
        try:
            idx = self.data['Line'].index(line)
            return {col: self.data[col][idx] for col in self.columns}
        except ValueError:
            return None