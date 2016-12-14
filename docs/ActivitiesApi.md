# swagger_client.ActivitiesApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_activity_occurrence_using_put**](ActivitiesApi.md#complete_activity_occurrence_using_put) | **PUT** /activity-occurrences/{activity_occurrence_id}/status | Updated the status of an activity occurrence
[**create_activity_occurrence_using_post**](ActivitiesApi.md#create_activity_occurrence_using_post) | **POST** /activity-occurrences | Create a new activity occurrence
[**create_activity_using_post**](ActivitiesApi.md#create_activity_using_post) | **POST** /activities | Create an activity
[**delete_activity_using_delete**](ActivitiesApi.md#delete_activity_using_delete) | **DELETE** /activities/{id} | Delete an activity
[**get_activities_using_get**](ActivitiesApi.md#get_activities_using_get) | **GET** /activities | List activity definitions
[**get_activity_using_get**](ActivitiesApi.md#get_activity_using_get) | **GET** /activities/{id} | Get a single activity
[**post_results_using_post**](ActivitiesApi.md#post_results_using_post) | **POST** /activity-occurrences/{activity_occurrence_id}/results | Sets the status of an activity occurrence to FINISHED and logs metrics
[**update_activity_using_put**](ActivitiesApi.md#update_activity_using_put) | **PUT** /activities/{id} | Update an activity


# **complete_activity_occurrence_using_put**
> complete_activity_occurrence_using_put(activity_occurrence_id, activity_cccurrence_status=activity_cccurrence_status)

Updated the status of an activity occurrence

If setting to 'FINISHED' you must POST to /results instead to record the metrics and get synchronous reward results

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
activity_occurrence_id = 789 # int | The id of the activity occurrence
activity_cccurrence_status = 'activity_cccurrence_status_example' # str | The activity occurrence status object (optional)

try: 
    # Updated the status of an activity occurrence
    api_instance.complete_activity_occurrence_using_put(activity_occurrence_id, activity_cccurrence_status=activity_cccurrence_status)
except ApiException as e:
    print("Exception when calling ActivitiesApi->complete_activity_occurrence_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_occurrence_id** | **int**| The id of the activity occurrence | 
 **activity_cccurrence_status** | **str**| The activity occurrence status object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity_occurrence_using_post**
> ActivityOccurrenceResource create_activity_occurrence_using_post(test=test, activity_occurrence_resource=activity_occurrence_resource)

Create a new activity occurrence

Has to enforce extra rules if not used as an admin

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
test = false # bool | if true, indicates that the occurrence should NOT be created. This can be used to test for eligibility and valid settings (optional) (default to false)
activity_occurrence_resource = swagger_client.ActivityOccurrenceResource() # ActivityOccurrenceResource | The activity occurrence object (optional)

try: 
    # Create a new activity occurrence
    api_response = api_instance.create_activity_occurrence_using_post(test=test, activity_occurrence_resource=activity_occurrence_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->create_activity_occurrence_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test** | **bool**| if true, indicates that the occurrence should NOT be created. This can be used to test for eligibility and valid settings | [optional] [default to false]
 **activity_occurrence_resource** | [**ActivityOccurrenceResource**](ActivityOccurrenceResource.md)| The activity occurrence object | [optional] 

### Return type

[**ActivityOccurrenceResource**](ActivityOccurrenceResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity_using_post**
> ActivityResource create_activity_using_post(activity_resource=activity_resource)

Create an activity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
activity_resource = swagger_client.ActivityResource() # ActivityResource | The activity resource object (optional)

try: 
    # Create an activity
    api_response = api_instance.create_activity_using_post(activity_resource=activity_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->create_activity_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_resource** | [**ActivityResource**](ActivityResource.md)| The activity resource object | [optional] 

### Return type

[**ActivityResource**](ActivityResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity_using_delete**
> delete_activity_using_delete(id)

Delete an activity

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
    # Delete an activity
    api_instance.delete_activity_using_delete(id)
except ApiException as e:
    print("Exception when calling ActivitiesApi->delete_activity_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the activity | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_using_get**
> PageBareActivityResource get_activities_using_get(filter_template=filter_template, size=size, page=page, order=order)

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
order = '1' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # List activity definitions
    api_response = api_instance.get_activities_using_get(filter_template=filter_template, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activities_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_template** | **bool**| Filter for activities that are templates, or specifically not if false | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageBareActivityResource**](PageBareActivityResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_using_get**
> ActivityResource get_activity_using_get(id)

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
    api_response = api_instance.get_activity_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activity_using_get: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_results_using_post**
> ActivityOccurrenceResults post_results_using_post(activity_occurrence_id, activity_occurrence_results=activity_occurrence_results)

Sets the status of an activity occurrence to FINISHED and logs metrics

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
activity_occurrence_id = 789 # int | The id of the activity occurrence
activity_occurrence_results = swagger_client.ActivityOccurrenceResults() # ActivityOccurrenceResults | The activity occurrence object (optional)

try: 
    # Sets the status of an activity occurrence to FINISHED and logs metrics
    api_response = api_instance.post_results_using_post(activity_occurrence_id, activity_occurrence_results=activity_occurrence_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->post_results_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_occurrence_id** | **int**| The id of the activity occurrence | 
 **activity_occurrence_results** | [**ActivityOccurrenceResults**](ActivityOccurrenceResults.md)| The activity occurrence object | [optional] 

### Return type

[**ActivityOccurrenceResults**](ActivityOccurrenceResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_using_put**
> update_activity_using_put(id, activity_resource=activity_resource)

Update an activity

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
activity_resource = swagger_client.ActivityResource() # ActivityResource | The activity resource object (optional)

try: 
    # Update an activity
    api_instance.update_activity_using_put(id, activity_resource=activity_resource)
except ApiException as e:
    print("Exception when calling ActivitiesApi->update_activity_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the activity | 
 **activity_resource** | [**ActivityResource**](ActivityResource.md)| The activity resource object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

