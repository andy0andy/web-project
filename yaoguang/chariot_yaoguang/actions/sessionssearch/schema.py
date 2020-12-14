# GENERATED BY CHARIOT SDK - DO NOT EDIT
import chariot
import json


class Component:
    DESCRIPTION = ""


class Input:
    WORKSPACEID = "workspaceid"
    SESSIONID = "sessionid"
    QUERY = "query"
    

class Output:
    STATUSCODE = "statuscode"
    SUCCESS = "success"
    WORKSPACEID = "workspaceid"
    SESSIONID = "sessionid"
    ENTRIES = "entries"
    

class SessionssearchInput(chariot.Input):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"query": {
			"type": "string",
			"title": "查询信息",
			"description": "",
			"order": 3
		},
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
		"sessionid",
		"query"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SessionssearchOutput(chariot.Output):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"entries": {
			"type": "array",
			"title": "查询得到的结果",
			"description": "",
			"order": 5,
			"items": {
				"type": "object"
			}
		},
		"sessionid": {
			"type": "string",
			"title": "会话id",
			"description": "",
			"order": 4
		},
		"statuscode": {
			"type": "integer",
			"title": "状态码",
			"description": "",
			"order": 1
		},
		"success": {
			"type": "string",
			"title": "结果",
			"description": "",
			"order": 2
		},
		"workspaceid": {
			"type": "string",
			"title": "项目id",
			"description": "",
			"order": 3
		}
	},
	"required": [
		"statuscode"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
