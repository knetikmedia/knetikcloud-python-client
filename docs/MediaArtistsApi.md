# swagger_client.MediaArtistsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_artist_using_post**](MediaArtistsApi.md#add_artist_using_post) | **POST** /media/artists | Adds a new artist in the system
[**create_artist_template_using_post**](MediaArtistsApi.md#create_artist_template_using_post) | **POST** /media/artists/templates | Create an artist template
[**delete_artist_template_using_delete**](MediaArtistsApi.md#delete_artist_template_using_delete) | **DELETE** /media/artists/templates/{id} | Delete an artist template
[**delete_artist_using_delete**](MediaArtistsApi.md#delete_artist_using_delete) | **DELETE** /media/artists/{id} | Removes an artist from the system IF no resources are attached to it
[**get_artist_template_using_get**](MediaArtistsApi.md#get_artist_template_using_get) | **GET** /media/artists/templates/{id} | Get a single artist template
[**get_artist_templates_using_get**](MediaArtistsApi.md#get_artist_templates_using_get) | **GET** /media/artists/templates | List and search artist templates
[**get_artist_using_get**](MediaArtistsApi.md#get_artist_using_get) | **GET** /media/artists/{id} | Loads a specific artist details
[**search_artists_using_get**](MediaArtistsApi.md#search_artists_using_get) | **GET** /media/artists | Search for artists
[**update_artist_template_using_put**](MediaArtistsApi.md#update_artist_template_using_put) | **PUT** /media/artists/templates/{id} | Update an artist template
[**update_artist_using_put**](MediaArtistsApi.md#update_artist_using_put) | **PUT** /media/artists/{id} | Modifies an artist details


# **add_artist_using_post**
> ArtistResource add_artist_using_post(artist_resource=artist_resource)

Adds a new artist in the system

Adds a new artist in the system. Use specific media contributions endpoint to add contributions

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
api_instance = swagger_client.MediaArtistsApi()
artist_resource = swagger_client.ArtistResource() # ArtistResource | The new artist (optional)

try: 
    # Adds a new artist in the system
    api_response = api_instance.add_artist_using_post(artist_resource=artist_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->add_artist_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_resource** | [**ArtistResource**](ArtistResource.md)| The new artist | [optional] 

### Return type

[**ArtistResource**](ArtistResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_artist_template_using_post**
> TemplateResource create_artist_template_using_post(artist_template_resource=artist_template_resource)

Create an artist template

Artist Templates define a type of artist and the properties they have

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
api_instance = swagger_client.MediaArtistsApi()
artist_template_resource = swagger_client.TemplateResource() # TemplateResource | The artist template resource object (optional)

try: 
    # Create an artist template
    api_response = api_instance.create_artist_template_using_post(artist_template_resource=artist_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->create_artist_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artist_template_resource** | [**TemplateResource**](TemplateResource.md)| The artist template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artist_template_using_delete**
> delete_artist_template_using_delete(id, cascade=cascade)

Delete an artist template

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
api_instance = swagger_client.MediaArtistsApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete an artist template
    api_instance.delete_artist_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->delete_artist_template_using_delete: %s\n" % e)
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

# **delete_artist_using_delete**
> delete_artist_using_delete(id)

Removes an artist from the system IF no resources are attached to it

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
api_instance = swagger_client.MediaArtistsApi()
id = 789 # int | The artist id

try: 
    # Removes an artist from the system IF no resources are attached to it
    api_instance.delete_artist_using_delete(id)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->delete_artist_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The artist id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artist_template_using_get**
> TemplateResource get_artist_template_using_get(id)

Get a single artist template

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
api_instance = swagger_client.MediaArtistsApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single artist template
    api_response = api_instance.get_artist_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->get_artist_template_using_get: %s\n" % e)
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

# **get_artist_templates_using_get**
> PageResourceTemplateResource get_artist_templates_using_get(size=size, page=page, order=order)

List and search artist templates

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
api_instance = swagger_client.MediaArtistsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search artist templates
    api_response = api_instance.get_artist_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->get_artist_templates_using_get: %s\n" % e)
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

# **get_artist_using_get**
> ArtistResource get_artist_using_get(id, show_contributions=show_contributions)

Loads a specific artist details

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaArtistsApi()
id = 789 # int | The artist id
show_contributions = 56 # int | The number of contributions to show fetch (optional)

try: 
    # Loads a specific artist details
    api_response = api_instance.get_artist_using_get(id, show_contributions=show_contributions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->get_artist_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The artist id | 
 **show_contributions** | **int**| The number of contributions to show fetch | [optional] 

### Return type

[**ArtistResource**](ArtistResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_artists_using_get**
> PageResourceArtistResource search_artists_using_get(filter_artists_by_name=filter_artists_by_name, size=size, page=page, order=order)

Search for artists

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MediaArtistsApi()
filter_artists_by_name = 'filter_artists_by_name_example' # str | Filter for artists which name *STARTS* with the given string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Search for artists
    api_response = api_instance.search_artists_using_get(filter_artists_by_name=filter_artists_by_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->search_artists_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_artists_by_name** | **str**| Filter for artists which name *STARTS* with the given string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceArtistResource**](PageResourceArtistResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artist_template_using_put**
> update_artist_template_using_put(id, artist_template_resource=artist_template_resource)

Update an artist template

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
api_instance = swagger_client.MediaArtistsApi()
id = 'id_example' # str | The id of the template
artist_template_resource = swagger_client.TemplateResource() # TemplateResource | The artist template resource object (optional)

try: 
    # Update an artist template
    api_instance.update_artist_template_using_put(id, artist_template_resource=artist_template_resource)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->update_artist_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **artist_template_resource** | [**TemplateResource**](TemplateResource.md)| The artist template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artist_using_put**
> update_artist_using_put(id, artist_resource=artist_resource)

Modifies an artist details

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
api_instance = swagger_client.MediaArtistsApi()
id = 789 # int | The artist id
artist_resource = swagger_client.ArtistResource() # ArtistResource | The new artist (optional)

try: 
    # Modifies an artist details
    api_instance.update_artist_using_put(id, artist_resource=artist_resource)
except ApiException as e:
    print("Exception when calling MediaArtistsApi->update_artist_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The artist id | 
 **artist_resource** | [**ArtistResource**](ArtistResource.md)| The new artist | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

