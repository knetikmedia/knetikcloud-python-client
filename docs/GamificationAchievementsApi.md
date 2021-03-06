# knetik_cloud.GamificationAchievementsApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_achievement**](GamificationAchievementsApi.md#create_achievement) | **POST** /achievements | Create a new achievement definition
[**create_achievement_template**](GamificationAchievementsApi.md#create_achievement_template) | **POST** /achievements/templates | Create an achievement template
[**delete_achievement**](GamificationAchievementsApi.md#delete_achievement) | **DELETE** /achievements/{name} | Delete an achievement definition
[**delete_achievement_template**](GamificationAchievementsApi.md#delete_achievement_template) | **DELETE** /achievements/templates/{id} | Delete an achievement template
[**get_achievement**](GamificationAchievementsApi.md#get_achievement) | **GET** /achievements/{name} | Get a single achievement definition
[**get_achievement_template**](GamificationAchievementsApi.md#get_achievement_template) | **GET** /achievements/templates/{id} | Get a single achievement template
[**get_achievement_templates**](GamificationAchievementsApi.md#get_achievement_templates) | **GET** /achievements/templates | List and search achievement templates
[**get_achievement_triggers**](GamificationAchievementsApi.md#get_achievement_triggers) | **GET** /achievements/triggers | Get the list of triggers that can be used to trigger an achievement progress update
[**get_achievements**](GamificationAchievementsApi.md#get_achievements) | **GET** /achievements | Get all achievement definitions in the system
[**get_derived_achievements**](GamificationAchievementsApi.md#get_derived_achievements) | **GET** /achievements/derived/{name} | Get a list of derived achievements
[**get_user_achievement_progress**](GamificationAchievementsApi.md#get_user_achievement_progress) | **GET** /users/{user_id}/achievements/{achievement_name} | Retrieve progress on a given achievement for a given user
[**get_user_achievements_progress**](GamificationAchievementsApi.md#get_user_achievements_progress) | **GET** /users/{user_id}/achievements | Retrieve progress on achievements for a given user
[**get_users_achievement_progress**](GamificationAchievementsApi.md#get_users_achievement_progress) | **GET** /users/achievements/{achievement_name} | Retrieve progress on a given achievement for all users
[**get_users_achievements_progress**](GamificationAchievementsApi.md#get_users_achievements_progress) | **GET** /users/achievements | Retrieve progress on achievements for all users
[**increment_achievement_progress**](GamificationAchievementsApi.md#increment_achievement_progress) | **POST** /users/{user_id}/achievements/{achievement_name}/progress | Increment an achievement progress record for a user
[**set_achievement_progress**](GamificationAchievementsApi.md#set_achievement_progress) | **PUT** /users/{user_id}/achievements/{achievement_name}/progress | Set an achievement progress record for a user
[**update_achievement**](GamificationAchievementsApi.md#update_achievement) | **PUT** /achievements/{name} | Update an achievement definition
[**update_achievement_template**](GamificationAchievementsApi.md#update_achievement_template) | **PUT** /achievements/templates/{id} | Update an achievement template


# **create_achievement**
> AchievementDefinitionResource create_achievement(achievement=achievement)

Create a new achievement definition

If the definition contains a trigger event name, a BRE rule is created, so that tracking logic is executed when the triggering event occurs. If no trigger event name is specified, the user's achievement status must manually be updated via the API. <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
achievement = knetik_cloud.AchievementDefinitionResource() # AchievementDefinitionResource | The achievement definition (optional)

try: 
    # Create a new achievement definition
    api_response = api_instance.create_achievement(achievement=achievement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->create_achievement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **achievement** | [**AchievementDefinitionResource**](AchievementDefinitionResource.md)| The achievement definition | [optional] 

### Return type

[**AchievementDefinitionResource**](AchievementDefinitionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_achievement_template**
> TemplateResource create_achievement_template(template=template)

Create an achievement template

Achievement templates define a type of achievement and the properties they have. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
template = knetik_cloud.TemplateResource() # TemplateResource | The achievement template to be created (optional)

try: 
    # Create an achievement template
    api_response = api_instance.create_achievement_template(template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->create_achievement_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | [**TemplateResource**](TemplateResource.md)| The achievement template to be created | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_achievement**
> delete_achievement(name)

Delete an achievement definition

Will also disable the associated generated rule, if any. <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
name = 'name_example' # str | The name of the achievement

try: 
    # Delete an achievement definition
    api_instance.delete_achievement(name)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->delete_achievement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the achievement | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_achievement_template**
> delete_achievement_template(id, cascade=cascade)

Delete an achievement template

If cascade = 'detach', it will force delete the template even if it's attached to other objects. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete an achievement template
    api_instance.delete_achievement_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->delete_achievement_template: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_achievement**
> AchievementDefinitionResource get_achievement(name)

Get a single achievement definition

<b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN or ACHIEVEMENTS_USER

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
name = 'name_example' # str | The name of the achievement

try: 
    # Get a single achievement definition
    api_response = api_instance.get_achievement(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_achievement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the achievement | 

### Return type

[**AchievementDefinitionResource**](AchievementDefinitionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_achievement_template**
> TemplateResource get_achievement_template(id)

Get a single achievement template

<b>Permissions Needed:</b> TEMPLATE_ADMIN or ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single achievement template
    api_response = api_instance.get_achievement_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_achievement_template: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_achievement_templates**
> PageResourceTemplateResource get_achievement_templates(size=size, page=page, order=order)

List and search achievement templates

<b>Permissions Needed:</b> TEMPLATE_ADMIN or ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search achievement templates
    api_response = api_instance.get_achievement_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_achievement_templates: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_achievement_triggers**
> list[BreTriggerResource] get_achievement_triggers()

Get the list of triggers that can be used to trigger an achievement progress update

<b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))

try: 
    # Get the list of triggers that can be used to trigger an achievement progress update
    api_response = api_instance.get_achievement_triggers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_achievement_triggers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BreTriggerResource]**](BreTriggerResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_achievements**
> PageResourceAchievementDefinitionResource get_achievements(filter_tagset=filter_tagset, filter_name=filter_name, filter_hidden=filter_hidden, size=size, page=page, order=order, filter_derived=filter_derived)

Get all achievement definitions in the system

<b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN or ACHIEVEMENTS_USER

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
filter_tagset = 'filter_tagset_example' # str | Filter for achievements with specified tags (separated by comma) (optional)
filter_name = 'filter_name_example' # str | Filter for achievements whose name contains a string (optional)
filter_hidden = true # bool | Filter for achievements that are hidden or not (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'name:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to name:ASC)
filter_derived = false # bool | Filter for achievements that are derived from other services (optional) (default to false)

try: 
    # Get all achievement definitions in the system
    api_response = api_instance.get_achievements(filter_tagset=filter_tagset, filter_name=filter_name, filter_hidden=filter_hidden, size=size, page=page, order=order, filter_derived=filter_derived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_achievements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_tagset** | **str**| Filter for achievements with specified tags (separated by comma) | [optional] 
 **filter_name** | **str**| Filter for achievements whose name contains a string | [optional] 
 **filter_hidden** | **bool**| Filter for achievements that are hidden or not | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to name:ASC]
 **filter_derived** | **bool**| Filter for achievements that are derived from other services | [optional] [default to false]

### Return type

[**PageResourceAchievementDefinitionResource**](PageResourceAchievementDefinitionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_derived_achievements**
> list[AchievementDefinitionResource] get_derived_achievements(name)

Get a list of derived achievements

Used by other services that depend on achievements.  <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
name = 'name_example' # str | The name of the derived achievement

try: 
    # Get a list of derived achievements
    api_response = api_instance.get_derived_achievements(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_derived_achievements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the derived achievement | 

### Return type

[**list[AchievementDefinitionResource]**](AchievementDefinitionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_achievement_progress**
> UserAchievementGroupResource get_user_achievement_progress(user_id, achievement_name)

Retrieve progress on a given achievement for a given user

Assets will not be filled in on the resources returned. Use 'Get a single poll' to retrieve the full resource with assets for a given item as needed. <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | The user's id
achievement_name = 'achievement_name_example' # str | The achievement's name

try: 
    # Retrieve progress on a given achievement for a given user
    api_response = api_instance.get_user_achievement_progress(user_id, achievement_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_user_achievement_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 
 **achievement_name** | **str**| The achievement&#39;s name | 

### Return type

[**UserAchievementGroupResource**](UserAchievementGroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_achievements_progress**
> PageResourceUserAchievementGroupResource get_user_achievements_progress(user_id, filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, size=size, page=page)

Retrieve progress on achievements for a given user

Assets will not be filled in on the resources returned. Use 'Get a single poll' to retrieve the full resource with assets for a given item as needed. <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | The user's id
filter_achievement_derived = true # bool | Filter for achievements that are derived from other services (optional)
filter_achievement_tagset = 'filter_achievement_tagset_example' # str | Filter for achievements with specified tags (separated by comma) (optional)
filter_achievement_name = 'filter_achievement_name_example' # str | Filter for achievements whose name contains a string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Retrieve progress on achievements for a given user
    api_response = api_instance.get_user_achievements_progress(user_id, filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_user_achievements_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 
 **filter_achievement_derived** | **bool**| Filter for achievements that are derived from other services | [optional] 
 **filter_achievement_tagset** | **str**| Filter for achievements with specified tags (separated by comma) | [optional] 
 **filter_achievement_name** | **str**| Filter for achievements whose name contains a string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUserAchievementGroupResource**](PageResourceUserAchievementGroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_achievement_progress**
> PageResourceUserAchievementGroupResource get_users_achievement_progress(achievement_name, filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, size=size, page=page)

Retrieve progress on a given achievement for all users

Assets will not be filled in on the resources returned. Use 'Get single achievement progress for user' to retrieve the full resource with assets for a given user as needed. <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
achievement_name = 'achievement_name_example' # str | The achievement's name
filter_achievement_derived = true # bool | Filter for achievements that are derived from other services (optional)
filter_achievement_tagset = 'filter_achievement_tagset_example' # str | Filter for achievements with specified tags (separated by comma) (optional)
filter_achievement_name = 'filter_achievement_name_example' # str | Filter for achievements whose name contains a string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Retrieve progress on a given achievement for all users
    api_response = api_instance.get_users_achievement_progress(achievement_name, filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_users_achievement_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **achievement_name** | **str**| The achievement&#39;s name | 
 **filter_achievement_derived** | **bool**| Filter for achievements that are derived from other services | [optional] 
 **filter_achievement_tagset** | **str**| Filter for achievements with specified tags (separated by comma) | [optional] 
 **filter_achievement_name** | **str**| Filter for achievements whose name contains a string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUserAchievementGroupResource**](PageResourceUserAchievementGroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_achievements_progress**
> PageResourceUserAchievementGroupResource get_users_achievements_progress(filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, size=size, page=page)

Retrieve progress on achievements for all users

Assets will not be filled in on the resources returned. Use 'Get single achievement progress for user' to retrieve the full resource with assets for a given user as needed. <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
filter_achievement_derived = true # bool | Filter for achievements that are derived from other services (optional)
filter_achievement_tagset = 'filter_achievement_tagset_example' # str | Filter for achievements with specified tags (separated by comma) (optional)
filter_achievement_name = 'filter_achievement_name_example' # str | Filter for achievements whose name contains a string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Retrieve progress on achievements for all users
    api_response = api_instance.get_users_achievements_progress(filter_achievement_derived=filter_achievement_derived, filter_achievement_tagset=filter_achievement_tagset, filter_achievement_name=filter_achievement_name, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->get_users_achievements_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_achievement_derived** | **bool**| Filter for achievements that are derived from other services | [optional] 
 **filter_achievement_tagset** | **str**| Filter for achievements with specified tags (separated by comma) | [optional] 
 **filter_achievement_name** | **str**| Filter for achievements whose name contains a string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUserAchievementGroupResource**](PageResourceUserAchievementGroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **increment_achievement_progress**
> UserAchievementGroupResource increment_achievement_progress(user_id, achievement_name, progress=progress)

Increment an achievement progress record for a user

If no progress record yet exists for the user, it will be created. Otherwise it will be updated and the provided value added to the existing progress. May be negative. If progress meets or exceeds the achievement's max_value it will be marked as earned and a BRE event will be triggered for the <code>BreAchievementEarnedTrigger</code>. <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | The user's id
achievement_name = 'achievement_name_example' # str | The achievement's name
progress = knetik_cloud.IntWrapper() # IntWrapper | The amount to add to the progress value (optional)

try: 
    # Increment an achievement progress record for a user
    api_response = api_instance.increment_achievement_progress(user_id, achievement_name, progress=progress)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->increment_achievement_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 
 **achievement_name** | **str**| The achievement&#39;s name | 
 **progress** | [**IntWrapper**](IntWrapper.md)| The amount to add to the progress value | [optional] 

### Return type

[**UserAchievementGroupResource**](UserAchievementGroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_achievement_progress**
> UserAchievementGroupResource set_achievement_progress(user_id, achievement_name, progress=progress)

Set an achievement progress record for a user

If no progress record yet exists for the user, it will be created. Otherwise it will be updated and progress set to the provided value. If progress meets or exceeds the achievement's max_value it will be marked as earned and a BRE event will be triggered for the <code>BreAchievementEarnedTrigger</code>. <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | The user's id
achievement_name = 'achievement_name_example' # str | The achievement's name
progress = knetik_cloud.IntWrapper() # IntWrapper | The new progress value (optional)

try: 
    # Set an achievement progress record for a user
    api_response = api_instance.set_achievement_progress(user_id, achievement_name, progress=progress)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->set_achievement_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 
 **achievement_name** | **str**| The achievement&#39;s name | 
 **progress** | [**IntWrapper**](IntWrapper.md)| The new progress value | [optional] 

### Return type

[**UserAchievementGroupResource**](UserAchievementGroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_achievement**
> AchievementDefinitionResource update_achievement(name, achievement=achievement)

Update an achievement definition

The existing generated rule, if any, will be deleted. A new rule will be created if a trigger event name is specified in the new version. <br><br><b>Permissions Needed:</b> ACHIEVEMENTS_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
name = 'name_example' # str | The name of the achievement
achievement = knetik_cloud.AchievementDefinitionResource() # AchievementDefinitionResource | The achievement definition (optional)

try: 
    # Update an achievement definition
    api_response = api_instance.update_achievement(name, achievement=achievement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->update_achievement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the achievement | 
 **achievement** | [**AchievementDefinitionResource**](AchievementDefinitionResource.md)| The achievement definition | [optional] 

### Return type

[**AchievementDefinitionResource**](AchievementDefinitionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_achievement_template**
> TemplateResource update_achievement_template(id, template=template)

Update an achievement template

<b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.GamificationAchievementsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
template = knetik_cloud.TemplateResource() # TemplateResource | The updated template (optional)

try: 
    # Update an achievement template
    api_response = api_instance.update_achievement_template(id, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationAchievementsApi->update_achievement_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **template** | [**TemplateResource**](TemplateResource.md)| The updated template | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

