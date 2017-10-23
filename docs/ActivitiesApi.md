# knetik_cloud.ActivitiesApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity**](ActivitiesApi.md#create_activity) | **POST** /activities | Create an activity
[**create_activity_occurrence**](ActivitiesApi.md#create_activity_occurrence) | **POST** /activity-occurrences | Create a new activity occurrence. Ex: start a game
[**create_activity_template**](ActivitiesApi.md#create_activity_template) | **POST** /activities/templates | Create a activity template
[**delete_activity**](ActivitiesApi.md#delete_activity) | **DELETE** /activities/{id} | Delete an activity
[**delete_activity_template**](ActivitiesApi.md#delete_activity_template) | **DELETE** /activities/templates/{id} | Delete a activity template
[**get_activities**](ActivitiesApi.md#get_activities) | **GET** /activities | List activity definitions
[**get_activity**](ActivitiesApi.md#get_activity) | **GET** /activities/{id} | Get a single activity
[**get_activity_occurrence_details**](ActivitiesApi.md#get_activity_occurrence_details) | **GET** /activity-occurrences/{activity_occurrence_id} | Load a single activity occurrence details
[**get_activity_template**](ActivitiesApi.md#get_activity_template) | **GET** /activities/templates/{id} | Get a single activity template
[**get_activity_templates**](ActivitiesApi.md#get_activity_templates) | **GET** /activities/templates | List and search activity templates
[**list_activity_occurrences**](ActivitiesApi.md#list_activity_occurrences) | **GET** /activity-occurrences | List activity occurrences
[**set_activity_occurrence_results**](ActivitiesApi.md#set_activity_occurrence_results) | **POST** /activity-occurrences/{activity_occurrence_id}/results | Sets the status of an activity occurrence to FINISHED and logs metrics
[**update_activity**](ActivitiesApi.md#update_activity) | **PUT** /activities/{id} | Update an activity
[**update_activity_occurrence**](ActivitiesApi.md#update_activity_occurrence) | **PUT** /activity-occurrences/{activity_occurrence_id}/status | Updated the status of an activity occurrence
[**update_activity_template**](ActivitiesApi.md#update_activity_template) | **PUT** /activities/templates/{id} | Update an activity template


# **create_activity**
> ActivityResource create_activity(activity_resource=activity_resource)

Create an activity

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
activity_resource = knetik_cloud.ActivityResource() # ActivityResource | The activity resource object (optional)

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

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity_occurrence**
> ActivityOccurrenceResource create_activity_occurrence(test=test, activity_occurrence_resource=activity_occurrence_resource)

Create a new activity occurrence. Ex: start a game

Has to enforce extra rules if not used as an admin

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
test = false # bool | if true, indicates that the occurrence should NOT be created. This can be used to test for eligibility and valid settings (optional) (default to false)
activity_occurrence_resource = knetik_cloud.CreateActivityOccurrenceRequest() # CreateActivityOccurrenceRequest | The activity occurrence object (optional)

try: 
    # Create a new activity occurrence. Ex: start a game
    api_response = api_instance.create_activity_occurrence(test=test, activity_occurrence_resource=activity_occurrence_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->create_activity_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test** | **bool**| if true, indicates that the occurrence should NOT be created. This can be used to test for eligibility and valid settings | [optional] [default to false]
 **activity_occurrence_resource** | [**CreateActivityOccurrenceRequest**](CreateActivityOccurrenceRequest.md)| The activity occurrence object | [optional] 

### Return type

[**ActivityOccurrenceResource**](ActivityOccurrenceResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity_template**
> TemplateResource create_activity_template(activity_template_resource=activity_template_resource)

Create a activity template

Activity Templates define a type of activity and the properties they have

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
activity_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The activity template resource object (optional)

try: 
    # Create a activity template
    api_response = api_instance.create_activity_template(activity_template_resource=activity_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->create_activity_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_template_resource** | [**TemplateResource**](TemplateResource.md)| The activity template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity**
> delete_activity(id)

Delete an activity

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
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

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activity_template**
> delete_activity_template(id, cascade=cascade)

Delete a activity template

If cascade = 'detach', it will force delete the template even if it's attached to other objects

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a activity template
    api_instance.delete_activity_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling ActivitiesApi->delete_activity_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| The value needed to delete used templates | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities**
> PageResourceBareActivityResource get_activities(filter_template=filter_template, filter_name=filter_name, filter_id=filter_id, size=size, page=page, order=order)

List activity definitions

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.ActivitiesApi()
filter_template = true # bool | Filter for activities that are templates, or specifically not if false (optional)
filter_name = 'filter_name_example' # str | Filter for activities that have a name starting with specified string (optional)
filter_id = 'filter_id_example' # str | Filter for activities with an id in the given comma separated list of ids (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List activity definitions
    api_response = api_instance.get_activities(filter_template=filter_template, filter_name=filter_name, filter_id=filter_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_template** | **bool**| Filter for activities that are templates, or specifically not if false | [optional] 
 **filter_name** | **str**| Filter for activities that have a name starting with specified string | [optional] 
 **filter_id** | **str**| Filter for activities with an id in the given comma separated list of ids | [optional] 
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
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.ActivitiesApi()
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

# **get_activity_occurrence_details**
> ActivityOccurrenceResource get_activity_occurrence_details(activity_occurrence_id)

Load a single activity occurrence details

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
activity_occurrence_id = 789 # int | The id of the activity occurrence

try: 
    # Load a single activity occurrence details
    api_response = api_instance.get_activity_occurrence_details(activity_occurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activity_occurrence_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_occurrence_id** | **int**| The id of the activity occurrence | 

### Return type

[**ActivityOccurrenceResource**](ActivityOccurrenceResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_template**
> TemplateResource get_activity_template(id)

Get a single activity template

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single activity template
    api_response = api_instance.get_activity_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activity_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_templates**
> PageResourceTemplateResource get_activity_templates(size=size, page=page, order=order)

List and search activity templates

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search activity templates
    api_response = api_instance.get_activity_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activity_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceTemplateResource**](PageResourceTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_activity_occurrences**
> PageResourceActivityOccurrenceResource list_activity_occurrences(filter_activity=filter_activity, filter_status=filter_status, filter_event=filter_event, filter_challenge=filter_challenge, size=size, page=page, order=order)

List activity occurrences

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
filter_activity = 'filter_activity_example' # str | Filter for occurrences of the given activity ID (optional)
filter_status = 'filter_status_example' # str | Filter for occurrences of the given activity ID (optional)
filter_event = 56 # int | Filter for occurrences played during the given event (optional)
filter_challenge = 56 # int | Filter for occurrences played within the given challenge (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List activity occurrences
    api_response = api_instance.list_activity_occurrences(filter_activity=filter_activity, filter_status=filter_status, filter_event=filter_event, filter_challenge=filter_challenge, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->list_activity_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_activity** | **str**| Filter for occurrences of the given activity ID | [optional] 
 **filter_status** | **str**| Filter for occurrences of the given activity ID | [optional] 
 **filter_event** | **int**| Filter for occurrences played during the given event | [optional] 
 **filter_challenge** | **int**| Filter for occurrences played within the given challenge | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceActivityOccurrenceResource**](PageResourceActivityOccurrenceResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_activity_occurrence_results**
> ActivityOccurrenceResults set_activity_occurrence_results(activity_occurrence_id, activity_occurrence_results=activity_occurrence_results)

Sets the status of an activity occurrence to FINISHED and logs metrics

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
activity_occurrence_id = 789 # int | The id of the activity occurrence
activity_occurrence_results = knetik_cloud.ActivityOccurrenceResultsResource() # ActivityOccurrenceResultsResource | The activity occurrence object (optional)

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
 **activity_occurrence_results** | [**ActivityOccurrenceResultsResource**](ActivityOccurrenceResultsResource.md)| The activity occurrence object | [optional] 

### Return type

[**ActivityOccurrenceResults**](ActivityOccurrenceResults.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity**
> ActivityResource update_activity(id, activity_resource=activity_resource)

Update an activity

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The id of the activity
activity_resource = knetik_cloud.ActivityResource() # ActivityResource | The activity resource object (optional)

try: 
    # Update an activity
    api_response = api_instance.update_activity(id, activity_resource=activity_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->update_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the activity | 
 **activity_resource** | [**ActivityResource**](ActivityResource.md)| The activity resource object | [optional] 

### Return type

[**ActivityResource**](ActivityResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_occurrence**
> update_activity_occurrence(activity_occurrence_id, activity_occurrence_status=activity_occurrence_status)

Updated the status of an activity occurrence

If setting to 'FINISHED' reward will be run based on current metrics that have been recorded already. Aternatively, see results endpoint to finish and record all metrics at once.

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
activity_occurrence_id = 789 # int | The id of the activity occurrence
activity_occurrence_status = 'activity_occurrence_status_example' # str | The activity occurrence status object (optional)

try: 
    # Updated the status of an activity occurrence
    api_instance.update_activity_occurrence(activity_occurrence_id, activity_occurrence_status=activity_occurrence_status)
except ApiException as e:
    print("Exception when calling ActivitiesApi->update_activity_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_occurrence_id** | **int**| The id of the activity occurrence | 
 **activity_occurrence_status** | **str**| The activity occurrence status object | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_template**
> TemplateResource update_activity_template(id, activity_template_resource=activity_template_resource)

Update an activity template

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
api_instance = knetik_cloud.ActivitiesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
activity_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The activity template resource object (optional)

try: 
    # Update an activity template
    api_response = api_instance.update_activity_template(id, activity_template_resource=activity_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->update_activity_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **activity_template_resource** | [**TemplateResource**](TemplateResource.md)| The activity template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

