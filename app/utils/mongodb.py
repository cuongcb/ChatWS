from flask_pymongo import PyMongo

class MongoDB(PyMongo):
    def init_app(self, app, config_prefix='MONGO'):
        def key(suffix):
            return "%s_%s" % (config_prefix, suffix)

        app.config.setdefault(key('HOST'), 'localhost')
        app.config.setdefault(key('PORT'), 27017)
        app.config.setdefault(key('DBNAME'), app.name)

