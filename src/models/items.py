import sqlalchemy

metadata = sqlalchemy.MetaData()

items_table = sqlalchemy.Table(
    'items',
    metadata,
    sqlalchemy.Column('itemid', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('price', sqlalchemy.Float)
)
