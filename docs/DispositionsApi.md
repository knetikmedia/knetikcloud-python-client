# swagger_client.DispositionsApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_disposition_using_post**](DispositionsApi.md#add_disposition_using_post) | **POST** /dispositions | Add a new disposition. 
[**delete_disposition_using_delete**](DispositionsApi.md#delete_disposition_using_delete) | **DELETE** /dispositions/{id} | Delete a disposition
[**get_disposition_count_using_get**](DispositionsApi.md#get_disposition_count_using_get) | **GET** /dispositions/count | Returns a list of disposition counts
[**get_disposition_using_get**](DispositionsApi.md#get_disposition_using_get) | **GET** /dispositions/{id} | Returns a disposition
[**get_dispositions_using_get**](DispositionsApi.md#get_dispositions_using_get) | **GET** /dispositions | Returns a page of dispositions


# **add_disposition_using_post**
> DispositionResource add_disposition_using_post(disposition=disposition)

Add a new disposition. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DispositionsApi()
disposition = swagger_client.DispositionResource() # DispositionResource | The new disposition record (optional)

try: 
    # Add a new disposition. 
    api_response = api_instance.add_disposition_using_post(disposition=disposition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispositionsApi->add_disposition_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disposition** | [**DispositionResource**](DispositionResource.md)| The new disposition record | [optional] 

### Return type

[**DispositionResource**](DispositionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disposition_using_delete**
> delete_disposition_using_delete(id)

Delete a disposition

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DispositionsApi()
id = 789 # int | The id of the disposition record

try: 
    # Delete a disposition
    api_instance.delete_disposition_using_delete(id)
except ApiException as e:
    print("Exception when calling DispositionsApi->delete_disposition_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the disposition record | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disposition_count_using_get**
> list[DispositionCount] get_disposition_count_using_get(filter_context=filter_context, filter_owner=filter_owner)

Returns a list of disposition counts

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DispositionsApi()
filter_context = 'filter_context_example' # str | Filter for dispositions within a context type (games, articles, polls, etc). Optionally with a specific id like filter_context=video:47 (optional)
filter_owner = 'filter_owner_example' # str | Filter for dispositions from a specific user by id or 'me' (optional)

try: 
    # Returns a list of disposition counts
    api_response = api_instance.get_disposition_count_using_get(filter_context=filter_context, filter_owner=filter_owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispositionsApi->get_disposition_count_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_context** | **str**| Filter for dispositions within a context type (games, articles, polls, etc). Optionally with a specific id like filter_context&#x3D;video:47 | [optional] 
 **filter_owner** | **str**| Filter for dispositions from a specific user by id or &#39;me&#39; | [optional] 

### Return type

[**list[DispositionCount]**](DispositionCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disposition_using_get**
> DispositionResource get_disposition_using_get(id)

Returns a disposition

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DispositionsApi()
id = 789 # int | The id of the disposition record

try: 
    # Returns a disposition
    api_response = api_instance.get_disposition_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispositionsApi->get_disposition_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the disposition record | 

### Return type

[**DispositionResource**](DispositionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispositions_using_get**
> PageDispositionResource get_dispositions_using_get(filter_context=filter_context, filter_owner=filter_owner, size=size, page=page, order=order)

Returns a page of dispositions

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DispositionsApi()
filter_context = 'filter_context_example' # str | Filter for dispositions within a context type (games, articles, polls, etc). Optionally with a specific id like filter_context=video:47 (optional)
filter_owner = 'filter_owner_example' # str | Filter for dispositions from a specific user by id or 'me' (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # Returns a page of dispositions
    api_response = api_instance.get_dispositions_using_get(filter_context=filter_context, filter_owner=filter_owner, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispositionsApi->get_dispositions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_context** | **str**| Filter for dispositions within a context type (games, articles, polls, etc). Optionally with a specific id like filter_context&#x3D;video:47 | [optional] 
 **filter_owner** | **str**| Filter for dispositions from a specific user by id or &#39;me&#39; | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageDispositionResource**](PageDispositionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

