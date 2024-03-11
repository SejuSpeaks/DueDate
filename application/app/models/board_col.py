from .db import db, environment, SCHEMA, add_prefix_for_prod


class BoardColumn(db.Model):
    __tablename__ = "board_columns"

    if environment == "production":
         __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    board_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('boards.id')))

    board = db.relationship('Board', back_populates='columns')
    tasks = db.relationship('Task', back_populates='column')
