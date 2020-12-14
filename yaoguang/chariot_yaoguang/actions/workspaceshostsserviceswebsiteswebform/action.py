import chariot
from .schema import WorkspaceshostsserviceswebsiteswebformInput, WorkspaceshostsserviceswebsiteswebformOutput, Input, Output, Component
# Custom imports below


class Workspaceshostsserviceswebsiteswebform(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspaceshostsserviceswebsiteswebform',
                description=Component.DESCRIPTION,
                input=WorkspaceshostsserviceswebsiteswebformInput(),
                output=WorkspaceshostsserviceswebsiteswebformOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspacesid = params.get(Input.WORKSPACESID)
        hostid = params.get(Input.HOSTID)
        serviceid = params.get(Input.SERVICEID)
        websitesid = params.get(Input.WEBSITESID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{workspacesid}/hosts/{hostid}/services/{serviceid}/web_sites/{websitesid}/web_forms"

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
