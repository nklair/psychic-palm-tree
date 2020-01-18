import cherrypy
from Frontend.SpendingController import SpendingController
from Frontend.IncomeController import IncomeController
from Backend.MemoryFacade import MemoryFacade

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "http://localhost"
 
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.CORS.on': True,
        }
    }
    cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
    cherrypy.tree.mount(SpendingController(MemoryFacade()), '/spending/', conf)
    cherrypy.tree.mount(IncomeController(MemoryFacade()), '/income/', conf)
    cherrypy.quickstart()