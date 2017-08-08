# knetik_cloud.StoreSubscriptionsApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](StoreSubscriptionsApi.md#create_subscription) | **POST** /subscriptions | Creates a subscription item and associated plans
[**create_subscription_template**](StoreSubscriptionsApi.md#create_subscription_template) | **POST** /subscriptions/templates | Create a subscription template
[**delete_subscription**](StoreSubscriptionsApi.md#delete_subscription) | **DELETE** /subscriptions/{id}/plans/{plan_id} | Delete a subscription plan
[**delete_subscription_template**](StoreSubscriptionsApi.md#delete_subscription_template) | **DELETE** /subscriptions/templates/{id} | Delete a subscription template
[**get_subscription**](StoreSubscriptionsApi.md#get_subscription) | **GET** /subscriptions/{id} | Retrieve a single subscription item and associated plans
[**get_subscription_template**](StoreSubscriptionsApi.md#get_subscription_template) | **GET** /subscriptions/templates/{id} | Get a single subscription template
[**get_subscription_templates**](StoreSubscriptionsApi.md#get_subscription_templates) | **GET** /subscriptions/templates | List and search subscription templates
[**get_subscriptions**](StoreSubscriptionsApi.md#get_subscriptions) | **GET** /subscriptions | List available subscription items and associated plans
[**process_subscriptions**](StoreSubscriptionsApi.md#process_subscriptions) | **POST** /subscriptions/process | Processes subscriptions and charge dues
[**update_subscription**](StoreSubscriptionsApi.md#update_subscription) | **PUT** /subscriptions/{id} | Updates a subscription item and associated plans
[**update_subscription_template**](StoreSubscriptionsApi.md#update_subscription_template) | **PUT** /subscriptions/templates/{id} | Update a subscription template


# **create_subscription**
> SubscriptionResource create_subscription(subscription_resource=subscription_resource)

Creates a subscription item and associated plans

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi(knetik_cloud.ApiClient(configuration))
subscription_resource = knetik_cloud.SubscriptionResource() # SubscriptionResource | The subscription to be created (optional)

try: 
    # Creates a subscription item and associated plans
    api_response = api_instance.create_subscription(subscription_resource=subscription_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_resource** | [**SubscriptionResource**](SubscriptionResource.md)| The subscription to be created | [optional] 

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_template**
> SubscriptionTemplateResource create_subscription_template(subscription_template_resource=subscription_template_resource)

Create a subscription template

Subscription Templates define a type of subscription and the properties they have.

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi(knetik_cloud.ApiClient(configuration))
subscription_template_resource = knetik_cloud.SubscriptionTemplateResource() # SubscriptionTemplateResource | The new subscription template (optional)

try: 
    # Create a subscription template
    api_response = api_instance.create_subscription_template(subscription_template_resource=subscription_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->create_subscription_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_template_resource** | [**SubscriptionTemplateResource**](SubscriptionTemplateResource.md)| The new subscription template | [optional] 

### Return type

[**SubscriptionTemplateResource**](SubscriptionTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(id, plan_id)

Delete a subscription plan

Must not be locked or a migration target

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id of the subscription
plan_id = 'plan_id_example' # str | The id of the plan

try: 
    # Delete a subscription plan
    api_instance.delete_subscription(id, plan_id)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the subscription | 
 **plan_id** | **str**| The id of the plan | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription_template**
> delete_subscription_template(id, cascade=cascade)

Delete a subscription template

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | force deleting the template if it's attached to other objects, cascade = detach (optional)

try: 
    # Delete a subscription template
    api_instance.delete_subscription_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->delete_subscription_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| force deleting the template if it&#39;s attached to other objects, cascade &#x3D; detach | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> SubscriptionResource get_subscription(id)

Retrieve a single subscription item and associated plans

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi()
id = 56 # int | The id of the subscription

try: 
    # Retrieve a single subscription item and associated plans
    api_response = api_instance.get_subscription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the subscription | 

### Return type

[**SubscriptionResource**](SubscriptionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_template**
> SubscriptionTemplateResource get_subscription_template(id)

Get a single subscription template

Subscription Templates define a type of subscription and the properties they have.

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single subscription template
    api_response = api_instance.get_subscription_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->get_subscription_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**SubscriptionTemplateResource**](SubscriptionTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_templates**
> PageResourceSubscriptionTemplateResource get_subscription_templates(size=size, page=page, order=order)

List and search subscription templates

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search subscription templates
    api_response = api_instance.get_subscription_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->get_subscription_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceSubscriptionTemplateResource**](PageResourceSubscriptionTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> PageResourceSubscriptionResource get_subscriptions(size=size, page=page, order=order)

List available subscription items and associated plans

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List available subscription items and associated plans
    api_response = api_instance.get_subscriptions(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->get_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceSubscriptionResource**](PageResourceSubscriptionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_subscriptions**
> process_subscriptions()

Processes subscriptions and charge dues

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi(knetik_cloud.ApiClient(configuration))

try: 
    # Processes subscriptions and charge dues
    api_instance.process_subscriptions()
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->process_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> update_subscription(id, subscription_resource=subscription_resource)

Updates a subscription item and associated plans

Will not remove plans left out

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id of the subscription
subscription_resource = knetik_cloud.SubscriptionResource() # SubscriptionResource | The subscription resource object (optional)

try: 
    # Updates a subscription item and associated plans
    api_instance.update_subscription(id, subscription_resource=subscription_resource)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->update_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the subscription | 
 **subscription_resource** | [**SubscriptionResource**](SubscriptionResource.md)| The subscription resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_template**
> SubscriptionTemplateResource update_subscription_template(id, subscription_template_resource=subscription_template_resource)

Update a subscription template

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreSubscriptionsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
subscription_template_resource = knetik_cloud.SubscriptionTemplateResource() # SubscriptionTemplateResource | The subscription template resource object (optional)

try: 
    # Update a subscription template
    api_response = api_instance.update_subscription_template(id, subscription_template_resource=subscription_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->update_subscription_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **subscription_template_resource** | [**SubscriptionTemplateResource**](SubscriptionTemplateResource.md)| The subscription template resource object | [optional] 

### Return type

[**SubscriptionTemplateResource**](SubscriptionTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

