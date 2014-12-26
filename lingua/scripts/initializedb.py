import os
import sys
import transaction
from sqlalchemy import engine_from_config, event
from sqlalchemy.schema import CreateSchema
from pyramid.paster import get_appsettings, setup_logging
from ..models.main_model import Base, DBSession, SCHEMA, Test

"""
Create Lingua db structure
"""

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    event.listen(Base.metadata, 'before_create', CreateSchema(SCHEMA))
    Base.metadata.create_all(engine)

##    with transaction.manager:
##        test = Test(id=2, name=u'test sqlalchemy é')
##        DBSession.add(test)
