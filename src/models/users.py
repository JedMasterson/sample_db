import sqlalchemy

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('userid', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('age', sqlalchemy.Integer)
)
