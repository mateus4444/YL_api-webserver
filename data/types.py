import sqlalchemy
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
# from .items import Item


class Type(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'types'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True,
                           nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)

    types = relationship("Item", order_by="Item.type")