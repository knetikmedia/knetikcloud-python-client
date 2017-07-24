# UserBaseResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** | The url of the user&#39;s avatar image | [optional] 
**display_name** | **str** | The chosen display name of the user, defaults to username if not present | [optional] 
**email** | **str** | The user&#39;s email address (private). May be required and/or unique depending on system configuration (both on by default). Must match standard email requirements if provided (RFC 2822) | 
**fullname** | **str** | The user&#39;s full name (private) | [optional] 
**id** | **int** | The id of the user | [optional] 
**last_activity** | **int** | The date the user last interacted with the API (private) | [optional] 
**last_updated** | **int** | The date the user&#39;s info was last updated as a unix timestamp | [optional] 
**member_since** | **int** | The user&#39;s date of registration as a unix timestamp | [optional] 
**username** | **str** | The login username for the user (private). May be set to match email if system does not require usernames separately. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


