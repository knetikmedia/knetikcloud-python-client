# knetik_cloud.UsersInventoryApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_item_to_user_inventory**](UsersInventoryApi.md#add_item_to_user_inventory) | **POST** /users/{id}/inventory | Adds an item to the user inventory
[**check_user_entitlement_item**](UsersInventoryApi.md#check_user_entitlement_item) | **GET** /users/{user_id}/entitlements/{item_id}/check | Check for access to an item without consuming
[**create_entitlement_item**](UsersInventoryApi.md#create_entitlement_item) | **POST** /entitlements | Create an entitlement item
[**create_entitlement_template**](UsersInventoryApi.md#create_entitlement_template) | **POST** /entitlements/templates | Create an entitlement template
[**delete_entitlement_item**](UsersInventoryApi.md#delete_entitlement_item) | **DELETE** /entitlements/{entitlement_id} | Delete an entitlement item
[**delete_entitlement_template**](UsersInventoryApi.md#delete_entitlement_template) | **DELETE** /entitlements/templates/{id} | Delete an entitlement template
[**get_entitlement_item**](UsersInventoryApi.md#get_entitlement_item) | **GET** /entitlements/{entitlement_id} | Get a single entitlement item
[**get_entitlement_items**](UsersInventoryApi.md#get_entitlement_items) | **GET** /entitlements | List and search entitlement items
[**get_entitlement_template**](UsersInventoryApi.md#get_entitlement_template) | **GET** /entitlements/templates/{id} | Get a single entitlement template
[**get_entitlement_templates**](UsersInventoryApi.md#get_entitlement_templates) | **GET** /entitlements/templates | List and search entitlement templates
[**get_user_inventories**](UsersInventoryApi.md#get_user_inventories) | **GET** /users/{id}/inventory | List the user inventory entries for a given user
[**get_user_inventory**](UsersInventoryApi.md#get_user_inventory) | **GET** /users/{user_id}/inventory/{id} | Get an inventory entry
[**get_user_inventory_log**](UsersInventoryApi.md#get_user_inventory_log) | **GET** /users/{user_id}/inventory/{id}/log | List the log entries for this inventory entry
[**get_users_inventory**](UsersInventoryApi.md#get_users_inventory) | **GET** /inventories | List the user inventory entries for all users
[**grant_user_entitlement**](UsersInventoryApi.md#grant_user_entitlement) | **POST** /users/{user_id}/entitlements | Grant an entitlement
[**update_entitlement_item**](UsersInventoryApi.md#update_entitlement_item) | **PUT** /entitlements/{entitlement_id} | Update an entitlement item
[**update_entitlement_template**](UsersInventoryApi.md#update_entitlement_template) | **PUT** /entitlements/templates/{id} | Update an entitlement template
[**update_user_inventory_behavior_data**](UsersInventoryApi.md#update_user_inventory_behavior_data) | **PUT** /users/{user_id}/inventory/{id}/behavior-data | Set the behavior data for an inventory entry
[**update_user_inventory_expires**](UsersInventoryApi.md#update_user_inventory_expires) | **PUT** /users/{user_id}/inventory/{id}/expires | Set the expiration date
[**update_user_inventory_status**](UsersInventoryApi.md#update_user_inventory_status) | **PUT** /users/{user_id}/inventory/{id}/status | Set the status for an inventory entry
[**use_user_entitlement_item**](UsersInventoryApi.md#use_user_entitlement_item) | **POST** /users/{user_id}/entitlements/{item_id}/use | Use an item


# **add_item_to_user_inventory**
> InvoiceResource add_item_to_user_inventory(id, user_inventory_add_request=user_inventory_add_request)

Adds an item to the user inventory

The inventory is fulfilled asynchronously UNLESS the invoice is explicitely skipped. Depending on the use case, it might require the client to verify that the entitlement was added after the fact or configure a BRE rule to get a notification in real time

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
id = 56 # int | The id of the user
user_inventory_add_request = knetik_cloud.UserInventoryAddRequest() # UserInventoryAddRequest | The user inventory add request object (optional)

try: 
    # Adds an item to the user inventory
    api_response = api_instance.add_item_to_user_inventory(id, user_inventory_add_request=user_inventory_add_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->add_item_to_user_inventory: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_user_entitlement_item**
> check_user_entitlement_item(user_id, item_id, sku=sku)

Check for access to an item without consuming

Useful for pre-check and accounts for all various buisness rules

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
user_id = 'user_id_example' # str | The id of the user to check for or 'me' for logged in user
item_id = 56 # int | The id of the item
sku = 'sku_example' # str | The specific sku of an entitlement list addition to check entitlement for. This is of very limited and specific use and should generally be left out (optional)

try: 
    # Check for access to an item without consuming
    api_instance.check_user_entitlement_item(user_id, item_id, sku=sku)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->check_user_entitlement_item: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entitlement_item**
> EntitlementItem create_entitlement_item(cascade=cascade, entitlement_item=entitlement_item)

Create an entitlement item

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
cascade = false # bool | Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values. (optional) (default to false)
entitlement_item = knetik_cloud.EntitlementItem() # EntitlementItem | The entitlement item object (optional)

try: 
    # Create an entitlement item
    api_response = api_instance.create_entitlement_item(cascade=cascade, entitlement_item=entitlement_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->create_entitlement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cascade** | **bool**| Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values. | [optional] [default to false]
 **entitlement_item** | [**EntitlementItem**](EntitlementItem.md)| The entitlement item object | [optional] 

### Return type

[**EntitlementItem**](EntitlementItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entitlement_template**
> ItemTemplateResource create_entitlement_template(template=template)

Create an entitlement template

Entitlement templates define a type of entitlement and the properties they have

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
template = knetik_cloud.ItemTemplateResource() # ItemTemplateResource | The entitlement template to be created (optional)

try: 
    # Create an entitlement template
    api_response = api_instance.create_entitlement_template(template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->create_entitlement_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | [**ItemTemplateResource**](ItemTemplateResource.md)| The entitlement template to be created | [optional] 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entitlement_item**
> delete_entitlement_item(entitlement_id)

Delete an entitlement item

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
entitlement_id = 56 # int | The id of the entitlement

try: 
    # Delete an entitlement item
    api_instance.delete_entitlement_item(entitlement_id)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->delete_entitlement_item: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entitlement_template**
> delete_entitlement_template(id, cascade=cascade)

Delete an entitlement template

If cascade = 'detach', it will force delete the template even if it's attached to other objects

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete an entitlement template
    api_instance.delete_entitlement_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->delete_entitlement_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| The value needed to delete used templates | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement_item**
> EntitlementItem get_entitlement_item(entitlement_id)

Get a single entitlement item

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
entitlement_id = 56 # int | The id of the entitlement

try: 
    # Get a single entitlement item
    api_response = api_instance.get_entitlement_item(entitlement_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_entitlement_item: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement_items**
> PageResourceEntitlementItem get_entitlement_items(size=size, page=page, order=order)

List and search entitlement items

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search entitlement items
    api_response = api_instance.get_entitlement_items(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_entitlement_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceEntitlementItem**](PageResourceEntitlementItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement_template**
> ItemTemplateResource get_entitlement_template(id)

Get a single entitlement template

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single entitlement template
    api_response = api_instance.get_entitlement_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_entitlement_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entitlement_templates**
> PageResourceItemTemplateResource get_entitlement_templates(size=size, page=page, order=order)

List and search entitlement templates

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search entitlement templates
    api_response = api_instance.get_entitlement_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_entitlement_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceItemTemplateResource**](PageResourceItemTemplateResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_inventories**
> PageResourceUserInventoryResource get_user_inventories(id, inactive=inactive, size=size, page=page, filter_item_name=filter_item_name, filter_item_id=filter_item_id, filter_username=filter_username, filter_group=filter_group, filter_date=filter_date)

List the user inventory entries for a given user

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
id = 56 # int | The id of the user
inactive = false # bool | If true, accepts inactive user inventories (optional) (default to false)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
filter_item_name = 'filter_item_name_example' # str | Filter by items whose name starts with a string (optional)
filter_item_id = 56 # int | Filter by item id (optional)
filter_username = 'filter_username_example' # str | Filter by entries owned by the user with the specified username (optional)
filter_group = 'filter_group_example' # str | Filter by entries owned by the users in a given group, by unique name (optional)
filter_date = 'filter_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the log start date, a unix timestamp in seconds. Can be repeated for a range, eg: GT,123,LT,456  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)

try: 
    # List the user inventory entries for a given user
    api_response = api_instance.get_user_inventories(id, inactive=inactive, size=size, page=page, filter_item_name=filter_item_name, filter_item_id=filter_item_id, filter_username=filter_username, filter_group=filter_group, filter_date=filter_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_user_inventories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the user | 
 **inactive** | **bool**| If true, accepts inactive user inventories | [optional] [default to false]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **filter_item_name** | **str**| Filter by items whose name starts with a string | [optional] 
 **filter_item_id** | **int**| Filter by item id | [optional] 
 **filter_username** | **str**| Filter by entries owned by the user with the specified username | [optional] 
 **filter_group** | **str**| Filter by entries owned by the users in a given group, by unique name | [optional] 
 **filter_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the log start date, a unix timestamp in seconds. Can be repeated for a range, eg: GT,123,LT,456  Allowed operators: (GT, LT, EQ, GOE, LOE). | [optional] 

### Return type

[**PageResourceUserInventoryResource**](PageResourceUserInventoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_inventory**
> UserInventoryResource get_user_inventory(user_id, id)

Get an inventory entry

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
user_id = 56 # int | The id of the inventory owner or 'me' for the logged in user
id = 56 # int | The id of the user inventory

try: 
    # Get an inventory entry
    api_response = api_instance.get_user_inventory(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_user_inventory: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_inventory_log**
> PageResourceUserItemLogResource get_user_inventory_log(user_id, id, size=size, page=page)

List the log entries for this inventory entry

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
user_id = 'user_id_example' # str | The id of the inventory owner or 'me' for the logged in user
id = 56 # int | The id of the user inventory
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List the log entries for this inventory entry
    api_response = api_instance.get_user_inventory_log(user_id, id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_user_inventory_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the inventory owner or &#39;me&#39; for the logged in user | 
 **id** | **int**| The id of the user inventory | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUserItemLogResource**](PageResourceUserItemLogResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_inventory**
> PageResourceUserInventoryResource get_users_inventory(inactive=inactive, size=size, page=page, filter_item_name=filter_item_name, filter_item_id=filter_item_id, filter_username=filter_username, filter_group=filter_group, filter_date=filter_date)

List the user inventory entries for all users

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
inactive = false # bool | If true, accepts inactive user inventories (optional) (default to false)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
filter_item_name = 'filter_item_name_example' # str | Filter by items whose name starts with a string (optional)
filter_item_id = 56 # int | Filter by item id (optional)
filter_username = 'filter_username_example' # str | Filter by entries owned by the user with the specified username (optional)
filter_group = 'filter_group_example' # str | Filter by entries owned by the users in a given group, by unique name (optional)
filter_date = 'filter_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the log start date, a unix timestamp in seconds. Can be repeated for a range, eg: GT,123,LT,456  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)

try: 
    # List the user inventory entries for all users
    api_response = api_instance.get_users_inventory(inactive=inactive, size=size, page=page, filter_item_name=filter_item_name, filter_item_id=filter_item_id, filter_username=filter_username, filter_group=filter_group, filter_date=filter_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->get_users_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inactive** | **bool**| If true, accepts inactive user inventories | [optional] [default to false]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **filter_item_name** | **str**| Filter by items whose name starts with a string | [optional] 
 **filter_item_id** | **int**| Filter by item id | [optional] 
 **filter_username** | **str**| Filter by entries owned by the user with the specified username | [optional] 
 **filter_group** | **str**| Filter by entries owned by the users in a given group, by unique name | [optional] 
 **filter_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the log start date, a unix timestamp in seconds. Can be repeated for a range, eg: GT,123,LT,456  Allowed operators: (GT, LT, EQ, GOE, LOE). | [optional] 

### Return type

[**PageResourceUserInventoryResource**](PageResourceUserInventoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_user_entitlement**
> grant_user_entitlement(user_id, grant_request)

Grant an entitlement

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
user_id = 56 # int | The id of the user to grant the entitlement to
grant_request = knetik_cloud.EntitlementGrantRequest() # EntitlementGrantRequest | grantRequest

try: 
    # Grant an entitlement
    api_instance.grant_user_entitlement(user_id, grant_request)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->grant_user_entitlement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user to grant the entitlement to | 
 **grant_request** | [**EntitlementGrantRequest**](EntitlementGrantRequest.md)| grantRequest | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entitlement_item**
> update_entitlement_item(entitlement_id, cascade=cascade, entitlement_item=entitlement_item)

Update an entitlement item

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
entitlement_id = 56 # int | The id of the entitlement
cascade = false # bool | Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values. (optional) (default to false)
entitlement_item = knetik_cloud.EntitlementItem() # EntitlementItem | The entitlement item object (optional)

try: 
    # Update an entitlement item
    api_instance.update_entitlement_item(entitlement_id, cascade=cascade, entitlement_item=entitlement_item)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->update_entitlement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_id** | **int**| The id of the entitlement | 
 **cascade** | **bool**| Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values. | [optional] [default to false]
 **entitlement_item** | [**EntitlementItem**](EntitlementItem.md)| The entitlement item object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entitlement_template**
> ItemTemplateResource update_entitlement_template(id, template=template)

Update an entitlement template

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
id = 'id_example' # str | The id of the template
template = knetik_cloud.ItemTemplateResource() # ItemTemplateResource | The updated template (optional)

try: 
    # Update an entitlement template
    api_response = api_instance.update_entitlement_template(id, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->update_entitlement_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **template** | [**ItemTemplateResource**](ItemTemplateResource.md)| The updated template | [optional] 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_inventory_behavior_data**
> update_user_inventory_behavior_data(user_id, id, data=data)

Set the behavior data for an inventory entry

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
user_id = 56 # int | The id of the user
id = 56 # int | The id of the user inventory
data = NULL # object | The data map (optional)

try: 
    # Set the behavior data for an inventory entry
    api_instance.update_user_inventory_behavior_data(user_id, id, data=data)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->update_user_inventory_behavior_data: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_inventory_expires**
> update_user_inventory_expires(user_id, id, timestamp=timestamp)

Set the expiration date

Will change the current grace period for a subscription but not the bill date (possibly even ending before having the chance to re-bill)

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
user_id = 56 # int | user_id
id = 56 # int | The id of the user inventory
timestamp = 789 # int | The new expiration date as a unix timestamp in seconds. May be null (no body). (optional)

try: 
    # Set the expiration date
    api_instance.update_user_inventory_expires(user_id, id, timestamp=timestamp)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->update_user_inventory_expires: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_inventory_status**
> update_user_inventory_status(user_id, id, inventory_status=inventory_status)

Set the status for an inventory entry

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
user_id = 56 # int | The id of the user
id = 56 # int | The id of the user inventory
inventory_status = 'inventory_status_example' # str | The inventory status object (optional)

try: 
    # Set the status for an inventory entry
    api_instance.update_user_inventory_status(user_id, id, inventory_status=inventory_status)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->update_user_inventory_status: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **use_user_entitlement_item**
> use_user_entitlement_item(user_id, item_id, sku=sku, info=info)

Use an item

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersInventoryApi()
user_id = 'user_id_example' # str | The id of the user to check for or 'me' for logged in user
item_id = 56 # int | The id of the item
sku = 'sku_example' # str | The specific sku of an entitlement_list addition to check entitlement for. This is of very limited and specific use and should generally be left out (optional)
info = 'info_example' # str | Any additional info to add to the log about this use (optional)

try: 
    # Use an item
    api_instance.use_user_entitlement_item(user_id, item_id, sku=sku, info=info)
except ApiException as e:
    print("Exception when calling UsersInventoryApi->use_user_entitlement_item: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

