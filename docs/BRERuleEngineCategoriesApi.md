# swagger_client.BRERuleEngineCategoriesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_template_using_post1**](BRERuleEngineCategoriesApi.md#create_template_using_post1) | **POST** /bre/categories/templates | Create a BRE category template
[**delete_template_using_delete**](BRERuleEngineCategoriesApi.md#delete_template_using_delete) | **DELETE** /bre/categories/templates/{id} | Delete a BRE category template
[**get_categories_using_get**](BRERuleEngineCategoriesApi.md#get_categories_using_get) | **GET** /bre/categories | List categories
[**get_category_using_get**](BRERuleEngineCategoriesApi.md#get_category_using_get) | **GET** /bre/categories/{name} | Get a single category
[**get_template_using_get**](BRERuleEngineCategoriesApi.md#get_template_using_get) | **GET** /bre/categories/templates/{id} | Get a single BRE category template
[**get_templates_using_get**](BRERuleEngineCategoriesApi.md#get_templates_using_get) | **GET** /bre/categories/templates | List and search BRE category templates
[**update_category_using_put**](BRERuleEngineCategoriesApi.md#update_category_using_put) | **PUT** /bre/categories/{name} | Update a category
[**update_template_using_put1**](BRERuleEngineCategoriesApi.md#update_template_using_put1) | **PUT** /bre/categories/templates/{id} | Update a BRE category template


# **create_template_using_post1**
> TemplateResource create_template_using_post1(template=template)

Create a BRE category template

Templates define a type of BRE category and the properties they have

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
template = swagger_client.TemplateResource() # TemplateResource | The category template to create (optional)

try: 
    # Create a BRE category template
    api_response = api_instance.create_template_using_post1(template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->create_template_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | [**TemplateResource**](TemplateResource.md)| The category template to create | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_using_delete**
> delete_template_using_delete(id, cascade=cascade)

Delete a BRE category template

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a BRE category template
    api_instance.delete_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->delete_template_using_delete: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories_using_get**
> PageBreCategoryResource get_categories_using_get(size=size, page=page)

List categories

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List categories
    api_response = api_instance.get_categories_using_get(size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->get_categories_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageBreCategoryResource**](PageBreCategoryResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_using_get**
> BreCategoryResource get_category_using_get(name)

Get a single category

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
name = 'name_example' # str | The category name

try: 
    # Get a single category
    api_response = api_instance.get_category_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->get_category_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The category name | 

### Return type

[**BreCategoryResource**](BreCategoryResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_using_get**
> TemplateResource get_template_using_get(id)

Get a single BRE category template

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single BRE category template
    api_response = api_instance.get_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->get_template_using_get: %s\n" % e)
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
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates_using_get**
> PageTemplateResource get_templates_using_get(size=size, page=page, order=order)

List and search BRE category templates

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # List and search BRE category templates
    api_response = api_instance.get_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->get_templates_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageTemplateResource**](PageTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category_using_put**
> update_category_using_put(name, category=category)

Update a category

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
name = 'name_example' # str | The category name
category = swagger_client.BreCategoryResource() # BreCategoryResource | The updated BRE category information (optional)

try: 
    # Update a category
    api_instance.update_category_using_put(name, category=category)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->update_category_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The category name | 
 **category** | [**BreCategoryResource**](BreCategoryResource.md)| The updated BRE category information | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_using_put1**
> update_template_using_put1(id, template=template)

Update a BRE category template

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
id = 'id_example' # str | The id of the template
template = swagger_client.TemplateResource() # TemplateResource | The updated category template definition (optional)

try: 
    # Update a BRE category template
    api_instance.update_template_using_put1(id, template=template)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->update_template_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **template** | [**TemplateResource**](TemplateResource.md)| The updated category template definition | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

