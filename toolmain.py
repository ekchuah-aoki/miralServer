# coding: UTF-8

import webapp2

from tools.master.importTrainCompanyKind import importTrainCompanyKind
from tools.master.importTrainKind import importTrainKind
from tools.master.importStationKind import importStationKind

app = webapp2.WSGIApplication([
                               ('/toolmain/importTrainCompanyKind', importTrainCompanyKind),
                               ('/toolmain/importTrainKind', importTrainKind),
                               ('/toolmain/importStationKind', importStationKind),
], debug=True)            
