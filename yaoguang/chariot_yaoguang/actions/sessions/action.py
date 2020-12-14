import chariot
from .schema import SessionsInput, SessionsOutput, Input, Output, Component
# Custom imports below


class Sessions(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='sessions',
                description=Component.DESCRIPTION,
                input=SessionsInput(),
                output=SessionsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v3/sessions"

        try:

            yaoguang.addBody("workspace_id", workspaceid)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data:
                result.update({Output.DATA: data})
        



            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")