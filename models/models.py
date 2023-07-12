from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON


metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False), # не может быть пустым и принимать Null
    Column('permissions', JSON),
)

roles = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False), # ?
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id')), #  ссылаемся на таблицу roles и столбец id
)