# swagger_client.LogsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_log_using_post**](LogsApi.md#add_user_log_using_post) | **POST** /audit/logs | Add a new user log entry
[**get_event_log_using_get**](LogsApi.md#get_event_log_using_get) | **GET** /bre/logs/event-log/{id} | Get an existing BRE event log entry by id
[**get_events_logs_using_get**](LogsApi.md#get_events_logs_using_get) | **GET** /bre/logs/event-log | Returns a list of BRE event log entries
[**get_forward_log_using_get**](LogsApi.md#get_forward_log_using_get) | **GET** /bre/logs/forward-log/{id} | Get an existing forward log entry by id
[**get_forward_logs_using_get**](LogsApi.md#get_forward_logs_using_get) | **GET** /bre/logs/forward-log | Returns a list of forward log entries
[**get_user_logs_using_get**](LogsApi.md#get_user_logs_using_get) | **GET** /audit/logs/{id} | Returns a user log entry by id
[**get_user_logs_using_get1**](LogsApi.md#get_user_logs_using_get1) | **GET** /audit/logs | Returns a page of user logs entries


# **add_user_log_using_post**
> add_user_log_using_post(log_entry=log_entry)

Add a new user log entry

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LogsApi()
log_entry = swagger_client.UserActionLog() # UserActionLog | The user log entry to be added (optional)

try: 
    # Add a new user log entry
    api_instance.add_user_log_using_post(log_entry=log_entry)
except ApiException as e:
    print("Exception when calling LogsApi->add_user_log_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_entry** | [**UserActionLog**](UserActionLog.md)| The user log entry to be added | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_log_using_get**
> BreEventLog get_event_log_using_get(id)

Get an existing BRE event log entry by id

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LogsApi()
id = 'id_example' # str | The BRE event log entry id

try: 
    # Get an existing BRE event log entry by id
    api_response = api_instance.get_event_log_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_event_log_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The BRE event log entry id | 

### Return type

[**BreEventLog**](BreEventLog.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_logs_using_get**
> PageResourceBreEventLog get_events_logs_using_get(filter_start_date=filter_start_date, filter_event_name=filter_event_name, size=size, page=page, order=order)

Returns a list of BRE event log entries

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LogsApi()
filter_start_date = 'filter_start_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the event log start date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)
filter_event_name = 'filter_event_name_example' # str | Filter event logs by event name (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:DESC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:DESC)

try: 
    # Returns a list of BRE event log entries
    api_response = api_instance.get_events_logs_using_get(filter_start_date=filter_start_date, filter_event_name=filter_event_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_events_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_start_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the event log start date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). | [optional] 
 **filter_event_name** | **str**| Filter event logs by event name | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:DESC]

### Return type

[**PageResourceBreEventLog**](PageResourceBreEventLog.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forward_log_using_get**
> ForwardLog get_forward_log_using_get(id)

Get an existing forward log entry by id

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LogsApi()
id = 'id_example' # str | The forward log entry id

try: 
    # Get an existing forward log entry by id
    api_response = api_instance.get_forward_log_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_forward_log_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The forward log entry id | 

### Return type

[**ForwardLog**](ForwardLog.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_forward_logs_using_get**
> PageResourceForwardLog get_forward_logs_using_get(filter_start_date=filter_start_date, filter_end_date=filter_end_date, filter_status_code=filter_status_code, size=size, page=page, order=order)

Returns a list of forward log entries

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LogsApi()
filter_start_date = 'filter_start_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the log start date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)
filter_end_date = 'filter_end_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the log end date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)
filter_status_code = 56 # int | Filter forward logs by http status code (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:DESC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:DESC)

try: 
    # Returns a list of forward log entries
    api_response = api_instance.get_forward_logs_using_get(filter_start_date=filter_start_date, filter_end_date=filter_end_date, filter_status_code=filter_status_code, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_forward_logs_using_get: %s\n" % e)
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

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_logs_using_get**
> UserActionLog get_user_logs_using_get(id)

Returns a user log entry by id

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LogsApi()
id = 'id_example' # str | The user log entry id

try: 
    # Returns a user log entry by id
    api_response = api_instance.get_user_logs_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_user_logs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user log entry id | 

### Return type

[**UserActionLog**](UserActionLog.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_logs_using_get1**
> PageResourceUserActionLog get_user_logs_using_get1(filter_user=filter_user, filter_action_name=filter_action_name, size=size, page=page)

Returns a page of user logs entries

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.LogsApi()
filter_user = 56 # int | Filter for actions taken by a specific user by id (optional)
filter_action_name = 'filter_action_name_example' # str | Filter for actions of a specific name (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of user logs entries
    api_response = api_instance.get_user_logs_using_get1(filter_user=filter_user, filter_action_name=filter_action_name, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsApi->get_user_logs_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_user** | **int**| Filter for actions taken by a specific user by id | [optional] 
 **filter_action_name** | **str**| Filter for actions of a specific name | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUserActionLog**](PageResourceUserActionLog.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
