# swagger_client.BRERuleEngineCategoriesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bre_category_template**](BRERuleEngineCategoriesApi.md#create_bre_category_template) | **POST** /bre/categories/templates | Create a BRE category template
[**delete_bre_category_template**](BRERuleEngineCategoriesApi.md#delete_bre_category_template) | **DELETE** /bre/categories/templates/{id} | Delete a BRE category template
[**get_bre_categories**](BRERuleEngineCategoriesApi.md#get_bre_categories) | **GET** /bre/categories | List categories
[**get_bre_category**](BRERuleEngineCategoriesApi.md#get_bre_category) | **GET** /bre/categories/{name} | Get a single category
[**get_bre_category_template**](BRERuleEngineCategoriesApi.md#get_bre_category_template) | **GET** /bre/categories/templates/{id} | Get a single BRE category template
[**get_bre_category_templates**](BRERuleEngineCategoriesApi.md#get_bre_category_templates) | **GET** /bre/categories/templates | List and search BRE category templates
[**update_bre_category**](BRERuleEngineCategoriesApi.md#update_bre_category) | **PUT** /bre/categories/{name} | Update a category
[**update_bre_category_template**](BRERuleEngineCategoriesApi.md#update_bre_category_template) | **PUT** /bre/categories/templates/{id} | Update a BRE category template


# **create_bre_category_template**
> TemplateResource create_bre_category_template(template=template)

Create a BRE category template

Templates define a type of BRE category and the properties they have

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
template = swagger_client.TemplateResource() # TemplateResource | The category template to create (optional)

try: 
    # Create a BRE category template
    api_response = api_instance.create_bre_category_template(template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->create_bre_category_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | [**TemplateResource**](TemplateResource.md)| The category template to create | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bre_category_template**
> delete_bre_category_template(id, cascade=cascade)

Delete a BRE category template

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a BRE category template
    api_instance.delete_bre_category_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->delete_bre_category_template: %s\n" % e)
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

# **get_bre_categories**
> PageResourceBreCategoryResource get_bre_categories(size=size, page=page)

List categories

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List categories
    api_response = api_instance.get_bre_categories(size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->get_bre_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceBreCategoryResource**](PageResourceBreCategoryResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_category**
> BreCategoryResource get_bre_category(name)

Get a single category

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
name = 'name_example' # str | The category name

try: 
    # Get a single category
    api_response = api_instance.get_bre_category(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->get_bre_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The category name | 

### Return type

[**BreCategoryResource**](BreCategoryResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_category_template**
> TemplateResource get_bre_category_template(id)

Get a single BRE category template

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single BRE category template
    api_response = api_instance.get_bre_category_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->get_bre_category_template: %s\n" % e)
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

# **get_bre_category_templates**
> PageResourceTemplateResource get_bre_category_templates(size=size, page=page, order=order)

List and search BRE category templates

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search BRE category templates
    api_response = api_instance.get_bre_category_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->get_bre_category_templates: %s\n" % e)
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

# **update_bre_category**
> update_bre_category(name, category=category)

Update a category

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
name = 'name_example' # str | The category name
category = swagger_client.BreCategoryResource() # BreCategoryResource | The updated BRE category information (optional)

try: 
    # Update a category
    api_instance.update_bre_category(name, category=category)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->update_bre_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The category name | 
 **category** | [**BreCategoryResource**](BreCategoryResource.md)| The updated BRE category information | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bre_category_template**
> update_bre_category_template(id, template=template)

Update a BRE category template

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
api_instance = swagger_client.BRERuleEngineCategoriesApi()
id = 'id_example' # str | The id of the template
template = swagger_client.TemplateResource() # TemplateResource | The updated category template definition (optional)

try: 
    # Update a BRE category template
    api_instance.update_bre_category_template(id, template=template)
except ApiException as e:
    print("Exception when calling BRERuleEngineCategoriesApi->update_bre_category_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **template** | [**TemplateResource**](TemplateResource.md)| The updated category template definition | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

