# knetik_cloud.BRERuleEngineEventsApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_bre_event**](BRERuleEngineEventsApi.md#send_bre_event) | **POST** /bre/events | Fire a new event, based on an existing trigger


# **send_bre_event**
> send_bre_event(bre_event=bre_event)

Fire a new event, based on an existing trigger

Parameters within the event must match names and types from the trigger. Actual rule execution is asynchornous.

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.BRERuleEngineEventsApi()
bre_event = knetik_cloud.BreEvent() # BreEvent | The BRE event object (optional)

try: 
    # Fire a new event, based on an existing trigger
    api_instance.send_bre_event(bre_event=bre_event)
except ApiException as e:
    print("Exception when calling BRERuleEngineEventsApi->send_bre_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bre_event** | [**BreEvent**](BreEvent.md)| The BRE event object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

