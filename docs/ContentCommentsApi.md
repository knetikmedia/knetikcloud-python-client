# swagger_client.ContentCommentsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment_using_post**](ContentCommentsApi.md#add_comment_using_post) | **POST** /comments | Add a new comment
[**delete_comment_using_delete**](ContentCommentsApi.md#delete_comment_using_delete) | **DELETE** /comments/{id} | Delete a comment
[**get_comment_using_get**](ContentCommentsApi.md#get_comment_using_get) | **GET** /comments/{id} | Returns a comment by comment id
[**get_comments_using_get**](ContentCommentsApi.md#get_comments_using_get) | **GET** /comments | Returns a page of comments
[**search_comments_using_post**](ContentCommentsApi.md#search_comments_using_post) | **POST** /comments/search | Search the comment index
[**update_comment_using_put**](ContentCommentsApi.md#update_comment_using_put) | **PUT** /comments/{id}/content | Update comment content


# **add_comment_using_post**
> CommentResource add_comment_using_post(comment_resource=comment_resource)

Add a new comment

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
api_instance = swagger_client.ContentCommentsApi()
comment_resource = swagger_client.CommentResource() # CommentResource | The comment to be added (optional)

try: 
    # Add a new comment
    api_response = api_instance.add_comment_using_post(comment_resource=comment_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentCommentsApi->add_comment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_resource** | [**CommentResource**](CommentResource.md)| The comment to be added | [optional] 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment_using_delete**
> delete_comment_using_delete(id)

Delete a comment

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
api_instance = swagger_client.ContentCommentsApi()
id = 789 # int | The comment id

try: 
    # Delete a comment
    api_instance.delete_comment_using_delete(id)
except ApiException as e:
    print("Exception when calling ContentCommentsApi->delete_comment_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The comment id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment_using_get**
> CommentResource get_comment_using_get(id)

Returns a comment by comment id

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentCommentsApi()
id = 789 # int | The comment id

try: 
    # Returns a comment by comment id
    api_response = api_instance.get_comment_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentCommentsApi->get_comment_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The comment id | 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments_using_get**
> PageResourceCommentResource get_comments_using_get(context, context_id, size=size, page=page)

Returns a page of comments

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentCommentsApi()
context = 'context_example' # str | Get comments by context type
context_id = 56 # int | Get comments by context id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of comments
    api_response = api_instance.get_comments_using_get(context, context_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentCommentsApi->get_comments_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context** | **str**| Get comments by context type | 
 **context_id** | **int**| Get comments by context id | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceCommentResource**](PageResourceCommentResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_comments_using_post**
> CommentSearch search_comments_using_post(query=query, size=size, page=page)

Search the comment index

The body is an ElasticSearch query json. Please see their <a href='https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html'>documentation</a> for details on the format and search options

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContentCommentsApi()
query = NULL # object | The search query (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Search the comment index
    api_response = api_instance.search_comments_using_post(query=query, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentCommentsApi->search_comments_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **object**| The search query | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**CommentSearch**](CommentSearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment_using_put**
> update_comment_using_put(id, content=content)

Update comment content

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
api_instance = swagger_client.ContentCommentsApi()
id = 789 # int | The comment id
content = 'content_example' # str | The comment content (optional)

try: 
    # Update comment content
    api_instance.update_comment_using_put(id, content=content)
except ApiException as e:
    print("Exception when calling ContentCommentsApi->update_comment_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The comment id | 
 **content** | **str**| The comment content | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

