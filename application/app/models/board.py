from .db import db, environment, SCHEMA, add_prefix_for_prod

user_boards = db.Table(
     "user_boards",
     db.Model.metadata,
     db.Column('user_id', db.ForeignKey('users.id'), primary_key=True),
     db.Column('board_id', db.ForeignKey('boards.id'), primary_key=True)
)

class Board(db.Model):
    __tablename__ = "boards"

    if environment == "production":
         __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    users = db.relationship('User',secondary=user_boards, back_populates='boards')
    columns = db.relationship('BoardColumn', back_populates='board')
