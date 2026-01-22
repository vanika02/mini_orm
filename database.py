# this is where my fake database is present 
# what happens here is we know in real world MySql/SQlite stores the data but here 
# python lists will store the data
# database.py == storage layer

database = {
    "students": [],
    "teachers": []
}

def get_next_id(table):
    """
    this simulates auto-increment primary key in SQL
    """
    if not table:
        return 1
    return table[-1]["id"] + 1
