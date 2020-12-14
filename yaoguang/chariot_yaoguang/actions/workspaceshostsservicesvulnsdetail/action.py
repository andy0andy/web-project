import chariot
from .schema import WorkspaceshostsservicesvulnsdetailInput, WorkspaceshostsservicesvulnsdetailOutput, Input, Output, Component
# Custom imports below


class Workspaceshostsservicesvulnsdetail(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspaceshostsservicesvulnsdetail',
                description=Component.DESCRIPTION,
                input=WorkspaceshostsservicesvulnsdetailInput(),
                output=WorkspaceshostsservicesvulnsdetailOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspacesid = params.get(Input.WORKSPACESID)
        hostid = params.get(Input.HOSTID) 
        serviceid = params.get(Input.SERVICEID)
        id = params.get(Input.ID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{workspacesid}/hosts/{hostid}/services/{serviceid}/vulns/{id}"

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