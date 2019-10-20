from .uifitapi import *
import falcon

api = application = falcon.API()
api.add_route('/fit', FitResource())

