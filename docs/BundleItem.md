# BundleItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type, or be an extra not from the template | [optional] 
**behaviors** | [**list[Behavior]**](Behavior.md) | The behaviors linked to the item, describing various options and interactions. May not be included in item lists | [optional] 
**category** | **str** | A category for filtering items | [optional] 
**created_date** | **int** | The date the item was created, unix timestamp in seconds | [optional] 
**id** | **int** | The id of the item | [optional] 
**long_description** | **str** | A long description of the item | [optional] 
**name** | **str** | The name of the item | 
**short_description** | **str** | A short description of the item, max 255 chars | [optional] 
**sort** | **int** | A number to use in sorting items.  Default 500 | [optional] 
**tags** | **list[str]** | List of tags used for filtering items | [optional] 
**template** | **str** | An item template this item is validated against.  May be null and no validation of additional_properties will be done.  Default &#x3D; null | [optional] 
**type_hint** | **str** | The type of the item | 
**unique_key** | **str** | The unique key for the item | [optional] 
**updated_date** | **int** | The date the item was last updated, unix timestamp in seconds | [optional] 
**displayable** | **bool** | Whether or not the item is currently displayable.  Default &#x3D; true | [optional] 
**geo_country_list** | **list[str]** | A list of country ID to include in the blacklist/whitelist geo policy | [optional] 
**geo_policy_type** | **str** | Whether to use the geo_country_list as a black list or white list for item geographical availability | [optional] 
**shipping_tier** | **int** | Provides the abstract shipping needs if this item is physical and can be shipped.  A value of zero means no shipping needed.  Default &#x3D; 0 | [optional] 
**skus** | [**list[Sku]**](Sku.md) | The skus for the item. Each defines a unique configuration for the item to be purchased (Large-Blue, Small-Green, etc). These are what is ultimately selected in the store and added to the cart | 
**store_end** | **int** | The date the item will leave the store, unix timestamp in seconds.  If set to null, item will never leave the store | [optional] 
**store_start** | **int** | The date the item will appear in the store, unix timestamp in seconds.  If set to null, item will appear in store immediately | [optional] 
**vendor_id** | **int** | The vendor who provides the item | 
**bundled_skus** | [**list[BundledSku]**](BundledSku.md) | The skus of items to be included in this bundle, and how they influence the bundle total price.  Must have at least one SKU | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


