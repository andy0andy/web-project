from yaoguang.chariot_yaoguang.actions.sessionssession.schema import SessionssessionOutput
import chariot
from .schema import SessionssearchInput, SessionssearchOutput, Input, Output, Component
# Custom imports below


class Sessionssearch(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sessionssearch',
                description=Component.DESCRIPTION,
                input=SessionssearchInput(),
                output=SessionssearchOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        sessionid = params.get(Input.SESSIONID)
        query = params.get(Input.QUERY)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/sessions/search"

        try:
            
            if workspaceid:
                yaoguang.addBody("workspace_id", workspaceid)
            if sessionid:
                yaoguang.addBody("session_id", sessionid)
            if query:
                yaoguang.addBody("query", query)


            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("success"):
                result.update({Output.SESSION: data['success']})
            if data.get("workspace_id"):
                result.update({Output.WORKSPACEID: data["workspace_id"]})
            if data.get("session_id"):
                result.update({Output.SESSIONID: data["session_id"]})
            if data.get("entries"):
                result.update({Output.ENTRIES: data["entries"]})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")