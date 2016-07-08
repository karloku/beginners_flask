from flask import url_for
from itertools import groupby
from functools import partial
import inspect

COLOR_FILE = '\033[95m'
COLOR_METHOD = '\033[94m'
COLOR_PATTERN = '\033[93m'
COLOR_CALLBACK = '\033[92m'
ENDC = '\033[0m'

def method(m):
    return (COLOR_METHOD + '{0: ^16}' + ENDC).format(','.join(m))

def pattern(p):
    return (COLOR_PATTERN + '{0: <36}' + ENDC).format(p)

def callback(c):
    c_name = function_name(c)
    return (COLOR_CALLBACK + '{0}' + ENDC).format(c_name)

def function_name(fn):
    if inspect.ismethod(fn) and hasattr(fn.__self__, '__name__'):
        return '#'.join([fn.__self__.__name__, fn.__name__])

    return fn.__name__

def get_function(app, endpoint):
    return app.view_functions[endpoint]

def get_route_sourcefile(route, app):
    return get_sourcefile(get_function(app, route.endpoint))

def get_sourcefile(callback):
    if callback.__closure__:
        for closure_cell in callback.__closure__:
            if inspect.isfunction(closure_cell.cell_contents):
                return get_sourcefile(closure_cell.cell_contents)

    return inspect.getsourcefile(callback)

def show_routes(app):
    app_route_sourcefile = partial(get_route_sourcefile, app=app)
    routes = sorted([route for route in app.url_map.iter_rules()], key=app_route_sourcefile)
    routes_grouped = groupby(routes, key=app_route_sourcefile)

    print routes_grouped
    for file, file_routes in routes_grouped:
        print (COLOR_FILE + '{0}:' + ENDC).format(file)
        for route in file_routes:
            print ('  | {0} | {1}\t | {2}').format(
                                                   method(route.methods),
                                                   pattern(route.rule),
                                                   callback(get_function(app, route.endpoint)))
        print ''

def list_routes(app):
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)
    
    for line in sorted(output):
        print line
