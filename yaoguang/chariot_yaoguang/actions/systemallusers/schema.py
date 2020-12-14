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
    ALLUSERS = "allusers"
    

class SystemallusersInput(chariot.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SystemallusersOutput(chariot.Output):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"allusers": {
			"type": "array",
			"title": "所有用户信息数组",
			"description": "",
			"order": 3,
			"items": {
				"type": "object"
			}
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
