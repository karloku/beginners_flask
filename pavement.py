import os
import sys
sys.path.append(os.path.dirname(__file__))

from paver.easy import *
from application import app

@task
def server():
    app.run()

@task
def shell():
    import code
    ctx = {}
    ctx.update(app.make_shell_context())
    code.interact(local=ctx)

@task
def routes():
    from lib.tasks.routes import show_routes, list_routes
    show_routes(app)
