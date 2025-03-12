Think that you are the Software engineer working in WSO2 Micro Integrator connector team. You have been assigned a task to revamp the connectors with the new improvements. 


1. Generate uischemas for the WSO2 connector operations if they dont already exist. Each connectors have operations which is written in synapse template XML files which are available inside src/main/resources. (We can skip scanning src/main/resources/config and src/main/resources/uischema). You have to generate uischema json files in src/main/resources/uischema.

Sample template

````
<template xmlns="http://ws.apache.org/ns/synapse" name="read">
    <parameter name="path" description="Path to the file or folder to read"/>
    <parameter name="filePattern" description="File pattern to match when choosing files to read"/>
    <parameter name="readMode" description="Read mode to use"/>
    <parameter name="startLineNum" description="Read file starting from this line"/>
    <parameter name="endLineNum" description="Read file up to this line"/>
    <parameter name="lineNum" description="Specific line number to read"/>
    <parameter name="contentType" description="MIME type of the message generated"/>
    <parameter name="encoding" description="Encoding of the message generated"/>
    <parameter name="includeResultTo" description="Specify where to place operation result."/>
    <parameter name="resultPropertyName" description="Name of property to add operation result."/>
    <parameter name="enableStreaming" description="Read the file in streaming manner. No message interpretation"/>
    <parameter name="enableLock" description="Whether to lock the file when reading"/>
    <parameter name="maxRetries" description="The maximum number of retry attempts in case of a failure."/>
    <parameter name="retryDelay" description="The delay between retry attempts in milliseconds."/>
    <sequence>
        <class name="org.wso2.carbon.connector.operations.ReadFile" />
    </sequence>
