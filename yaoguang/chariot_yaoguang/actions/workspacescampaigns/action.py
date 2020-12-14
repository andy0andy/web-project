import chariot
from .schema import WorkspacescampaignsInput, WorkspacescampaignsOutput, Input, Output, Component
# Custom imports below


class Workspacescampaigns(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspacescampaigns',
                description=Component.DESCRIPTION,
                input=WorkspacescampaignsInput(),
                output=WorkspacescampaignsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/workspaces/{workspaceid}/campaigns"

        try:
        
            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }
            
            if data:
                result.update({Output.DATA: data})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")