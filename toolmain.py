# coding: UTF-8

import webapp2

from tools.master.importTrainCompanyKind import importTrainCompanyKind
from tools.master.importTrainKind import importTrainKind
from tools.master.importStationKind import importStationKind
from tools.master.DeleteTrainKind import DeleteTrainKind

app = webapp2.WSGIApplication([
                               ('/toolmain/importTrainCompanyKind', importTrainCompanyKind),
                               ('/toolmain/importTrainKind', importTrainKind),
                               ('/toolmain/importStationKind', importStationKind),
                               ('/toolmain/DeleteTrainKind', DeleteTrainKind),
                               
], debug=True)            
