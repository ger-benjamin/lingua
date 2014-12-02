from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/index.pt')
def get_home(request):
    return {'project': 'Lingua'}
