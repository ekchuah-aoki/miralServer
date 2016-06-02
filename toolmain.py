# coding: UTF-8

import webapp2

from tools.master.importTrainCompanyKind import importTrainCompanyKind
from tools.master.importTrainKind import importTrainKind
from tools.master.importStationKind import importStationKind
from tools.master.DeleteTrainKind import DeleteTrainKind
from tools.imageSample1 import imageSample1

app = webapp2.WSGIApplication([
                               ('/toolmain/importTrainCompanyKind', importTrainCompanyKind),
                               ('/toolmain/importTrainKind', importTrainKind),
                               ('/toolmain/importStationKind', importStationKind),
                               ('/toolmain/DeleteTrainKind', DeleteTrainKind),
                               ('/toolmain/imageSample1', imageSample1),
                               
], debug=True)            
