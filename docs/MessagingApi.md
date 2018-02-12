# knetik_cloud.MessagingApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compile_message_template**](MessagingApi.md#compile_message_template) | **POST** /messaging/templates/compilations | Compile a message template
[**create_message_template**](MessagingApi.md#create_message_template) | **POST** /messaging/templates | Create a message template
[**delete_message_template**](MessagingApi.md#delete_message_template) | **DELETE** /messaging/templates/{id} | Delete an existing message template
[**get_message_template**](MessagingApi.md#get_message_template) | **GET** /messaging/templates/{id} | Get a single message template
[**get_message_templates**](MessagingApi.md#get_message_templates) | **GET** /messaging/templates | List and search message templates
[**send_message1**](MessagingApi.md#send_message1) | **POST** /messaging/message | Send a message
[**send_raw_email**](MessagingApi.md#send_raw_email) | **POST** /messaging/raw-email | Send a raw email to one or more users
[**send_raw_push**](MessagingApi.md#send_raw_push) | **POST** /messaging/raw-push | Send a raw push notification
[**send_raw_sms**](MessagingApi.md#send_raw_sms) | **POST** /messaging/raw-sms | Send a raw SMS
[**send_templated_email**](MessagingApi.md#send_templated_email) | **POST** /messaging/templated-email | Send a templated email to one or more users
[**send_templated_push**](MessagingApi.md#send_templated_push) | **POST** /messaging/templated-push | Send a templated push notification
[**send_templated_sms**](MessagingApi.md#send_templated_sms) | **POST** /messaging/templated-sms | Send a new templated SMS
[**send_websocket**](MessagingApi.md#send_websocket) | **POST** /messaging/websocket-message | Send a websocket message
[**update_message_template**](MessagingApi.md#update_message_template) | **PUT** /messaging/templates/{id} | Update an existing message template


# **compile_message_template**
> dict(str, str) compile_message_template(request=request)

Compile a message template

Processes a set of input data against the template and returnes the compiled result. <br><br><b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
request = knetik_cloud.MessageTemplateBulkRequest() # MessageTemplateBulkRequest | request (optional)

try: 
    # Compile a message template
    api_response = api_instance.compile_message_template(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->compile_message_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**MessageTemplateBulkRequest**](MessageTemplateBulkRequest.md)| request | [optional] 

### Return type

**dict(str, str)**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_message_template**
> MessageTemplateResource create_message_template(message_template=message_template)

Create a message template

<b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
message_template = knetik_cloud.MessageTemplateResource() # MessageTemplateResource | The new template email to be sent (optional)

try: 
    # Create a message template
    api_response = api_instance.create_message_template(message_template=message_template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->create_message_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_template** | [**MessageTemplateResource**](MessageTemplateResource.md)| The new template email to be sent | [optional] 

### Return type

[**MessageTemplateResource**](MessageTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message_template**
> delete_message_template(id)

Delete an existing message template

<b>Permissions Needed:</b> ARTICLES_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The message_template id

try: 
    # Delete an existing message template
    api_instance.delete_message_template(id)
except ApiException as e:
    print("Exception when calling MessagingApi->delete_message_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The message_template id | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_template**
> MessageTemplateResource get_message_template(id)

Get a single message template

<b>Permissions Needed:</b> ARTICLES_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The message_template id

try: 
    # Get a single message template
    api_response = api_instance.get_message_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_message_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The message_template id | 

### Return type

[**MessageTemplateResource**](MessageTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_templates**
> PageResourceMessageTemplateResource get_message_templates(filter_tagset=filter_tagset, filter_tag_intersection=filter_tag_intersection, filter_tag_exclusion=filter_tag_exclusion, size=size, page=page, order=order)

List and search message templates

Get a list of message templates with optional filtering. <br><br><b>Permissions Needed:</b> ARTICLES_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
filter_tagset = 'filter_tagset_example' # str | Filter for message templates with at least one of a specified set of tags (separated by comma) (optional)
filter_tag_intersection = 'filter_tag_intersection_example' # str | Filter for message templates with all of a specified set of tags (separated by comma) (optional)
filter_tag_exclusion = 'filter_tag_exclusion_example' # str | Filter for message templates with none of a specified set of tags (separated by comma) (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search message templates
    api_response = api_instance.get_message_templates(filter_tagset=filter_tagset, filter_tag_intersection=filter_tag_intersection, filter_tag_exclusion=filter_tag_exclusion, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->get_message_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_tagset** | **str**| Filter for message templates with at least one of a specified set of tags (separated by comma) | [optional] 
 **filter_tag_intersection** | **str**| Filter for message templates with all of a specified set of tags (separated by comma) | [optional] 
 **filter_tag_exclusion** | **str**| Filter for message templates with none of a specified set of tags (separated by comma) | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceMessageTemplateResource**](PageResourceMessageTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message1**
> send_message1(message_resource=message_resource)

Send a message

Sends a message with one or more formats to one or more users. Fill in any message formats desired (email, sms, websockets) and each user will recieve all valid formats. <br><br><b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
message_resource = knetik_cloud.MessageResource() # MessageResource | The message to be sent (optional)

try: 
    # Send a message
    api_instance.send_message1(message_resource=message_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_message1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_resource** | [**MessageResource**](MessageResource.md)| The message to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_raw_email**
> send_raw_email(raw_email_resource=raw_email_resource)

Send a raw email to one or more users

<b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
raw_email_resource = knetik_cloud.RawEmailResource() # RawEmailResource | The new raw email to be sent (optional)

try: 
    # Send a raw email to one or more users
    api_instance.send_raw_email(raw_email_resource=raw_email_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_raw_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_email_resource** | [**RawEmailResource**](RawEmailResource.md)| The new raw email to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_raw_push**
> send_raw_push(raw_push_resource=raw_push_resource)

Send a raw push notification

Sends a raw push notification message to one or more users. User's without registered mobile device for the application will be skipped. <br><br><b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
raw_push_resource = knetik_cloud.RawPushResource() # RawPushResource | The new raw push notification to be sent (optional)

try: 
    # Send a raw push notification
    api_instance.send_raw_push(raw_push_resource=raw_push_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_raw_push: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_push_resource** | [**RawPushResource**](RawPushResource.md)| The new raw push notification to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_raw_sms**
> send_raw_sms(raw_sms_resource=raw_sms_resource)

Send a raw SMS

Sends a raw SMS text message to one or more users. User's without registered mobile numbers will be skipped. <br><br><b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
raw_sms_resource = knetik_cloud.RawSMSResource() # RawSMSResource | The new raw SMS to be sent (optional)

try: 
    # Send a raw SMS
    api_instance.send_raw_sms(raw_sms_resource=raw_sms_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_raw_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_sms_resource** | [**RawSMSResource**](RawSMSResource.md)| The new raw SMS to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_templated_email**
> send_templated_email(message_resource=message_resource)

Send a templated email to one or more users

<b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
message_resource = knetik_cloud.TemplateEmailResource() # TemplateEmailResource | The new template email to be sent (optional)

try: 
    # Send a templated email to one or more users
    api_instance.send_templated_email(message_resource=message_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_templated_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_resource** | [**TemplateEmailResource**](TemplateEmailResource.md)| The new template email to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_templated_push**
> send_templated_push(template_push_resource=template_push_resource)

Send a templated push notification

Sends a templated push notification message to one or more users. User's without registered mobile device for the application will be skipped. <br><br><b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
template_push_resource = knetik_cloud.TemplatePushResource() # TemplatePushResource | The new templated push notification to be sent (optional)

try: 
    # Send a templated push notification
    api_instance.send_templated_push(template_push_resource=template_push_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_templated_push: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_push_resource** | [**TemplatePushResource**](TemplatePushResource.md)| The new templated push notification to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_templated_sms**
> send_templated_sms(template_sms_resource=template_sms_resource)

Send a new templated SMS

Sends a templated SMS text message to one or more users. User's without registered mobile numbers will be skipped. <br><br><b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
template_sms_resource = knetik_cloud.TemplateSMSResource() # TemplateSMSResource | The new template SMS to be sent (optional)

try: 
    # Send a new templated SMS
    api_instance.send_templated_sms(template_sms_resource=template_sms_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_templated_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_sms_resource** | [**TemplateSMSResource**](TemplateSMSResource.md)| The new template SMS to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_websocket**
> send_websocket(websocket_resource=websocket_resource)

Send a websocket message

Sends a websocket message to one or more users. <br><br><b>Permissions Needed:</b> MESSAGING_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
websocket_resource = knetik_cloud.WebsocketMessageResource() # WebsocketMessageResource | The new websocket message to be sent (optional)

try: 
    # Send a websocket message
    api_instance.send_websocket(websocket_resource=websocket_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_websocket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **websocket_resource** | [**WebsocketMessageResource**](WebsocketMessageResource.md)| The new websocket message to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_message_template**
> MessageTemplateResource update_message_template(id, message_template_resource=message_template_resource)

Update an existing message template

<b>Permissions Needed:</b> ARTICLES_ADMIN

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
api_instance = knetik_cloud.MessagingApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The message_template id
message_template_resource = knetik_cloud.MessageTemplateResource() # MessageTemplateResource | The message template (optional)

try: 
    # Update an existing message template
    api_response = api_instance.update_message_template(id, message_template_resource=message_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingApi->update_message_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The message_template id | 
 **message_template_resource** | [**MessageTemplateResource**](MessageTemplateResource.md)| The message template | [optional] 

### Return type

[**MessageTemplateResource**](MessageTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

