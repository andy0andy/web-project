# GENERATED BY CHARIOT SDK - DO NOT EDIT
import chariot
import json


class Component:
    DESCRIPTION = ""


class Input:
    pass
    

class Output:
    STATUSCODE = "statuscode"
    STATUS = "status"
    LOGINUSER = "loginuser"
    

class SystemloginuserInput(chariot.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SystemloginuserOutput(chariot.Output):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"loginuser": {
			"type": "object",
			"title": "登陆用户信息",
			"description": "",
			"order": 3
		},
		"status": {
			"type": "string",
			"title": "Status",
			"description": "",
			"order": 2
		},
		"statuscode": {
			"type": "integer",
			"title": "状态码",
			"description": "",
			"order": 1
		}
	},
	"required": [
		"statuscode"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
