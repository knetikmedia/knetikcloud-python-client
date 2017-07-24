# VideoPropertyDefinitionResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_list** | [**PropertyFieldListResource**](PropertyFieldListResource.md) | A list of the fields on both the property definition and property of this type | [optional] 
**name** | **str** | The name of the property | 
**required** | **bool** | Whether the property is required | 
**type** | **str** | The type of the property. Used for polymorphic type recognition and thus must match an expected type with additional properties. | 
**file_type** | **str** | If provided, a file type that teh property must match | [optional] 
**max_height** | **int** | If provided, the maximum height of the video | [optional] 
**max_length** | **int** | If provided, the maximum length of the video | [optional] 
**max_width** | **int** | If provided, the maximum width of the video | [optional] 
**min_height** | **int** | If provided, the minimum height of the video | [optional] 
**min_length** | **int** | If provided, the minimum length of the video | [optional] 
**min_width** | **int** | If provided, the minimum width of the video | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

