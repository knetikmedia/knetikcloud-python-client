# knetik_cloud.DispositionsApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_disposition**](DispositionsApi.md#add_disposition) | **POST** /dispositions | Add a new disposition
[**delete_disposition**](DispositionsApi.md#delete_disposition) | **DELETE** /dispositions/{id} | Delete a disposition
[**get_disposition**](DispositionsApi.md#get_disposition) | **GET** /dispositions/{id} | Returns a disposition
[**get_disposition_counts**](DispositionsApi.md#get_disposition_counts) | **GET** /dispositions/count | Returns a list of disposition counts
[**get_dispositions**](DispositionsApi.md#get_dispositions) | **GET** /dispositions | Returns a page of dispositions


# **add_disposition**
> DispositionResource add_disposition(disposition=disposition)

Add a new disposition

<b>Permissions Needed:</b> DISPOSITIONS_USER and user, or DISPOSITIONS_ADMIN

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
api_instance = knetik_cloud.DispositionsApi(knetik_cloud.ApiClient(configuration))
disposition = knetik_cloud.DispositionResource() # DispositionResource | The new disposition record (optional)

try: 
    # Add a new disposition
    api_response = api_instance.add_disposition(disposition=disposition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispositionsApi->add_disposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disposition** | [**DispositionResource**](DispositionResource.md)| The new disposition record | [optional] 

### Return type

[**DispositionResource**](DispositionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disposition**
> delete_disposition(id)

Delete a disposition

<b>Permissions Needed:</b> DISPOSITIONS_USER and owner, or DISPOSITIONS_ADMIN

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
api_instance = knetik_cloud.DispositionsApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The id of the disposition record

try: 
    # Delete a disposition
    api_instance.delete_disposition(id)
except ApiException as e:
    print("Exception when calling DispositionsApi->delete_disposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the disposition record | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disposition**
> DispositionResource get_disposition(id)

Returns a disposition

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
api_instance = knetik_cloud.DispositionsApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The id of the disposition record

try: 
    # Returns a disposition
    api_response = api_instance.get_disposition(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispositionsApi->get_disposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the disposition record | 

### Return type

[**DispositionResource**](DispositionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disposition_counts**
> list[DispositionCount] get_disposition_counts(filter_context=filter_context, filter_owner=filter_owner)

Returns a list of disposition counts

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
api_instance = knetik_cloud.DispositionsApi(knetik_cloud.ApiClient(configuration))
filter_context = 'filter_context_example' # str | Filter for dispositions within a context type (games, articles, polls, etc). Optionally with a specific id like filter_context=video:47 (optional)
filter_owner = 'filter_owner_example' # str | Filter for dispositions from a specific user by id or 'me' (optional)

try: 
    # Returns a list of disposition counts
    api_response = api_instance.get_disposition_counts(filter_context=filter_context, filter_owner=filter_owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispositionsApi->get_disposition_counts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_context** | **str**| Filter for dispositions within a context type (games, articles, polls, etc). Optionally with a specific id like filter_context&#x3D;video:47 | [optional] 
 **filter_owner** | **str**| Filter for dispositions from a specific user by id or &#39;me&#39; | [optional] 

### Return type

[**list[DispositionCount]**](DispositionCount.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispositions**
> PageResourceDispositionResource get_dispositions(filter_context=filter_context, filter_owner=filter_owner, size=size, page=page, order=order)

Returns a page of dispositions

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
api_instance = knetik_cloud.DispositionsApi(knetik_cloud.ApiClient(configuration))
filter_context = 'filter_context_example' # str | Filter for dispositions within a context type (games, articles, polls, etc). Optionally with a specific id like filter_context=video:47 (optional)
filter_owner = 'filter_owner_example' # str | Filter for dispositions from a specific user by id or 'me' (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Returns a page of dispositions
    api_response = api_instance.get_dispositions(filter_context=filter_context, filter_owner=filter_owner, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispositionsApi->get_dispositions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_context** | **str**| Filter for dispositions within a context type (games, articles, polls, etc). Optionally with a specific id like filter_context&#x3D;video:47 | [optional] 
 **filter_owner** | **str**| Filter for dispositions from a specific user by id or &#39;me&#39; | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceDispositionResource**](PageResourceDispositionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

