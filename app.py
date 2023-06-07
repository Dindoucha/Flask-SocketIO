from app import socketio, create_app,db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

if __name__ == "__main__":
    app = create_app()
    manager = Manager(app)
    migrate = Migrate(app, db)
    manager.add_command('db', MigrateCommand)
    socketio.run(app)
