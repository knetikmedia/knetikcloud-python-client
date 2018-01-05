# PropertyDefinitionResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the property | [optional] 
**field_list** | [**PropertyFieldListResource**](PropertyFieldListResource.md) | A list of the fields on both the property definition and property of this type | [optional] 
**friendly_name** | **str** | The friendly front-facing name of the property | [optional] 
**name** | **str** | The name of the property | 
**option_label_path** | **str** | The JSON path to the option label | [optional] 
**option_value_path** | **str** | The JSON path to the option value | [optional] 
**options_url** | **str** | URL of service containing the property options (assumed JSON array) | [optional] 
**required** | **bool** | Whether the property is required | 
**type** | **str** | The type of the property. Used for polymorphic type recognition and thus must match an expected type with additional properties. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


