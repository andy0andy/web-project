import chariot
from .schema import LootsInput, LootsOutput, Input, Output, Component
# Custom imports below


class Loots(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='loots',
                description=Component.DESCRIPTION,
                input=LootsInput(),
                output=LootsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        hostid = params.get(Input.HOSTID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/loots"

        try:
            
            if workspaceid:
                yaoguang.addBody("workspace_id", workspaceid)
            if hostid:
                yaoguang.addBody("host_id", hostid)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("status"):
                result.update({Output.STATUS: data['status']})
            if data.get("loots"):
                result.update({Output.LOOTS: data['loots']})

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")