import chariot
from .schema import PayloaddetailInput, PayloaddetailOutput, Input, Output, Component
# Custom imports below


class Payloaddetail(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='payloaddetail',
                description=Component.DESCRIPTION,
                input=PayloaddetailInput(),
                output=PayloaddetailOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        payloadid = params.get(Input.PAYLOADID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/payload/{payloadid}"

        try:

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("status"):
                result.update({Output.STATUS: data['status']})
            if data.get("path"):
                result.update({Output.PATH: data['path']})
            if data.get("content"):
                result.update({Output.CONTENT: data['content']})
            if data.get("message"):
                result.update({Output.MESSAGE: data['message']})

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")