</template>
```

Sample UI schema

```
{
  "connectorName": "file",
  "operationName": "read",
  "title": "Read a file or files in a directory",
  "help": "Read a File",
  "elements": [
    {
      "type": "attributeGroup",
      "value": {
        "groupName": "General",
        "elements": [
          {
            "type": "attribute",
            "value": {
              "name": "configRef",
              "displayName": "File Connection",
              "inputType": "connection",
              "allowedConnectionTypes": [
                "LOCAL",
                "FTP",
                "FTPS",
                "SFTP",
                "SMB2"
              ],
              "defaultType": "connection.local",
              "defaultValue": "",
              "required": "true",
              "helpTip": "File connection to be used"
            }
          },
          {
            "type": "attributeGroup",
            "value": {
              "groupName": "Basic",
              "elements": [
                {
                  "type": "attribute",
                  "value": {
                    "name": "path",
                    "displayName": "File/Directory Path",
                    "inputType": "stringOrExpression",
                    "defaultValue": "",
                    "required": "true",
                    "helpTip": "Path to the file or folder to read."
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "filePattern",
                    "displayName": "File Pattern",
                    "inputType": "stringOrExpression",
                    "defaultValue": "",
                    "required": "false",
                    "helpTip": "File pattern to match when choosing files to read in a folder. Not applicable when reading a file."
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "readMode",
                    "displayName": "Read Mode",
                    "inputType": "comboOrExpression",
                    "comboValues": [
                      "Complete File",
                      "Starting From Line",
                      "Up To Line",
                      "Between Lines",
                      "Specific Line",
                      "Metadata Only"
                    ],
                    "defaultValue": "Complete File",
                    "required": "true",
                    "enableCondition": [
                      {
                        "enableStreaming": "false"
                      }
                    ],
                    "helpTip": "Read mode to use. "
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "startLineNum",
                    "displayName": "Start Line Number",
                    "inputType": "stringOrExpression",
                    "defaultValue": "0",
                    "required": "true",
                    "enableCondition": [
                      "OR",
                      {
                        "readMode": "Starting From Line"
                      },
                      {
                        "readMode": "Between Lines"
                      }
                    ],
                    "helpTip": "Read file starting from this line."
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "endLineNum",
                    "displayName": "End Line Number",
                    "inputType": "stringOrExpression",
                    "defaultValue": "0",
                    "required": "true",
                    "enableCondition": [
                      "OR",
                      {
                        "readMode": "Up To Line"
                      },
                      {
                        "readMode": "Between Lines"
                      }
                    ],
                    "helpTip": "Read file up to this line."
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "lineNum",
                    "displayName": "Specific Line Number",
                    "inputType": "stringOrExpression",
                    "defaultValue": "0",
                    "required": "true",
                    "enableCondition": [
                      {
                        "readMode": "Specific Line"
                      }
                    ],
                    "helpTip": "Specific line number to read"
                  }
                }
              ]
            }
          },
          {
            "type": "attributeGroup",
            "value": {
              "groupName": "Advance",
              "elements": [
                {
                  "type": "attribute",
                  "value": {
                    "name": "contentType",
                    "displayName": "MIME Type",
                    "inputType": "stringOrExpression",
                    "defaultValue": "",
                    "required": "false",
                    "enableCondition": [
                      "NOT",
                      {
                        "readMode": "Metadata Only"
                      }
                    ],
                    "helpTip": "MIME type of the message generated. If not provided it will try to interpret."
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "encoding",
                    "displayName": "Encoding",
                    "inputType": "stringOrExpression",
                    "defaultValue": "UTF-8",
                    "required": "false",
                    "enableCondition": [
                      "NOT",
                      {
                        "readMode": "Metadata Only"
                      }
                    ],
                    "helpTip": "Encoding of the message generated."
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "enableStreaming",
                    "displayName": "Enable Streaming",
                    "inputType": "booleanOrExpression",
                    "defaultValue": "false",
                    "required": "true",
                    "helpTip": "Read the file in streaming manner."
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "enableLock",
                    "displayName": "Enable Locking",
                    "inputType": "booleanOrExpression",
                    "defaultValue": "false",
                    "required": "true",
                    "helpTip": "Whether to lock the file when reading"
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "maxRetries",
                    "displayName": "Max Retries",
                    "inputType": "integerOrExpression",
                    "defaultValue": "0",
                    "required": "false",
                    "helpTip": "The maximum number of retries to be done in case of a failure."
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "retryDelay",
                    "displayName": "Retry Interval",
                    "inputType": "integerOrExpression",
                    "defaultValue": "0",
                    "required": "false",
                    "helpTip": "The time interval between retries in milliseconds."
                  }
                }
              ]
            }
          },
          {
            "type": "attributeGroup",
            "value": {
              "groupName": "Operation Result",
              "elements": [
                {
                  "type": "attribute",
                  "value": {
                    "name": "includeResultTo",
                    "displayName": "Add Result To",
                    "inputType": "comboOrExpression",
                    "comboValues": [
                      "Message Body",
                      "Message Property"
                    ],
                    "defaultValue": "Message Body",
                    "required": "true",
                    "helpTip": "Specify where to place operation result. Setting to a property will not change current payload at message body."
                  }
                },
                {
                  "type": "attribute",
                  "value": {
                    "name": "resultPropertyName",
                    "displayName": "Property Name",
                    "inputType": "stringOrExpression",
                    "defaultValue": "",
                    "required": "false",
                    "enableCondition": [
                      {
                        "includeResultTo": "Message Property"
                      }
                    ],
                    "helpTip": "Name of property to add operation result"
                  }
                }
              ]
            }
          }
        ]
      }
    }
  ]
}
```

2. The connection configurations are stored in src/main/resources/config. Normally the init.xml file will contain the connection configurations. We need to create a uischema for the connection depending on the parameters in the init.xml file. The uischema should be stored in src/main/resources/uischema. This connection type should be added to the allowedConnectionTypes in the uischema of the operation. After generating the uischema for the connection, you have to hide the init operation in the component.xml in which init.xml file is present.

```
<component name="config" type="synapse/template" >
    <subComponents> 
		<component name="init" >
			<file>init.xml</file>
			<description>Init operation</description>
			<hidden>true</hidden>
		</component>
    </subComponents>    
</component>
```

3. Inside each operations folder in src/main/resources, there should be a file called component.xml. This file should contain the following information.

````
<component name="userProfile" type="synapse/template">
    <subComponents>
        <component name="getUserProfile">
            <file>getUserProfile.xml</file>
            <description>Get the user profile</description>
        </component>
    </subComponents>
</component>
```

Each component inside the subComponent should be updated with the display Name of the operation. The display name should be something readable like "Get User Profile" instead of "getUserProfile".

````
<component name="userProfile" type="synapse/template">
    <subComponents>
        <component name="getUserProfile">
            <displayName>Get User Profile</displayName>
            <file>getUserProfile.xml</file>
            <description>Get the user profile</description>
        </component>
    </subComponents>
