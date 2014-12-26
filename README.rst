Lingua
=======
Lingua is an application to train my vocabulary on a foreign language.
And an application to train myself with AngularJS, Pyramid, less, ...

Just for me, not thought for an extern fork by you :-)


Install
=========
see http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html#installing-chapter


Install apache and modwsgi
---------------------------

``sudo apt-get install apache2``

``sudo apt-get install libapache2-mod-wsgi-py3``


Install setuptools
-------------------

Copy ``https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py``

And run it ``sudo python3 ez_setup.py``

Try it by executing ``python3 -c 'import setuptools'``


Installing the virtualenv Package
----------------------------------

``easy_install virtualenv``


Creating the Virtual Python Environment
----------------------------------------

``export VENV=/var/www/lingua``

``virtualenv $VENV``


Installing the project
-------------------------

``git clone https://github.com/ger-benjamin/lingua.git``

or ``$VENV/bin/easy_install "pyramid==1.5.2"`` (from scratch)


Create an apache conf file
-----------------------------

Create a conf file in your apache conf directory. Add this content::

    WSGIApplicationGroup %{GLOBAL}                                                   
    WSGIPassAuthorization On                                                         
    WSGIDaemonProcess pyramid threads=4 \                                            
      python-path=/var/www/lingua/lib/python3.3/site-packages                       
    WSGIScriptAlias /lingua /var/www/lingua/pyramid.wsgi                             
                                                                                 
    <Directory /var/www/lingua>                                                      
      WSGIProcessGroup pyramid                                                       
      Order allow,deny                                                               
      Allow from all                                                                 
    </Directory>  


Create a wsgi script to call the pyramid content
-------------------------------------------------

At root of your VENV, create a pyramid.wsgi file::

    from pyramid.paster import get_app, setup_logging
    ini_path = '/var/www/lingua/lingua/development.ini'
    setup_logging(ini_path)
    application = get_app(ini_path, 'main')


Build
=====

``$VENV/bin/python3 setup.py install``

``apache2ctl graceful``
