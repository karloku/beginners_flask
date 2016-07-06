import code
from application import app

ctx = {}
ctx.update(app.make_shell_context())
code.interact(local=ctx)
