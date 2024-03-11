from .db import db, environment, SCHEMA, add_prefix_for_prod


class Task(db.Model):
    __tablename__ = "tasks"

    if environment == "production":
         __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    board_column_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('board_columns.id')))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    status = db.Column(db.String, nullable = False)

    column = db.relationship('BoardColumn', back_populates='tasks')
    sub_tasks = db.relationship('SubTask', back_populates='task' )
