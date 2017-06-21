# DeviceResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | **str** | The authorization code for the device | [optional] 
**condition** | **str** | The current condition of the device (New, Defective, Reconditioned) | [optional] 
**created_date** | **int** | The date the device log was created | [optional] 
**data** | **dict(str, str)** | The key/value pairs for extended data | [optional] 
**description** | **str** | The description of the device | [optional] 
**device_type** | **str** | The type of the device | [optional] 
**id** | **int** | The unique ID for this device. Cannot be changed once created | 
**location** | **str** | The location of the device | [optional] 
**mac_address** | **str** | The MAC (media access control) address of the device | [optional] 
**make** | **str** | The make of the device | [optional] 
**model** | **str** | The model of the device | [optional] 
**name** | **str** | The name of the device | [optional] 
**os** | **str** | The OS (operating system) on the device | [optional] 
**serial** | **str** | The serial number of the device | [optional] 
**status** | **str** | The current status the device (Active, Pending Active, Inactive, Repair | [optional] 
**updated_date** | **int** | The date the device log was updated | [optional] 
**user** | [**SimpleUserResource**](SimpleUserResource.md) | The user that owns the device | [optional] 
**users** | [**list[SimpleUserResource]**](SimpleUserResource.md) | The users currently using the device | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


