import cherrypy

@cherrypy.expose
class SpendingController:
    @cherrypy.tools.accept(media='application/json')

    def __init__(self, datastore_facade):
        self.datastore = datastore_facade

    def GET(self, start, end):
        items = self.datastore.GetItems()
        return items