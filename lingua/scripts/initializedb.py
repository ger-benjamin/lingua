import os
import sys
import transaction
from sqlalchemy import engine_from_config, event
from sqlalchemy.schema import CreateSchema
from pyramid.paster import get_appsettings, setup_logging
from ..models.main_model import Base, DBSession, SCHEMA
#For test datas
from ..models.main_model import Base, DBSession, SCHEMA, Voc, Word, Word_fr, Word_de

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
    
    #Test datas
    with transaction.manager:
        voc = Voc(name='test')
        DBSession.add(voc)

    with transaction.manager:
        DBSession.add_all([
            Word(id_voc=1),
            Word(id_voc=1),
            ])

    with transaction.manager:
        DBSession.add_all([
            Word_de(id_word=1, kind='die', word='Schaufel', vari='n'),
            Word_fr(id_word=1, kind='la', word='pelle', vari='s'),
            Word_de(id_word=2, kind='der', word='Hammer', vari='ä'),
            Word_fr(id_word=2, kind='le', word='marteau', vari='x'),
           ])
