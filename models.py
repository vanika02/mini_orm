# now as we know ORM's main job is to convert the tables into classes
# so here we do the same 
# students table --> Student class
# teachers table --> Teacher class

from database import database, get_next_id
from query import query_set
