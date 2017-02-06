# swagger_client.CampaignsChallengesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_challenge**](CampaignsChallengesApi.md#create_challenge) | **POST** /challenges | Create a challenge
[**create_challenge_activity**](CampaignsChallengesApi.md#create_challenge_activity) | **POST** /challenges/{challenge_id}/activities | Create a challenge activity
[**create_challenge_template**](CampaignsChallengesApi.md#create_challenge_template) | **POST** /challenges/templates | Create a challenge template
[**delete_challenge**](CampaignsChallengesApi.md#delete_challenge) | **DELETE** /challenges/{id} | Delete a challenge
[**delete_challenge_activity**](CampaignsChallengesApi.md#delete_challenge_activity) | **DELETE** /challenges/{challenge_id}/activities/{activity_id} | Delete a challenge activity
[**delete_challenge_event**](CampaignsChallengesApi.md#delete_challenge_event) | **DELETE** /challenges/events/{id} | Delete a challenge event
[**delete_challenge_template**](CampaignsChallengesApi.md#delete_challenge_template) | **DELETE** /challenges/templates/{id} | Delete a challenge template
[**get_challenge**](CampaignsChallengesApi.md#get_challenge) | **GET** /challenges/{id} | Retrieve a challenge
[**get_challenge_activities**](CampaignsChallengesApi.md#get_challenge_activities) | **GET** /challenges/{challenge_id}/activities | List and search challenge activities
[**get_challenge_activity**](CampaignsChallengesApi.md#get_challenge_activity) | **GET** /challenges/{challenge_id}/activities/{activity_id} | Get a single challenge activity
[**get_challenge_event**](CampaignsChallengesApi.md#get_challenge_event) | **GET** /challenges/events/{id} | Retrieve a single challenge event details
[**get_challenge_events**](CampaignsChallengesApi.md#get_challenge_events) | **GET** /challenges/events | Retrieve a list of challenge events
[**get_challenge_template**](CampaignsChallengesApi.md#get_challenge_template) | **GET** /challenges/templates/{id} | Get a single challenge template
[**get_challenge_templates**](CampaignsChallengesApi.md#get_challenge_templates) | **GET** /challenges/templates | List and search challenge templates
[**get_challenges**](CampaignsChallengesApi.md#get_challenges) | **GET** /challenges | Retrieve a list of challenges
[**update_challenge**](CampaignsChallengesApi.md#update_challenge) | **PUT** /challenges/{id} | Update a challenge
[**update_challenge_activity**](CampaignsChallengesApi.md#update_challenge_activity) | **PUT** /challenges/{challenge_id}/activities/{activity_id} | Update a challenge activity
[**update_challenge_template**](CampaignsChallengesApi.md#update_challenge_template) | **PUT** /challenges/templates/{id} | Update a challenge template


# **create_challenge**
> ChallengeResource create_challenge(challenge_resource=challenge_resource)

Create a challenge

Challenges do not run on their own.  They must be added to a campaign before events will spawn.

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
api_instance = swagger_client.CampaignsChallengesApi()
challenge_resource = swagger_client.ChallengeResource() # ChallengeResource | The challenge resource object (optional)

try: 
    # Create a challenge
    api_response = api_instance.create_challenge(challenge_resource=challenge_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->create_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_resource** | [**ChallengeResource**](ChallengeResource.md)| The challenge resource object | [optional] 

### Return type

[**ChallengeResource**](ChallengeResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_challenge_activity**
> ChallengeActivityResource create_challenge_activity(challenge_id, challenge_activity_resource=challenge_activity_resource, validate_settings=validate_settings)

Create a challenge activity

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
api_instance = swagger_client.CampaignsChallengesApi()
challenge_id = 789 # int | The challenge id
challenge_activity_resource = swagger_client.ChallengeActivityResource() # ChallengeActivityResource | The challenge activity resource object (optional)
validate_settings = false # bool | Whether to validate the settings being sent against the available settings on the base activity. (optional) (default to false)

try: 
    # Create a challenge activity
    api_response = api_instance.create_challenge_activity(challenge_id, challenge_activity_resource=challenge_activity_resource, validate_settings=validate_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->create_challenge_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **int**| The challenge id | 
 **challenge_activity_resource** | [**ChallengeActivityResource**](ChallengeActivityResource.md)| The challenge activity resource object | [optional] 
 **validate_settings** | **bool**| Whether to validate the settings being sent against the available settings on the base activity. | [optional] [default to false]

### Return type

[**ChallengeActivityResource**](ChallengeActivityResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_challenge_template**
> TemplateResource create_challenge_template(challenge_template_resource=challenge_template_resource)

Create a challenge template

Challenge Templates define a type of challenge and the properties they have

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
api_instance = swagger_client.CampaignsChallengesApi()
challenge_template_resource = swagger_client.TemplateResource() # TemplateResource | The challenge template resource object (optional)

try: 
    # Create a challenge template
    api_response = api_instance.create_challenge_template(challenge_template_resource=challenge_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->create_challenge_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_template_resource** | [**TemplateResource**](TemplateResource.md)| The challenge template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_challenge**
> delete_challenge(id)

Delete a challenge

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
api_instance = swagger_client.CampaignsChallengesApi()
id = 789 # int | The challenge id

try: 
    # Delete a challenge
    api_instance.delete_challenge(id)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->delete_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The challenge id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_challenge_activity**
> delete_challenge_activity(activity_id, challenge_id)

Delete a challenge activity

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
api_instance = swagger_client.CampaignsChallengesApi()
activity_id = 789 # int | The activity id
challenge_id = 789 # int | The challenge id

try: 
    # Delete a challenge activity
    api_instance.delete_challenge_activity(activity_id, challenge_id)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->delete_challenge_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| The activity id | 
 **challenge_id** | **int**| The challenge id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_challenge_event**
> delete_challenge_event(id)

Delete a challenge event

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
api_instance = swagger_client.CampaignsChallengesApi()
id = 789 # int | The challenge event id

try: 
    # Delete a challenge event
    api_instance.delete_challenge_event(id)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->delete_challenge_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The challenge event id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_challenge_template**
> delete_challenge_template(id, cascade=cascade)

Delete a challenge template

If cascade = 'detach', it will force delete the template even if it's attached to other objects

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
api_instance = swagger_client.CampaignsChallengesApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a challenge template
    api_instance.delete_challenge_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->delete_challenge_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| The value needed to delete used templates | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge**
> ChallengeResource get_challenge(id)

Retrieve a challenge

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsChallengesApi()
id = 789 # int | The challenge id

try: 
    # Retrieve a challenge
    api_response = api_instance.get_challenge(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->get_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The challenge id | 

### Return type

[**ChallengeResource**](ChallengeResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge_activities**
> PageResourceBareChallengeActivityResource get_challenge_activities(challenge_id, size=size, page=page, order=order)

List and search challenge activities

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsChallengesApi()
challenge_id = 789 # int | The challenge id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search challenge activities
    api_response = api_instance.get_challenge_activities(challenge_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->get_challenge_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_id** | **int**| The challenge id | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceBareChallengeActivityResource**](PageResourceBareChallengeActivityResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge_activity**
> ChallengeActivityResource get_challenge_activity(activity_id)

Get a single challenge activity

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsChallengesApi()
activity_id = 789 # int | The activity id

try: 
    # Get a single challenge activity
    api_response = api_instance.get_challenge_activity(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->get_challenge_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| The activity id | 

### Return type

[**ChallengeActivityResource**](ChallengeActivityResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge_event**
> ChallengeEventResource get_challenge_event(id)

Retrieve a single challenge event details

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsChallengesApi()
id = 789 # int | The challenge event id

try: 
    # Retrieve a single challenge event details
    api_response = api_instance.get_challenge_event(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->get_challenge_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The challenge event id | 

### Return type

[**ChallengeEventResource**](ChallengeEventResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge_events**
> PageResourceChallengeEventResource get_challenge_events(filter_start_date=filter_start_date, filter_end_date=filter_end_date, filter_campaigns=filter_campaigns, filter_challenge=filter_challenge, size=size, page=page, order=order)

Retrieve a list of challenge events

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsChallengesApi()
filter_start_date = 'filter_start_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the event start date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)
filter_end_date = 'filter_end_date_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the event end date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)
filter_campaigns = true # bool | check only for events from currently running campaigns (optional)
filter_challenge = 789 # int | check only for events from the challenge specified by id (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Retrieve a list of challenge events
    api_response = api_instance.get_challenge_events(filter_start_date=filter_start_date, filter_end_date=filter_end_date, filter_campaigns=filter_campaigns, filter_challenge=filter_challenge, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->get_challenge_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_start_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the event start date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). | [optional] 
 **filter_end_date** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the event end date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). | [optional] 
 **filter_campaigns** | **bool**| check only for events from currently running campaigns | [optional] 
 **filter_challenge** | **int**| check only for events from the challenge specified by id | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceChallengeEventResource**](PageResourceChallengeEventResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge_template**
> TemplateResource get_challenge_template(id)

Get a single challenge template

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
api_instance = swagger_client.CampaignsChallengesApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single challenge template
    api_response = api_instance.get_challenge_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->get_challenge_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge_templates**
> PageResourceTemplateResource get_challenge_templates(size=size, page=page, order=order)

List and search challenge templates

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
api_instance = swagger_client.CampaignsChallengesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search challenge templates
    api_response = api_instance.get_challenge_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->get_challenge_templates: %s\n" % e)
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

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenges**
> PageResourceChallengeResource get_challenges(filter_template=filter_template, filter_active_campaign=filter_active_campaign)

Retrieve a list of challenges

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsChallengesApi()
filter_template = true # bool | Filter for challenges that are not tied to campaigns (templates) (optional)
filter_active_campaign = true # bool | Filter for challenges that are tied to active campaigns (optional)

try: 
    # Retrieve a list of challenges
    api_response = api_instance.get_challenges(filter_template=filter_template, filter_active_campaign=filter_active_campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->get_challenges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_template** | **bool**| Filter for challenges that are not tied to campaigns (templates) | [optional] 
 **filter_active_campaign** | **bool**| Filter for challenges that are tied to active campaigns | [optional] 

### Return type

[**PageResourceChallengeResource**](PageResourceChallengeResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_challenge**
> ChallengeResource update_challenge(id, challenge_resource=challenge_resource)

Update a challenge

If the challenge is a copy, changes will propagate to all the related challenges

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
api_instance = swagger_client.CampaignsChallengesApi()
id = 789 # int | The challenge id
challenge_resource = swagger_client.ChallengeResource() # ChallengeResource | The challenge resource object (optional)

try: 
    # Update a challenge
    api_response = api_instance.update_challenge(id, challenge_resource=challenge_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->update_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The challenge id | 
 **challenge_resource** | [**ChallengeResource**](ChallengeResource.md)| The challenge resource object | [optional] 

### Return type

[**ChallengeResource**](ChallengeResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_challenge_activity**
> update_challenge_activity(activity_id, challenge_id, challenge_activity_resource=challenge_activity_resource)

Update a challenge activity

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
api_instance = swagger_client.CampaignsChallengesApi()
activity_id = 789 # int | The activity id
challenge_id = 789 # int | The challenge id
challenge_activity_resource = swagger_client.ChallengeActivityResource() # ChallengeActivityResource | The challenge activity resource object (optional)

try: 
    # Update a challenge activity
    api_instance.update_challenge_activity(activity_id, challenge_id, challenge_activity_resource=challenge_activity_resource)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->update_challenge_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| The activity id | 
 **challenge_id** | **int**| The challenge id | 
 **challenge_activity_resource** | [**ChallengeActivityResource**](ChallengeActivityResource.md)| The challenge activity resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_challenge_template**
> update_challenge_template(id, challenge_template_resource=challenge_template_resource)

Update a challenge template

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
api_instance = swagger_client.CampaignsChallengesApi()
id = 'id_example' # str | The id of the template
challenge_template_resource = swagger_client.TemplateResource() # TemplateResource | The challenge template resource object (optional)

try: 
    # Update a challenge template
    api_instance.update_challenge_template(id, challenge_template_resource=challenge_template_resource)
except ApiException as e:
    print("Exception when calling CampaignsChallengesApi->update_challenge_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **challenge_template_resource** | [**TemplateResource**](TemplateResource.md)| The challenge template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

