# swagger_client.SearchApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**external_add_using_post**](SearchApi.md#external_add_using_post) | **POST** /search/index/{type}/{id} | Add a new object to an index
[**external_delete_all_using_delete**](SearchApi.md#external_delete_all_using_delete) | **DELETE** /search/index/{type} | Delete all objects in an index
[**external_delete_using_delete**](SearchApi.md#external_delete_using_delete) | **DELETE** /search/index/{type}/{id} | Delete an object
[**external_register_using_post**](SearchApi.md#external_register_using_post) | **POST** /search/mappings | Register reference mappings
[**search_using_post**](SearchApi.md#search_using_post) | **POST** /search/index/{type} | Search an index


# **external_add_using_post**
> external_add_using_post(type, id, object=object)

Add a new object to an index

Mainly intended for internal use.

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
api_instance = swagger_client.SearchApi()
type = 'type_example' # str | The index type
id = 'id_example' # str | The ID of the object
object = NULL # object | The object to add (optional)

try: 
    # Add a new object to an index
    api_instance.external_add_using_post(type, id, object=object)
except ApiException as e:
    print("Exception when calling SearchApi->external_add_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The index type | 
 **id** | **str**| The ID of the object | 
 **object** | **object**| The object to add | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_delete_all_using_delete**
> external_delete_all_using_delete(type)

Delete all objects in an index

Mainly intended for internal use

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
api_instance = swagger_client.SearchApi()
type = 'type_example' # str | The index type

try: 
    # Delete all objects in an index
    api_instance.external_delete_all_using_delete(type)
except ApiException as e:
    print("Exception when calling SearchApi->external_delete_all_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The index type | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_delete_using_delete**
> external_delete_using_delete(type, id)

Delete an object

Mainly intended for internal use. Requires SEARCH_ADMIN.

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
api_instance = swagger_client.SearchApi()
type = 'type_example' # str | The index type
id = 'id_example' # str | The ID of the object to delete

try: 
    # Delete an object
    api_instance.external_delete_using_delete(type, id)
except ApiException as e:
    print("Exception when calling SearchApi->external_delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The index type | 
 **id** | **str**| The ID of the object to delete | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **external_register_using_post**
> external_register_using_post(mappings=mappings)

Register reference mappings

Add a new type mapping to connect data from one index to another, or discover an exsting one. Mainly intended for internal use.

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
api_instance = swagger_client.SearchApi()
mappings = [swagger_client.SearchReferenceMapping()] # list[SearchReferenceMapping] | The mappings to add (optional)

try: 
    # Register reference mappings
    api_instance.external_register_using_post(mappings=mappings)
except ApiException as e:
    print("Exception when calling SearchApi->external_register_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mappings** | [**list[SearchReferenceMapping]**](SearchReferenceMapping.md)| The mappings to add | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_using_post**
> PageMapstringobject search_using_post(type, query=query, size=size, page=page)

Search an index

The body is an ElasticSearch query in JSON format. Please see their <a href='https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html'>documentation</a> for details on the format and search options. The searchable object's format depends on on the type. See individual search endpoints on other resources for details on their format.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SearchApi()
type = 'type_example' # str | The index type
query = NULL # object | The query to be used for the search (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Search an index
    api_response = api_instance.search_using_post(type, query=query, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The index type | 
 **query** | **object**| The query to be used for the search | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageMapstringobject**](PageMapstringobject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

