# knetik_cloud.UtilBatchApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch**](UtilBatchApi.md#get_batch) | **GET** /batch/{token} | Get batch result with token
[**send_batch**](UtilBatchApi.md#send_batch) | **POST** /batch | Request to run API call given the method, content type, path url, and body of request


# **get_batch**
> list[BatchReturn] get_batch(token)

Get batch result with token

Tokens expire in 24 hours. <br><br><b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.UtilBatchApi(knetik_cloud.ApiClient(configuration))
token = 'token_example' # str | token

try: 
    # Get batch result with token
    api_response = api_instance.get_batch(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilBatchApi->get_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token | 

### Return type

[**list[BatchReturn]**](BatchReturn.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_batch**
> list[BatchReturn] send_batch(batch=batch)

Request to run API call given the method, content type, path url, and body of request

Should the request take longer than one of the alloted timeout parameters, a token will be returned instead, which can be used on the token endpoint in this service. <br><br><b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.UtilBatchApi(knetik_cloud.ApiClient(configuration))
batch = knetik_cloud.Batch() # Batch | The batch object (optional)

try: 
    # Request to run API call given the method, content type, path url, and body of request
    api_response = api_instance.send_batch(batch=batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilBatchApi->send_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch** | [**Batch**](Batch.md)| The batch object | [optional] 

### Return type

[**list[BatchReturn]**](BatchReturn.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

