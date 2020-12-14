import chariot
from .schema import SessionsdeleteInput, SessionsdeleteOutput, Input, Output, Component
# Custom imports below


class Sessionsdelete(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sessionsdelete',
                description=Component.DESCRIPTION,
                input=SessionsdeleteInput(),
                output=SessionsdeleteOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        sessionid = params.get(Input.SESSIONID)
        path = params.get(Input.PATH)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/sessions/delete"

        try:
            
            if workspaceid:
                yaoguang.addBody("workspace_id", workspaceid)
            if sessionid:
                yaoguang.addBody("session_id", sessionid)
            if path:
                yaoguang.addBody("path", path)


            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("data"):
                result.update({Output.DATA: data})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")