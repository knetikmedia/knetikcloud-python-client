# knetik_cloud.DevicesApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_device_users**](DevicesApi.md#add_device_users) | **POST** /devices/{id}/users | Add device users
[**create_device**](DevicesApi.md#create_device) | **POST** /devices | Create a device
[**create_device_template**](DevicesApi.md#create_device_template) | **POST** /devices/templates | Create a device template
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /devices/{id} | Delete a device
[**delete_device_template**](DevicesApi.md#delete_device_template) | **DELETE** /devices/templates/{id} | Delete an device template
[**delete_device_user**](DevicesApi.md#delete_device_user) | **DELETE** /devices/{id}/users/{user_id} | Delete a device user
[**delete_device_users**](DevicesApi.md#delete_device_users) | **DELETE** /devices/{id}/users | Delete all device users
[**get_device**](DevicesApi.md#get_device) | **GET** /devices/{id} | Get a single device
[**get_device_template**](DevicesApi.md#get_device_template) | **GET** /devices/templates/{id} | Get a single device template
[**get_device_templates**](DevicesApi.md#get_device_templates) | **GET** /devices/templates | List and search device templates
[**get_devices**](DevicesApi.md#get_devices) | **GET** /devices | List and search devices
[**update_device**](DevicesApi.md#update_device) | **PUT** /devices/{id} | Update a device
[**update_device_template**](DevicesApi.md#update_device_template) | **PUT** /devices/templates/{id} | Update an device template


# **add_device_users**
> DeviceResource add_device_users(user_resources, id)

Add device users

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
user_resources = [knetik_cloud.SimpleUserResource()] # list[SimpleUserResource] | userResources
id = 'id_example' # str | id

try: 
    # Add device users
    api_response = api_instance.add_device_users(user_resources, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->add_device_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_resources** | [**list[SimpleUserResource]**](SimpleUserResource.md)| userResources | 
 **id** | **str**| id | 

### Return type

[**DeviceResource**](DeviceResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device**
> DeviceResource create_device(device)

Create a device

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
device = knetik_cloud.DeviceResource() # DeviceResource | device

try: 
    # Create a device
    api_response = api_instance.create_device(device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**DeviceResource**](DeviceResource.md)| device | 

### Return type

[**DeviceResource**](DeviceResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_template**
> TemplateResource create_device_template(device_template_resource=device_template_resource)

Create a device template

Device Templates define a type of device and the properties they have

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
device_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The device template resource object (optional)

try: 
    # Create a device template
    api_response = api_instance.create_device_template(device_template_resource=device_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_template_resource** | [**TemplateResource**](TemplateResource.md)| The device template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> delete_device(id)

Delete a device

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | id

try: 
    # Delete a device
    api_instance.delete_device(id)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_template**
> delete_device_template(id, cascade=cascade)

Delete an device template

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete an device template
    api_instance.delete_device_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device_template: %s\n" % e)
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

# **delete_device_user**
> delete_device_user(id, user_id)

Delete a device user

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the device
user_id = 56 # int | The user id of the device user

try: 
    # Delete a device user
    api_instance.delete_device_user(id, user_id)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **user_id** | **int**| The user id of the device user | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_users**
> delete_device_users(id, filter_id=filter_id)

Delete all device users

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the device
filter_id = 'filter_id_example' # str | Filter for device users to delete with a user id in a given comma separated list of ids (optional)

try: 
    # Delete all device users
    api_instance.delete_device_users(id, filter_id=filter_id)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the device | 
 **filter_id** | **str**| Filter for device users to delete with a user id in a given comma separated list of ids | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> DeviceResource get_device(id)

Get a single device

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | id

try: 
    # Get a single device
    api_response = api_instance.get_device(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**DeviceResource**](DeviceResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_template**
> TemplateResource get_device_template(id)

Get a single device template

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single device template
    api_response = api_instance.get_device_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_template: %s\n" % e)
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

# **get_device_templates**
> PageResourceTemplateResource get_device_templates(size=size, page=page, order=order)

List and search device templates

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search device templates
    api_response = api_instance.get_device_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_templates: %s\n" % e)
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

# **get_devices**
> PageResourceDeviceResource get_devices(filter_make=filter_make, filter_model=filter_model, filter_os=filter_os, filter_serial=filter_serial, filter_type=filter_type, filter_tag=filter_tag, size=size, page=page, order=order)

List and search devices

Get a list of devices with optional filtering

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
filter_make = 'filter_make_example' # str | Filter for devices with specified make (optional)
filter_model = 'filter_model_example' # str | Filter for devices with specified model (optional)
filter_os = 'filter_os_example' # str | Filter for devices with specified OS (optional)
filter_serial = 'filter_serial_example' # str | Filter for devices with specified serial (optional)
filter_type = 'filter_type_example' # str | Filter for devices with specified type (optional)
filter_tag = 'filter_tag_example' # str | A comma separated list without spaces to filter for devices with specified tags (matches any) (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search devices
    api_response = api_instance.get_devices(filter_make=filter_make, filter_model=filter_model, filter_os=filter_os, filter_serial=filter_serial, filter_type=filter_type, filter_tag=filter_tag, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_make** | **str**| Filter for devices with specified make | [optional] 
 **filter_model** | **str**| Filter for devices with specified model | [optional] 
 **filter_os** | **str**| Filter for devices with specified OS | [optional] 
 **filter_serial** | **str**| Filter for devices with specified serial | [optional] 
 **filter_type** | **str**| Filter for devices with specified type | [optional] 
 **filter_tag** | **str**| A comma separated list without spaces to filter for devices with specified tags (matches any) | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceDeviceResource**](PageResourceDeviceResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> DeviceResource update_device(device, id)

Update a device

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
device = knetik_cloud.DeviceResource() # DeviceResource | device
id = 'id_example' # str | id

try: 
    # Update a device
    api_response = api_instance.update_device(device, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**DeviceResource**](DeviceResource.md)| device | 
 **id** | **str**| id | 

### Return type

[**DeviceResource**](DeviceResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_template**
> TemplateResource update_device_template(id, device_template_resource=device_template_resource)

Update an device template

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
api_instance = knetik_cloud.DevicesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
device_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The device template resource object (optional)

try: 
    # Update an device template
    api_response = api_instance.update_device_template(id, device_template_resource=device_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **device_template_resource** | [**TemplateResource**](TemplateResource.md)| The device template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

