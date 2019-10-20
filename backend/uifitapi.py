from .measurements import Measurements
import falcon
import json
from PIL import Image
from io import BytesIO
from io import StringIO
import base64

class FitResource(object):

    def on_post(self, req, resp):
        try:
            raw_json = req.stream.read().decode()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

        try:
            data_json = json.loads(raw_json, encoding='utf-8')
            #if 'image1' not in data_json and 'image2' not in data_json and 'image3' not in data_json and \
            #        'height' not in data_json and 'style' not in data_json and 'size' not in data_json and 'brand' not in data_json:
            #    raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON',
            #                       'Does not have the right attributes')
            if not data_json['image1']:
                raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON', '')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400, 'Invalid JSON',
                                   'Could not decode the request body. The JSON is incorrect.')
        
        #cvimg = FitResource.readb64(json.dumps(data_json['image1']))
        encoded_string = ""
        with open("tucked1.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        #image_data = str(json.dumps(data_json['image1']))
        #im = Image.open(BytesIO(base64.b64decode(image_data)))

        resp.body = json.dumps({"ok": str(encoded_string)})
        resp.status = falcon.HTTP_200

    def readb64(base64_string):
        sbuf = BytesIO()
        sbuf.write(base64.b64decode(base64_string))
        pimg = Image.open(sbuf)
        return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)
