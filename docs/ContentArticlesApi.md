# swagger_client.ContentArticlesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_article_template_using_post**](ContentArticlesApi.md#create_article_template_using_post) | **POST** /content/articles/templates | Create an article template
[**create_article_using_post**](ContentArticlesApi.md#create_article_using_post) | **POST** /content/articles | Create a new article
[**delete_article_template_using_delete**](ContentArticlesApi.md#delete_article_template_using_delete) | **DELETE** /content/articles/templates/{id} | Delete an article template
[**delete_article_using_delete**](ContentArticlesApi.md#delete_article_using_delete) | **DELETE** /content/articles/{id} | Delete an existing article
[**get_article_template_using_get**](ContentArticlesApi.md#get_article_template_using_get) | **GET** /content/articles/templates/{id} | Get a single article template
[**get_article_templates_using_get**](ContentArticlesApi.md#get_article_templates_using_get) | **GET** /content/articles/templates | List and search article templates
[**get_article_using_get**](ContentArticlesApi.md#get_article_using_get) | **GET** /content/articles/{id} | Get a single article
[**get_articles_using_get**](ContentArticlesApi.md#get_articles_using_get) | **GET** /content/articles | List and search articles
[**update_article_template_using_put**](ContentArticlesApi.md#update_article_template_using_put) | **PUT** /content/articles/templates/{id} | Update an article template
[**update_article_using_put**](ContentArticlesApi.md#update_article_using_put) | **PUT** /content/articles/{id} | Update an existing article


# **create_article_template_using_post**
> TemplateResource create_article_template_using_post(article_template_resource=article_template_resource)

Create an article template

Article Templates define a type of article and the properties they have

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
api_instance = swagger_client.ContentArticlesApi()
article_template_resource = swagger_client.TemplateResource() # TemplateResource | The article template resource object (optional)

try: 
    # Create an article template
    api_response = api_instance.create_article_template_using_post(article_template_resource=article_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->create_article_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_template_resource** | [**TemplateResource**](TemplateResource.md)| The article template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_article_using_post**
> ArticleResource create_article_using_post(article_resource=article_resource)

Create a new article

Articles are blobs of text with titles, a category and assets. Formatting and display of the text is in the hands of the front end.

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
api_instance = swagger_client.ContentArticlesApi()
article_resource = swagger_client.ArticleResource() # ArticleResource | The new article (optional)

try: 
    # Create a new article
    api_response = api_instance.create_article_using_post(article_resource=article_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->create_article_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_resource** | [**ArticleResource**](ArticleResource.md)| The new article | [optional] 

### Return type

[**ArticleResource**](ArticleResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_article_template_using_delete**
> delete_article_template_using_delete(id, cascade=cascade)

Delete an article template

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
api_instance = swagger_client.ContentArticlesApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete an article template
    api_instance.delete_article_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->delete_article_template_using_delete: %s\n" % e)
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

# **delete_article_using_delete**
> delete_article_using_delete(id)

Delete an existing article

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
api_instance = swagger_client.ContentArticlesApi()
id = 'id_example' # str | The article id

try: 
    # Delete an existing article
    api_instance.delete_article_using_delete(id)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->delete_article_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The article id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_article_template_using_get**
> TemplateResource get_article_template_using_get(id)

Get a single article template

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
api_instance = swagger_client.ContentArticlesApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single article template
    api_response = api_instance.get_article_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->get_article_template_using_get: %s\n" % e)
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

# **get_article_templates_using_get**
> PageTemplateResource get_article_templates_using_get(size=size, page=page, order=order)

List and search article templates

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
api_instance = swagger_client.ContentArticlesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search article templates
    api_response = api_instance.get_article_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->get_article_templates_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageTemplateResource**](PageTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_article_using_get**
> ArticleResource get_article_using_get(id)

Get a single article

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentArticlesApi()
id = 'id_example' # str | The article id

try: 
    # Get a single article
    api_response = api_instance.get_article_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->get_article_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The article id | 

### Return type

[**ArticleResource**](ArticleResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_articles_using_get**
> PageArticleResource get_articles_using_get(filter_category=filter_category, filter_tagset=filter_tagset, filter_title=filter_title, size=size, page=page, order=order)

List and search articles

Get a list of articles with optional filtering. Assets will not be filled in on the resources returned. Use 'Get a single article' to retrieve the full resource with assets for a given item as needed.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentArticlesApi()
filter_category = 'filter_category_example' # str | Filter for articles from a specific category by id (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for articles with specified tags (separated by comma) (optional)
filter_title = 'filter_title_example' # str | Filter for articles whose title contains a string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search articles
    api_response = api_instance.get_articles_using_get(filter_category=filter_category, filter_tagset=filter_tagset, filter_title=filter_title, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->get_articles_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_category** | **str**| Filter for articles from a specific category by id | [optional] 
 **filter_tagset** | **str**| Filter for articles with specified tags (separated by comma) | [optional] 
 **filter_title** | **str**| Filter for articles whose title contains a string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageArticleResource**](PageArticleResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_article_template_using_put**
> update_article_template_using_put(id, article_template_resource=article_template_resource)

Update an article template

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
api_instance = swagger_client.ContentArticlesApi()
id = 'id_example' # str | The id of the template
article_template_resource = swagger_client.TemplateResource() # TemplateResource | The article template resource object (optional)

try: 
    # Update an article template
    api_instance.update_article_template_using_put(id, article_template_resource=article_template_resource)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->update_article_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **article_template_resource** | [**TemplateResource**](TemplateResource.md)| The article template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_article_using_put**
> update_article_using_put(id, article_resource=article_resource)

Update an existing article

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
api_instance = swagger_client.ContentArticlesApi()
id = 'id_example' # str | The article id
article_resource = swagger_client.ArticleResource() # ArticleResource | The article object (optional)

try: 
    # Update an existing article
    api_instance.update_article_using_put(id, article_resource=article_resource)
except ApiException as e:
    print("Exception when calling ContentArticlesApi->update_article_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The article id | 
 **article_resource** | [**ArticleResource**](ArticleResource.md)| The article object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

