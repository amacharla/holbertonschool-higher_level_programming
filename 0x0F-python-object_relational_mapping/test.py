#!/usr/bin/python3

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
# engine <> database
engine = create_engine('sqlite:///:memory:', echo=True)

# holds table objects
meta = MetaData()

#simple table creation
users = Table('users', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String(128)),
        Column('fullname', String(128))
        )
addresses = Table('addressess', meta,
        Column('id', Integer, primary_key=True),
        Column('user_id', None, ForeignKey('users.id')),
        Column('email_address', String, nullable=False)
        )
meta.create_all(engine)  # sends tables into database

# insert..values
row = users.insert().values(name='noop', fullname='noopLion')

#
connect = engine.connect()
result = connect.execute(row)
