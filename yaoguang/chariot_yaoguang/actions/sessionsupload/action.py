import chariot
from .schema import SessionsuploadInput, SessionsuploadOutput, Input, Output, Component
# Custom imports below


class Sessionsupload(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sessionsupload',
                description=Component.DESCRIPTION,
                input=SessionsuploadInput(),
                output=SessionsuploadOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        sessionid = params.get(Input.SESSIONID)
        path = params.get(Input.PATH)
        file = params.get(Input.FILE)
        name = params.get(Input.NAME)
        execute = params.get(Input.EXECUTE)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/sessions/upload"

        try:

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("session_id", sessionid)
            yaoguang.addBody("path", path)
            yaoguang.addField(file)
            yaoguang.addBody("execute", execute)
            yaoguang.addBody("namet", name)
            
            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("data"):
                result.update({Output.DATA: data})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")