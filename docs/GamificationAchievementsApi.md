# swagger_client.GamificationAchievementsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_achievement_using_post**](GamificationAchievementsApi.md#create_achievement_using_post) | **POST** /achievements | Create a new achievement definition
[**create_template_using_post**](GamificationAchievementsApi.md#create_template_using_post) | **POST** /achievements/templates | Create an achievement template
[**delete_achievement_template_using_delete**](GamificationAchievementsApi.md#delete_achievement_template_using_delete) | **DELETE** /achievements/templates/{id} | Delete an achievement template
[**delete_achievement_using_delete**](GamificationAchievementsApi.md#delete_achievement_using_delete) | **DELETE** /achievements/{name} | Delete an achievement definition
[**find_all_by_group_name_using_get**](GamificationAchievementsApi.md#find_all_by_group_name_using_get) | **GET** /achievements/derived/{name} | Get a list of derived achievements
[**get_achievement_template_using_get**](GamificationAchievementsApi.md#get_achievement_template_using_get) | **GET** /achievements/templates/{id} | Get a single achievement template
[**get_achievement_templates_using_get**](GamificationAchievementsApi.md#get_achievement_templates_using_get) | **GET** /achievements/templates | List and search achievement templates
[**get_achievement_using_get**](GamificationAchievementsApi.md#get_achievement_using_get) | **GET** /achievements/{name} | Get a single achievement definition
[**get_achievements_using_get**](GamificationAchievementsApi.md#get_achievements_using_get) | **GET** /achievements | Get all achievement definitions in the system
[**get_all_user_progress_for_achievement_using_get**](GamificationAchievementsApi.md#get_all_user_progress_for_achievement_using_get) | **GET** /users/achievements/{achievement_name} | Retrieve progress on a given achievement for all users
[**get_all_user_progress_using_get**](GamificationAchievementsApi.md#get_all_user_progress_using_get) | **GET** /users/achievements | Retrieve progress on achievements for all users
[**get_available_triggers_using_get**](GamificationAchievementsApi.md#get_available_triggers_using_get) | **GET** /achievements/triggers | Get the list of triggers that can be used to trigger an achievement progress update
[**get_user_progress_for_achievement_using_get**](GamificationAchievementsApi.md#get_user_progress_for_achievement_using_get) | **GET** /users/{user_id}/achievements/{achievement_name} | Retrieve progress on a given achievement for a given user
[**get_user_progress_using_get**](GamificationAchievementsApi.md#get_user_progress_using_get) | **GET** /users/{user_id}/achievements | Retrieve progress on achievements for a given user
[**update_achievement_using_put**](GamificationAchievementsApi.md#update_achievement_using_put) | **PUT** /achievements/{name} | Update an achievement definition
[**update_progress_using_put**](GamificationAchievementsApi.md#update_progress_using_put) | **PUT** /users/{user_id}/achievements/{achievement_name} | Update or create an achievement progress record for a user
[**update_template_using_put**](GamificationAchievementsApi.md#update_template_using_put) | **PUT** /achievements/templates/{id} | Update an achievement template


# **create_achievement_using_post**
> AchievementDefinitionResource create_achievement_using_post(achievement=achievement)

Create a new achievement definition

If the definition contains a trigger event name, a BRE rule is created, so that tracking logic is executed when the triggering event occurs. If no trigger event name is specified, the user's achievement status must manually be updated via the API.

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
api_instance = swagger_client.GamificationAchievementsApi()
achievement = swagger_client.AchievementDefinitionResource() # AchievementDefinitionResource | The achievement definition (optional)

try: 
    # Create a new achievement definition
    api_response = api_instance.create_achievement_using_post(achievement=achievement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->create_achievement_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **achievement** | [**AchievementDefinitionResource**](AchievementDefinitionResource.md)| The achievement definition | [optional] 

### Return type

[**AchievementDefinitionResource**](AchievementDefinitionResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template_using_post**
> TemplateResource create_template_using_post(template=template)

Create an achievement template

Achievement templates define a type of achievement and the properties they have

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
api_instance = swagger_client.GamificationAchievementsApi()
template = swagger_client.TemplateResource() # TemplateResource | The achievement template to be created (optional)

try: 
    # Create an achievement template
    api_response = api_instance.create_template_using_post(template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->create_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | [**TemplateResource**](TemplateResource.md)| The achievement template to be created | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_achievement_template_using_delete**
> delete_achievement_template_using_delete(id, cascade=cascade)

Delete an achievement template

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
api_instance = swagger_client.GamificationAchievementsApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete an achievement template
    api_instance.delete_achievement_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->delete_achievement_template_using_delete: %s\n" % e)
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

# **delete_achievement_using_delete**
> delete_achievement_using_delete(name)

Delete an achievement definition

Will also disable the associated generated rule, if any.

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
api_instance = swagger_client.GamificationAchievementsApi()
name = 'name_example' # str | The name of the achievement

try: 
    # Delete an achievement definition
    api_instance.delete_achievement_using_delete(name)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->delete_achievement_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the achievement | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_by_group_name_using_get**
> list[AchievementDefinitionResource] find_all_by_group_name_using_get(name)

Get a list of derived achievements

Used by other services that depend on achievements

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
api_instance = swagger_client.GamificationAchievementsApi()
name = 'name_example' # str | The name of the derived achievement

try: 
    # Get a list of derived achievements
    api_response = api_instance.find_all_by_group_name_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->find_all_by_group_name_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the derived achievement | 

### Return type

[**list[AchievementDefinitionResource]**](AchievementDefinitionResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_achievement_template_using_get**
> TemplateResource get_achievement_template_using_get(id)

Get a single achievement template

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
api_instance = swagger_client.GamificationAchievementsApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single achievement template
    api_response = api_instance.get_achievement_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_achievement_template_using_get: %s\n" % e)
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

# **get_achievement_templates_using_get**
> PageResourceTemplateResource get_achievement_templates_using_get(size=size, page=page, order=order)

List and search achievement templates

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
api_instance = swagger_client.GamificationAchievementsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search achievement templates
    api_response = api_instance.get_achievement_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_achievement_templates_using_get: %s\n" % e)
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

# **get_achievement_using_get**
> AchievementDefinitionResource get_achievement_using_get(name)

Get a single achievement definition

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
api_instance = swagger_client.GamificationAchievementsApi()
name = 'name_example' # str | The name of the achievement

try: 
    # Get a single achievement definition
    api_response = api_instance.get_achievement_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_achievement_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the achievement | 

### Return type

[**AchievementDefinitionResource**](AchievementDefinitionResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_achievements_using_get**
> PageResourceAchievementDefinitionResource get_achievements_using_get(filter_tagset=filter_tagset, filter_name=filter_name, filter_hidden=filter_hidden, filter_derived=filter_derived, size=size, page=page, order=order)

Get all achievement definitions in the system

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
api_instance = swagger_client.GamificationAchievementsApi()
filter_tagset = 'filter_tagset_example' # str | Filter for achievements with specified tags (separated by comma) (optional)
filter_name = 'filter_name_example' # str | Filter for achievements whose name contains a string (optional)
filter_hidden = true # bool | Filter for achievements that are hidden or not (optional)
filter_derived = true # bool | Filter for achievements that are derived from other services (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'name:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to name:ASC)

try: 
    # Get all achievement definitions in the system
    api_response = api_instance.get_achievements_using_get(filter_tagset=filter_tagset, filter_name=filter_name, filter_hidden=filter_hidden, filter_derived=filter_derived, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_achievements_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_tagset** | **str**| Filter for achievements with specified tags (separated by comma) | [optional] 
 **filter_name** | **str**| Filter for achievements whose name contains a string | [optional] 
 **filter_hidden** | **bool**| Filter for achievements that are hidden or not | [optional] 
 **filter_derived** | **bool**| Filter for achievements that are derived from other services | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to name:ASC]

### Return type

[**PageResourceAchievementDefinitionResource**](PageResourceAchievementDefinitionResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_progress_for_achievement_using_get**
> PageResourceUserAchievementGroupResource get_all_user_progress_for_achievement_using_get(achievement_name, filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_hidden=filter_achievement_hidden, size=size, page=page)

Retrieve progress on a given achievement for all users

Assets will not be filled in on the resources returned. Use 'Get single achievement progress for user' to retrieve the full resource with assets for a given user as needed.

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
api_instance = swagger_client.GamificationAchievementsApi()
achievement_name = 'achievement_name_example' # str | The achievement's name
filter_achievement_derived = true # bool | Filter for achievements that are derived from other services (optional)
filter_achievement_tagset = 'filter_achievement_tagset_example' # str | Filter for achievements with specified tags (separated by comma) (optional)
filter_achievement_hidden = true # bool | Filter for achievements that are hidden or not (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Retrieve progress on a given achievement for all users
    api_response = api_instance.get_all_user_progress_for_achievement_using_get(achievement_name, filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_hidden=filter_achievement_hidden, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_all_user_progress_for_achievement_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **achievement_name** | **str**| The achievement&#39;s name | 
 **filter_achievement_derived** | **bool**| Filter for achievements that are derived from other services | [optional] 
 **filter_achievement_tagset** | **str**| Filter for achievements with specified tags (separated by comma) | [optional] 
 **filter_achievement_hidden** | **bool**| Filter for achievements that are hidden or not | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUserAchievementGroupResource**](PageResourceUserAchievementGroupResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_user_progress_using_get**
> PageResourceUserAchievementGroupResource get_all_user_progress_using_get(filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, filter_achievement_hidden=filter_achievement_hidden, size=size, page=page)

Retrieve progress on achievements for all users

Assets will not be filled in on the resources returned. Use 'Get single achievement progress for user' to retrieve the full resource with assets for a given user as needed.

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
api_instance = swagger_client.GamificationAchievementsApi()
filter_achievement_derived = true # bool | Filter for achievements that are derived from other services (optional)
filter_achievement_tagset = 'filter_achievement_tagset_example' # str | Filter for achievements with specified tags (separated by comma) (optional)
filter_achievement_name = 'filter_achievement_name_example' # str | Filter for achievements whose name contains a string (optional)
filter_achievement_hidden = true # bool | Filter for achievements that are hidden or not (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Retrieve progress on achievements for all users
    api_response = api_instance.get_all_user_progress_using_get(filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, filter_achievement_hidden=filter_achievement_hidden, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_all_user_progress_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_achievement_derived** | **bool**| Filter for achievements that are derived from other services | [optional] 
 **filter_achievement_tagset** | **str**| Filter for achievements with specified tags (separated by comma) | [optional] 
 **filter_achievement_name** | **str**| Filter for achievements whose name contains a string | [optional] 
 **filter_achievement_hidden** | **bool**| Filter for achievements that are hidden or not | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUserAchievementGroupResource**](PageResourceUserAchievementGroupResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_triggers_using_get**
> list[BreTriggerResource] get_available_triggers_using_get()

Get the list of triggers that can be used to trigger an achievement progress update

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
api_instance = swagger_client.GamificationAchievementsApi()

try: 
    # Get the list of triggers that can be used to trigger an achievement progress update
    api_response = api_instance.get_available_triggers_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_available_triggers_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BreTriggerResource]**](BreTriggerResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_progress_for_achievement_using_get**
> UserAchievementGroupResource get_user_progress_for_achievement_using_get(user_id, achievement_name)

Retrieve progress on a given achievement for a given user

Assets will not be filled in on the resources returned. Use 'Get a single poll' to retrieve the full resource with assets for a given item as needed.

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
api_instance = swagger_client.GamificationAchievementsApi()
user_id = 56 # int | The user's id
achievement_name = 'achievement_name_example' # str | The achievement's name

try: 
    # Retrieve progress on a given achievement for a given user
    api_response = api_instance.get_user_progress_for_achievement_using_get(user_id, achievement_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_user_progress_for_achievement_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 
 **achievement_name** | **str**| The achievement&#39;s name | 

### Return type

[**UserAchievementGroupResource**](UserAchievementGroupResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_progress_using_get**
> PageResourceUserAchievementGroupResource get_user_progress_using_get(user_id, filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, filter_achievement_hidden=filter_achievement_hidden, size=size, page=page)

Retrieve progress on achievements for a given user

Assets will not be filled in on the resources returned. Use 'Get a single poll' to retrieve the full resource with assets for a given item as needed.

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
api_instance = swagger_client.GamificationAchievementsApi()
user_id = 56 # int | The user's id
filter_achievement_derived = true # bool | Filter for achievements that are derived from other services (optional)
filter_achievement_tagset = 'filter_achievement_tagset_example' # str | Filter for achievements with specified tags (separated by comma) (optional)
filter_achievement_name = 'filter_achievement_name_example' # str | Filter for achievements whose name contains a string (optional)
filter_achievement_hidden = true # bool | Filter for achievements that are hidden or not (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Retrieve progress on achievements for a given user
    api_response = api_instance.get_user_progress_using_get(user_id, filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, filter_achievement_hidden=filter_achievement_hidden, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_user_progress_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 
 **filter_achievement_derived** | **bool**| Filter for achievements that are derived from other services | [optional] 
 **filter_achievement_tagset** | **str**| Filter for achievements with specified tags (separated by comma) | [optional] 
 **filter_achievement_name** | **str**| Filter for achievements whose name contains a string | [optional] 
 **filter_achievement_hidden** | **bool**| Filter for achievements that are hidden or not | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUserAchievementGroupResource**](PageResourceUserAchievementGroupResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_achievement_using_put**
> update_achievement_using_put(name, achievement=achievement)

Update an achievement definition

The existing generated rule, if any, will be deleted. A new rule will be created if a trigger event name is specified in the new version.

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
api_instance = swagger_client.GamificationAchievementsApi()
name = 'name_example' # str | The name of the achievement
achievement = swagger_client.AchievementDefinitionResource() # AchievementDefinitionResource | The achievement definition (optional)

try: 
    # Update an achievement definition
    api_instance.update_achievement_using_put(name, achievement=achievement)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->update_achievement_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the achievement | 
 **achievement** | [**AchievementDefinitionResource**](AchievementDefinitionResource.md)| The achievement definition | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_progress_using_put**
> UserAchievementGroupResource update_progress_using_put(user_id, achievement_name, request=request)

Update or create an achievement progress record for a user

If no progress record yet exists for the user, it will be created. Otherwise it will be updated. If progress meets or exceeds the achievement's max_value it will be marked as earned and a BRE event will be triggered for the <code>BreAchievementEarnedTrigger</code>.

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
api_instance = swagger_client.GamificationAchievementsApi()
user_id = 56 # int | The user's id
achievement_name = 'achievement_name_example' # str | The achievement's name
request = swagger_client.AchievementProgressUpdateRequest() # AchievementProgressUpdateRequest | The progress update details (optional)

try: 
    # Update or create an achievement progress record for a user
    api_response = api_instance.update_progress_using_put(user_id, achievement_name, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->update_progress_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 
 **achievement_name** | **str**| The achievement&#39;s name | 
 **request** | [**AchievementProgressUpdateRequest**](AchievementProgressUpdateRequest.md)| The progress update details | [optional] 

### Return type

[**UserAchievementGroupResource**](UserAchievementGroupResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_using_put**
> update_template_using_put(id, template=template)

Update an achievement template

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
api_instance = swagger_client.GamificationAchievementsApi()
id = 'id_example' # str | The id of the template
template = swagger_client.TemplateResource() # TemplateResource | The updated template (optional)

try: 
    # Update an achievement template
    api_instance.update_template_using_put(id, template=template)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->update_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **template** | [**TemplateResource**](TemplateResource.md)| The updated template | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
