from app import create_app, db, cli
from app.models import User, User_dataset, Data_subset

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'User_dataset': User_dataset}
