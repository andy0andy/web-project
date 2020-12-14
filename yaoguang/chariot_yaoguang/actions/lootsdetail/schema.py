# GENERATED BY CHARIOT SDK - DO NOT EDIT
import chariot
import json


class Component:
    DESCRIPTION = ""


class Input:
    LOOTID = "lootid"
    

class Output:
    STATUSCODE = "statuscode"
    STATUS = "status"
    PATH = "path"
    CONTENT = "content"
    CONTENTTYPE = "contenttype"
    MESSAGE = "message"
    

class LootsdetailInput(chariot.Input):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"lootid": {
			"type": "string",
			"title": "项目id",
			"description": "",
			"order": 1
		}
	},
	"required": [
		"lootid"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class LootsdetailOutput(chariot.Output):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"content": {
			"type": "string",
			"title": "文件内容",
			"description": "",
			"order": 4
		},
		"contenttype": {
			"type": "string",
			"title": "文件类型",
			"description": "",
			"order": 5
		},
		"message": {
			"type": "string",
			"title": "返回信息",
			"description": "",
			"order": 6
		},
		"path": {
			"type": "string",
			"title": "文件路径",
			"description": "",
			"order": 3
		},
		"status": {
			"type": "string",
			"title": "结果",
			"description": "",
			"order": 2,
			"enum": [
				"error",
				"success"
			]
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
