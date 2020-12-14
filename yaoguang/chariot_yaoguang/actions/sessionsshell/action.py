import chariot
from .schema import SessionsshellInput, SessionsshellOutput, Input, Output, Component
# Custom imports below


class Sessionsshell(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sessionsshell',
                description=Component.DESCRIPTION,
                input=SessionsshellInput(),
                output=SessionsshellOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        sessionid = params.get(Input.SESSIONID)

        special = params.get(Input.SPECIAL)
        cmd = params.get(Input.CMD)
        read = params.get(Input.READ)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/sessions/shell"

        try:
            

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("session_id", sessionid)
            if special:
                yaoguang.addBody("special", special)
            if cmd:
                yaoguang.addBody("cmd", cmd)
            if read:
                yaoguang.addBody("read", read)


            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("success"):
                result.update({Output.SUCCESS: data['success']})
            if data.get("event"):
                result.update({Output.EVENT: data['event']})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")