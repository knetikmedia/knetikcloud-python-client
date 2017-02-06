# swagger_client.ActivitiesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity**](ActivitiesApi.md#create_activity) | **POST** /activities | Create an activity
[**create_activity_occurrence**](ActivitiesApi.md#create_activity_occurrence) | **POST** /activity-occurrences | Create a new activity occurrence
[**delete_activity**](ActivitiesApi.md#delete_activity) | **DELETE** /activities/{id} | Delete an activity
[**get_activities**](ActivitiesApi.md#get_activities) | **GET** /activities | List activity definitions
[**get_activity**](ActivitiesApi.md#get_activity) | **GET** /activities/{id} | Get a single activity
[**set_activity_occurrence_results**](ActivitiesApi.md#set_activity_occurrence_results) | **POST** /activity-occurrences/{activity_occurrence_id}/results | Sets the status of an activity occurrence to FINISHED and logs metrics
[**update_activity**](ActivitiesApi.md#update_activity) | **PUT** /activities/{id} | Update an activity
[**update_activity_occurrence**](ActivitiesApi.md#update_activity_occurrence) | **PUT** /activity-occurrences/{activity_occurrence_id}/status | Updated the status of an activity occurrence


# **create_activity**
> ActivityResource create_activity(activity_resource=activity_resource)

Create an activity

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
api_instance = swagger_client.ActivitiesApi()
activity_resource = swagger_client.ActivityResource() # ActivityResource | The activity resource object (optional)

try: 
    # Create an activity
    api_response = api_instance.create_activity(activity_resource=activity_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->create_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_resource** | [**ActivityResource**](ActivityResource.md)| The activity resource object | [optional] 

### Return type

[**ActivityResource**](ActivityResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity_occurrence**
> ActivityOccurrenceResource create_activity_occurrence(test=test, activity_occurrence_resource=activity_occurrence_resource)

Create a new activity occurrence

Has to enforce extra rules if not used as an admin

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
api_instance = swagger_client.ActivitiesApi()
test = false # bool | if true, indicates that the occurrence should NOT be created. This can be used to test for eligibility and valid settings (optional) (default to false)
activity_occurrence_resource = swagger_client.ActivityOccurrenceResource() # ActivityOccurrenceResource | The activity occurrence object (optional)

try: 
    # Create a new activity occurrence
    api_response = api_instance.create_activity_occurrence(test=test, activity_occurrence_resource=activity_occurrence_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->create_activity_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test** | **bool**| if true, indicates that the occurrence should NOT be created. This can be used to test for eligibility and valid settings | [optional] [default to false]
 **activity_occurrence_resource** | [**ActivityOccurrenceResource**](ActivityOccurrenceResource.md)| The activity occurrence object | [optional] 

### Return type

[**ActivityOccurrenceResource**](ActivityOccurrenceResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity**
> delete_activity(id)

Delete an activity

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
api_instance = swagger_client.ActivitiesApi()
id = 789 # int | The id of the activity

try: 
    # Delete an activity
    api_instance.delete_activity(id)
except ApiException as e:
    print("Exception when calling ActivitiesApi->delete_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the activity | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities**
> PageResourceBareActivityResource get_activities(filter_template=filter_template, size=size, page=page, order=order)

List activity definitions

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
filter_template = true # bool | Filter for activities that are templates, or specifically not if false (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List activity definitions
    api_response = api_instance.get_activities(filter_template=filter_template, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_template** | **bool**| Filter for activities that are templates, or specifically not if false | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceBareActivityResource**](PageResourceBareActivityResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity**
> ActivityResource get_activity(id)

Get a single activity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
id = 789 # int | The id of the activity

try: 
    # Get a single activity
    api_response = api_instance.get_activity(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the activity | 

### Return type

[**ActivityResource**](ActivityResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_activity_occurrence_results**
> ActivityOccurrenceResults set_activity_occurrence_results(activity_occurrence_id, activity_occurrence_results=activity_occurrence_results)

Sets the status of an activity occurrence to FINISHED and logs metrics

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
api_instance = swagger_client.ActivitiesApi()
activity_occurrence_id = 789 # int | The id of the activity occurrence
activity_occurrence_results = swagger_client.ActivityOccurrenceResults() # ActivityOccurrenceResults | The activity occurrence object (optional)

try: 
    # Sets the status of an activity occurrence to FINISHED and logs metrics
    api_response = api_instance.set_activity_occurrence_results(activity_occurrence_id, activity_occurrence_results=activity_occurrence_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->set_activity_occurrence_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_occurrence_id** | **int**| The id of the activity occurrence | 
 **activity_occurrence_results** | [**ActivityOccurrenceResults**](ActivityOccurrenceResults.md)| The activity occurrence object | [optional] 

### Return type

[**ActivityOccurrenceResults**](ActivityOccurrenceResults.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity**
> update_activity(id, activity_resource=activity_resource)

Update an activity

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
api_instance = swagger_client.ActivitiesApi()
id = 789 # int | The id of the activity
activity_resource = swagger_client.ActivityResource() # ActivityResource | The activity resource object (optional)

try: 
    # Update an activity
    api_instance.update_activity(id, activity_resource=activity_resource)
except ApiException as e:
    print("Exception when calling ActivitiesApi->update_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the activity | 
 **activity_resource** | [**ActivityResource**](ActivityResource.md)| The activity resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_occurrence**
> update_activity_occurrence(activity_occurrence_id, activity_cccurrence_status=activity_cccurrence_status)

Updated the status of an activity occurrence

If setting to 'FINISHED' you must POST to /results instead to record the metrics and get synchronous reward results

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
api_instance = swagger_client.ActivitiesApi()
activity_occurrence_id = 789 # int | The id of the activity occurrence
activity_cccurrence_status = 'activity_cccurrence_status_example' # str | The activity occurrence status object (optional)

try: 
    # Updated the status of an activity occurrence
    api_instance.update_activity_occurrence(activity_occurrence_id, activity_cccurrence_status=activity_cccurrence_status)
except ApiException as e:
    print("Exception when calling ActivitiesApi->update_activity_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_occurrence_id** | **int**| The id of the activity occurrence | 
 **activity_cccurrence_status** | **str**| The activity occurrence status object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

