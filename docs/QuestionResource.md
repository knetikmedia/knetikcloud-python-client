# QuestionResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type | [optional] 
**answers** | [**list[AnswerResource]**](AnswerResource.md) | The list of available answers | [optional] 
**category** | [**NestedCategory**](NestedCategory.md) | The category for the question | 
**created_date** | **int** | The date/time this resource was created in seconds since unix epoch | [optional] 
**difficulty** | **int** | The difficulty of the question | 
**id** | **str** | The unique ID for that resource | [optional] 
**import_id** | **int** | The id of the import job that created the question, or null if not from an import | [optional] 
**published_date** | **int** | When the question becomes available, null for never, in seconds since epoch | [optional] 
**question** | [**ModelProperty**](ModelProperty.md) | The question. Different &#39;type&#39; values indicate different structures as the question may be test, image, etc. See information on additional properties for the list and their structures | 
**source1** | **str** | The first source of the question | [optional] 
**source2** | **str** | The second source of the question | [optional] 
**tags** | **list[str]** | The list of tags | [optional] 
**template** | **str** | A question template this question is validated against (private). May be null and no validation of additional_properties will be done | [optional] 
**updated_date** | **int** | The date/time this resource was last updated in seconds since unix epoch | [optional] 
**vendor** | **str** | The supplier of the question | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


