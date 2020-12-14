# GENERATED BY CHARIOT SDK - DO NOT EDIT
import chariot
import json


class Component:
    DESCRIPTION = ""


class Input:
    WORKSPACEID = "workspaceid"
    SESSIONID = "sessionid"
    

class Output:
    STATUSCODE = "statuscode"
    SUCCESS = "success"
    ERRORS = "errors"
    

class SessionsdestroyInput(chariot.Input):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"sessionid": {
			"type": "string",
			"title": "会话id",
			"description": "",
			"order": 2
		},
		"workspaceid": {
			"type": "string",
			"title": "项目id",
			"description": "",
			"order": 1
		}
	},
	"required": [
		"workspaceid",
		"sessionid"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SessionsdestroyOutput(chariot.Output):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"errors": {
			"type": "string",
			"title": "错误信息",
			"description": "",
			"order": 3
		},
		"statuscode": {
			"type": "integer",
			"title": "状态码",
			"description": "",
			"order": 1
		},
		"success": {
			"type": "string",
			"title": "是否成功",
			"description": "",
			"order": 2
		}
	},
	"required": [
		"statuscode"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
