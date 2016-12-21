# swagger_client.BRERuleEngineTriggersApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trigger_using_post**](BRERuleEngineTriggersApi.md#create_trigger_using_post) | **POST** /bre/triggers | Create a trigger
[**delete_trigger_using_delete**](BRERuleEngineTriggersApi.md#delete_trigger_using_delete) | **DELETE** /bre/triggers/{event_name} | Delete a trigger
[**get_trigger_using_get**](BRERuleEngineTriggersApi.md#get_trigger_using_get) | **GET** /bre/triggers/{event_name} | Get a single trigger
[**get_triggers_using_get**](BRERuleEngineTriggersApi.md#get_triggers_using_get) | **GET** /bre/triggers | List triggers
[**update_trigger_using_put**](BRERuleEngineTriggersApi.md#update_trigger_using_put) | **PUT** /bre/triggers/{event_name} | Update a trigger


# **create_trigger_using_post**
> BreTriggerResource create_trigger_using_post(bre_trigger_resource=bre_trigger_resource)

Create a trigger

Customer added triggers will not be fired automatically or have rules associated with them by default. Custom rules must be added to get use from the trigger and it must then be fired from the outside. See the Bre Event services

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineTriggersApi()
bre_trigger_resource = swagger_client.BreTriggerResource() # BreTriggerResource | The BRE trigger resource object (optional)

try: 
    # Create a trigger
    api_response = api_instance.create_trigger_using_post(bre_trigger_resource=bre_trigger_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineTriggersApi->create_trigger_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bre_trigger_resource** | [**BreTriggerResource**](BreTriggerResource.md)| The BRE trigger resource object | [optional] 

### Return type

[**BreTriggerResource**](BreTriggerResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trigger_using_delete**
> delete_trigger_using_delete(event_name)

Delete a trigger

May fail if there are existing rules against it. Cannot delete core triggers

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineTriggersApi()
event_name = 'event_name_example' # str | The trigger event name

try: 
    # Delete a trigger
    api_instance.delete_trigger_using_delete(event_name)
except ApiException as e:
    print("Exception when calling BRERuleEngineTriggersApi->delete_trigger_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| The trigger event name | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trigger_using_get**
> BreTriggerResource get_trigger_using_get(event_name)

Get a single trigger

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineTriggersApi()
event_name = 'event_name_example' # str | The trigger event name

try: 
    # Get a single trigger
    api_response = api_instance.get_trigger_using_get(event_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineTriggersApi->get_trigger_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| The trigger event name | 

### Return type

[**BreTriggerResource**](BreTriggerResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_triggers_using_get**
> PageResourceBreTriggerResource get_triggers_using_get(filter_system=filter_system, filter_category=filter_category, filter_name=filter_name, size=size, page=page)

List triggers

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineTriggersApi()
filter_system = true # bool | Filter for triggers that are system triggers when true, or not when false. Leave off for both mixed (optional)
filter_category = 'filter_category_example' # str | Filter for triggers that are within a specific category (optional)
filter_name = 'filter_name_example' # str | Filter for triggers that have names containing the given string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List triggers
    api_response = api_instance.get_triggers_using_get(filter_system=filter_system, filter_category=filter_category, filter_name=filter_name, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineTriggersApi->get_triggers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_system** | **bool**| Filter for triggers that are system triggers when true, or not when false. Leave off for both mixed | [optional] 
 **filter_category** | **str**| Filter for triggers that are within a specific category | [optional] 
 **filter_name** | **str**| Filter for triggers that have names containing the given string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceBreTriggerResource**](PageResourceBreTriggerResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_trigger_using_put**
> update_trigger_using_put(event_name, bre_trigger_resource=bre_trigger_resource)

Update a trigger

May fail if new parameters mismatch requirements of existing rules. Cannot update core triggers

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineTriggersApi()
event_name = 'event_name_example' # str | The trigger event name
bre_trigger_resource = swagger_client.BreTriggerResource() # BreTriggerResource | The BRE trigger resource object (optional)

try: 
    # Update a trigger
    api_instance.update_trigger_using_put(event_name, bre_trigger_resource=bre_trigger_resource)
except ApiException as e:
    print("Exception when calling BRERuleEngineTriggersApi->update_trigger_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| The trigger event name | 
 **bre_trigger_resource** | [**BreTriggerResource**](BreTriggerResource.md)| The BRE trigger resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
