import chariot
from .schema import ValidatevulnsvalidateInput, ValidatevulnsvalidateOutput, Input, Output, Component
# Custom imports below


class Validatevulnsvalidate(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='validatevulnsvalidate',
                description=Component.DESCRIPTION,
                input=ValidatevulnsvalidateInput(),
                output=ValidatevulnsvalidateOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        report = params.get(Input.REPORT)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/validate_vulns/validate"

        try:
        
            yaoguang.addFiles(report)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("status"):
                result.update({Output.STATUS: data['status']})
            if data.get("ids"):
                result.update({Output.IDS: {"list": data['ids']}})
            if data.get("error"):
                result.update({Output.ERROR: data['error']})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")