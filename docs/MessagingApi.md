# swagger_client.MessagingApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_raw_email_using_post**](MessagingApi.md#send_raw_email_using_post) | **POST** /messaging/raw-email | Send a raw email to one or more users
[**send_raw_sms_using_post**](MessagingApi.md#send_raw_sms_using_post) | **POST** /messaging/raw-sms | Send a raw SMS
[**send_raw_sms_using_post1**](MessagingApi.md#send_raw_sms_using_post1) | **POST** /messaging/templated-sms | Send a new templated SMS
[**send_template_email_using_post**](MessagingApi.md#send_template_email_using_post) | **POST** /messaging/templated-email | Send a templated email to one or more users


# **send_raw_email_using_post**
> send_raw_email_using_post(raw_email_resource=raw_email_resource)

Send a raw email to one or more users

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
raw_email_resource = swagger_client.RawEmailResource() # RawEmailResource | The new raw email to be sent (optional)

try: 
    # Send a raw email to one or more users
    api_instance.send_raw_email_using_post(raw_email_resource=raw_email_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_raw_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_email_resource** | [**RawEmailResource**](RawEmailResource.md)| The new raw email to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_raw_sms_using_post**
> send_raw_sms_using_post(raw_sms_resource=raw_sms_resource)

Send a raw SMS

Sends a raw SMS text message to one or more users. User's without registered mobile numbers will be skipped.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
raw_sms_resource = swagger_client.RawSMSResource() # RawSMSResource | The new raw SMS to be sent (optional)

try: 
    # Send a raw SMS
    api_instance.send_raw_sms_using_post(raw_sms_resource=raw_sms_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_raw_sms_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_sms_resource** | [**RawSMSResource**](RawSMSResource.md)| The new raw SMS to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_raw_sms_using_post1**
> send_raw_sms_using_post1(template_sms_resource=template_sms_resource)

Send a new templated SMS

Sends a templated SMS text message to one or more users. User's without registered mobile numbers will be skipped.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
template_sms_resource = swagger_client.TemplateSMSResource() # TemplateSMSResource | The new template SMS to be sent (optional)

try: 
    # Send a new templated SMS
    api_instance.send_raw_sms_using_post1(template_sms_resource=template_sms_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_raw_sms_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_sms_resource** | [**TemplateSMSResource**](TemplateSMSResource.md)| The new template SMS to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_template_email_using_post**
> send_template_email_using_post(message_resource=message_resource)

Send a templated email to one or more users

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
message_resource = swagger_client.TemplateEmailResource() # TemplateEmailResource | The new template email to be sent (optional)

try: 
    # Send a templated email to one or more users
    api_instance.send_template_email_using_post(message_resource=message_resource)
except ApiException as e:
    print("Exception when calling MessagingApi->send_template_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_resource** | [**TemplateEmailResource**](TemplateEmailResource.md)| The new template email to be sent | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

