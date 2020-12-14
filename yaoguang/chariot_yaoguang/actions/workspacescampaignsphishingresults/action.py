import chariot
from .schema import WorkspacescampaignsphishingresultsInput, WorkspacescampaignsphishingresultsOutput, Input, Output, Component
# Custom imports below


class Workspacescampaignsphishingresults(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspacescampaignsphishingresults',
                description=Component.DESCRIPTION,
                input=WorkspacescampaignsphishingresultsInput(),
                output=WorkspacescampaignsphishingresultsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        campaignid = params.get(Input.CAMPAIGNID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/workspaces/{workspaceid}/campaigns/{campaignid}/phishing_results"

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