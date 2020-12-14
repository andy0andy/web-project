# GENERATED BY CHARIOT SDK - DO NOT EDIT
import chariot
import json


class Component:
    DESCRIPTION = ""


class Input:
    NAME = "name"
    DESCRIPTION = "description"
    BOUNDARY = "boundary"
    LIMIT_TO_NETWORK = "limit_to_network"
    OWNER_ID = "owner_id"
    

class Output:
    STATUSCODE = "statuscode"
    RESULT = "result"
    WORKSPACE = "workspace"
    PATH = "path"
    

class WorkspacescreateInput(chariot.Input):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"boundary": {
			"type": "string",
			"title": "项目网络区间",
			"description": "",
			"order": 3
		},
		"description": {
			"type": "string",
			"title": "项目描述",
			"description": "",
			"order": 2
		},
		"limit_to_network": {
			"type": "string",
			"title": "是否限定网络范围",
			"description": "",
			"order": 4,
			"enum": [
				"0",
				"1"
			]
		},
		"name": {
			"type": "string",
			"title": "项目名称",
			"description": "",
			"order": 1
		},
		"owner_id": {
			"type": "string",
			"title": "项目所属用户ID",
			"description": "创建项目时必填，更新时不填",
			"order": 5
		}
	},
	"required": [
		"name",
		"description",
		"boundary",
		"limit_to_network",
		"owner_id"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class WorkspacescreateOutput(chariot.Output):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"path": {
			"type": "string",
			"title": "Path",
			"description": "",
			"order": 4
		},
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
		},
		"workspace": {
			"type": "object",
			"title": "Workspace",
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
