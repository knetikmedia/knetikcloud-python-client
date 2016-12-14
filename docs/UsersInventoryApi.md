# swagger_client.UsersInventoryApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_using_post1**](UsersInventoryApi.md#add_item_using_post1) | **POST** /users/{id}/inventory | Adds an item to the user inventory
[**create_item_using_post**](UsersInventoryApi.md#create_item_using_post) | **POST** /entitlements | Create an entitlement item
[**delete_item_using_delete**](UsersInventoryApi.md#delete_item_using_delete) | **DELETE** /entitlements/{entitlement_id} | Delete an entitlement item
[**entitlement_check_using_get**](UsersInventoryApi.md#entitlement_check_using_get) | **GET** /users/{user_id}/entitlements/{item_id}/check | Check for access to an item without consuming
[**entitlement_use_using_post**](UsersInventoryApi.md#entitlement_use_using_post) | **POST** /users/{user_id}/entitlements/{item_id}/use | Use an item
[**get_currencies_using_get1**](UsersInventoryApi.md#get_currencies_using_get1) | **GET** /entitlements | List and search entitlement items
[**get_inventory_list_using_get**](UsersInventoryApi.md#get_inventory_list_using_get) | **GET** /inventories | List the user inventory entries for all users
[**get_inventory_using_get**](UsersInventoryApi.md#get_inventory_using_get) | **GET** /users/{user_id}/inventory/{id} | Get an inventory entry
[**get_item_using_get**](UsersInventoryApi.md#get_item_using_get) | **GET** /entitlements/{entitlement_id} | Get a single entitlement item
[**get_user_inventory_list_using_get**](UsersInventoryApi.md#get_user_inventory_list_using_get) | **GET** /users/{id}/inventory | List the user inventory entries for a given user
[**get_user_inventory_log_using_get**](UsersInventoryApi.md#get_user_inventory_log_using_get) | **GET** /users/{user_id}/inventory/{id}/log | List the log entries for this inventory entry.
[**update_item_using_put1**](UsersInventoryApi.md#update_item_using_put1) | **PUT** /entitlements/{entitlement_id} | Update an entitlement item
[**update_user_inventory_behavior_data_using_put**](UsersInventoryApi.md#update_user_inventory_behavior_data_using_put) | **PUT** /users/{user_id}/inventory/{id}/behavior-data | Set the behavior data for an inventory entry
[**update_user_inventory_expires_using_put**](UsersInventoryApi.md#update_user_inventory_expires_using_put) | **PUT** /users/{user_id}/inventory/{id}/expires | Set the expiration date
[**update_user_inventory_status_using_put**](UsersInventoryApi.md#update_user_inventory_status_using_put) | **PUT** /users/{user_id}/inventory/{id}/status | Set the status for an inventory entry


# **add_item_using_post1**
> InvoiceResource add_item_using_post1(id, user_inventory_add_request=user_inventory_add_request)

Adds an item to the user inventory

The inventory is fulfilled asynchronously UNLESS the invoice is explicitely skipped. Depending on the use case, it might require the client to verify that the entitlement was added after the fact or configure a BRE rule to get a notification in real time

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
id = 56 # int | The id of the user
user_inventory_add_request = swagger_client.UserInventoryAddRequest() # UserInventoryAddRequest | The user inventory add request object (optional)

try: 
    # Adds an item to the user inventory
    api_response = api_instance.add_item_using_post1(id, user_inventory_add_request=user_inventory_add_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->add_item_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the user | 
 **user_inventory_add_request** | [**UserInventoryAddRequest**](UserInventoryAddRequest.md)| The user inventory add request object | [optional] 

### Return type

[**InvoiceResource**](InvoiceResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_using_post**
> EntitlementItem create_item_using_post(entitlement_item=entitlement_item)

Create an entitlement item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
entitlement_item = swagger_client.EntitlementItem() # EntitlementItem | The entitlement item object (optional)

try: 
    # Create an entitlement item
    api_response = api_instance.create_item_using_post(entitlement_item=entitlement_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->create_item_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_item** | [**EntitlementItem**](EntitlementItem.md)| The entitlement item object | [optional] 

### Return type

[**EntitlementItem**](EntitlementItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item_using_delete**
> delete_item_using_delete(entitlement_id)

Delete an entitlement item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
entitlement_id = 56 # int | The id of the entitlement

try: 
    # Delete an entitlement item
    api_instance.delete_item_using_delete(entitlement_id)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->delete_item_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_id** | **int**| The id of the entitlement | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlement_check_using_get**
> entitlement_check_using_get(user_id, item_id, sku=sku)

Check for access to an item without consuming

Useful for pre-check and accounts for all various buisness rules

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
user_id = 'user_id_example' # str | The id of the user to check for or 'me' for logged in user
item_id = 56 # int | The id of the item
sku = 'sku_example' # str | The specific sku of an entitlement list addition to check entitlement for. This is of very limited and specific use and should generally be left out (optional)

try: 
    # Check for access to an item without consuming
    api_instance.entitlement_check_using_get(user_id, item_id, sku=sku)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->entitlement_check_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user to check for or &#39;me&#39; for logged in user | 
 **item_id** | **int**| The id of the item | 
 **sku** | **str**| The specific sku of an entitlement list addition to check entitlement for. This is of very limited and specific use and should generally be left out | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlement_use_using_post**
> entitlement_use_using_post(user_id, item_id, sku=sku, info=info)

Use an item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
user_id = 'user_id_example' # str | The id of the user to check for or 'me' for logged in user
item_id = 56 # int | The id of the item
sku = 'sku_example' # str | The specific sku of an entitlement_list addition to check entitlement for. This is of very limited and specific use and should generally be left out (optional)
info = 'info_example' # str | Any additional info to add to the log about this use (optional)

try: 
    # Use an item
    api_instance.entitlement_use_using_post(user_id, item_id, sku=sku, info=info)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->entitlement_use_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user to check for or &#39;me&#39; for logged in user | 
 **item_id** | **int**| The id of the item | 
 **sku** | **str**| The specific sku of an entitlement_list addition to check entitlement for. This is of very limited and specific use and should generally be left out | [optional] 
 **info** | **str**| Any additional info to add to the log about this use | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies_using_get1**
> PageEntitlementItem get_currencies_using_get1(size=size, page=page, order=order)

List and search entitlement items

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # List and search entitlement items
    api_response = api_instance.get_currencies_using_get1(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_currencies_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageEntitlementItem**](PageEntitlementItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_list_using_get**
> PageUserInventoryResource get_inventory_list_using_get(inactive=inactive, size=size, page=page, filter_item_name=filter_item_name, filter_min_date=filter_min_date, filter_max_date=filter_max_date)

List the user inventory entries for all users

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
inactive = false # bool | If true, accepts inactive user inventories (optional) (default to false)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
filter_item_name = 'filter_item_name_example' # str | Filter by items whose name starts with a string (optional)
filter_min_date = 789 # int | Filter for inventory added after the specified date, unix timestamp in seconds (optional)
filter_max_date = 789 # int | Filter for inventory added before the specified date, unix timestamp in seconds (optional)

try: 
    # List the user inventory entries for all users
    api_response = api_instance.get_inventory_list_using_get(inactive=inactive, size=size, page=page, filter_item_name=filter_item_name, filter_min_date=filter_min_date, filter_max_date=filter_max_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_inventory_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inactive** | **bool**| If true, accepts inactive user inventories | [optional] [default to false]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **filter_item_name** | **str**| Filter by items whose name starts with a string | [optional] 
 **filter_min_date** | **int**| Filter for inventory added after the specified date, unix timestamp in seconds | [optional] 
 **filter_max_date** | **int**| Filter for inventory added before the specified date, unix timestamp in seconds | [optional] 

### Return type

[**PageUserInventoryResource**](PageUserInventoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_using_get**
> UserInventoryResource get_inventory_using_get(user_id, id)

Get an inventory entry

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
user_id = 56 # int | The id of the inventory owner or 'me' for the logged in user
id = 56 # int | The id of the user inventory

try: 
    # Get an inventory entry
    api_response = api_instance.get_inventory_using_get(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_inventory_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the inventory owner or &#39;me&#39; for the logged in user | 
 **id** | **int**| The id of the user inventory | 

### Return type

[**UserInventoryResource**](UserInventoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_using_get**
> EntitlementItem get_item_using_get(entitlement_id)

Get a single entitlement item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
entitlement_id = 56 # int | The id of the entitlement

try: 
    # Get a single entitlement item
    api_response = api_instance.get_item_using_get(entitlement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_item_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_id** | **int**| The id of the entitlement | 

### Return type

[**EntitlementItem**](EntitlementItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_inventory_list_using_get**
> PageUserInventoryResource get_user_inventory_list_using_get(id, inactive=inactive, size=size, page=page, filter_item_name=filter_item_name, filter_min_date=filter_min_date, filter_max_date=filter_max_date)

List the user inventory entries for a given user

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
id = 56 # int | The id of the user
inactive = false # bool | If true, accepts inactive user inventories (optional) (default to false)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
filter_item_name = 'filter_item_name_example' # str | Filter by items whose name starts with a string (optional)
filter_min_date = 789 # int | Filter for inventory added after the specified date, unix timestamp in seconds (optional)
filter_max_date = 789 # int | Filter for inventory added before the specified date, unix timestamp in seconds (optional)

try: 
    # List the user inventory entries for a given user
    api_response = api_instance.get_user_inventory_list_using_get(id, inactive=inactive, size=size, page=page, filter_item_name=filter_item_name, filter_min_date=filter_min_date, filter_max_date=filter_max_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_user_inventory_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the user | 
 **inactive** | **bool**| If true, accepts inactive user inventories | [optional] [default to false]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **filter_item_name** | **str**| Filter by items whose name starts with a string | [optional] 
 **filter_min_date** | **int**| Filter for inventory added after the specified date, unix timestamp in seconds | [optional] 
 **filter_max_date** | **int**| Filter for inventory added before the specified date, unix timestamp in seconds | [optional] 

### Return type

[**PageUserInventoryResource**](PageUserInventoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_inventory_log_using_get**
> PageUserItemLogResource get_user_inventory_log_using_get(user_id, id, size=size, page=page)

List the log entries for this inventory entry.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
user_id = 'user_id_example' # str | The id of the inventory owner or 'me' for the logged in user
id = 56 # int | The id of the user inventory
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List the log entries for this inventory entry.
    api_response = api_instance.get_user_inventory_log_using_get(user_id, id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_user_inventory_log_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the inventory owner or &#39;me&#39; for the logged in user | 
 **id** | **int**| The id of the user inventory | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageUserItemLogResource**](PageUserItemLogResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_using_put1**
> update_item_using_put1(entitlement_id, entitlement_item=entitlement_item)

Update an entitlement item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
entitlement_id = 56 # int | The id of the entitlement
entitlement_item = swagger_client.EntitlementItem() # EntitlementItem | The entitlement item object (optional)

try: 
    # Update an entitlement item
    api_instance.update_item_using_put1(entitlement_id, entitlement_item=entitlement_item)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->update_item_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_id** | **int**| The id of the entitlement | 
 **entitlement_item** | [**EntitlementItem**](EntitlementItem.md)| The entitlement item object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_inventory_behavior_data_using_put**
> update_user_inventory_behavior_data_using_put(user_id, id, data=data)

Set the behavior data for an inventory entry

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
user_id = 56 # int | The id of the user
id = 56 # int | The id of the user inventory
data = NULL # object | The data map (optional)

try: 
    # Set the behavior data for an inventory entry
    api_instance.update_user_inventory_behavior_data_using_put(user_id, id, data=data)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->update_user_inventory_behavior_data_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **id** | **int**| The id of the user inventory | 
 **data** | **object**| The data map | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_inventory_expires_using_put**
> update_user_inventory_expires_using_put(user_id, id, timestamp=timestamp)

Set the expiration date

Will change the current grace period for a subscription but not the bill date (possibly even ending before having the chance to re-bill)

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
user_id = 56 # int | user_id
id = 56 # int | The id of the user inventory
timestamp = 789 # int | The new expiration date as a unix timestamp in seconds. May be null (no body). (optional)

try: 
    # Set the expiration date
    api_instance.update_user_inventory_expires_using_put(user_id, id, timestamp=timestamp)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->update_user_inventory_expires_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| user_id | 
 **id** | **int**| The id of the user inventory | 
 **timestamp** | **int**| The new expiration date as a unix timestamp in seconds. May be null (no body). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_inventory_status_using_put**
> update_user_inventory_status_using_put(user_id, id, inventory_status=inventory_status)

Set the status for an inventory entry

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersInventoryApi()
user_id = 56 # int | The id of the user
id = 56 # int | The id of the user inventory
inventory_status = 'inventory_status_example' # str | The inventory status object (optional)

try: 
    # Set the status for an inventory entry
    api_instance.update_user_inventory_status_using_put(user_id, id, inventory_status=inventory_status)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->update_user_inventory_status_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **id** | **int**| The id of the user inventory | 
 **inventory_status** | **str**| The inventory status object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

