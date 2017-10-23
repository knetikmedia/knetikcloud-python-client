# knetik_cloud.MediaModerationApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_flag**](MediaModerationApi.md#add_flag) | **POST** /moderation/flags | Add a flag
[**delete_flag**](MediaModerationApi.md#delete_flag) | **DELETE** /moderation/flags | Delete a flag
[**get_flags**](MediaModerationApi.md#get_flags) | **GET** /moderation/flags | Returns a page of flags
[**get_moderation_report**](MediaModerationApi.md#get_moderation_report) | **GET** /moderation/reports/{id} | Get a flag report
[**get_moderation_reports**](MediaModerationApi.md#get_moderation_reports) | **GET** /moderation/reports | Returns a page of flag reports
[**update_moderation_report**](MediaModerationApi.md#update_moderation_report) | **PUT** /moderation/reports/{id} | Update a flag report


# **add_flag**
> FlagResource add_flag(flag_resource=flag_resource)

Add a flag

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
api_instance = knetik_cloud.MediaModerationApi(knetik_cloud.ApiClient(configuration))
flag_resource = knetik_cloud.FlagResource() # FlagResource | The flag resource object (optional)

try: 
    # Add a flag
    api_response = api_instance.add_flag(flag_resource=flag_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaModerationApi->add_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_resource** | [**FlagResource**](FlagResource.md)| The flag resource object | [optional] 

### Return type

[**FlagResource**](FlagResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flag**
> delete_flag(context_name=context_name, context_id=context_id, user_id=user_id)

Delete a flag

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
api_instance = knetik_cloud.MediaModerationApi(knetik_cloud.ApiClient(configuration))
context_name = 'context_name_example' # str | The name of the context (optional)
context_id = 'context_id_example' # str | The id of the context (optional)
user_id = 56 # int | The id of the user (optional)

try: 
    # Delete a flag
    api_instance.delete_flag(context_name=context_name, context_id=context_id, user_id=user_id)
except ApiException as e:
    print("Exception when calling MediaModerationApi->delete_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_name** | **str**| The name of the context | [optional] 
 **context_id** | **str**| The id of the context | [optional] 
 **user_id** | **int**| The id of the user | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flags**
> PageResourceFlagResource get_flags(filter_context=filter_context, filter_context_id=filter_context_id, filter_user_id=filter_user_id, size=size, page=page)

Returns a page of flags

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
api_instance = knetik_cloud.MediaModerationApi(knetik_cloud.ApiClient(configuration))
filter_context = 'filter_context_example' # str | Filter by flag context (optional)
filter_context_id = 'filter_context_id_example' # str | Filter by flag context ID (optional)
filter_user_id = 56 # int | Filter by user ID (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of flags
    api_response = api_instance.get_flags(filter_context=filter_context, filter_context_id=filter_context_id, filter_user_id=filter_user_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaModerationApi->get_flags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_context** | **str**| Filter by flag context | [optional] 
 **filter_context_id** | **str**| Filter by flag context ID | [optional] 
 **filter_user_id** | **int**| Filter by user ID | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceFlagResource**](PageResourceFlagResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_moderation_report**
> FlagReportResource get_moderation_report(id)

Get a flag report

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
api_instance = knetik_cloud.MediaModerationApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The flag report id

try: 
    # Get a flag report
    api_response = api_instance.get_moderation_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaModerationApi->get_moderation_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The flag report id | 

### Return type

[**FlagReportResource**](FlagReportResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_moderation_reports**
> PageResourceFlagReportResource get_moderation_reports(exclude_resolved=exclude_resolved, filter_context=filter_context, filter_context_id=filter_context_id, size=size, page=page)

Returns a page of flag reports

Context can be either a free-form string or a pre-defined context name

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
api_instance = knetik_cloud.MediaModerationApi(knetik_cloud.ApiClient(configuration))
exclude_resolved = true # bool | Ignore resolved context (optional) (default to true)
filter_context = 'filter_context_example' # str | Filter by moderation context (optional)
filter_context_id = 'filter_context_id_example' # str | Filter by moderation context ID (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of flag reports
    api_response = api_instance.get_moderation_reports(exclude_resolved=exclude_resolved, filter_context=filter_context, filter_context_id=filter_context_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaModerationApi->get_moderation_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_resolved** | **bool**| Ignore resolved context | [optional] [default to true]
 **filter_context** | **str**| Filter by moderation context | [optional] 
 **filter_context_id** | **str**| Filter by moderation context ID | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceFlagReportResource**](PageResourceFlagReportResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_moderation_report**
> update_moderation_report(id, flag_report_resource=flag_report_resource)

Update a flag report

Lets you set the resolution of a report. Resolution types is {banned,ignore} in case of 'banned' you will need to pass the reason.

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
api_instance = knetik_cloud.MediaModerationApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The flag report id
flag_report_resource = knetik_cloud.FlagReportResource() # FlagReportResource | The new flag report (optional)

try: 
    # Update a flag report
    api_instance.update_moderation_report(id, flag_report_resource=flag_report_resource)
except ApiException as e:
    print("Exception when calling MediaModerationApi->update_moderation_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The flag report id | 
 **flag_report_resource** | [**FlagReportResource**](FlagReportResource.md)| The new flag report | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

