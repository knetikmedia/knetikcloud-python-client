# knetik_cloud.RuleEngineEventsApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_bre_event**](RuleEngineEventsApi.md#send_bre_event) | **POST** /bre/events | Fire a new event, based on an existing trigger


# **send_bre_event**
> str send_bre_event(bre_event=bre_event)

Fire a new event, based on an existing trigger

Parameters within the event must match names and types from the trigger. Actual rule execution is asynchornous.  Returns request id, which will be used as the event id. <br><br><b>Permissions Needed:</b> BRE_RULE_ENGINE_EVENTS_USER

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
api_instance = knetik_cloud.RuleEngineEventsApi(knetik_cloud.ApiClient(configuration))
bre_event = knetik_cloud.BreEvent() # BreEvent | The BRE event object (optional)

try: 
    # Fire a new event, based on an existing trigger
    api_response = api_instance.send_bre_event(bre_event=bre_event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RuleEngineEventsApi->send_bre_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bre_event** | [**BreEvent**](BreEvent.md)| The BRE event object | [optional] 

### Return type

**str**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

