# WebhookConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **String** | A string defining the URL to which the payloads will be delivered. | 
**contentType** | [**ContentTypeEnum**](#ContentTypeEnum) | A string defining the media type used to serialize the payloads. | 
**secret** | **String** | An optional string that&#x27;s passed with the HTTP requests body. |  [optional]

<a name="ContentTypeEnum"></a>
## Enum: ContentTypeEnum
Name | Value
---- | -----
JSON | &quot;json&quot;
FORM | &quot;form&quot;
