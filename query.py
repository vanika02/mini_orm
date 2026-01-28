# this file will converts python into filtering logic

class query_set:
    def __init__(self, table):
        self.table = table

    # filter
    def filter(self, **kwargs):
        result = []
        for row in self.table:
            match = True
            for k, v in kwargs.items():
                if row.get(k) != v:
                    match = False
            if match:
                result.append(row)
            return result

    # get
    def get(self, **kwargs):
        for row in self.table:
            match = True
            for k, v in kwargs.items():
                if row.get(k) != v:
                    match = False
            if match:
                return row
            return None
    
    # update
    def update(self, where, **new_values):
        for row in self.table:
            if all(row[k] == v for k, v in where.items()):
                row.update(new_values)
    # delete
    def delete(self, **where):
        self.table[:] = [
            row for row in self.table
            if not all(row[k] == v for k, v in where.items())
        ]

    # all
    def all(self):
        return self.table