import cherrypy
import json
import datetime
from dateutil.parser import parse

@cherrypy.expose
class IncomeController:
    @cherrypy.tools.accept(media='application/json')
    def __init__(self, datastore_facade):
        self.datastore = datastore_facade

    def GET(self, start=None, end=None, page=0, pagesize=15):
        income_list = None
        if start == None or end == None:
            income_list = self.datastore.GetIncome(page, pagesize)
        else:
            income_list = self.datastore.GetIncomeInRange(parse(start), parse(end))

        result = list()
        for pay in income_list:
            result.append(pay.to_json())
        
        return json.dumps(result)

    def POST(self):
        body = json.loads(cherrypy.request.body.read())
        date = body["date"]
        amount = body["amount"]
        self.datastore.AddIncome(parse(date), amount)
        return json.dumps('{"result":"success","date":"' + str(date) + '","amount":' + str(amount) + '}')
        
