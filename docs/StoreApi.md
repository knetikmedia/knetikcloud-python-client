# knetik_cloud.StoreApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_template**](StoreApi.md#create_item_template) | **POST** /store/items/templates | Create an item template
[**create_store_item**](StoreApi.md#create_store_item) | **POST** /store/items | Create a store item
[**delete_item_template**](StoreApi.md#delete_item_template) | **DELETE** /store/items/templates/{id} | Delete an item template
[**delete_store_item**](StoreApi.md#delete_store_item) | **DELETE** /store/items/{id} | Delete a store item
[**get_behaviors**](StoreApi.md#get_behaviors) | **GET** /store/items/behaviors | List available item behaviors
[**get_item_template**](StoreApi.md#get_item_template) | **GET** /store/items/templates/{id} | Get a single item template
[**get_item_templates**](StoreApi.md#get_item_templates) | **GET** /store/items/templates | List and search item templates
[**get_store_item**](StoreApi.md#get_store_item) | **GET** /store/items/{id} | Get a single store item
[**get_store_items**](StoreApi.md#get_store_items) | **GET** /store/items | List and search store items
[**quick_buy**](StoreApi.md#quick_buy) | **POST** /store/quick-buy | One-step purchase and pay for a single SKU item from a user&#39;s wallet
[**update_item_template**](StoreApi.md#update_item_template) | **PUT** /store/items/templates/{id} | Update an item template
[**update_store_item**](StoreApi.md#update_store_item) | **PUT** /store/items/{id} | Update a store item


# **create_item_template**
> StoreItemTemplateResource create_item_template(item_template_resource=item_template_resource)

Create an item template

Item Templates define a type of item and the properties they have. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
item_template_resource = knetik_cloud.StoreItemTemplateResource() # StoreItemTemplateResource | The new item template (optional)

try: 
    # Create an item template
    api_response = api_instance.create_item_template(item_template_resource=item_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->create_item_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_template_resource** | [**StoreItemTemplateResource**](StoreItemTemplateResource.md)| The new item template | [optional] 

### Return type

[**StoreItemTemplateResource**](StoreItemTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_store_item**
> StoreItem create_store_item(cascade=cascade, store_item=store_item)

Create a store item

SKUs have to be unique in the entire store. If a duplicate SKU is found, a 400 error is generated and the response will have a \"parameters\" field that is a list of duplicates. A duplicate is an object like {item_id, offending_sku_list}. Ex:<br /> {..., parameters: [[{item: 1, skus: [\"SKU-1\"]}]]}<br /> If an item is brand new and has duplicate SKUs within itself, the item ID will be 0.  Item subclasses are not allowed here, you will have to use their respective endpoints. <br><br><b>Permissions Needed:</b> STORE_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
cascade = false # bool | Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values. (optional) (default to false)
store_item = knetik_cloud.StoreItem() # StoreItem | The store item object (optional)

try: 
    # Create a store item
    api_response = api_instance.create_store_item(cascade=cascade, store_item=store_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->create_store_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cascade** | **bool**| Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values. | [optional] [default to false]
 **store_item** | [**StoreItem**](StoreItem.md)| The store item object | [optional] 

### Return type

[**StoreItem**](StoreItem.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_template**
> delete_item_template(id, cascade=cascade)

Delete an item template

<b>Permissions Needed:</b> TEMPLATE_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | force deleting the template if it's attached to other objects, cascade = detach (optional)

try: 
    # Delete an item template
    api_instance.delete_item_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling StoreApi->delete_item_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| force deleting the template if it&#39;s attached to other objects, cascade &#x3D; detach | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_store_item**
> delete_store_item(id)

Delete a store item

<b>Permissions Needed:</b> STORE_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id of the item

try: 
    # Delete a store item
    api_instance.delete_store_item(id)
except ApiException as e:
    print("Exception when calling StoreApi->delete_store_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the item | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_behaviors**
> list[BehaviorDefinitionResource] get_behaviors()

List available item behaviors

<b>Permissions Needed:</b> ANY

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))

try: 
    # List available item behaviors
    api_response = api_instance.get_behaviors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_behaviors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BehaviorDefinitionResource]**](BehaviorDefinitionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_template**
> StoreItemTemplateResource get_item_template(id)

Get a single item template

Item Templates define a type of item and the properties they have. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single item template
    api_response = api_instance.get_item_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_item_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**StoreItemTemplateResource**](StoreItemTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_templates**
> PageResourceStoreItemTemplateResource get_item_templates(size=size, page=page, order=order)

List and search item templates

<b>Permissions Needed:</b> TEMPLATE_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search item templates
    api_response = api_instance.get_item_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_item_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceStoreItemTemplateResource**](PageResourceStoreItemTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_item**
> StoreItem get_store_item(id)

Get a single store item

<b>Permissions Needed:</b> ANY

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id of the item

try: 
    # Get a single store item
    api_response = api_instance.get_store_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_store_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the item | 

### Return type

[**StoreItem**](StoreItem.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_items**
> PageResourceStoreItem get_store_items(filter_name_search=filter_name_search, filter_unique_key=filter_unique_key, filter_published=filter_published, filter_displayable=filter_displayable, filter_start=filter_start, filter_end=filter_end, filter_start_date=filter_start_date, filter_stop_date=filter_stop_date, filter_sku=filter_sku, filter_price=filter_price, filter_tag=filter_tag, filter_items_by_type=filter_items_by_type, filter_bundled_skus=filter_bundled_skus, filter_vendor=filter_vendor, size=size, page=page, order=order)

List and search store items

If called without permission STORE_ADMIN the only items marked displayable, whose start and end date are null or appropriate to the current date, and whose geo policy allows the caller's country will be returned. Similarly skus will be filtered, possibly resulting in an item returned with no skus the user can purchase. br><br><b>Permissions Needed:</b> ANY

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
filter_name_search = 'filter_name_search_example' # str | Filter for items whose name starts with a given string. (optional)
filter_unique_key = 'filter_unique_key_example' # str | Filter for items whose unique_key is a given string. (optional)
filter_published = true # bool | Filter for skus that have been published. (optional)
filter_displayable = true # bool | Filter for items that are displayable. (optional)
filter_start = 'filter_start_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the store start date, a unix timestamp in seconds.  Allowed operators: (LT, GT, LTE, GTE, EQ). (optional)
filter_end = 'filter_end_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the store end date, a unix timestamp in seconds.  Allowed operators: (LT, GT, LTE, GTE, EQ). (optional)
filter_start_date = 'filter_start_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the sku start date, a unix timestamp in seconds.  Allowed operators: (LT, GT, LTE, GTE, EQ). (optional)
filter_stop_date = 'filter_stop_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the sku end date, a unix timestamp in seconds.  Allowed operators: (LT, GT, LTE, GTE, EQ). (optional)
filter_sku = 'filter_sku_example' # str | Filter for skus whose name starts with a given string. (optional)
filter_price = 'filter_price_example' # str | A colon separated string without spaces.  First value is the operator to search on, second value is the price of a sku.  Allowed operators: (LT, GT, LTE, GTE, EQ). (optional)
filter_tag = 'filter_tag_example' # str | A comma separated list without spaces of the names of tags. Will only return items with at least one of the tags. (optional)
filter_items_by_type = 'filter_items_by_type_example' # str | Filter for item type based on its type hint. (optional)
filter_bundled_skus = 'filter_bundled_skus_example' # str | Filter for skus inside bundles whose name starts with a given string.  Used only when type hint is 'bundle_item' (optional)
filter_vendor = 56 # int | Filter for items from a given vendor, by id. (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search store items
    api_response = api_instance.get_store_items(filter_name_search=filter_name_search, filter_unique_key=filter_unique_key, filter_published=filter_published, filter_displayable=filter_displayable, filter_start=filter_start, filter_end=filter_end, filter_start_date=filter_start_date, filter_stop_date=filter_stop_date, filter_sku=filter_sku, filter_price=filter_price, filter_tag=filter_tag, filter_items_by_type=filter_items_by_type, filter_bundled_skus=filter_bundled_skus, filter_vendor=filter_vendor, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_store_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name_search** | **str**| Filter for items whose name starts with a given string. | [optional] 
 **filter_unique_key** | **str**| Filter for items whose unique_key is a given string. | [optional] 
 **filter_published** | **bool**| Filter for skus that have been published. | [optional] 
 **filter_displayable** | **bool**| Filter for items that are displayable. | [optional] 
 **filter_start** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the store start date, a unix timestamp in seconds.  Allowed operators: (LT, GT, LTE, GTE, EQ). | [optional] 
 **filter_end** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the store end date, a unix timestamp in seconds.  Allowed operators: (LT, GT, LTE, GTE, EQ). | [optional] 
 **filter_start_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the sku start date, a unix timestamp in seconds.  Allowed operators: (LT, GT, LTE, GTE, EQ). | [optional] 
 **filter_stop_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the sku end date, a unix timestamp in seconds.  Allowed operators: (LT, GT, LTE, GTE, EQ). | [optional] 
 **filter_sku** | **str**| Filter for skus whose name starts with a given string. | [optional] 
 **filter_price** | **str**| A colon separated string without spaces.  First value is the operator to search on, second value is the price of a sku.  Allowed operators: (LT, GT, LTE, GTE, EQ). | [optional] 
 **filter_tag** | **str**| A comma separated list without spaces of the names of tags. Will only return items with at least one of the tags. | [optional] 
 **filter_items_by_type** | **str**| Filter for item type based on its type hint. | [optional] 
 **filter_bundled_skus** | **str**| Filter for skus inside bundles whose name starts with a given string.  Used only when type hint is &#39;bundle_item&#39; | [optional] 
 **filter_vendor** | **int**| Filter for items from a given vendor, by id. | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceStoreItem**](PageResourceStoreItem.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quick_buy**
> InvoiceResource quick_buy(quick_buy_request=quick_buy_request)

One-step purchase and pay for a single SKU item from a user's wallet

Used to create and automatically pay an invoice for a single unit of a single SKU from a user's wallet. SKU must be priced in virtual currency and must not be an item that requires shipping. PAYMENTS_ADMIN permission is required if user ID is specified and is not the ID of the currently logged in user. If invoice price does not match expected price, purchase is aborted. <br><br><b>Permissions Needed:</b> PAYMENTS_USER and owner, or PAYMENTS_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
quick_buy_request = knetik_cloud.QuickBuyRequest() # QuickBuyRequest | Quick buy details (optional)

try: 
    # One-step purchase and pay for a single SKU item from a user's wallet
    api_response = api_instance.quick_buy(quick_buy_request=quick_buy_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->quick_buy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_buy_request** | [**QuickBuyRequest**](QuickBuyRequest.md)| Quick buy details | [optional] 

### Return type

[**InvoiceResource**](InvoiceResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_template**
> StoreItemTemplateResource update_item_template(id, item_template_resource=item_template_resource)

Update an item template

<b>Permissions Needed:</b> TEMPLATE_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
item_template_resource = knetik_cloud.StoreItemTemplateResource() # StoreItemTemplateResource | The item template resource object (optional)

try: 
    # Update an item template
    api_response = api_instance.update_item_template(id, item_template_resource=item_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->update_item_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **item_template_resource** | [**StoreItemTemplateResource**](StoreItemTemplateResource.md)| The item template resource object | [optional] 

### Return type

[**StoreItemTemplateResource**](StoreItemTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_store_item**
> StoreItem update_store_item(id, cascade=cascade, store_item=store_item)

Update a store item

<b>Permissions Needed:</b> STORE_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id of the item
cascade = false # bool | Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values. (optional) (default to false)
store_item = knetik_cloud.StoreItem() # StoreItem | The store item object (optional)

try: 
    # Update a store item
    api_response = api_instance.update_store_item(id, cascade=cascade, store_item=store_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->update_store_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the item | 
 **cascade** | **bool**| Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values. | [optional] [default to false]
 **store_item** | [**StoreItem**](StoreItem.md)| The store item object | [optional] 

### Return type

[**StoreItem**](StoreItem.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

