# swagger_client.FulfillmentApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fulfillment_type_using_post**](FulfillmentApi.md#create_fulfillment_type_using_post) | **POST** /store/fulfillment/types | Create a fulfillment type
[**delete_fulfillment_type_using_delete**](FulfillmentApi.md#delete_fulfillment_type_using_delete) | **DELETE** /store/fulfillment/types/{id} | Delete a fulfillment type
[**get_fulfillment_type_using_get**](FulfillmentApi.md#get_fulfillment_type_using_get) | **GET** /store/fulfillment/types/{id} | Get a single fulfillment type
[**get_fulfillments_using_get**](FulfillmentApi.md#get_fulfillments_using_get) | **GET** /store/fulfillment/types | List and search fulfillment types
[**update_fulfillment_type_using_put**](FulfillmentApi.md#update_fulfillment_type_using_put) | **PUT** /store/fulfillment/types/{id} | Update a fulfillment type


# **create_fulfillment_type_using_post**
> FulfillmentType create_fulfillment_type_using_post(type=type)

Create a fulfillment type

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
api_instance = swagger_client.FulfillmentApi()
type = swagger_client.FulfillmentType() # FulfillmentType | The fulfillment type (optional)

try: 
    # Create a fulfillment type
    api_response = api_instance.create_fulfillment_type_using_post(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentApi->create_fulfillment_type_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**FulfillmentType**](FulfillmentType.md)| The fulfillment type | [optional] 

### Return type

[**FulfillmentType**](FulfillmentType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_type_using_delete**
> delete_fulfillment_type_using_delete(id)

Delete a fulfillment type

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
api_instance = swagger_client.FulfillmentApi()
id = 56 # int | The id

try: 
    # Delete a fulfillment type
    api_instance.delete_fulfillment_type_using_delete(id)
except ApiException as e:
    print("Exception when calling FulfillmentApi->delete_fulfillment_type_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_type_using_get**
> FulfillmentType get_fulfillment_type_using_get(id)

Get a single fulfillment type

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FulfillmentApi()
id = 56 # int | The id

try: 
    # Get a single fulfillment type
    api_response = api_instance.get_fulfillment_type_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentApi->get_fulfillment_type_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id | 

### Return type

[**FulfillmentType**](FulfillmentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillments_using_get**
> PageFulfillmentType get_fulfillments_using_get(size=size, page=page, order=order)

List and search fulfillment types

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FulfillmentApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search fulfillment types
    api_response = api_instance.get_fulfillments_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentApi->get_fulfillments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageFulfillmentType**](PageFulfillmentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fulfillment_type_using_put**
> update_fulfillment_type_using_put(id, fulfillment_type=fulfillment_type)

Update a fulfillment type

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
api_instance = swagger_client.FulfillmentApi()
id = 56 # int | The id
fulfillment_type = swagger_client.FulfillmentType() # FulfillmentType | The fulfillment type (optional)

try: 
    # Update a fulfillment type
    api_instance.update_fulfillment_type_using_put(id, fulfillment_type=fulfillment_type)
except ApiException as e:
    print("Exception when calling FulfillmentApi->update_fulfillment_type_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id | 
 **fulfillment_type** | [**FulfillmentType**](FulfillmentType.md)| The fulfillment type | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

