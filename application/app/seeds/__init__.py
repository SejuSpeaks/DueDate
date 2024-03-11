from flask.cli import AppGroup
from .users import seed_users, undo_users
from .boards import seed_boards, undo_boards
from .user_boards import seed_user_boards, undo_user_boards
from .columns import seed_columns, undo_columns
from .tasks import seed_tasks, undo_tasks
from .sub_tasks import seed_sub_tasks, undo_sub_tasks

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_boards()
        undo_user_boards()
        undo_columns()
        undo_tasks()
        undo_sub_tasks()
    seed_users()
    seed_boards()
    seed_user_boards()
    seed_columns()
    seed_tasks()
    seed_sub_tasks()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_boards()
    undo_user_boards()
    undo_columns()
    undo_tasks()
    undo_sub_tasks()
    # Add other undo functions here
