from .measurements import Measurements
import falcon
import json

class FitResource(object):

    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read().decode()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

        try:
            data_json = json.loads(raw_json, encoding='utf-8')
            if 'image1' not in data_json and 'image2' not in data_json and 'image3' not in data_json and \
                    'height' not in data_json and 'style' not in data_json and 'size' not in data_json and 'brand' not in data_json:
                raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON',
                                   'Does not have the right attributes')
            if not data_json['image1']:
                raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON', '')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON',
                                   'Could not decode the request body. The JSON is incorrect.')