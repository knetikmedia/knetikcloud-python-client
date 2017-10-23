# knetik_cloud.MessagingApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_raw_email**](MessagingApi.md#send_raw_email) | **POST** /messaging/raw-email | Send a raw email to one or more users
[**send_raw_push**](MessagingApi.md#send_raw_push) | **POST** /messaging/raw-push | Send a raw push notification
[**send_raw_sms**](MessagingApi.md#send_raw_sms) | **POST** /messaging/raw-sms | Send a raw SMS
[**send_templated_email**](MessagingApi.md#send_templated_email) | **POST** /messaging/templated-email | Send a templated email to one or more users
[**send_templated_push**](MessagingApi.md#send_templated_push) | **POST** /messaging/templated-push | Send a templated push notification
[**send_templated_sms**](MessagingApi.md#send_templated_sms) | **POST** /messaging/templated-sms | Send a new templated SMS


# **send_raw_email**
> send_raw_email(raw_email_resource=raw_email_resource)

Send a raw email to one or more users

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

Sends a raw push notification message to one or more users. User's without registered mobile device for the application will be skipped.

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

Sends a raw SMS text message to one or more users. User's without registered mobile numbers will be skipped.

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

Sends a templated push notification message to one or more users. User's without registered mobile device for the application will be skipped.

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

Sends a templated SMS text message to one or more users. User's without registered mobile numbers will be skipped.

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

