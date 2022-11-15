import sqlalchemy

metadata = sqlalchemy.MetaData()

purchases_table = sqlalchemy.Table(
    'purchases',
    metadata,
    sqlalchemy.Column('purchaseid', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('itemid', sqlalchemy.Integer),
    sqlalchemy.Column('userid', sqlalchemy.Integer),
    sqlalchemy.Column('date', sqlalchemy.String)
)
