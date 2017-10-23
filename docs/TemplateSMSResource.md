# TemplateSMSResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | The phone number to attribute the outgoing message to. Optional if the config text.out_number is set. | [optional] 
**recipients** | **list[int]** | A list of user ids to send the message to. | 
**template** | **str** | A mustache template | 
**template_vars** | **object** | A map of values to fill in the template | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


