import numpy


class Frame:
    """
    Create DataFrames with jsonr.

    Paramaters:
        - columns (list): List of column names.
        - rows (list): List of rows.

    Attrubutes:
        - columns (list): List of column names.
        - rows (list): List of rows.
        - values (numpy.array): NumpyArray of values.
        - shape (tuple): Shape of values.

    Methods:
        - column/add_column (column_name, values=None): Add a column to the DataFrame.
        - row/add_row (row_name, values=None): Add a row to the DataFrame.
        - get_column (column_name): Get a column from the DataFrame.
        - shape (tuple): Get the shape of the DataFrame.
        - save/write (file_name): Save the DataFrame to a file.
        - load/read (file_name): Load the DataFrame from a file.
        - drop (columns=None, rows=None): Drop row(s) or column(s) from the DataFrame.
        - head (n=5): Get the first n rows of the DataFrame.
        - tail (n=5): Get the last n rows of the DataFrame.

        - describe (n=5): Get the descriptive statistics of the DataFrame.
        - rename_column (old_name, new_name): Rename a column in the DataFrame.
        - filter_rows (condition): Filter rows in the DataFrame.
        - filter_by_value (column_name, value): Filter rows by value in the DataFrame.
        - sort_by_column (column_name, ascending=True): Sort the DataFrame by a column.
        - drop_duplicates (column_name): Drop duplicate rows in the DataFrame.
        - group_by (by): Group the DataFrame by a column.
    """

    def __init__(self, columns=None, rows=None):
        self.columns = columns or []
        self.rows = rows or []
        self.values = numpy.array([row for row in self.rows])
        self.shape = self.shape()
        self.column = self.add_column
        self.row = self.add_row
        self.save = self.write
        self.read = self.load

        self._update_attrs()

    def _update_attrs(self):
        """Update attributes."""
        if self.columns != []:
            for column in self.columns:
                key = str(column).replace(" ", "_").replace("-", "_")
                if key[0].isdigit():
                    key = f"_{key}"

                setattr(self, key, self.get_column(column))
        return self

    @classmethod
    def string(cls, data_string):
        """Create a DataFrame from a string."""
        lines = data_string.strip().split("\n")
        columns = lines[0].split(",")
        rows = [line.split(",") for line in lines[1:]]
        return cls(columns=columns, rows=rows)

    def load(self, file):
        """Load a DataFrame from a file."""
        with open(file, "r") as f:
            data_string = f.read()

        cls = self.string(data_string)
        self.columns = cls.columns
        self.rows = cls.rows
        self._update_attrs()
        return self

    def write(self, file, raw=True):
        """Save a DataFrame to a file."""
        if raw:
            columns_string = ",".join(self.columns)

            rows_string = "\n".join(
                [",".join(str(item) for item in row) for row in self.rows]
            ) 

            raw_frame = f"{columns_string}\n{rows_string}"
            with open(file, "w") as f:
                f.write(raw_frame)
        else:
            with open(file, "w") as f:
                f.write(self.__repr__())
        return self

    def __getitem__(self, column_name):
        if column_name in self.columns:
            column_index = self.columns.index(column_name)
            return [row[column_index] for row in self.rows]
        else:
            raise KeyError(f"Column '{column_name}' does not exist in the Frame.")

    def __repr__(self):
        rows = []
        num_columns = len(self.columns)
        num_rows = len(self.rows)

        if self.columns:
            column_widths = [
                max(len(str(row[i])) for row in self.rows + [self.columns])
                for i in range(num_columns)
            ]

            header = ["{:>{width}}".format("", width=4)] + [
                "{:>{width}}".format(str(col), width=column_widths[i])
                for i, col in enumerate(self.columns)
            ]
            rows.append(" | ".join(header))
            rows.append("-" * (sum(column_widths) + (num_columns + 1) * 3))

        for i, row in enumerate(self.rows):
            line_number = "{:<4}".format(str(i))
            row_values = [line_number] + [
                "{:>{width}}".format(str(cell), width=column_widths[j])
                for j, cell in enumerate(row)
            ]
            rows.append(" | ".join(row_values))

        return "\n".join(rows)

    def head(self, n=5):
        """Get the first n rows of the DataFrame."""
        return Frame(columns=self.columns, rows=self.rows[:n])._update_attrs()

    def tail(self, n=5):
        """Get the last n rows of the DataFrame."""
        return Frame(columns=self.columns, rows=self.rows[-n:])._update_attrs()

    def drop(self, columns=None, rows=None):
        """Drop row(s) or column(s) from the DataFrame."""
        new_columns = [col for col in self.columns if col not in (columns or [])]
        new_data = []
        rows = rows or []
        for row in self.rows:
            if row not in rows:
                new_row = [
                    value
                    for col, value in zip(self.columns, row)
                    if col not in (columns or [])
                ]
                new_data.append(new_row)
        return Frame(columns=new_columns, rows=new_data)._update_attrs()

    def add_row(self, row):
        """Add a row to the DataFrame."""
        row = list(row)
        if not self.columns:
            self.columns = [f"column_{i+1}" for i in range(len(row))]
        self.rows.append(row)
        self._update_attrs()
        return self.rows[-1]

    def add_column(self, name, data):
        """Add a column to the DataFrame."""
        self.columns.append(name)
        for i, value in enumerate(data):
            if i >= len(self.rows):
                self.rows.append([])
            self.rows[i].append(value)
        self._update_attrs()
        return self.get_column(name)

    def get_column(self, column_name):
        """Get a column from the DataFrame."""
        column_index = self.columns.index(column_name)
        return [row[column_index] for row in self.rows]

    def shape(self):
        """Get the shape of the DataFrame."""
        num_rows = len(self.rows)
        num_cols = len(self.columns)
        return num_rows, num_cols

    def describe(self):
        """Get the descriptive statistics of the DataFrame."""
        data_transposed = zip(*self.rows)
        description = {}
        for column, values in zip(self.columns, data_transposed):
            if all(isinstance(value, (int, float)) for value in values):
                description[column] = {
                    "count": len(values),
                    "mean": sum(values) / len(values),
                    "std": (
                        sum((x - (sum(values) / len(values))) ** 2 for x in values)
                        / len(values)
                    )
                    ** 0.5,
                    "min": min(values),
                    "25%": sorted(values)[int(len(values) * 0.25)],
                    "50%": sorted(values)[int(len(values) * 0.5)],
                    "75%": sorted(values)[int(len(values) * 0.75)],
                    "max": max(values),
                }
            else:
                description[column] = {
                    "count": len(values),
                    "unique_values": list(set(values)),
                }
        return description

    def rename_column(self, old_name, new_name):
        """Rename a column in the DataFrame."""
        if old_name not in self.columns:
            raise KeyError(f"Column '{old_name}' does not exist in the Frame.")
        if new_name in self.columns:
            raise ValueError(f"Column '{new_name}' already exists in the Frame.")
        column_index = self.columns.index(old_name)
        self.columns[column_index] = new_name

    def filter_rows(self, condition):
        """Filter rows in the DataFrame."""
        filtered_data = [row for row in self.rows if condition(row)]
        return Frame(columns=self.columns, rows=filtered_data)._update_attrs()

    def filter_by_value(self, column_name, value):
        """Filter rows by value in the DataFrame."""
        column_index = self.columns.index(column_name)
        filtered_data = [row for row in self.rows if row[column_index] == value]
        return Frame(columns=self.columns, rows=filtered_data)._update_attrs()

    def sort_by_column(self, column_name, ascending=True):
        """Sort the DataFrame by a column."""
        if column_name not in self.columns:
            raise KeyError(f"Column '{column_name}' does not exist in the Frame.")
        column_index = self.columns.index(column_name)
        sorted_data = sorted(
            self.rows, key=lambda row: row[column_index], reverse=not ascending
        )
        return Frame(columns=self.columns, rows=sorted_data)._update_attrs()

    def drop_duplicates(self, subset=None):
        """Drop duplicate rows in the DataFrame."""
        subset = subset or self.columns
        unique_rows = []
        seen = set()
        for row in self.rows:
            key = tuple(row[self.columns.index(col)] for col in subset)
            if key not in seen:
                unique_rows.append(row)
                seen.add(key)
        return Frame(columns=self.columns, rows=unique_rows)._update_attrs()

    def group_by(self, by):
        """Group the DataFrame by a column."""
        grouped_data = {}
        by_columns = by if isinstance(by, list) else [by]
        for row in self.rows:
            key = tuple(row[self.columns.index(col)] for col in by_columns)
            if key not in grouped_data:
                grouped_data[key] = []
            grouped_data[key].append(row)
        return grouped_data

    def __setitem__(self, column_name, values):
        if column_name in self.columns:
            column_index = self.columns.index(column_name)
            for i in range(len(self.rows)):
                self.rows[i][column_index] = values[i]
        else:
            raise KeyError(f"Column '{column_name}' does not exist in the Frame.")
