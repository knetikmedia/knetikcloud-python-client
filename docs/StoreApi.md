# swagger_client.StoreApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_item_template_using_post**](StoreApi.md#create_item_template_using_post) | **POST** /store/items/templates | Create an item template
[**create_store_item_external_using_post**](StoreApi.md#create_store_item_external_using_post) | **POST** /store/items | Create a store item
[**delete_item_template_using_delete**](StoreApi.md#delete_item_template_using_delete) | **DELETE** /store/items/templates/{id} | Delete an item template
[**delete_store_item_using_delete1**](StoreApi.md#delete_store_item_using_delete1) | **DELETE** /store/items/{id} | Delete a store item
[**get_item_template_using_get**](StoreApi.md#get_item_template_using_get) | **GET** /store/items/templates/{id} | Get a single item template
[**get_item_templates_using_get**](StoreApi.md#get_item_templates_using_get) | **GET** /store/items/templates | List and search item templates
[**get_store_item_using_get1**](StoreApi.md#get_store_item_using_get1) | **GET** /store/items/{id} | Get a single store item
[**get_store_items_using_get**](StoreApi.md#get_store_items_using_get) | **GET** /store/items | List and search store items
[**get_using_get2**](StoreApi.md#get_using_get2) | **GET** /store | Get a listing of store items
[**update_item_template_using_put**](StoreApi.md#update_item_template_using_put) | **PUT** /store/items/templates/{id} | Update an item template
[**update_store_item_external_using_put**](StoreApi.md#update_store_item_external_using_put) | **PUT** /store/items/{id} | Update a store item


# **create_item_template_using_post**
> StoreItemTemplateResource create_item_template_using_post(item_template_resource=item_template_resource)

Create an item template

Item Templates define a type of item and the properties they have.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StoreApi()
item_template_resource = swagger_client.StoreItemTemplateResource() # StoreItemTemplateResource | The new item template (optional)

try: 
    # Create an item template
    api_response = api_instance.create_item_template_using_post(item_template_resource=item_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->create_item_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_template_resource** | [**StoreItemTemplateResource**](StoreItemTemplateResource.md)| The new item template | [optional] 

### Return type

[**StoreItemTemplateResource**](StoreItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_store_item_external_using_post**
> StoreItem create_store_item_external_using_post(store_item=store_item)

Create a store item

SKUs have to be unique in the entire store. If a duplicate SKU is found, a 400 error is generated and the response will have a \"parameters\" field that is a list of duplicates. A duplicate is an object like {item_id, offending_sku_list}. Ex:<br /> {..., parameters: [[{item: 1, skus: [\"SKU-1\"]}]]}<br /> If an item is brand new and has duplicate SKUs within itself, the item ID will be 0.  Item subclasses are not allowed here, you will have to use their respective endpoints.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StoreApi()
store_item = swagger_client.StoreItem() # StoreItem | The store item object (optional)

try: 
    # Create a store item
    api_response = api_instance.create_store_item_external_using_post(store_item=store_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->create_store_item_external_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_item** | [**StoreItem**](StoreItem.md)| The store item object | [optional] 

### Return type

[**StoreItem**](StoreItem.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_template_using_delete**
> delete_item_template_using_delete(id, cascade=cascade)

Delete an item template

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StoreApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | force deleting the template if it's attached to other objects, cascade = detach (optional)

try: 
    # Delete an item template
    api_instance.delete_item_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling StoreApi->delete_item_template_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| force deleting the template if it&#39;s attached to other objects, cascade &#x3D; detach | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_store_item_using_delete1**
> delete_store_item_using_delete1(id)

Delete a store item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StoreApi()
id = 56 # int | The id of the item

try: 
    # Delete a store item
    api_instance.delete_store_item_using_delete1(id)
except ApiException as e:
    print("Exception when calling StoreApi->delete_store_item_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the item | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_template_using_get**
> StoreItemTemplateResource get_item_template_using_get(id)

Get a single item template

Item Templates define a type of item and the properties they have.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StoreApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single item template
    api_response = api_instance.get_item_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_item_template_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**StoreItemTemplateResource**](StoreItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_templates_using_get**
> PageStoreItemTemplateResource get_item_templates_using_get(size=size, page=page, order=order)

List and search item templates

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StoreApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search item templates
    api_response = api_instance.get_item_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_item_templates_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageStoreItemTemplateResource**](PageStoreItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_item_using_get1**
> StoreItem get_store_item_using_get1(id)

Get a single store item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreApi()
id = 56 # int | The id of the item

try: 
    # Get a single store item
    api_response = api_instance.get_store_item_using_get1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_store_item_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the item | 

### Return type

[**StoreItem**](StoreItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_items_using_get**
> PageStoreItem get_store_items_using_get(filter_name_search=filter_name_search, filter_unique_key=filter_unique_key, filter_published=filter_published, filter_displayable=filter_displayable, filter_start=filter_start, filter_end=filter_end, filter_start_date=filter_start_date, filter_stop_date=filter_stop_date, filter_sku=filter_sku, filter_price=filter_price, filter_tag=filter_tag, filter_items_by_type=filter_items_by_type, filter_bundled_skus=filter_bundled_skus, size=size, page=page, order=order)

List and search store items

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreApi()
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
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search store items
    api_response = api_instance.get_store_items_using_get(filter_name_search=filter_name_search, filter_unique_key=filter_unique_key, filter_published=filter_published, filter_displayable=filter_displayable, filter_start=filter_start, filter_end=filter_end, filter_start_date=filter_start_date, filter_stop_date=filter_stop_date, filter_sku=filter_sku, filter_price=filter_price, filter_tag=filter_tag, filter_items_by_type=filter_items_by_type, filter_bundled_skus=filter_bundled_skus, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_store_items_using_get: %s\n" % e)
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
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageStoreItem**](PageStoreItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get2**
> PageStoreItem get_using_get2(store_list_request=store_list_request)

Get a listing of store items

The exact structure of each items may differ to include fields specific to the type. The same is true for behaviors.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreApi()
store_list_request = swagger_client.StoreListRequest() # StoreListRequest | The store list request object (optional)

try: 
    # Get a listing of store items
    api_response = api_instance.get_using_get2(store_list_request=store_list_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreApi->get_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_list_request** | [**StoreListRequest**](StoreListRequest.md)| The store list request object | [optional] 

### Return type

[**PageStoreItem**](PageStoreItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_template_using_put**
> update_item_template_using_put(id, item_template_resource=item_template_resource)

Update an item template

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StoreApi()
id = 'id_example' # str | The id of the template
item_template_resource = swagger_client.StoreItemTemplateResource() # StoreItemTemplateResource | The item template resource object (optional)

try: 
    # Update an item template
    api_instance.update_item_template_using_put(id, item_template_resource=item_template_resource)
except ApiException as e:
    print("Exception when calling StoreApi->update_item_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **item_template_resource** | [**StoreItemTemplateResource**](StoreItemTemplateResource.md)| The item template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_store_item_external_using_put**
> update_store_item_external_using_put(id, store_item=store_item)

Update a store item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StoreApi()
id = 56 # int | The id of the item
store_item = swagger_client.StoreItem() # StoreItem | The store item object (optional)

try: 
    # Update a store item
    api_instance.update_store_item_external_using_put(id, store_item=store_item)
except ApiException as e:
    print("Exception when calling StoreApi->update_store_item_external_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the item | 
 **store_item** | [**StoreItem**](StoreItem.md)| The store item object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

