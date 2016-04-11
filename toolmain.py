# coding: UTF-8

import webapp2

from tools.master import importTrainKind

app = webapp2.WSGIApplication([
                               ('/toolmain/importTarainKind', importTrainKind.importTrainKind),
], debug=True)            
