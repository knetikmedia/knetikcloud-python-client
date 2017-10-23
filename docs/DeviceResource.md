# DeviceResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name.  Must match the names and types defined in the template if one is specified | [optional] 
**created_date** | **int** | The date the device log was created | [optional] 
**description** | **str** | The description of the device | [optional] 
**device_type** | **str** | The type of device. Use mobile to specifically register mobile devices. This particular type will be used to send and receive notifications | [optional] 
**id** | **str** | The unique ID for this device | [optional] 
**location** | **str** | The physical location of the device, coordinates or named place (office, living room, etc) | [optional] 
**mac_address** | **str** | The MAC (media access control) address of the device | [optional] 
**make** | **str** | The make of the device | [optional] 
**model** | **str** | The model of the device | [optional] 
**name** | **str** | The name of the device | [optional] 
**os** | **str** | The OS (operating system) on the device | [optional] 
**owner** | [**SimpleUserResource**](SimpleUserResource.md) | The user that owns the device | [optional] 
**serial** | **str** | The serial number of the device | [optional] 
**tags** | **list[str]** | Random tags to facilitate search | [optional] 
**template** | **str** | Use to describe and validate custom properties (custom schema). May be null and no validation of additional_properties will be done | [optional] 
**updated_date** | **int** | The date the device log was updated | [optional] 
**users** | [**list[SimpleUserResource]**](SimpleUserResource.md) | The users currently using the device | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


