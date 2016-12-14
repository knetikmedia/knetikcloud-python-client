# CouponItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type, or be an extra not from the template | [optional] 
**behaviors** | [**list[Behavior]**](Behavior.md) | The behaviors linked to the item, describing various options and interactions. May not be included in item lists | [optional] 
**category** | **str** | A category for filtering items | [optional] 
**coupon_type_hint** | **str** | The type of coupon | 
**created_date** | **int** | The date the item was created, unix timestamp in seconds | [optional] 
**discount_max** | **float** | The amount this coupon is maxed out at.  Applies if coupon_type_hint is coupon_cart | [optional] 
**discount_min_cart_value** | **float** | The minimium amount needed in the cart for the coupon to apply.  Applies if coupon_type_hint is coupon_cart | [optional] 
**discount_type** | **str** | The type of coupon discount | 
**discount_value** | **float** | The amount the coupon will discount the item | 
**displayable** | **bool** | Whether or not the item is currently displayable.  Default &#x3D; true | [optional] 
**exclusive** | **bool** | Whether this coupon is exclusive or not.  Default &#x3D; false | [optional] 
**geo_country_list** | **list[str]** | A list of country ID to include in the blacklist/whitelist geo policy | [optional] 
**geo_policy_type** | **str** | Whether to use the geo_country_list as a black list or white list for item geographical availability | [optional] 
**id** | **int** | The id of the item | [optional] 
**item_id** | **int** | The id of the item the coupon is applied to.  Applies if coupon_type_hint is coupon_single_item or coupon_voucher | [optional] 
**long_description** | **str** | A long description of the item | [optional] 
**max_quantity** | **int** | The maximum quantity of items the coupon can apply to, null if no limit and minimum 1 otherwise.  Applies if coupon_type_hint is coupon_single_item or coupon_voucher | [optional] 
**name** | **str** | The name of the item | 
**shipping_tier** | **int** | Provides the abstract shipping needs if this item is physical and can be shipped.  A value of zero means no shipping needed.  Default &#x3D; 0 | [optional] 
**short_description** | **str** | A short description of the item, max 255 chars | [optional] 
**skus** | [**list[Sku]**](Sku.md) | The skus for the item. Each defines a unique configuration for the item to be purchased (Large-Blue, Small-Green, etc). These are what is ultimately selected in the store and added to the cart | 
**sort** | **int** | A number to use in sorting items.  Default 500 | [optional] 
**store_end** | **int** | The date the item will leave the store, unix timestamp in seconds.  If set to null, item will never leave the store | [optional] 
**store_start** | **int** | The date the item will appear in the store, unix timestamp in seconds.  If set to null, item will appear in store immediately | [optional] 
**tags** | **list[str]** | List of tags used for filtering items | [optional] 
**template** | **str** | An item template this item is validated against.  May be null and no validation of additional_properties will be done.  Default &#x3D; null | [optional] 
**type_hint** | **str** | The type of the item | 
**unique_key** | **str** | The unique key for the item | [optional] 
**updated_date** | **int** | The date the item was last updated, unix timestamp in seconds | [optional] 
**valid_for_tags** | **list[str]** | A list of tags for a coupon.  The coupon can only apply to an item that has at least one of these tags.  Applies if coupon_type_hint is coupon_tag | [optional] 
**vendor_id** | **int** | The vendor who provides the item | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


