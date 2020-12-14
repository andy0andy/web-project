import chariot
from .schema import CredsInput, CredsOutput, Input, Output, Component
# Custom imports below


class Creds(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='creds',
                description=Component.DESCRIPTION,
                input=CredsInput(),
                output=CredsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/creds"

        try:
            
            yaoguang.addBody("workspace_id", workspaceid)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("status"):
                result.update({Output.STATUS: data['status']})
            if data.get("creds"):
                result.update({Output.CREDS: data['creds']})

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")