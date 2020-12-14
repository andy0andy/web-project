import chariot
from .schema import SocialengineeringtargetlistsdetailInput, SocialengineeringtargetlistsdetailOutput, Input, Output, Component
# Custom imports below


class Socialengineeringtargetlistsdetail(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='socialengineeringtargetlistsdetail',
                description=Component.DESCRIPTION,
                input=SocialengineeringtargetlistsdetailInput(),
                output=SocialengineeringtargetlistsdetailOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        id = params.get(Input.ID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/social_engineering/target_lists/{id}"

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