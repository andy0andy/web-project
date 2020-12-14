import chariot
from .schema import SessionsdestroyInput, SessionsdestroyOutput, Input, Output, Component
# Custom imports below


class Sessionsdestroy(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sessionsdestroy',
                description=Component.DESCRIPTION,
                input=SessionsdestroyInput(),
                output=SessionsdestroyOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
         
        workspaceid = params.get(Input.WORKSPACEID)
        sessionid = params.get(Input.SESSIONID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v3/sessions/destroy"

        try:

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("session_id", sessionid)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("success"):
                result.update({Output.SUCCESS: data['success']})
            if data.get("error"):
                result.update({Output.ERROR: data['error']})
        



            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")