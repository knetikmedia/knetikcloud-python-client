# swagger_client.ContentPollsApi

All URIs are relative to *https://sandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**answer_poll**](ContentPollsApi.md#answer_poll) | **POST** /media/polls/{id}/response | Add your vote to a poll
[**create_poll**](ContentPollsApi.md#create_poll) | **POST** /media/polls | Create a new poll
[**create_poll_template**](ContentPollsApi.md#create_poll_template) | **POST** /media/polls/templates | Create a poll template
[**delete_poll**](ContentPollsApi.md#delete_poll) | **DELETE** /media/polls/{id} | Delete an existing poll
[**delete_poll_template**](ContentPollsApi.md#delete_poll_template) | **DELETE** /media/polls/templates/{id} | Delete a poll template
[**get_poll**](ContentPollsApi.md#get_poll) | **GET** /media/polls/{id} | Get a single poll
[**get_poll_answer**](ContentPollsApi.md#get_poll_answer) | **GET** /media/polls/{id}/response | Get poll answer
[**get_poll_template**](ContentPollsApi.md#get_poll_template) | **GET** /media/polls/templates/{id} | Get a single poll template
[**get_poll_templates**](ContentPollsApi.md#get_poll_templates) | **GET** /media/polls/templates | List and search poll templates
[**get_polls**](ContentPollsApi.md#get_polls) | **GET** /media/polls | List and search polls
[**update_poll**](ContentPollsApi.md#update_poll) | **PUT** /media/polls/{id} | Update an existing poll
[**update_poll_template**](ContentPollsApi.md#update_poll_template) | **PUT** /media/polls/templates/{id} | Update a poll template


# **answer_poll**
> PollResponseResource answer_poll(id, answer_key=answer_key)

Add your vote to a poll

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
id = 'id_example' # str | The poll id
answer_key = 'answer_key_example' # str | The answer key (optional)

try: 
    # Add your vote to a poll
    api_response = api_instance.answer_poll(id, answer_key=answer_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentPollsApi->answer_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 
 **answer_key** | **str**| The answer key | [optional] 

### Return type

[**PollResponseResource**](PollResponseResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_poll**
> PollResource create_poll(poll_resource=poll_resource)

Create a new poll

Polls are blobs of text with titles, a category and assets. Formatting and display of the text is in the hands of the front end.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
poll_resource = swagger_client.PollResource() # PollResource | The poll object (optional)

try: 
    # Create a new poll
    api_response = api_instance.create_poll(poll_resource=poll_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentPollsApi->create_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_resource** | [**PollResource**](PollResource.md)| The poll object | [optional] 

### Return type

[**PollResource**](PollResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_poll_template**
> TemplateResource create_poll_template(poll_template_resource=poll_template_resource)

Create a poll template

Poll templates define a type of poll and the properties they have

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
poll_template_resource = swagger_client.TemplateResource() # TemplateResource | The poll template resource object (optional)

try: 
    # Create a poll template
    api_response = api_instance.create_poll_template(poll_template_resource=poll_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentPollsApi->create_poll_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_template_resource** | [**TemplateResource**](TemplateResource.md)| The poll template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_poll**
> delete_poll(id)

Delete an existing poll

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
id = 'id_example' # str | The poll id

try: 
    # Delete an existing poll
    api_instance.delete_poll(id)
except ApiException as e:
    print("Exception when calling ContentPollsApi->delete_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_poll_template**
> delete_poll_template(id, cascade=cascade)

Delete a poll template

If cascade = 'detach', it will force delete the template even if it's attached to other objects

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a poll template
    api_instance.delete_poll_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling ContentPollsApi->delete_poll_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| The value needed to delete used templates | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll**
> PollResource get_poll(id)

Get a single poll

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
id = 'id_example' # str | The poll id

try: 
    # Get a single poll
    api_response = api_instance.get_poll(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentPollsApi->get_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 

### Return type

[**PollResource**](PollResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll_answer**
> PollResponseResource get_poll_answer(id)

Get poll answer

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
id = 'id_example' # str | The poll id

try: 
    # Get poll answer
    api_response = api_instance.get_poll_answer(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentPollsApi->get_poll_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 

### Return type

[**PollResponseResource**](PollResponseResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll_template**
> TemplateResource get_poll_template(id)

Get a single poll template

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single poll template
    api_response = api_instance.get_poll_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentPollsApi->get_poll_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poll_templates**
> PageResourceTemplateResource get_poll_templates(size=size, page=page, order=order)

List and search poll templates

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search poll templates
    api_response = api_instance.get_poll_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentPollsApi->get_poll_templates: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_polls**
> PageResourcePollResource get_polls(filter_category=filter_category, filter_tagset=filter_tagset, filter_text=filter_text, size=size, page=page, order=order)

List and search polls

Get a list of polls with optional filtering. Assets will not be filled in on the resources returned. Use 'Get a single poll' to retrieve the full resource with assets for a given item as needed.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
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
    print("Exception when calling ContentPollsApi->get_polls: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_poll**
> PollResource update_poll(id, poll_resource=poll_resource)

Update an existing poll

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
id = 'id_example' # str | The poll id
poll_resource = swagger_client.PollResource() # PollResource | The poll object (optional)

try: 
    # Update an existing poll
    api_response = api_instance.update_poll(id, poll_resource=poll_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentPollsApi->update_poll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The poll id | 
 **poll_resource** | [**PollResource**](PollResource.md)| The poll object | [optional] 

### Return type

[**PollResource**](PollResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_poll_template**
> TemplateResource update_poll_template(id, poll_template_resource=poll_template_resource)

Update a poll template

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ContentPollsApi()
id = 'id_example' # str | The id of the template
poll_template_resource = swagger_client.TemplateResource() # TemplateResource | The poll template resource object (optional)

try: 
    # Update a poll template
    api_response = api_instance.update_poll_template(id, poll_template_resource=poll_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentPollsApi->update_poll_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **poll_template_resource** | [**TemplateResource**](TemplateResource.md)| The poll template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
