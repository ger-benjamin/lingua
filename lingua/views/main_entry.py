import logging
from lingua.models import main_model as mmodel
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPPreconditionFailed

log = logging.getLogger(__name__)


"""
Lingua main page CRUD
Accepted params:
 * max_results
 * vocs
 * lang 
 * 
"""
class MainEntry(object):

    def __init__(self, request):
        self.request = request
        self.max_results = 100
        self.vocs = None
        self.avaliable_langs = ['fr', 'de']
        self.lang = None
        self.dbs = mmodel.DBSession 

    @view_config(route_name='words', renderer='json', request_method='GET')
    def get_words(self):
        self._get_params()
        words = {'voc': self.vocs, 'lang': self.lang,\
                 'max_results': self.max_results}
        return words 

    @view_config(route_name='vocs', renderer='json', request_method='GET')
    def get_vocs(self):
        vocs = []
        for voc in self.dbs.query(mmodel.Voc).all():
            vocs.append({
                'id': voc.id,
                'name': voc.name
                })
        return vocs

    def _get_params(self):
        params = self.request.params;

        max_results = params.get('max_results')
        if max_results and max_results.isdigit():
            self.max_results = min(self.max_results, int(max_results))

        lang = params.get('lang')
        if lang in self.avaliable_langs:
            self.lang = lang

        vocs = params.get('vocs')
        if vocs :
            self.vocs = vocs.split(',')
