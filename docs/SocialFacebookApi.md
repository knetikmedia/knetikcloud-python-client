# knetik_cloud.SocialFacebookApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**link_accounts**](SocialFacebookApi.md#link_accounts) | **POST** /social/facebook/users | Link facebook account


# **link_accounts**
> link_accounts(facebook_token=facebook_token)

Link facebook account

Links the current user account to a facebook account, using the acccess token from facebook. Can also be used to update the access token after it has expired. <br><br><b>Permissions Needed:</b> Non-facebook user token

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
api_instance = knetik_cloud.SocialFacebookApi(knetik_cloud.ApiClient(configuration))
facebook_token = knetik_cloud.FacebookToken() # FacebookToken | The token from facebook (optional)

try: 
    # Link facebook account
    api_instance.link_accounts(facebook_token=facebook_token)
except ApiException as e:
    print("Exception when calling SocialFacebookApi->link_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_token** | [**FacebookToken**](FacebookToken.md)| The token from facebook | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

