# knetik_cloud.SocialGoogleApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**link_accounts1**](SocialGoogleApi.md#link_accounts1) | **POST** /social/google/users | Link google account


# **link_accounts1**
> link_accounts1(google_token=google_token)

Link google account

Links the current user account to a google account, using the acccess token from google. Can also be used to update the access token after it has expired.

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.SocialGoogleApi()
google_token = knetik_cloud.GoogleToken() # GoogleToken | The token from google (optional)

try: 
    # Link google account
    api_instance.link_accounts1(google_token=google_token)
except ApiException as e:
    print("Exception when calling SocialGoogleApi->link_accounts1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_token** | [**GoogleToken**](GoogleToken.md)| The token from google | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

