from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.main_model import Base, DBSession, Test


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('ng', 'static/js/ng', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('words', '/words')
    config.add_route('vocs', '/vocs')

    config.scan()
    return config.make_wsgi_app()
