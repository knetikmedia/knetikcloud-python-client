# swagger_client.MediaModerationApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_flag_report_using_get**](MediaModerationApi.md#get_flag_report_using_get) | **GET** /moderation/reports/{id} | Get a flag report
[**get_flags_report_using_get**](MediaModerationApi.md#get_flags_report_using_get) | **GET** /moderation/reports | Returns a page of flag reports
[**set_flag_resolution_using_put**](MediaModerationApi.md#set_flag_resolution_using_put) | **PUT** /moderation/reports/{id} | Update a flag report


# **get_flag_report_using_get**
> get_flag_report_using_get(id)

Get a flag report

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaModerationApi()
id = 789 # int | The flag report id

try: 
    # Get a flag report
    api_instance.get_flag_report_using_get(id)
except ApiException as e:
    print("Exception when calling MediaModerationApi->get_flag_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The flag report id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flags_report_using_get**
> PageFlagReportResource get_flags_report_using_get(exclude_resolved=exclude_resolved, filter_context=filter_context, size=size, page=page)

Returns a page of flag reports

Context can be either a free-form string or a pre-defined context name

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaModerationApi()
exclude_resolved = true # bool | Ignore resolved context (optional) (default to true)
filter_context = 'filter_context_example' # str | Filter by moderation context (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of flag reports
    api_response = api_instance.get_flags_report_using_get(exclude_resolved=exclude_resolved, filter_context=filter_context, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaModerationApi->get_flags_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_resolved** | **bool**| Ignore resolved context | [optional] [default to true]
 **filter_context** | **str**| Filter by moderation context | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageFlagReportResource**](PageFlagReportResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_flag_resolution_using_put**
> set_flag_resolution_using_put(id, flag_report_resource=flag_report_resource)

Update a flag report

Lets you set the resolution of a report. Resolution types is {banned,ignore} in case of 'banned' you will need to pass the reason.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaModerationApi()
id = 789 # int | The flag report id
flag_report_resource = swagger_client.FlagReportResource() # FlagReportResource | The new flag report (optional)

try: 
    # Update a flag report
    api_instance.set_flag_resolution_using_put(id, flag_report_resource=flag_report_resource)
except ApiException as e:
    print("Exception when calling MediaModerationApi->set_flag_resolution_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The flag report id | 
 **flag_report_resource** | [**FlagReportResource**](FlagReportResource.md)| The new flag report | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

