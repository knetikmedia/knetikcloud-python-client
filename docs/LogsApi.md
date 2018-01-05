# knetik_cloud.LogsApi

All URIs are relative to *https://devsandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_log**](LogsApi.md#add_user_log) | **POST** /audit/logs | Add a user log entry
[**get_bre_event_log**](LogsApi.md#get_bre_event_log) | **GET** /bre/logs/event-log/{id} | Get an existing BRE event log entry by id
[**get_bre_event_logs**](LogsApi.md#get_bre_event_logs) | **GET** /bre/logs/event-log | Returns a list of BRE event log entries
[**get_bre_forward_log**](LogsApi.md#get_bre_forward_log) | **GET** /bre/logs/forward-log/{id} | Get an existing forward log entry by id
[**get_bre_forward_logs**](LogsApi.md#get_bre_forward_logs) | **GET** /bre/logs/forward-log | Returns a list of forward log entries
[**get_user_log**](LogsApi.md#get_user_log) | **GET** /audit/logs/{id} | Returns a user log entry by id
[**get_user_logs**](LogsApi.md#get_user_logs) | **GET** /audit/logs | Returns a page of user logs entries


# **add_user_log**
> add_user_log(log_entry=log_entry)

Add a user log entry

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
api_instance = knetik_cloud.LogsApi(knetik_cloud.ApiClient(configuration))
log_entry = knetik_cloud.UserActionLog() # UserActionLog | The user log entry to be added (optional)

try: 
    # Add a user log entry
    api_instance.add_user_log(log_entry=log_entry)
except ApiException as e:
    print("Exception when calling LogsApi->add_user_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_entry** | [**UserActionLog**](UserActionLog.md)| The user log entry to be added | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_event_log**
> BreEventLog get_bre_event_log(id)

Get an existing BRE event log entry by id

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
api_instance = knetik_cloud.LogsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The BRE event log entry id

try: 
    # Get an existing BRE event log entry by id
    api_response = api_instance.get_bre_event_log(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_bre_event_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The BRE event log entry id | 

### Return type

[**BreEventLog**](BreEventLog.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_event_logs**
> PageResourceBreEventLog get_bre_event_logs(filter_start_date=filter_start_date, filter_event_name=filter_event_name, filter_event_id=filter_event_id, size=size, page=page, order=order)

Returns a list of BRE event log entries

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
api_instance = knetik_cloud.LogsApi(knetik_cloud.ApiClient(configuration))
filter_start_date = 'filter_start_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the event log start date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)
filter_event_name = 'filter_event_name_example' # str | Filter event logs by event name (optional)
filter_event_id = 'filter_event_id_example' # str | Filter event logs by request id (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:DESC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:DESC)

try: 
    # Returns a list of BRE event log entries
    api_response = api_instance.get_bre_event_logs(filter_start_date=filter_start_date, filter_event_name=filter_event_name, filter_event_id=filter_event_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_bre_event_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_start_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the event log start date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). | [optional] 
 **filter_event_name** | **str**| Filter event logs by event name | [optional] 
 **filter_event_id** | **str**| Filter event logs by request id | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:DESC]

### Return type

[**PageResourceBreEventLog**](PageResourceBreEventLog.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_forward_log**
> ForwardLog get_bre_forward_log(id)

Get an existing forward log entry by id

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
api_instance = knetik_cloud.LogsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The forward log entry id

try: 
    # Get an existing forward log entry by id
    api_response = api_instance.get_bre_forward_log(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_bre_forward_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The forward log entry id | 

### Return type

[**ForwardLog**](ForwardLog.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_forward_logs**
> PageResourceForwardLog get_bre_forward_logs(filter_start_date=filter_start_date, filter_end_date=filter_end_date, filter_status_code=filter_status_code, size=size, page=page, order=order)

Returns a list of forward log entries

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
api_instance = knetik_cloud.LogsApi(knetik_cloud.ApiClient(configuration))
filter_start_date = 'filter_start_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the log start date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)
filter_end_date = 'filter_end_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the log end date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)
filter_status_code = 56 # int | Filter forward logs by http status code (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:DESC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:DESC)

try: 
    # Returns a list of forward log entries
    api_response = api_instance.get_bre_forward_logs(filter_start_date=filter_start_date, filter_end_date=filter_end_date, filter_status_code=filter_status_code, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_bre_forward_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_start_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the log start date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). | [optional] 
 **filter_end_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the log end date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). | [optional] 
 **filter_status_code** | **int**| Filter forward logs by http status code | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:DESC]

### Return type

[**PageResourceForwardLog**](PageResourceForwardLog.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_log**
> UserActionLog get_user_log(id)

Returns a user log entry by id

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
api_instance = knetik_cloud.LogsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The user log entry id

try: 
    # Returns a user log entry by id
    api_response = api_instance.get_user_log(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_user_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user log entry id | 

### Return type

[**UserActionLog**](UserActionLog.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_logs**
> PageResourceUserActionLog get_user_logs(filter_user=filter_user, filter_action_name=filter_action_name, size=size, page=page, order=order)

Returns a page of user logs entries

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
api_instance = knetik_cloud.LogsApi(knetik_cloud.ApiClient(configuration))
filter_user = 56 # int | Filter for actions taken by a specific user by id (optional)
filter_action_name = 'filter_action_name_example' # str | Filter for actions of a specific name (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'timestamp:DESC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to timestamp:DESC)

try: 
    # Returns a page of user logs entries
    api_response = api_instance.get_user_logs(filter_user=filter_user, filter_action_name=filter_action_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_user_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_user** | **int**| Filter for actions taken by a specific user by id | [optional] 
 **filter_action_name** | **str**| Filter for actions of a specific name | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to timestamp:DESC]

### Return type

[**PageResourceUserActionLog**](PageResourceUserActionLog.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

