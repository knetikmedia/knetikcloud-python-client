# knetik_cloud.MediaPollsApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**answer_poll**](MediaPollsApi.md#answer_poll) | **POST** /media/polls/{id}/response | Add your vote to a poll
[**create_poll**](MediaPollsApi.md#create_poll) | **POST** /media/polls | Create a new poll
[**create_poll_template**](MediaPollsApi.md#create_poll_template) | **POST** /media/polls/templates | Create a poll template
[**delete_poll**](MediaPollsApi.md#delete_poll) | **DELETE** /media/polls/{id} | Delete an existing poll
[**delete_poll_template**](MediaPollsApi.md#delete_poll_template) | **DELETE** /media/polls/templates/{id} | Delete a poll template
[**get_poll**](MediaPollsApi.md#get_poll) | **GET** /media/polls/{id} | Get a single poll
[**get_poll_answer**](MediaPollsApi.md#get_poll_answer) | **GET** /media/polls/{id}/response | Get poll answer
[**get_poll_template**](MediaPollsApi.md#get_poll_template) | **GET** /media/polls/templates/{id} | Get a single poll template
[**get_poll_templates**](MediaPollsApi.md#get_poll_templates) | **GET** /media/polls/templates | List and search poll templates
[**get_polls**](MediaPollsApi.md#get_polls) | **GET** /media/polls | List and search polls
[**update_poll**](MediaPollsApi.md#update_poll) | **PUT** /media/polls/{id} | Update an existing poll
[**update_poll_template**](MediaPollsApi.md#update_poll_template) | **PUT** /media/polls/templates/{id} | Update a poll template


# **answer_poll**
> PollResponseResource answer_poll(id, answer_key=answer_key)

Add your vote to a poll

<b>Permissions Needed:</b> POLLS_ADMIN or POLLS_USER

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The poll id
answer_key = knetik_cloud.StringWrapper() # StringWrapper | The answer key (optional)

try: 
    # Add your vote to a poll
    api_response = api_instance.answer_poll(id, answer_key=answer_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->answer_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 
 **answer_key** | [**StringWrapper**](StringWrapper.md)| The answer key | [optional] 

### Return type

[**PollResponseResource**](PollResponseResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_poll**
> PollResource create_poll(poll_resource=poll_resource)

Create a new poll

Polls are blobs of text with titles, a category and assets. Formatting and display of the text is in the hands of the front end. <br><br><b>Permissions Needed:</b> POLLS_ADMIN

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
poll_resource = knetik_cloud.PollResource() # PollResource | The poll object (optional)

try: 
    # Create a new poll
    api_response = api_instance.create_poll(poll_resource=poll_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->create_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_resource** | [**PollResource**](PollResource.md)| The poll object | [optional] 

### Return type

[**PollResource**](PollResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_poll_template**
> TemplateResource create_poll_template(poll_template_resource=poll_template_resource)

Create a poll template

Poll templates define a type of poll and the properties they have. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
poll_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The poll template resource object (optional)

try: 
    # Create a poll template
    api_response = api_instance.create_poll_template(poll_template_resource=poll_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->create_poll_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_template_resource** | [**TemplateResource**](TemplateResource.md)| The poll template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_poll**
> delete_poll(id)

Delete an existing poll

<b>Permissions Needed:</b> POLLS_ADMIN

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The poll id

try: 
    # Delete an existing poll
    api_instance.delete_poll(id)
except ApiException as e:
    print("Exception when calling MediaPollsApi->delete_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_poll_template**
> delete_poll_template(id, cascade=cascade)

Delete a poll template

If cascade = 'detach', it will force delete the template even if it's attached to other objects. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a poll template
    api_instance.delete_poll_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling MediaPollsApi->delete_poll_template: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll**
> PollResource get_poll(id)

Get a single poll

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The poll id

try: 
    # Get a single poll
    api_response = api_instance.get_poll(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->get_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 

### Return type

[**PollResource**](PollResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll_answer**
> PollResponseResource get_poll_answer(id)

Get poll answer

<b>Permissions Needed:</b> POLLS_ADMIN or POLLS_USER

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The poll id

try: 
    # Get poll answer
    api_response = api_instance.get_poll_answer(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->get_poll_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 

### Return type

[**PollResponseResource**](PollResponseResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll_template**
> TemplateResource get_poll_template(id)

Get a single poll template

<b>Permissions Needed:</b> TEMPLATE_ADMIN or POLLS_ADMIN

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single poll template
    api_response = api_instance.get_poll_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->get_poll_template: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll_templates**
> PageResourceTemplateResource get_poll_templates(size=size, page=page, order=order)

List and search poll templates

<b>Permissions Needed:</b> TEMPLATE_ADMIN or POLLS_ADMIN

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search poll templates
    api_response = api_instance.get_poll_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->get_poll_templates: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_polls**
> PageResourcePollResource get_polls(filter_category=filter_category, filter_tagset=filter_tagset, filter_text=filter_text, size=size, page=page, order=order)

List and search polls

Get a list of polls with optional filtering. Assets will not be filled in on the resources returned. Use 'Get a single poll' to retrieve the full resource with assets for a given item as needed. <br><br><b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
filter_category = 'filter_category_example' # str | Filter for polls from a specific category by id (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for polls with specified tags (separated by comma) (optional)
filter_text = 'filter_text_example' # str | Filter for polls whose text contains a string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search polls
    api_response = api_instance.get_polls(filter_category=filter_category, filter_tagset=filter_tagset, filter_text=filter_text, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->get_polls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_category** | **str**| Filter for polls from a specific category by id | [optional] 
 **filter_tagset** | **str**| Filter for polls with specified tags (separated by comma) | [optional] 
 **filter_text** | **str**| Filter for polls whose text contains a string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourcePollResource**](PageResourcePollResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_poll**
> PollResource update_poll(id, poll_resource=poll_resource)

Update an existing poll

<b>Permissions Needed:</b> POLLS_ADMIN

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The poll id
poll_resource = knetik_cloud.PollResource() # PollResource | The poll object (optional)

try: 
    # Update an existing poll
    api_response = api_instance.update_poll(id, poll_resource=poll_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->update_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 
 **poll_resource** | [**PollResource**](PollResource.md)| The poll object | [optional] 

### Return type

[**PollResource**](PollResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_poll_template**
> TemplateResource update_poll_template(id, poll_template_resource=poll_template_resource)

Update a poll template

<b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.MediaPollsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
poll_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The poll template resource object (optional)

try: 
    # Update a poll template
    api_response = api_instance.update_poll_template(id, poll_template_resource=poll_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaPollsApi->update_poll_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **poll_template_resource** | [**TemplateResource**](TemplateResource.md)| The poll template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

