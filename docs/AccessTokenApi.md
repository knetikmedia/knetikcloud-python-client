# knetik_cloud.AccessTokenApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_o_auth_token**](AccessTokenApi.md#get_o_auth_token) | **POST** /oauth/token | Get access token


# **get_o_auth_token**
> OAuth2Resource get_o_auth_token(grant_type, client_id, client_secret=client_secret, username=username, password=password)

Get access token

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.AccessTokenApi()
grant_type = 'client_credentials' # str | Grant type (default to client_credentials)
client_id = 'knetik' # str | The id of the client (default to knetik)
client_secret = 'client_secret_example' # str | The secret key of the client.  Used only with a grant_type of client_credentials (optional)
username = 'username_example' # str | The username of the client.  Used only with a grant_type of password (optional)
password = 'password_example' # str | The password of the client.  Used only with a grant_type of password (optional)

try: 
    # Get access token
    api_response = api_instance.get_o_auth_token(grant_type, client_id, client_secret=client_secret, username=username, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessTokenApi->get_o_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Grant type | [default to client_credentials]
 **client_id** | **str**| The id of the client | [default to knetik]
 **client_secret** | **str**| The secret key of the client.  Used only with a grant_type of client_credentials | [optional] 
 **username** | **str**| The username of the client.  Used only with a grant_type of password | [optional] 
 **password** | **str**| The password of the client.  Used only with a grant_type of password | [optional] 

### Return type

[**OAuth2Resource**](OAuth2Resource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

