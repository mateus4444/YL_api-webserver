import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

# from .companies import Company
from .db_session import SqlAlchemyBase
# from .types import Type


class Item(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'items'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True,
                           nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    amount = sqlalchemy.Column(sqlalchemy.String)

    company = sqlalchemy.Column(sqlalchemy.String, ForeignKey('companies.name'))

    date = sqlalchemy.Column(sqlalchemy.String)
    rating = sqlalchemy.Column(sqlalchemy.String)
    image = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)

    type = sqlalchemy.Column(sqlalchemy.String, ForeignKey('types.name'))

    types = relationship("Type", order_by="Type.name")