import chariot
from .schema import SessionsvncInput, SessionsvncOutput, Input, Output, Component
# Custom imports below


class Sessionsvnc(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sessionsvnc',
                description=Component.DESCRIPTION,
                input=SessionsvncInput(),
                output=SessionsvncOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        sessionid = params.get(Input.SESSIONID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/sessions/vnc"

        try:

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("session_id", sessionid)


            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("data"):
                result.update({Output.DATA: data})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")