# GENERATED BY CHARIOT SDK - DO NOT EDIT
import chariot
import json


class Component:
    DESCRIPTION = ""


class Input:
    ID = "id"
    

class Output:
    STATUSCODE = "statuscode"
    RESULT = "result"
    

class WorkspacesdeleteInput(chariot.Input):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"id": {
			"type": "string",
			"title": "项目ID",
			"description": "",
			"order": 1
		}
	},
	"required": [
		"id"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class WorkspacesdeleteOutput(chariot.Output):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"result": {
			"type": "string",
			"title": "Result",
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
