# GroupMemberResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name (private). Must match the names and types defined in the template for this type, or be an extra not from the template | [optional] 
**avatar_url** | **str** | The url of the user&#39;s avatar image | [optional] 
**display_name** | **str** | The public username of the user | [optional] 
**id** | **int** | The id of the user | 
**order** | **str** | The position of the member in the group if applicable. Read notes for details | [optional] 
**status** | **str** | The member&#39;s access level. Default: member | [optional] 
**template** | **str** | A template this member additional properties are validated against (private). May be null and no validation of properties will be done | [optional] 
**username** | **str** | The username of the user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


