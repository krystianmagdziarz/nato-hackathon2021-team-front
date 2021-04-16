from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import subprocess


def home(request):
    return Response('Welcome!')


def followup(request):
    s = subprocess.Popen(["scrapy", "runspider", "/home/app/web/hospitalfollowup/hospitalfollowup/spiders/followup.py"],
                         stdout=subprocess.PIPE,
                         close_fds=True)
    print(s)
    return Response(status_code=200)


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(home, route_name='home')

        config.add_route('followup', '/followup/')
        config.add_view(followup, route_name='followup')

        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
