import chariot
from .schema import SyncconfigstatusInput, SyncconfigstatusOutput, Input, Output, Component
# Custom imports below


class Syncconfigstatus(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='syncconfigstatus',
                description=Component.DESCRIPTION,
                input=SyncconfigstatusInput(),
                output=SyncconfigstatusOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        randomstring = params.get(Input.RANDOMSTRING)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/sync_config/status"

        try:
            
            yaoguang.addBody('random_string', randomstring)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("status"):
                result.update({Output.STATUS: data['status']})
            if data.get("error"):
                result.update({Output.ERROR: data['error']})
            if data.get("random_string"):
                result.update({Output.RANDOMSTRING: data['random_string']})

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")