</component>
```


4. For each connector operation, an outputschema should be introduced to provide suggestions for expressions. The outputschema should reside in src/main/resources/outputschema. The output schema will sections such as payload, header and attributes. The attributes section should contain metadata about the operation. If it is a rest api based connector, then will have headers section as well. The payload will be stored in the payload section. To identify whether it is rest api based connector, you can check the template file. If the template file contains a call mediator with an endpoint, then it is a rest api based connector. If it contains a class mediator, then it is a non rest api based connector.

Sample output schema
```
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "title": "Output Schema for read Operation",
    "description": "Output schema for the read operation in the connector.",
    "properties": {
        "payload": {
            "type": "object",
            "description": "The main response payload from the read operation."
        },
        "attributes": {
            "type": "object",
            "description": "Metadata about the read operation.",
            "properties": {
                "FILE_LAST_MODIFIED_TIME": {
                    "type": "string",
                    "format": "date-time",
                    "description": "The last modified time of the file."
                },
                "FILE_IS_DIR": {
                    "type": "boolean",
                    "description": "Indicates whether the file is a directory."
                },
                "FILE_PATH": {
                    "type": "string",
                    "description": "The absolute path of the file."
                },
                "FILE_URL": {
                    "type": "string",
                    "format": "uri",
                    "description": "The URL associated with the file."
                },
                "FILE_NAME": {
                    "type": "string",
                    "description": "The name of the file including its extension."
                },
                "FILE_NAME_WITHOUT_EXTENSION": {
                    "type": "string",
                    "description": "The name of the file without its extension."
                },
                "FILE_SIZE": {
                    "type": "integer",
                    "description": "The size of the file in bytes.",
                    "minimum": 0
                }
            },
            "additionalProperties": false
        }
    },
    "required": [
        "payload",
        "attributes"
    ],
    "additionalProperties": false
}
```

Some connectors have older outputschema files. You can refer to them and generate the new outputschema files. The older schema files are available in src/main/resources/<operation_section>/output_schema/*.


If it is a rest api based connector, it will only return the statusCode inside attributes.


5. There is a new response model introduced. The output of the connector will be stored in the variable by default. The output will contain the above sections such as payload, headers and attributes based on relevance. There is also another option to override the payload in the message context. If this is selected then the output will be stored in the message context.

To support this new response model, you have to update the template files in src/main/resources with two new parameters. 

Sample template

```
<template xmlns="http://ws.apache.org/ns/synapse" name="delete">
    <parameter name="path" description="Path to file or directory to delete"/>
    <parameter name="matchingPattern" description="Pattern matching to use when deleting files"/>
    <parameter name="maxRetries" description="The maximum number of retry attempts in case of a failure."/>
    <parameter name="retryDelay" description="The delay between retry attempts in milliseconds."/>
    <sequence>
        <class name="org.wso2.carbon.connector.operations.DeleteFileOrFolder"/>
    </sequence>
</template>
```

New template
```
<template xmlns="http://ws.apache.org/ns/synapse" name="delete">
    <parameter name="path" description="Path to file or directory to delete"/>
    <parameter name="matchingPattern" description="Pattern matching to use when deleting files"/>
    <parameter name="maxRetries" description="The maximum number of retry attempts in case of a failure."/>
    <parameter name="retryDelay" description="The delay between retry attempts in milliseconds."/>
    <parameter name="responseVariable" description="The name of the variable to which the output should be stored."/>
        <parameter name="overwriteBody" description="Replace the Message Body in Message Context with the response of the operation."/>
    <sequence>
        <class name="org.wso2.carbon.connector.operations.DeleteFileOrFolder"/>
    </sequence>
</template>
```

Also the relevant ui schema should be updated to support the new parameters. This will be at the end of the ui schema file.

Eg:

```
...
                      {
                        "type":"attributeGroup",
                        "value":{
                            "groupName": "Output",
                            "elements":[
                                {
                                    "type":"attribute",
                                    "value":{
                                        "name": "responseVariable",
                                        "displayName": "Output Variable Name",
                                        "inputType": "string",
                                        "deriveResponseVariable" : true,
                                        "required": "true",
                                        "helpTip": "Name of the variable to which the output of the operation should be assigned"
                                    }
                                },
                                {
                                    "type":"attribute",
                                    "value":{
                                        "name": "overwriteBody",
                                        "displayName": "Replace Message Body",
                                        "inputType": "checkbox",
                                        "defaultValue": "false",
                                        "helpTip": "Replace the Message Body in Message Context with the output of the operation (This will remove the payload from the above variable).",
                                        "required": "false"
                                    }
                                }
                            ]
                        }
                      }
