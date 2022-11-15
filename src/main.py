import sqlalchemy
from sqlalchemy_utils import database_exists, create_database

from models.users import users_table
from models.items import items_table
from models.purchases import purchases_table

import random
import time


def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y/%m/%d', prop)


DATABASE_URL = f'sqlite:///./database.db'


def main():
    engine = sqlalchemy.create_engine(DATABASE_URL)
    if not database_exists(engine.url):
        create_database(engine.url)

    connection = engine.connect()

    des_tables = [users_table, items_table, purchases_table]
    for cur_table in des_tables:
        if not engine.dialect.has_table(connection, cur_table.name):
            cur_table.create(connection)

    users_table.drop(engine)
    items_table.drop(engine)
    purchases_table.drop(engine)

    user_list = []
    for id in range(93):
        age = random.randint(14, 85)
        user_list.append({'userid': id, 'age': age})
    connection.execute(users_table.insert(), user_list)



    items_list = []
    for id in range(205):
        price = round(random.uniform(640, 95350), 2)
        items_list.append({'itemid': id, 'price': price})
    connection.execute(items_table.insert(), items_list)

    purchases_list = []
    for id in range(25205):
        item = random.randint(0, 205)
        user = random.randint(0, 93)
        pur_date = random_date("2016/01/01", "2019/10/13", random.random())
        purchases_list.append({'purchase': id, 'itemid': item, 'userid': user, 'date': pur_date})
    connection.execute(purchases_table.insert(), purchases_list)


if __name__ == "__main__":
    main()
