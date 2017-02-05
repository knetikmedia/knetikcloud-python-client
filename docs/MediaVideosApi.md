# swagger_client.MediaVideosApi

All URIs are relative to *https://integration.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment_using_post1**](MediaVideosApi.md#add_comment_using_post1) | **POST** /media/videos/{video_id}/comments | Add a new video comment
[**add_contributor_using_post**](MediaVideosApi.md#add_contributor_using_post) | **POST** /media/videos/{video_id}/contributors | Adds a contributor to a video
[**add_disposition_using_post1**](MediaVideosApi.md#add_disposition_using_post1) | **POST** /media/videos/{video_id}/dispositions | Add a new Video disposition
[**add_flag_using_post**](MediaVideosApi.md#add_flag_using_post) | **POST** /media/videos/{video_id}/moderation | Add a new flag
[**add_related_using_post**](MediaVideosApi.md#add_related_using_post) | **POST** /media/videos/{video_id}/related | Adds one or more existing videos as related to this one
[**add_video_using_post**](MediaVideosApi.md#add_video_using_post) | **POST** /media/videos | Adds a new video in the system
[**add_whitelist_using_post**](MediaVideosApi.md#add_whitelist_using_post) | **POST** /media/videos/{id}/whitelist | Adds a user to a video&#39;s whitelist
[**delete_comment_using_delete1**](MediaVideosApi.md#delete_comment_using_delete1) | **DELETE** /media/videos/{video_id}/comments/{id} | Delete a video comment
[**delete_disposition_using_delete1**](MediaVideosApi.md#delete_disposition_using_delete1) | **DELETE** /media/videos/{video_id}/dispositions/{disposition_id} | Delete a video comment
[**delete_flag_using_delete**](MediaVideosApi.md#delete_flag_using_delete) | **DELETE** /media/videos/{video_id}/moderation | Delete a flag
[**delete_relationship_using_delete1**](MediaVideosApi.md#delete_relationship_using_delete1) | **DELETE** /media/videos/{video_id}/related/{id} | Delete a video&#39;s relationship
[**delete_video_using_delete**](MediaVideosApi.md#delete_video_using_delete) | **DELETE** /media/videos/{id} | Removes a video from the system if no resources are attached to it
[**get_comments_using_get1**](MediaVideosApi.md#get_comments_using_get1) | **GET** /media/videos/{video_id}/comments | Returns a page of comments for a video
[**get_dispositions_using_get1**](MediaVideosApi.md#get_dispositions_using_get1) | **GET** /media/videos/{video_id}/dispositions | Returns a page of dispositions for a video
[**get_related_using_get**](MediaVideosApi.md#get_related_using_get) | **GET** /media/videos/{video_id}/related | Returns a page of video relationships
[**get_user_videos_using_get**](MediaVideosApi.md#get_user_videos_using_get) | **GET** /users/{user_id}/videos | Get user videos
[**get_video_using_get**](MediaVideosApi.md#get_video_using_get) | **GET** /media/videos/{id} | Loads a specific video details
[**remove_contributor_using_delete**](MediaVideosApi.md#remove_contributor_using_delete) | **DELETE** /media/videos/{video_id}/contributors/{id} | Removes a contributor from a video
[**remove_whitelist_using_delete**](MediaVideosApi.md#remove_whitelist_using_delete) | **DELETE** /media/videos/{video_id}/whitelist/{id} | Removes a user from a video&#39;s whitelist
[**search_videos_using_get**](MediaVideosApi.md#search_videos_using_get) | **GET** /media/videos | Search videos using the documented filters
[**update_comment_using_put1**](MediaVideosApi.md#update_comment_using_put1) | **PUT** /media/videos/{video_id}/comments/{id}/content | Update video comment content 
[**update_relationship_using_put1**](MediaVideosApi.md#update_relationship_using_put1) | **PUT** /media/videos/{video_id}/related/{id}/relationship_details | Update a video&#39;s relationship details
[**update_video_using_put**](MediaVideosApi.md#update_video_using_put) | **PUT** /media/videos/{id} | Modifies a video&#39;s details
[**view_video_using_post**](MediaVideosApi.md#view_video_using_post) | **POST** /media/videos/{id}/views | Increment a video&#39;s view count


# **add_comment_using_post1**
> CommentResource add_comment_using_post1(video_id, comment_resource=comment_resource)

Add a new video comment

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
api_instance = swagger_client.MediaVideosApi()
video_id = 56 # int | The video id 
comment_resource = swagger_client.CommentResource() # CommentResource | The comment object (optional)

try: 
    # Add a new video comment
    api_response = api_instance.add_comment_using_post1(video_id, comment_resource=comment_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_comment_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id  | 
 **comment_resource** | [**CommentResource**](CommentResource.md)| The comment object | [optional] 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_contributor_using_post**
> add_contributor_using_post(video_id, contribution_resource=contribution_resource)

Adds a contributor to a video

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
contribution_resource = swagger_client.ContributionResource() # ContributionResource | The contribution object (optional)

try: 
    # Adds a contributor to a video
    api_instance.add_contributor_using_post(video_id, contribution_resource=contribution_resource)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_contributor_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **contribution_resource** | [**ContributionResource**](ContributionResource.md)| The contribution object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_disposition_using_post1**
> DispositionResource add_disposition_using_post1(video_id, disposition_resource=disposition_resource)

Add a new Video disposition

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
api_instance = swagger_client.MediaVideosApi()
video_id = 56 # int | The video id
disposition_resource = swagger_client.DispositionResource() # DispositionResource | The disposition object (optional)

try: 
    # Add a new Video disposition
    api_response = api_instance.add_disposition_using_post1(video_id, disposition_resource=disposition_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_disposition_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **disposition_resource** | [**DispositionResource**](DispositionResource.md)| The disposition object | [optional] 

### Return type

[**DispositionResource**](DispositionResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_flag_using_post**
> add_flag_using_post(video_id, reason=reason)

Add a new flag

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
reason = 'reason_example' # str | The flag reason (optional)

try: 
    # Add a new flag
    api_instance.add_flag_using_post(video_id, reason=reason)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_flag_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **reason** | **str**| The flag reason | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_related_using_post**
> VideoRelationshipResource add_related_using_post(video_id, video_relationship_resource=video_relationship_resource)

Adds one or more existing videos as related to this one

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
video_relationship_resource = swagger_client.VideoRelationshipResource() # VideoRelationshipResource | The video relationship object  (optional)

try: 
    # Adds one or more existing videos as related to this one
    api_response = api_instance.add_related_using_post(video_id, video_relationship_resource=video_relationship_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_related_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **video_relationship_resource** | [**VideoRelationshipResource**](VideoRelationshipResource.md)| The video relationship object  | [optional] 

### Return type

[**VideoRelationshipResource**](VideoRelationshipResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_video_using_post**
> VideoResource add_video_using_post(video_resource=video_resource)

Adds a new video in the system

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
api_instance = swagger_client.MediaVideosApi()
video_resource = swagger_client.VideoResource() # VideoResource | The video object (optional)

try: 
    # Adds a new video in the system
    api_response = api_instance.add_video_using_post(video_resource=video_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_video_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_resource** | [**VideoResource**](VideoResource.md)| The video object | [optional] 

### Return type

[**VideoResource**](VideoResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_whitelist_using_post**
> add_whitelist_using_post(id, user_id=user_id)

Adds a user to a video's whitelist

Whitelisted users can view video regardless of privacy setting.

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
api_instance = swagger_client.MediaVideosApi()
id = 789 # int | The video id
user_id = 56 # int | The user id (optional)

try: 
    # Adds a user to a video's whitelist
    api_instance.add_whitelist_using_post(id, user_id=user_id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_whitelist_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The video id | 
 **user_id** | **int**| The user id | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment_using_delete1**
> delete_comment_using_delete1(video_id, id)

Delete a video comment

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
id = 789 # int | The comment id

try: 
    # Delete a video comment
    api_instance.delete_comment_using_delete1(video_id, id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_comment_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **id** | **int**| The comment id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_disposition_using_delete1**
> delete_disposition_using_delete1(disposition_id)

Delete a video comment

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
api_instance = swagger_client.MediaVideosApi()
disposition_id = 789 # int | The disposition id

try: 
    # Delete a video comment
    api_instance.delete_disposition_using_delete1(disposition_id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_disposition_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disposition_id** | **int**| The disposition id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_flag_using_delete**
> delete_flag_using_delete(video_id)

Delete a flag

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id

try: 
    # Delete a flag
    api_instance.delete_flag_using_delete(video_id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_flag_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_relationship_using_delete1**
> delete_relationship_using_delete1(video_id, id)

Delete a video's relationship

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
id = 789 # int | The relationship id

try: 
    # Delete a video's relationship
    api_instance.delete_relationship_using_delete1(video_id, id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_relationship_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **id** | **int**| The relationship id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_using_delete**
> delete_video_using_delete(id)

Removes a video from the system if no resources are attached to it

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
api_instance = swagger_client.MediaVideosApi()
id = 789 # int | The video id

try: 
    # Removes a video from the system if no resources are attached to it
    api_instance.delete_video_using_delete(id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_video_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The video id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments_using_get1**
> PageResourceCommentResource get_comments_using_get1(video_id, size=size, page=page)

Returns a page of comments for a video

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaVideosApi()
video_id = 56 # int | The video id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of comments for a video
    api_response = api_instance.get_comments_using_get1(video_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_comments_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
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

# **get_dispositions_using_get1**
> PageResourceDispositionResource get_dispositions_using_get1(video_id, size=size, page=page)

Returns a page of dispositions for a video

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaVideosApi()
video_id = 56 # int | The video id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of dispositions for a video
    api_response = api_instance.get_dispositions_using_get1(video_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_dispositions_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceDispositionResource**](PageResourceDispositionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_using_get**
> PageResourceVideoRelationshipResource get_related_using_get(video_id, size=size, page=page)

Returns a page of video relationships

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of video relationships
    api_response = api_instance.get_related_using_get(video_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_related_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceVideoRelationshipResource**](PageResourceVideoRelationshipResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_videos_using_get**
> PageResourceVideoResource get_user_videos_using_get(user_id, exclude_flagged=exclude_flagged, size=size, page=page)

Get user videos

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
api_instance = swagger_client.MediaVideosApi()
user_id = 56 # int | The user id
exclude_flagged = true # bool | Skip videos that have been flagged by the current user (optional) (default to true)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Get user videos
    api_response = api_instance.get_user_videos_using_get(user_id, exclude_flagged=exclude_flagged, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_user_videos_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user id | 
 **exclude_flagged** | **bool**| Skip videos that have been flagged by the current user | [optional] [default to true]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceVideoResource**](PageResourceVideoResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_using_get**
> VideoResource get_video_using_get(id)

Loads a specific video details

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
api_instance = swagger_client.MediaVideosApi()
id = 789 # int | The video id

try: 
    # Loads a specific video details
    api_response = api_instance.get_video_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_video_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The video id | 

### Return type

[**VideoResource**](VideoResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_contributor_using_delete**
> remove_contributor_using_delete(video_id, id)

Removes a contributor from a video

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
id = 56 # int | The contributor id

try: 
    # Removes a contributor from a video
    api_instance.remove_contributor_using_delete(video_id, id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->remove_contributor_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **id** | **int**| The contributor id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_whitelist_using_delete**
> remove_whitelist_using_delete(video_id, id)

Removes a user from a video's whitelist

Remove the user with the id given in the path from the whitelist of users that can view this video regardless of privacy setting.

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
id = 56 # int | The user id

try: 
    # Removes a user from a video's whitelist
    api_instance.remove_whitelist_using_delete(video_id, id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->remove_whitelist_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **id** | **int**| The user id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_videos_using_get**
> PageResourceVideoResource search_videos_using_get(exclude_flagged=exclude_flagged, filter_videos_by_uploader=filter_videos_by_uploader, filter_category=filter_category, filter_tagset=filter_tagset, filter_videos_by_name=filter_videos_by_name, filter_videos_by_contributor=filter_videos_by_contributor, filter_videos_by_author=filter_videos_by_author, filter_has_author=filter_has_author, filter_has_uploader=filter_has_uploader, filter_related_to=filter_related_to, filter_friends=filter_friends, filter_disposition=filter_disposition, size=size, page=page, order=order)

Search videos using the documented filters

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaVideosApi()
exclude_flagged = true # bool | Skip videos that have been flagged by the current user (optional) (default to true)
filter_videos_by_uploader = 'filter_videos_by_uploader_example' # str | Filter for videos by uploader id (optional)
filter_category = 'filter_category_example' # str | Filter for videos from a specific category by id (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for videos with specified tags (separated by comma) (optional)
filter_videos_by_name = 'filter_videos_by_name_example' # str | Filter for videos which name *STARTS* with the given string (optional)
filter_videos_by_contributor = 'filter_videos_by_contributor_example' # str | Filter for videos with contribution from the artist specified by ID (optional)
filter_videos_by_author = 'filter_videos_by_author_example' # str | Filter for videos with an artist as author specified by ID (optional)
filter_has_author = true # bool | Filter for videos that have an author set if true, or that have no author if false (optional)
filter_has_uploader = true # bool | Filter for videos that have an uploader set if true, or that have no uploader if false (optional)
filter_related_to = 'filter_related_to_example' # str | Filter for videos that have designated a particular video as the TO of a relationship. Pattern should match VIDEO_ID or VIDEO_ID:DETAILS to match with a specific details string as well (optional)
filter_friends = true # bool | Filter for videos uploaded by friends. 'true' for friends of the caller (requires user token) or a user id for a specific user's friends (requires VIDEOS_ADMIN permission) (optional)
filter_disposition = 'filter_disposition_example' # str | Filter for videos a given user has a given disposition towards. USER_ID:DISPOSITION where USER_ID is the id of the user who has this disposition or 'me' for the caller (requires user token for 'me') and DISPOSITION is the name of the disposition. E.G. filter_disposition=123:like or filter_disposition=me:favorite (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'author:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to author:ASC)

try: 
    # Search videos using the documented filters
    api_response = api_instance.search_videos_using_get(exclude_flagged=exclude_flagged, filter_videos_by_uploader=filter_videos_by_uploader, filter_category=filter_category, filter_tagset=filter_tagset, filter_videos_by_name=filter_videos_by_name, filter_videos_by_contributor=filter_videos_by_contributor, filter_videos_by_author=filter_videos_by_author, filter_has_author=filter_has_author, filter_has_uploader=filter_has_uploader, filter_related_to=filter_related_to, filter_friends=filter_friends, filter_disposition=filter_disposition, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->search_videos_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_flagged** | **bool**| Skip videos that have been flagged by the current user | [optional] [default to true]
 **filter_videos_by_uploader** | **str**| Filter for videos by uploader id | [optional] 
 **filter_category** | **str**| Filter for videos from a specific category by id | [optional] 
 **filter_tagset** | **str**| Filter for videos with specified tags (separated by comma) | [optional] 
 **filter_videos_by_name** | **str**| Filter for videos which name *STARTS* with the given string | [optional] 
 **filter_videos_by_contributor** | **str**| Filter for videos with contribution from the artist specified by ID | [optional] 
 **filter_videos_by_author** | **str**| Filter for videos with an artist as author specified by ID | [optional] 
 **filter_has_author** | **bool**| Filter for videos that have an author set if true, or that have no author if false | [optional] 
 **filter_has_uploader** | **bool**| Filter for videos that have an uploader set if true, or that have no uploader if false | [optional] 
 **filter_related_to** | **str**| Filter for videos that have designated a particular video as the TO of a relationship. Pattern should match VIDEO_ID or VIDEO_ID:DETAILS to match with a specific details string as well | [optional] 
 **filter_friends** | **bool**| Filter for videos uploaded by friends. &#39;true&#39; for friends of the caller (requires user token) or a user id for a specific user&#39;s friends (requires VIDEOS_ADMIN permission) | [optional] 
 **filter_disposition** | **str**| Filter for videos a given user has a given disposition towards. USER_ID:DISPOSITION where USER_ID is the id of the user who has this disposition or &#39;me&#39; for the caller (requires user token for &#39;me&#39;) and DISPOSITION is the name of the disposition. E.G. filter_disposition&#x3D;123:like or filter_disposition&#x3D;me:favorite | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to author:ASC]

### Return type

[**PageResourceVideoResource**](PageResourceVideoResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment_using_put1**
> update_comment_using_put1(video_id, id, content=content)

Update video comment content 

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
id = 789 # int | The comment id
content = 'content_example' # str | The comment content (optional)

try: 
    # Update video comment content 
    api_instance.update_comment_using_put1(video_id, id, content=content)
except ApiException as e:
    print("Exception when calling MediaVideosApi->update_comment_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
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

# **update_relationship_using_put1**
> update_relationship_using_put1(video_id, relationship_id, details=details)

Update a video's relationship details

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
api_instance = swagger_client.MediaVideosApi()
video_id = 789 # int | The video id
relationship_id = 789 # int | The relationship id
details = 'details_example' # str | The video relationship details (optional)

try: 
    # Update a video's relationship details
    api_instance.update_relationship_using_put1(video_id, relationship_id, details=details)
except ApiException as e:
    print("Exception when calling MediaVideosApi->update_relationship_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **relationship_id** | **int**| The relationship id | 
 **details** | **str**| The video relationship details | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video_using_put**
> update_video_using_put(id, video_resource=video_resource)

Modifies a video's details

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
api_instance = swagger_client.MediaVideosApi()
id = 789 # int | The video id
video_resource = swagger_client.VideoResource() # VideoResource | The video object (optional)

try: 
    # Modifies a video's details
    api_instance.update_video_using_put(id, video_resource=video_resource)
except ApiException as e:
    print("Exception when calling MediaVideosApi->update_video_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The video id | 
 **video_resource** | [**VideoResource**](VideoResource.md)| The video object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_video_using_post**
> view_video_using_post(id)

Increment a video's view count

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaVideosApi()
id = 789 # int | The video id

try: 
    # Increment a video's view count
    api_instance.view_video_using_post(id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->view_video_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The video id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