...
```

6. To divide the operations into sections, you have to update the component.xml file in src/main/resources. The component.xml file should contain the following information.

Example, if the folder name inside src/main/resources is tables, then the templates files should contain the following information.

```
<template name="deleteRecordById" xmlns="http://ws.apache.org/ns/synapse" displayName="tablles">
    <parameter name="sysId" description="System Id which is different for every raw."/>
    <parameter name="tableName" description="Name of the Table you ar going to get data."/>
    <sequence>
        <property name="uri.var.sysId" expression="$func:sysId"/>
        <property name="uri.var.tableName" expression="$func:tableName"/>
        <property name="messageType" value="application/json" scope="axis2"/>
        <call>
            <endpoint>
                <http method="DELETE"
                      uri-template="{uri.var.serviceNowInstanceURL}/api/now/table/{+uri.var.tableName}/{uri.var.sysId}"/>
            </endpoint>
        </call>
    </sequence>
</template>
```

7. To publish the connector to the WSO2 store, you have to create .connector-store/meta.json file as follows if it does not exist. Update the previous one if it exists. In the meta.json, the name of each operations should be equal to the displayName field which we gave inside the component.xml files. No need to update the description of each operation.

```
{
    "name": "Email",
    "owner": "WSO2",
    "product": "MI",
    "category": "Communication",
    "documentationUrl": "https://mi.docs.wso2.com/en/latest/reference/connectors/email-connector/email-connector-overview/",
    "mavenGroupId": "org.wso2.integration.connector",
    "mavenArtifactId": "mi-connector-email",
    "description": "The Email Connector allows you to list, send emails and perform other actions such as mark email as read, mark email as deleted, delete email and expunge folder on different mailboxes using protocols IMAP, POP3 and SMTP.",
    "status": "Active",
    "rank": 6,
    "type": "Connector",
    "labels": [
        "email",
        "communication"
    ],
    "releases": [
        {
            "tagName": "v1.1.4",
            "products": [
                "MI 4.4.0",
                "MI 4.3.0",
                "MI 4.2.0",
                "MI 4.1.0",
                "MI 4.0.0"
            ],
            "operations": [
                {
                    "name": "init",
                    "description": "Init operation",
                    "isHidden": true
                },
                {
                    "name": "list",
                    "description": "List all the emails.",
                    "isHidden": false
                },
                {
                    "name": "expungeFolder",
                    "description": "Delete all the messages scheduled for deletion with the DELETED flag set from the mailbox.",
                    "isHidden": false
                },
                {
                    "name": "markAsDeleted",
                    "description": "Mark an incoming email as DELETED. Not physically deleted, only a state change.",
                    "isHidden": false
                },
                {
                    "name": "markAsRead",
                    "description": "Marks a single email as READ changing its state in the specified mailbox folder.",
                    "isHidden": false
                },
                {
                    "name": "send",
                    "description": "Sends an email message.",
                    "isHidden": false
                },
                {
                    "name": "delete",
                    "description": "Deletes an email.",
                    "isHidden": false
                },
                {
                    "name": "getEmailBody",
                    "description": "Retrieves email body by index.",
                    "isHidden": false
                },
                {
                    "name": "getEmailAttachment",
                    "description": "Retrieves email attachment by index.",
                    "isHidden": false
                }
            ],
            "connections": [
                {
                    "name": "POP3",
                    "description": "Connection for retrieving emails via POP3."
                },
                {
                    "name": "POP3S",
                    "description": "Secure connection for retrieving emails via POP3S."
                },
                {
                    "name": "IMAP",
                    "description": "Connection for accessing emails via IMAP."
                },
                {
                    "name": "IMAPS",
                    "description": "Secure connection for accessing emails via IMAPS."
                },
                {
                    "name": "SMTP",
                    "description": "Connection for sending emails via SMTP."
                },
                {
                    "name": "SMTPS",
                    "description": "Secure connection for sending emails via SMTPS."
                }
            ],
            "isHidden": false
        }
    ]
}

```
