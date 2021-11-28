from .test_controller import api as test_route
from .auth_controller import api as auth_route
from .app_controller import api as app_route
from .rating_controller import api as rating_route

controllers = [
    {"name": test_route,"path": "/test"}, 
    {"name": auth_route, "path" : "/auth"},
    {"name": app_route, "path" : "/app"},
    {"name": rating_route, "path": "/rating"}
]