# swagger_client.StoreSubscriptionsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription_template_using_post**](StoreSubscriptionsApi.md#create_subscription_template_using_post) | **POST** /subscriptions/templates | Create a subscription template
[**create_subscription_using_post**](StoreSubscriptionsApi.md#create_subscription_using_post) | **POST** /subscriptions | Creates a subscription item and associated plans
[**delete_plan_using_delete**](StoreSubscriptionsApi.md#delete_plan_using_delete) | **DELETE** /subscriptions/{id}/plans/{plan_id} | Delete a subscription plan
[**delete_subscription_template_using_delete**](StoreSubscriptionsApi.md#delete_subscription_template_using_delete) | **DELETE** /subscriptions/templates/{id} | Delete a subscription template
[**get_subscription_template_using_get**](StoreSubscriptionsApi.md#get_subscription_template_using_get) | **GET** /subscriptions/templates/{id} | Get a single subscription template
[**get_subscription_templates_using_get**](StoreSubscriptionsApi.md#get_subscription_templates_using_get) | **GET** /subscriptions/templates | List and search subscription templates
[**get_subscription_using_get**](StoreSubscriptionsApi.md#get_subscription_using_get) | **GET** /subscriptions/{id} | Retrieve a single subscription item and associated plans
[**list_subscriptions_using_get**](StoreSubscriptionsApi.md#list_subscriptions_using_get) | **GET** /subscriptions | List available subscription items and associated plans
[**process_using_post**](StoreSubscriptionsApi.md#process_using_post) | **POST** /subscriptions/process | Processes subscriptions and charge dues
[**update_subscription_template_using_put**](StoreSubscriptionsApi.md#update_subscription_template_using_put) | **PUT** /subscriptions/templates/{id} | Update a subscription template
[**update_subscription_using_put**](StoreSubscriptionsApi.md#update_subscription_using_put) | **PUT** /subscriptions/{id} | Updates a subscription item and associated plans


# **create_subscription_template_using_post**
> SubscriptionTemplateResource create_subscription_template_using_post(subscription_template_resource=subscription_template_resource)

Create a subscription template

Subscription Templates define a type of subscription and the properties they have.

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
api_instance = swagger_client.StoreSubscriptionsApi()
subscription_template_resource = swagger_client.SubscriptionTemplateResource() # SubscriptionTemplateResource | The new subscription template (optional)

try: 
    # Create a subscription template
    api_response = api_instance.create_subscription_template_using_post(subscription_template_resource=subscription_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->create_subscription_template_using_post: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_using_post**
> SubscriptionResource create_subscription_using_post(subscription_resource=subscription_resource)

Creates a subscription item and associated plans

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
api_instance = swagger_client.StoreSubscriptionsApi()
subscription_resource = swagger_client.SubscriptionResource() # SubscriptionResource | The subscription to be created (optional)

try: 
    # Creates a subscription item and associated plans
    api_response = api_instance.create_subscription_using_post(subscription_resource=subscription_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->create_subscription_using_post: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plan_using_delete**
> delete_plan_using_delete(id, plan_id)

Delete a subscription plan

Must not be locked or a migration target

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
api_instance = swagger_client.StoreSubscriptionsApi()
id = 56 # int | The id of the subscription
plan_id = 'plan_id_example' # str | The id of the plan

try: 
    # Delete a subscription plan
    api_instance.delete_plan_using_delete(id, plan_id)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->delete_plan_using_delete: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription_template_using_delete**
> delete_subscription_template_using_delete(id, cascade=cascade)

Delete a subscription template

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
api_instance = swagger_client.StoreSubscriptionsApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | force deleting the template if it's attached to other objects, cascade = detach (optional)

try: 
    # Delete a subscription template
    api_instance.delete_subscription_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->delete_subscription_template_using_delete: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_template_using_get**
> SubscriptionTemplateResource get_subscription_template_using_get(id)

Get a single subscription template

Subscription Templates define a type of subscription and the properties they have.

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
api_instance = swagger_client.StoreSubscriptionsApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single subscription template
    api_response = api_instance.get_subscription_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->get_subscription_template_using_get: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_templates_using_get**
> PageSubscriptionTemplateResource get_subscription_templates_using_get(size=size, page=page, order=order)

List and search subscription templates

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
api_instance = swagger_client.StoreSubscriptionsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search subscription templates
    api_response = api_instance.get_subscription_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->get_subscription_templates_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageSubscriptionTemplateResource**](PageSubscriptionTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_using_get**
> SubscriptionResource get_subscription_using_get(id)

Retrieve a single subscription item and associated plans

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreSubscriptionsApi()
id = 56 # int | The id of the subscription

try: 
    # Retrieve a single subscription item and associated plans
    api_response = api_instance.get_subscription_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->get_subscription_using_get: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions_using_get**
> PageSubscriptionResource list_subscriptions_using_get(size=size, page=page, order=order)

List available subscription items and associated plans

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreSubscriptionsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List available subscription items and associated plans
    api_response = api_instance.list_subscriptions_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->list_subscriptions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageSubscriptionResource**](PageSubscriptionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_using_post**
> process_using_post()

Processes subscriptions and charge dues

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
api_instance = swagger_client.StoreSubscriptionsApi()

try: 
    # Processes subscriptions and charge dues
    api_instance.process_using_post()
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->process_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_template_using_put**
> update_subscription_template_using_put(id, subscription_template_resource=subscription_template_resource)

Update a subscription template

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
api_instance = swagger_client.StoreSubscriptionsApi()
id = 'id_example' # str | The id of the template
subscription_template_resource = swagger_client.SubscriptionTemplateResource() # SubscriptionTemplateResource | The subscription template resource object (optional)

try: 
    # Update a subscription template
    api_instance.update_subscription_template_using_put(id, subscription_template_resource=subscription_template_resource)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->update_subscription_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **subscription_template_resource** | [**SubscriptionTemplateResource**](SubscriptionTemplateResource.md)| The subscription template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_using_put**
> update_subscription_using_put(id, subscription_resource=subscription_resource)

Updates a subscription item and associated plans

Will not remove plans left out

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
api_instance = swagger_client.StoreSubscriptionsApi()
id = 56 # int | The id of the subscription
subscription_resource = swagger_client.SubscriptionResource() # SubscriptionResource | The subscription resource object (optional)

try: 
    # Updates a subscription item and associated plans
    api_instance.update_subscription_using_put(id, subscription_resource=subscription_resource)
except ApiException as e:
    print("Exception when calling StoreSubscriptionsApi->update_subscription_using_put: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

