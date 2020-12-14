import chariot
from .schema import SocialengineeringhumantargetsdetailInput, SocialengineeringhumantargetsdetailOutput, Input, Output, Component
# Custom imports below


class Socialengineeringhumantargetsdetail(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='socialengineeringhumantargetsdetail',
                description=Component.DESCRIPTION,
                input=SocialengineeringhumantargetsdetailInput(),
                output=SocialengineeringhumantargetsdetailOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        id = params.get(Input.ID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/social_engineering/human_targets/{id}"

        try:
        
            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }
            
            if data:
                result.update({Output.DATA: data})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")