# knetik_cloud.MediaVideosApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_video_whitelist**](MediaVideosApi.md#add_user_to_video_whitelist) | **POST** /media/videos/{id}/whitelist | Adds a user to a video&#39;s whitelist
[**add_video**](MediaVideosApi.md#add_video) | **POST** /media/videos | Adds a new video in the system
[**add_video_comment**](MediaVideosApi.md#add_video_comment) | **POST** /media/videos/{video_id}/comments | Add a new video comment
[**add_video_contributor**](MediaVideosApi.md#add_video_contributor) | **POST** /media/videos/{video_id}/contributors | Adds a contributor to a video
[**add_video_flag**](MediaVideosApi.md#add_video_flag) | **POST** /media/videos/{video_id}/moderation | Add a new flag
[**add_video_relationships**](MediaVideosApi.md#add_video_relationships) | **POST** /media/videos/{video_id}/related | Adds one or more existing videos as related to this one
[**create_video_disposition**](MediaVideosApi.md#create_video_disposition) | **POST** /media/videos/{video_id}/dispositions | Create a video disposition
[**delete_video**](MediaVideosApi.md#delete_video) | **DELETE** /media/videos/{id} | Deletes a video from the system if no resources are attached to it
[**delete_video_comment**](MediaVideosApi.md#delete_video_comment) | **DELETE** /media/videos/{video_id}/comments/{id} | Delete a video comment
[**delete_video_disposition**](MediaVideosApi.md#delete_video_disposition) | **DELETE** /media/videos/{video_id}/dispositions/{disposition_id} | Delete a video disposition
[**delete_video_flag**](MediaVideosApi.md#delete_video_flag) | **DELETE** /media/videos/{video_id}/moderation | Delete a flag
[**delete_video_relationship**](MediaVideosApi.md#delete_video_relationship) | **DELETE** /media/videos/{video_id}/related/{id} | Delete a video&#39;s relationship
[**get_user_videos**](MediaVideosApi.md#get_user_videos) | **GET** /users/{user_id}/videos | Get user videos
[**get_video**](MediaVideosApi.md#get_video) | **GET** /media/videos/{id} | Loads a specific video details
[**get_video_comments**](MediaVideosApi.md#get_video_comments) | **GET** /media/videos/{video_id}/comments | Returns a page of comments for a video
[**get_video_dispositions**](MediaVideosApi.md#get_video_dispositions) | **GET** /media/videos/{video_id}/dispositions | Returns a page of dispositions for a video
[**get_video_relationships**](MediaVideosApi.md#get_video_relationships) | **GET** /media/videos/{video_id}/related | Returns a page of video relationships
[**get_videos**](MediaVideosApi.md#get_videos) | **GET** /media/videos | Search videos using the documented filters
[**remove_user_from_video_whitelist**](MediaVideosApi.md#remove_user_from_video_whitelist) | **DELETE** /media/videos/{video_id}/whitelist/{id} | Removes a user from a video&#39;s whitelist
[**remove_video_contributor**](MediaVideosApi.md#remove_video_contributor) | **DELETE** /media/videos/{video_id}/contributors/{id} | Removes a contributor from a video
[**update_video**](MediaVideosApi.md#update_video) | **PUT** /media/videos/{id} | Modifies a video&#39;s details
[**update_video_comment**](MediaVideosApi.md#update_video_comment) | **PUT** /media/videos/{video_id}/comments/{id}/content | Update a video comment
[**update_video_relationship**](MediaVideosApi.md#update_video_relationship) | **PUT** /media/videos/{video_id}/related/{id}/relationship_details | Update a video&#39;s relationship details
[**view_video**](MediaVideosApi.md#view_video) | **POST** /media/videos/{id}/views | Increment a video&#39;s view count


# **add_user_to_video_whitelist**
> add_user_to_video_whitelist(id, user_id=user_id)

Adds a user to a video's whitelist

Whitelisted users can view video regardless of privacy setting.

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The video id
user_id = knetik_cloud.IntWrapper() # IntWrapper | The user id (optional)

try: 
    # Adds a user to a video's whitelist
    api_instance.add_user_to_video_whitelist(id, user_id=user_id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_user_to_video_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The video id | 
 **user_id** | [**IntWrapper**](IntWrapper.md)| The user id | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_video**
> VideoResource add_video(video_resource=video_resource)

Adds a new video in the system

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_resource = knetik_cloud.VideoResource() # VideoResource | The video object (optional)

try: 
    # Adds a new video in the system
    api_response = api_instance.add_video(video_resource=video_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_resource** | [**VideoResource**](VideoResource.md)| The video object | [optional] 

### Return type

[**VideoResource**](VideoResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_video_comment**
> CommentResource add_video_comment(video_id, comment_resource=comment_resource)

Add a new video comment

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 56 # int | The video id 
comment_resource = knetik_cloud.CommentResource() # CommentResource | The comment object (optional)

try: 
    # Add a new video comment
    api_response = api_instance.add_video_comment(video_id, comment_resource=comment_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_video_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id  | 
 **comment_resource** | [**CommentResource**](CommentResource.md)| The comment object | [optional] 

### Return type

[**CommentResource**](CommentResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_video_contributor**
> add_video_contributor(video_id, contribution_resource=contribution_resource)

Adds a contributor to a video

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id
contribution_resource = knetik_cloud.ContributionResource() # ContributionResource | The contribution object (optional)

try: 
    # Adds a contributor to a video
    api_instance.add_video_contributor(video_id, contribution_resource=contribution_resource)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_video_contributor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **contribution_resource** | [**ContributionResource**](ContributionResource.md)| The contribution object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_video_flag**
> FlagResource add_video_flag(video_id, reason=reason)

Add a new flag

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id
reason = knetik_cloud.StringWrapper() # StringWrapper | The flag reason (optional)

try: 
    # Add a new flag
    api_response = api_instance.add_video_flag(video_id, reason=reason)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_video_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **reason** | [**StringWrapper**](StringWrapper.md)| The flag reason | [optional] 

### Return type

[**FlagResource**](FlagResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_video_relationships**
> VideoRelationshipResource add_video_relationships(video_id, video_relationship_resource=video_relationship_resource)

Adds one or more existing videos as related to this one

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id
video_relationship_resource = knetik_cloud.VideoRelationshipResource() # VideoRelationshipResource | The video relationship object  (optional)

try: 
    # Adds one or more existing videos as related to this one
    api_response = api_instance.add_video_relationships(video_id, video_relationship_resource=video_relationship_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->add_video_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **video_relationship_resource** | [**VideoRelationshipResource**](VideoRelationshipResource.md)| The video relationship object  | [optional] 

### Return type

[**VideoRelationshipResource**](VideoRelationshipResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_video_disposition**
> DispositionResource create_video_disposition(video_id, disposition_resource=disposition_resource)

Create a video disposition

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 56 # int | The video id
disposition_resource = knetik_cloud.DispositionResource() # DispositionResource | The disposition object (optional)

try: 
    # Create a video disposition
    api_response = api_instance.create_video_disposition(video_id, disposition_resource=disposition_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->create_video_disposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **disposition_resource** | [**DispositionResource**](DispositionResource.md)| The disposition object | [optional] 

### Return type

[**DispositionResource**](DispositionResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video**
> delete_video(id)

Deletes a video from the system if no resources are attached to it

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The video id

try: 
    # Deletes a video from the system if no resources are attached to it
    api_instance.delete_video(id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The video id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_comment**
> delete_video_comment(video_id, id)

Delete a video comment

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id
id = 789 # int | The comment id

try: 
    # Delete a video comment
    api_instance.delete_video_comment(video_id, id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_video_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **id** | **int**| The comment id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_disposition**
> delete_video_disposition(disposition_id)

Delete a video disposition

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
disposition_id = 789 # int | The disposition id

try: 
    # Delete a video disposition
    api_instance.delete_video_disposition(disposition_id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_video_disposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disposition_id** | **int**| The disposition id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_flag**
> delete_video_flag(video_id)

Delete a flag

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id

try: 
    # Delete a flag
    api_instance.delete_video_flag(video_id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_video_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_video_relationship**
> delete_video_relationship(video_id, id)

Delete a video's relationship

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id
id = 789 # int | The relationship id

try: 
    # Delete a video's relationship
    api_instance.delete_video_relationship(video_id, id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->delete_video_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **id** | **int**| The relationship id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_videos**
> PageResourceVideoResource get_user_videos(user_id, exclude_flagged=exclude_flagged, size=size, page=page)

Get user videos

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | The user id
exclude_flagged = true # bool | Skip videos that have been flagged by the current user (optional) (default to true)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Get user videos
    api_response = api_instance.get_user_videos(user_id, exclude_flagged=exclude_flagged, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_user_videos: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video**
> VideoResource get_video(id)

Loads a specific video details

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The video id

try: 
    # Loads a specific video details
    api_response = api_instance.get_video(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The video id | 

### Return type

[**VideoResource**](VideoResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_comments**
> PageResourceCommentResource get_video_comments(video_id, size=size, page=page)

Returns a page of comments for a video

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.MediaVideosApi()
video_id = 56 # int | The video id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of comments for a video
    api_response = api_instance.get_video_comments(video_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_video_comments: %s\n" % e)
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

# **get_video_dispositions**
> PageResourceDispositionResource get_video_dispositions(video_id, size=size, page=page)

Returns a page of dispositions for a video

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.MediaVideosApi()
video_id = 56 # int | The video id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of dispositions for a video
    api_response = api_instance.get_video_dispositions(video_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_video_dispositions: %s\n" % e)
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

# **get_video_relationships**
> PageResourceVideoRelationshipResource get_video_relationships(video_id, size=size, page=page)

Returns a page of video relationships

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.MediaVideosApi()
video_id = 789 # int | The video id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns a page of video relationships
    api_response = api_instance.get_video_relationships(video_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_video_relationships: %s\n" % e)
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

# **get_videos**
> PageResourceVideoResource get_videos(exclude_flagged=exclude_flagged, filter_videos_by_uploader=filter_videos_by_uploader, filter_category=filter_category, filter_tagset=filter_tagset, filter_videos_by_name=filter_videos_by_name, filter_videos_by_contributor=filter_videos_by_contributor, filter_videos_by_author=filter_videos_by_author, filter_has_author=filter_has_author, filter_has_uploader=filter_has_uploader, filter_related_to=filter_related_to, filter_friends=filter_friends, filter_disposition=filter_disposition, size=size, page=page, order=order)

Search videos using the documented filters

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.MediaVideosApi()
exclude_flagged = true # bool | Skip videos that have been flagged by the current user (optional) (default to true)
filter_videos_by_uploader = 56 # int | Filter for videos by uploader id (optional)
filter_category = 'filter_category_example' # str | Filter for videos from a specific category by id (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for videos with specified tags (separated by comma) (optional)
filter_videos_by_name = 'filter_videos_by_name_example' # str | Filter for videos which name *STARTS* with the given string (optional)
filter_videos_by_contributor = 56 # int | Filter for videos with contribution from the artist specified by ID (optional)
filter_videos_by_author = 56 # int | Filter for videos with an artist as author specified by ID (optional)
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
    api_response = api_instance.get_videos(exclude_flagged=exclude_flagged, filter_videos_by_uploader=filter_videos_by_uploader, filter_category=filter_category, filter_tagset=filter_tagset, filter_videos_by_name=filter_videos_by_name, filter_videos_by_contributor=filter_videos_by_contributor, filter_videos_by_author=filter_videos_by_author, filter_has_author=filter_has_author, filter_has_uploader=filter_has_uploader, filter_related_to=filter_related_to, filter_friends=filter_friends, filter_disposition=filter_disposition, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaVideosApi->get_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_flagged** | **bool**| Skip videos that have been flagged by the current user | [optional] [default to true]
 **filter_videos_by_uploader** | **int**| Filter for videos by uploader id | [optional] 
 **filter_category** | **str**| Filter for videos from a specific category by id | [optional] 
 **filter_tagset** | **str**| Filter for videos with specified tags (separated by comma) | [optional] 
 **filter_videos_by_name** | **str**| Filter for videos which name *STARTS* with the given string | [optional] 
 **filter_videos_by_contributor** | **int**| Filter for videos with contribution from the artist specified by ID | [optional] 
 **filter_videos_by_author** | **int**| Filter for videos with an artist as author specified by ID | [optional] 
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

# **remove_user_from_video_whitelist**
> remove_user_from_video_whitelist(video_id, id)

Removes a user from a video's whitelist

Remove the user with the id given in the path from the whitelist of users that can view this video regardless of privacy setting.

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id
id = 56 # int | The user id

try: 
    # Removes a user from a video's whitelist
    api_instance.remove_user_from_video_whitelist(video_id, id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->remove_user_from_video_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **id** | **int**| The user id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_video_contributor**
> remove_video_contributor(video_id, id)

Removes a contributor from a video

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id
id = 56 # int | The contributor id

try: 
    # Removes a contributor from a video
    api_instance.remove_video_contributor(video_id, id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->remove_video_contributor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **id** | **int**| The contributor id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video**
> update_video(id, video_resource=video_resource)

Modifies a video's details

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The video id
video_resource = knetik_cloud.VideoResource() # VideoResource | The video object (optional)

try: 
    # Modifies a video's details
    api_instance.update_video(id, video_resource=video_resource)
except ApiException as e:
    print("Exception when calling MediaVideosApi->update_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The video id | 
 **video_resource** | [**VideoResource**](VideoResource.md)| The video object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video_comment**
> update_video_comment(video_id, id, content=content)

Update a video comment

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id
id = 789 # int | The comment id
content = knetik_cloud.StringWrapper() # StringWrapper | The comment content (optional)

try: 
    # Update a video comment
    api_instance.update_video_comment(video_id, id, content=content)
except ApiException as e:
    print("Exception when calling MediaVideosApi->update_video_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **id** | **int**| The comment id | 
 **content** | [**StringWrapper**](StringWrapper.md)| The comment content | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video_relationship**
> update_video_relationship(video_id, relationship_id, details=details)

Update a video's relationship details

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
api_instance = knetik_cloud.MediaVideosApi(knetik_cloud.ApiClient(configuration))
video_id = 789 # int | The video id
relationship_id = 789 # int | The relationship id
details = knetik_cloud.StringWrapper() # StringWrapper | The video relationship details (optional)

try: 
    # Update a video's relationship details
    api_instance.update_video_relationship(video_id, relationship_id, details=details)
except ApiException as e:
    print("Exception when calling MediaVideosApi->update_video_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The video id | 
 **relationship_id** | **int**| The relationship id | 
 **details** | [**StringWrapper**](StringWrapper.md)| The video relationship details | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_video**
> view_video(id)

Increment a video's view count

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.MediaVideosApi()
id = 789 # int | The video id

try: 
    # Increment a video's view count
    api_instance.view_video(id)
except ApiException as e:
    print("Exception when calling MediaVideosApi->view_video: %s\n" % e)
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

