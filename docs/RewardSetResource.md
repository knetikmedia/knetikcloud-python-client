# RewardSetResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **int** | The date/time this resource was created in seconds since unix epoch | [optional] 
**currency_rewards** | [**list[RewardCurrencyResource]**](RewardCurrencyResource.md) | The currency to give as rewards | [optional] 
**id** | **int** | The assigned unique ID for this reward set | [optional] 
**item_rewards** | [**list[RewardItemResource]**](RewardItemResource.md) | The items to give as rewards | [optional] 
**long_description** | **str** | A longer describe the reward set, usually included in details | [optional] 
**max_placing** | **int** | The maximum placing that will receive a reward | [optional] 
**name** | **str** | The user friendly name for this reward set | 
**short_description** | **str** | A short paragraph to describe the reward set, usually included in listings.  Max 255 characters | [optional] 
**unique_key** | **str** | A provided unique key for this reward set | [optional] 
**updated_date** | **int** | The date/time this resource was last updated in seconds since unix epoch | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


