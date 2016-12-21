# swagger_client.CategoriesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_category_using_post**](CategoriesApi.md#create_category_using_post) | **POST** /categories | Create a new category
[**create_template_using_post2**](CategoriesApi.md#create_template_using_post2) | **POST** /categories/templates | Create a category template
[**delete_category_using_delete**](CategoriesApi.md#delete_category_using_delete) | **DELETE** /categories/{id} | Delete an existing category
[**delete_template_using_delete1**](CategoriesApi.md#delete_template_using_delete1) | **DELETE** /categories/templates/{id} | Delete a category template
[**get_article_templates_using_get1**](CategoriesApi.md#get_article_templates_using_get1) | **GET** /categories/templates | List and search category templates
[**get_categories_using_get1**](CategoriesApi.md#get_categories_using_get1) | **GET** /categories | List and search categories with optional filters
[**get_category_using_get1**](CategoriesApi.md#get_category_using_get1) | **GET** /categories/{id} | Get a single category
[**get_tags_using_get**](CategoriesApi.md#get_tags_using_get) | **GET** /tags | List all trivia tags in the system
[**get_template_using_get1**](CategoriesApi.md#get_template_using_get1) | **GET** /categories/templates/{id} | Get a single category template
[**update_category_using_put1**](CategoriesApi.md#update_category_using_put1) | **PUT** /categories/{id} | Update an existing category
[**update_template_using_put2**](CategoriesApi.md#update_template_using_put2) | **PUT** /categories/templates/{id} | Update a category template


# **create_category_using_post**
> CategoryResource create_category_using_post(category=category)

Create a new category

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
api_instance = swagger_client.CategoriesApi()
category = swagger_client.CategoryResource() # CategoryResource | The category to create (optional)

try: 
    # Create a new category
    api_response = api_instance.create_category_using_post(category=category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->create_category_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | [**CategoryResource**](CategoryResource.md)| The category to create | [optional] 

### Return type

[**CategoryResource**](CategoryResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_using_post2**
> TemplateResource create_template_using_post2(template=template)

Create a category template

Templates define a type of category and the properties they have

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
api_instance = swagger_client.CategoriesApi()
template = swagger_client.TemplateResource() # TemplateResource | The template to create (optional)

try: 
    # Create a category template
    api_response = api_instance.create_template_using_post2(template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->create_template_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | [**TemplateResource**](TemplateResource.md)| The template to create | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category_using_delete**
> delete_category_using_delete(id)

Delete an existing category

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
api_instance = swagger_client.CategoriesApi()
id = 'id_example' # str | The id of the category to be deleted

try: 
    # Delete an existing category
    api_instance.delete_category_using_delete(id)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the category to be deleted | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template_using_delete1**
> delete_template_using_delete1(id, cascade=cascade)

Delete a category template

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
api_instance = swagger_client.CategoriesApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a category template
    api_instance.delete_template_using_delete1(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_template_using_delete1: %s\n" % e)
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

# **get_article_templates_using_get1**
> PageResourceTemplateResource get_article_templates_using_get1(size=size, page=page, order=order)

List and search category templates

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
api_instance = swagger_client.CategoriesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search category templates
    api_response = api_instance.get_article_templates_using_get1(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_article_templates_using_get1: %s\n" % e)
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

# **get_categories_using_get1**
> PageResourceCategoryResource get_categories_using_get1(filter_search=filter_search, filter_active=filter_active, size=size, page=page, order=order)

List and search categories with optional filters

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CategoriesApi()
filter_search = 'filter_search_example' # str | Filter for categories whose names begin with provided string (optional)
filter_active = true # bool | Filter for categories that are specifically active or inactive (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search categories with optional filters
    api_response = api_instance.get_categories_using_get1(filter_search=filter_search, filter_active=filter_active, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_search** | **str**| Filter for categories whose names begin with provided string | [optional] 
 **filter_active** | **bool**| Filter for categories that are specifically active or inactive | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceCategoryResource**](PageResourceCategoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_using_get1**
> CategoryResource get_category_using_get1(id)

Get a single category

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CategoriesApi()
id = 'id_example' # str | The id of the category to retrieve

try: 
    # Get a single category
    api_response = api_instance.get_category_using_get1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the category to retrieve | 

### Return type

[**CategoryResource**](CategoryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_using_get**
> PageResourcestring get_tags_using_get(size=size, page=page)

List all trivia tags in the system

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CategoriesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List all trivia tags in the system
    api_response = api_instance.get_tags_using_get(size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_tags_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourcestring**](PageResourcestring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_using_get1**
> TemplateResource get_template_using_get1(id)

Get a single category template

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
api_instance = swagger_client.CategoriesApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single category template
    api_response = api_instance.get_template_using_get1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_template_using_get1: %s\n" % e)
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

# **update_category_using_put1**
> update_category_using_put1(id, category=category)

Update an existing category

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
api_instance = swagger_client.CategoriesApi()
id = 'id_example' # str | The id of the category
category = swagger_client.CategoryResource() # CategoryResource | The category to update (optional)

try: 
    # Update an existing category
    api_instance.update_category_using_put1(id, category=category)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_category_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the category | 
 **category** | [**CategoryResource**](CategoryResource.md)| The category to update | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_using_put2**
> update_template_using_put2(id, template=template)

Update a category template

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
api_instance = swagger_client.CategoriesApi()
id = 'id_example' # str | The id of the template
template = swagger_client.TemplateResource() # TemplateResource | The updated template information (optional)

try: 
    # Update a category template
    api_instance.update_template_using_put2(id, template=template)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_template_using_put2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **template** | [**TemplateResource**](TemplateResource.md)| The updated template information | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
