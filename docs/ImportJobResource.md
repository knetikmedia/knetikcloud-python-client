# ImportJobResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The id of the category to assign all questions in the import to | 
**created_date** | **int** | The date the job was created in seconds since unix epoc | [optional] 
**id** | **int** | The id of the job | [optional] 
**name** | **str** | A name for this import for later reference | 
**output** | [**list[ImportJobOutputResource]**](ImportJobOutputResource.md) | Error information from validation | [optional] 
**record_count** | **int** | The number of questions form the CSV file. Filled in after validation | [optional] 
**status** | **str** | The status of the job | [optional] 
**updated_date** | **int** | The date the job was last updated in seconds since unix epoc | [optional] 
**url** | **str** | The url of a CSV file to pull trivia questions from. Cannot be changed after initial POST | 
**vendor** | **str** | The vendor who supplied this set of questions | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


