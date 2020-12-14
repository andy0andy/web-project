import chariot
from .schema import SessionshistoryInput, SessionshistoryOutput, Input, Output, Component
# Custom imports below


class Sessionshistory(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sessionshistory',
                description=Component.DESCRIPTION,
                input=SessionshistoryInput(),
                output=SessionshistoryOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        sessionid = params.get(Input.SESSIONID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v3/sessions/history"

        try:

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("session_id", sessionid)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data:
                result.update({Output.DATA: data})
        



            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")