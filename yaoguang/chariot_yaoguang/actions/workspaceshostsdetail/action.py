import chariot
from .schema import WorkspaceshostsdetailInput, WorkspaceshostsdetailOutput, Input, Output, Component
# Custom imports below


class Workspaceshostsdetail(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspaceshostsdetail',
                description=Component.DESCRIPTION,
                input=WorkspaceshostsdetailInput(),
                output=WorkspaceshostsdetailOutput())

    def run(self, params={}):
        # TODO: Implement run function
        

        workspacesid = params.get(Input.WORKSPACESID)
        id = params.get(Input.ID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{workspacesid}/hosts/{id}"

        try:
        
            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("success"):
                result.update({Output.SUCCESS: data['success']})
            
            if data.get("host"):
                result.update({Output.HOST: data['host']})
            
            if data.get("success"):
                result.update({Output.SERVICES: data['services']})

            



            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")
