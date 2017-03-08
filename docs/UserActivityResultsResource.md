# UserActivityResultsResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_rewards** | [**list[RewardCurrencyResource]**](RewardCurrencyResource.md) | Any currency rewarded to this user | [optional] 
**item_rewards** | [**list[RewardItemResource]**](RewardItemResource.md) | Any items rewarded to this user | [optional] 
**rank** | **int** | The position of the user in the leaderboard. Null means non-compete or disqualification | [optional] 
**score** | **int** | The raw score in this leaderboard. Null means non-compete or disqualification | [optional] 
**tags** | **list[str]** | Any tags for the metric. Each unique tag will translate into a unique leaderboard. Maximum 5 tags and 50 characters each | [optional] 
**ties** | **int** | The number of users tied at this rank, including this user. 1 means no tie | [optional] 
**user** | [**SimpleUserResource**](SimpleUserResource.md) | The player for this entry | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


