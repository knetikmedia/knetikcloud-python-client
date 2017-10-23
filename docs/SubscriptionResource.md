# SubscriptionResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | The additional properties for the subscription | [optional] 
**availability** | **str** | Who can purchase this subscription | [optional] 
**behaviors** | [**list[Behavior]**](Behavior.md) | The behaviors linked to the item, describing various options and interactions. May not be included in item lists | [optional] 
**category** | **str** | The category of the subscription | [optional] 
**consolidation_day_of_month** | **int** | The day of the month 1..31 this subscription will renew | [optional] 
**created_date** | **int** | The date the item was created, unix timestamp in seconds | [optional] 
**displayable** | **bool** | Whether or not the item is currently visible to users. Does not block purchase; Use store_start or store_end to block purchase.  Default &#x3D; true | [optional] 
**geo_country_list** | **list[str]** | The geo country list for the subscription | [optional] 
**geo_policy_type** | **str** | The geo policy type for the subscription | [optional] 
**id** | **int** | The id of the item | [optional] 
**long_description** | **str** | A long description of the subscription | [optional] 
**name** | **str** | The name of the item | 
**plans** | [**list[SubscriptionPlanResource]**](SubscriptionPlanResource.md) | The billing options for this subscription | [optional] 
**short_description** | **str** | A short description of the subscription.  Max 255 characters | [optional] 
**sort** | **int** | A number to use in sorting items.  Default 500 | [optional] 
**store_end** | **int** | Used to schedule removal from store.  Null means the subscription will never be removed | [optional] 
**store_start** | **int** | Used to schedule appearance in store.  Null means the subscription will appear now | [optional] 
**tags** | **list[str]** | The tags for the subscription | [optional] 
**template** | **str** | The template being used | [optional] 
**unique_key** | **str** | The unique key of the subscription | [optional] 
**updated_date** | **int** | The date the item was last updated | [optional] 
**vendor_id** | **int** | The id of the vendor | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


