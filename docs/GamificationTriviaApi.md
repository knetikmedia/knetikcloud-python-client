# knetik_cloud.GamificationTriviaApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_question_answers**](GamificationTriviaApi.md#add_question_answers) | **POST** /trivia/questions/{question_id}/answers | Add an answer to a question
[**add_question_tag**](GamificationTriviaApi.md#add_question_tag) | **POST** /trivia/questions/{id}/tags | Add a tag to a question
[**add_tag_to_questions_batch**](GamificationTriviaApi.md#add_tag_to_questions_batch) | **POST** /trivia/questions/tags | Add a tag to a batch of questions
[**create_import_job**](GamificationTriviaApi.md#create_import_job) | **POST** /trivia/import | Create an import job
[**create_question**](GamificationTriviaApi.md#create_question) | **POST** /trivia/questions | Create a question
[**create_question_template**](GamificationTriviaApi.md#create_question_template) | **POST** /trivia/questions/templates | Create a question template
[**delete_import_job**](GamificationTriviaApi.md#delete_import_job) | **DELETE** /trivia/import/{id} | Delete an import job
[**delete_question**](GamificationTriviaApi.md#delete_question) | **DELETE** /trivia/questions/{id} | Delete a question
[**delete_question_answers**](GamificationTriviaApi.md#delete_question_answers) | **DELETE** /trivia/questions/{question_id}/answers/{id} | Remove an answer from a question
[**delete_question_template**](GamificationTriviaApi.md#delete_question_template) | **DELETE** /trivia/questions/templates/{id} | Delete a question template
[**get_import_job**](GamificationTriviaApi.md#get_import_job) | **GET** /trivia/import/{id} | Get an import job
[**get_import_jobs**](GamificationTriviaApi.md#get_import_jobs) | **GET** /trivia/import | Get a list of import job
[**get_question**](GamificationTriviaApi.md#get_question) | **GET** /trivia/questions/{id} | Get a single question
[**get_question_answer**](GamificationTriviaApi.md#get_question_answer) | **GET** /trivia/questions/{question_id}/answers/{id} | Get an answer for a question
[**get_question_answers**](GamificationTriviaApi.md#get_question_answers) | **GET** /trivia/questions/{question_id}/answers | List the answers available for a question
[**get_question_deltas**](GamificationTriviaApi.md#get_question_deltas) | **GET** /trivia/questions/delta | List question deltas in ascending order of updated date
[**get_question_tags**](GamificationTriviaApi.md#get_question_tags) | **GET** /trivia/questions/{id}/tags | List the tags for a question
[**get_question_template**](GamificationTriviaApi.md#get_question_template) | **GET** /trivia/questions/templates/{id} | Get a single question template
[**get_question_templates**](GamificationTriviaApi.md#get_question_templates) | **GET** /trivia/questions/templates | List and search question templates
[**get_questions**](GamificationTriviaApi.md#get_questions) | **GET** /trivia/questions | List and search questions
[**get_questions_count**](GamificationTriviaApi.md#get_questions_count) | **GET** /trivia/questions/count | Count questions based on filters
[**process_import_job**](GamificationTriviaApi.md#process_import_job) | **POST** /trivia/import/{id}/process | Start processing an import job
[**remove_question_tag**](GamificationTriviaApi.md#remove_question_tag) | **DELETE** /trivia/questions/{id}/tags/{tag} | Remove a tag from a question
[**remove_tag_to_questions_batch**](GamificationTriviaApi.md#remove_tag_to_questions_batch) | **DELETE** /trivia/questions/tags/{tag} | Remove a tag from a batch of questions
[**search_question_tags**](GamificationTriviaApi.md#search_question_tags) | **GET** /trivia/tags | List and search tags by the beginning of the string
[**update_import_job**](GamificationTriviaApi.md#update_import_job) | **PUT** /trivia/import/{id} | Update an import job
[**update_question**](GamificationTriviaApi.md#update_question) | **PUT** /trivia/questions/{id} | Update a question
[**update_question_answer**](GamificationTriviaApi.md#update_question_answer) | **PUT** /trivia/questions/{question_id}/answers/{id} | Update an answer for a question
[**update_question_template**](GamificationTriviaApi.md#update_question_template) | **PUT** /trivia/questions/templates/{id} | Update a question template
[**update_questions_in_bulk**](GamificationTriviaApi.md#update_questions_in_bulk) | **PUT** /trivia/questions | Bulk update questions


# **add_question_answers**
> AnswerResource add_question_answers(question_id, answer=answer)

Add an answer to a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
question_id = 'question_id_example' # str | The id of the question
answer = knetik_cloud.AnswerResource() # AnswerResource | The new answer (optional)

try: 
    # Add an answer to a question
    api_response = api_instance.add_question_answers(question_id, answer=answer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->add_question_answers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **str**| The id of the question | 
 **answer** | [**AnswerResource**](AnswerResource.md)| The new answer | [optional] 

### Return type

[**AnswerResource**](AnswerResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_question_tag**
> add_question_tag(id, tag=tag)

Add a tag to a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the question
tag = knetik_cloud.StringWrapper() # StringWrapper | The new tag (optional)

try: 
    # Add a tag to a question
    api_instance.add_question_tag(id, tag=tag)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->add_question_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 
 **tag** | [**StringWrapper**](StringWrapper.md)| The new tag | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tag_to_questions_batch**
> int add_tag_to_questions_batch(tag=tag, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)

Add a tag to a batch of questions

All questions that dont't have the tag and match filters will have it added. The returned number is the number of questions updated. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
tag = knetik_cloud.StringWrapper() # StringWrapper | The tag to add (optional)
filter_search = 'filter_search_example' # str | Filter for documents whose question, answers or tags contains provided string (optional)
filter_idset = 'filter_idset_example' # str | Filter for documents whose id is in the comma separated list provided (optional)
filter_category = 'filter_category_example' # str | Filter for questions with specified category, by id (optional)
filter_tag = 'filter_tag_example' # str | Filter for questions with specified tag (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for questions with specified tags (separated by comma) (optional)
filter_type = 'filter_type_example' # str | Filter for questions with specified type (optional)
filter_published = true # bool | Filter for questions currenctly published or not (optional)
filter_import_id = 789 # int | Filter for questions from a specific import job (optional)

try: 
    # Add a tag to a batch of questions
    api_response = api_instance.add_tag_to_questions_batch(tag=tag, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->add_tag_to_questions_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**StringWrapper**](StringWrapper.md)| The tag to add | [optional] 
 **filter_search** | **str**| Filter for documents whose question, answers or tags contains provided string | [optional] 
 **filter_idset** | **str**| Filter for documents whose id is in the comma separated list provided | [optional] 
 **filter_category** | **str**| Filter for questions with specified category, by id | [optional] 
 **filter_tag** | **str**| Filter for questions with specified tag | [optional] 
 **filter_tagset** | **str**| Filter for questions with specified tags (separated by comma) | [optional] 
 **filter_type** | **str**| Filter for questions with specified type | [optional] 
 **filter_published** | **bool**| Filter for questions currenctly published or not | [optional] 
 **filter_import_id** | **int**| Filter for questions from a specific import job | [optional] 

### Return type

**int**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_import_job**
> ImportJobResource create_import_job(request=request)

Create an import job

Set up a job to import a set of trivia questions from a cvs file at a remote url. the file will be validated asynchronously but will not be processed until started manually with the process endpoint. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
request = knetik_cloud.ImportJobResource() # ImportJobResource | The new import job (optional)

try: 
    # Create an import job
    api_response = api_instance.create_import_job(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->create_import_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ImportJobResource**](ImportJobResource.md)| The new import job | [optional] 

### Return type

[**ImportJobResource**](ImportJobResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_question**
> QuestionResource create_question(question=question)

Create a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
question = knetik_cloud.QuestionResource() # QuestionResource | The new question (optional)

try: 
    # Create a question
    api_response = api_instance.create_question(question=question)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->create_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | [**QuestionResource**](QuestionResource.md)| The new question | [optional] 

### Return type

[**QuestionResource**](QuestionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_question_template**
> QuestionTemplateResource create_question_template(question_template_resource=question_template_resource)

Create a question template

Question templates define a type of question and the properties they have. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
question_template_resource = knetik_cloud.QuestionTemplateResource() # QuestionTemplateResource | The question template resource object (optional)

try: 
    # Create a question template
    api_response = api_instance.create_question_template(question_template_resource=question_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->create_question_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_template_resource** | [**QuestionTemplateResource**](QuestionTemplateResource.md)| The question template resource object | [optional] 

### Return type

[**QuestionTemplateResource**](QuestionTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import_job**
> delete_import_job(id)

Delete an import job

Also deletes all questions that were imported by it. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The id of the job

try: 
    # Delete an import job
    api_instance.delete_import_job(id)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->delete_import_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the job | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_question**
> delete_question(id)

Delete a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the question

try: 
    # Delete a question
    api_instance.delete_question(id)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->delete_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_question_answers**
> delete_question_answers(question_id, id)

Remove an answer from a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
question_id = 'question_id_example' # str | The id of the question
id = 'id_example' # str | The id of the answer

try: 
    # Remove an answer from a question
    api_instance.delete_question_answers(question_id, id)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->delete_question_answers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **str**| The id of the question | 
 **id** | **str**| The id of the answer | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_question_template**
> delete_question_template(id, cascade=cascade)

Delete a question template

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a question template
    api_instance.delete_question_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->delete_question_template: %s\n" % e)
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

# **get_import_job**
> ImportJobResource get_import_job(id)

Get an import job

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The id of the job

try: 
    # Get an import job
    api_response = api_instance.get_import_job(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_import_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the job | 

### Return type

[**ImportJobResource**](ImportJobResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_jobs**
> PageResourceImportJobResource get_import_jobs(filter_vendor=filter_vendor, filter_category=filter_category, filter_name=filter_name, filter_status=filter_status, size=size, page=page, order=order)

Get a list of import job

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
filter_vendor = 'filter_vendor_example' # str | Filter for jobs by vendor id (optional)
filter_category = 'filter_category_example' # str | Filter for jobs by category id (optional)
filter_name = 'filter_name_example' # str | Filter for jobs which name *STARTS* with the given string (optional)
filter_status = 'filter_status_example' # str | Filter for jobs that are in a specific set of statuses (comma separated) (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get a list of import job
    api_response = api_instance.get_import_jobs(filter_vendor=filter_vendor, filter_category=filter_category, filter_name=filter_name, filter_status=filter_status, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_import_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_vendor** | **str**| Filter for jobs by vendor id | [optional] 
 **filter_category** | **str**| Filter for jobs by category id | [optional] 
 **filter_name** | **str**| Filter for jobs which name *STARTS* with the given string | [optional] 
 **filter_status** | **str**| Filter for jobs that are in a specific set of statuses (comma separated) | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceImportJobResource**](PageResourceImportJobResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question**
> QuestionResource get_question(id)

Get a single question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the question

try: 
    # Get a single question
    api_response = api_instance.get_question(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 

### Return type

[**QuestionResource**](QuestionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_answer**
> AnswerResource get_question_answer(question_id, id)

Get an answer for a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
question_id = 'question_id_example' # str | The id of the question
id = 'id_example' # str | The id of the answer

try: 
    # Get an answer for a question
    api_response = api_instance.get_question_answer(question_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **str**| The id of the question | 
 **id** | **str**| The id of the answer | 

### Return type

[**AnswerResource**](AnswerResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_answers**
> list[AnswerResource] get_question_answers(question_id)

List the answers available for a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
question_id = 'question_id_example' # str | The id of the question

try: 
    # List the answers available for a question
    api_response = api_instance.get_question_answers(question_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question_answers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **str**| The id of the question | 

### Return type

[**list[AnswerResource]**](AnswerResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_deltas**
> list[DeltaResource] get_question_deltas(since=since)

List question deltas in ascending order of updated date

The 'since' parameter is important to avoid getting a full list of all questions. Implementors should make sure they pass the updated date of the last resource loaded, not the date of the last request, in order to avoid gaps. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
since = 789 # int | Timestamp in seconds (optional)

try: 
    # List question deltas in ascending order of updated date
    api_response = api_instance.get_question_deltas(since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question_deltas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| Timestamp in seconds | [optional] 

### Return type

[**list[DeltaResource]**](DeltaResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_tags**
> list[str] get_question_tags(id)

List the tags for a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the question

try: 
    # List the tags for a question
    api_response = api_instance.get_question_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 

### Return type

**list[str]**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_template**
> QuestionTemplateResource get_question_template(id)

Get a single question template

<b>Permissions Needed:</b> TEMPLATE_ADMIN or TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single question template
    api_response = api_instance.get_question_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**QuestionTemplateResource**](QuestionTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_templates**
> PageResourceQuestionTemplateResource get_question_templates(size=size, page=page, order=order)

List and search question templates

<b>Permissions Needed:</b> TEMPLATE_ADMIN or TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search question templates
    api_response = api_instance.get_question_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceQuestionTemplateResource**](PageResourceQuestionTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_questions**
> PageResourceQuestionResource get_questions(size=size, page=page, order=order, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tagset=filter_tagset, filter_tag=filter_tag, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)

List and search questions

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)
filter_search = 'filter_search_example' # str | Filter for documents whose question, answers or tags contains provided string (optional)
filter_idset = 'filter_idset_example' # str | Filter for documents whose id is in the comma separated list provided (optional)
filter_category = 'filter_category_example' # str | Filter for questions with specified category, by id (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for questions with specified tags (separated by comma) (optional)
filter_tag = 'filter_tag_example' # str | Filter for questions with specified tag (optional)
filter_type = 'filter_type_example' # str | Filter for questions with specified type.  Allowable values: ('TEXT', 'IMAGE', 'VIDEO', 'AUDIO') (optional)
filter_published = true # bool | Filter for questions currenctly published or not (optional)
filter_import_id = 789 # int | Filter for questions from a specific import job (optional)

try: 
    # List and search questions
    api_response = api_instance.get_questions(size=size, page=page, order=order, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tagset=filter_tagset, filter_tag=filter_tag, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]
 **filter_search** | **str**| Filter for documents whose question, answers or tags contains provided string | [optional] 
 **filter_idset** | **str**| Filter for documents whose id is in the comma separated list provided | [optional] 
 **filter_category** | **str**| Filter for questions with specified category, by id | [optional] 
 **filter_tagset** | **str**| Filter for questions with specified tags (separated by comma) | [optional] 
 **filter_tag** | **str**| Filter for questions with specified tag | [optional] 
 **filter_type** | **str**| Filter for questions with specified type.  Allowable values: (&#39;TEXT&#39;, &#39;IMAGE&#39;, &#39;VIDEO&#39;, &#39;AUDIO&#39;) | [optional] 
 **filter_published** | **bool**| Filter for questions currenctly published or not | [optional] 
 **filter_import_id** | **int**| Filter for questions from a specific import job | [optional] 

### Return type

[**PageResourceQuestionResource**](PageResourceQuestionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_questions_count**
> int get_questions_count(filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published)

Count questions based on filters

This is also provided by the list endpoint so you don't need to call this for pagination purposes. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
filter_search = 'filter_search_example' # str | Filter for documents whose question, answers or tags contains provided string (optional)
filter_idset = 'filter_idset_example' # str | Filter for documents whose id is in the comma separated list provided (optional)
filter_category = 'filter_category_example' # str | Filter for questions with specified category, by id (optional)
filter_tag = 'filter_tag_example' # str | Filter for questions with specified tag (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for questions with specified tags (separated by comma) (optional)
filter_type = 'filter_type_example' # str | Filter for questions with specified type.  Allowable values: ('TEXT', 'IMAGE', 'VIDEO', 'AUDIO') (optional)
filter_published = true # bool | Filter for questions currenctly published or not (optional)

try: 
    # Count questions based on filters
    api_response = api_instance.get_questions_count(filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_questions_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_search** | **str**| Filter for documents whose question, answers or tags contains provided string | [optional] 
 **filter_idset** | **str**| Filter for documents whose id is in the comma separated list provided | [optional] 
 **filter_category** | **str**| Filter for questions with specified category, by id | [optional] 
 **filter_tag** | **str**| Filter for questions with specified tag | [optional] 
 **filter_tagset** | **str**| Filter for questions with specified tags (separated by comma) | [optional] 
 **filter_type** | **str**| Filter for questions with specified type.  Allowable values: (&#39;TEXT&#39;, &#39;IMAGE&#39;, &#39;VIDEO&#39;, &#39;AUDIO&#39;) | [optional] 
 **filter_published** | **bool**| Filter for questions currenctly published or not | [optional] 

### Return type

**int**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_import_job**
> ImportJobResource process_import_job(id, publish_now)

Start processing an import job

Will process the CSV file and add new questions asynchronously. The status of the job must be 'VALID'. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The id of the job
publish_now = true # bool | Whether the new questions should be published live immediately

try: 
    # Start processing an import job
    api_response = api_instance.process_import_job(id, publish_now)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->process_import_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the job | 
 **publish_now** | **bool**| Whether the new questions should be published live immediately | 

### Return type

[**ImportJobResource**](ImportJobResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_question_tag**
> remove_question_tag(id, tag)

Remove a tag from a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the question
tag = 'tag_example' # str | The tag to remove

try: 
    # Remove a tag from a question
    api_instance.remove_question_tag(id, tag)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->remove_question_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 
 **tag** | **str**| The tag to remove | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tag_to_questions_batch**
> int remove_tag_to_questions_batch(tag, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)

Remove a tag from a batch of questions

ll questions that have the tag and match filters will have it removed. The returned number is the number of questions updated. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
tag = 'tag_example' # str | The tag to remove
filter_search = 'filter_search_example' # str | Filter for documents whose question, answers or tags contains provided string (optional)
filter_idset = 'filter_idset_example' # str | Filter for documents whose id is in the comma separated list provided (optional)
filter_category = 'filter_category_example' # str | Filter for questions with specified category, by id (optional)
filter_tag = 'filter_tag_example' # str | Filter for questions with specified tag (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for questions with specified tags (separated by comma) (optional)
filter_type = 'filter_type_example' # str | Filter for questions with specified type.  Allowable values: ('TEXT', 'IMAGE', 'VIDEO', 'AUDIO') (optional)
filter_published = true # bool | Filter for questions currenctly published or not (optional)
filter_import_id = 789 # int | Filter for questions from a specific import job (optional)

try: 
    # Remove a tag from a batch of questions
    api_response = api_instance.remove_tag_to_questions_batch(tag, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->remove_tag_to_questions_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| The tag to remove | 
 **filter_search** | **str**| Filter for documents whose question, answers or tags contains provided string | [optional] 
 **filter_idset** | **str**| Filter for documents whose id is in the comma separated list provided | [optional] 
 **filter_category** | **str**| Filter for questions with specified category, by id | [optional] 
 **filter_tag** | **str**| Filter for questions with specified tag | [optional] 
 **filter_tagset** | **str**| Filter for questions with specified tags (separated by comma) | [optional] 
 **filter_type** | **str**| Filter for questions with specified type.  Allowable values: (&#39;TEXT&#39;, &#39;IMAGE&#39;, &#39;VIDEO&#39;, &#39;AUDIO&#39;) | [optional] 
 **filter_published** | **bool**| Filter for questions currenctly published or not | [optional] 
 **filter_import_id** | **int**| Filter for questions from a specific import job | [optional] 

### Return type

**int**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_question_tags**
> list[str] search_question_tags(filter_search=filter_search, filter_category=filter_category, filter_import_id=filter_import_id)

List and search tags by the beginning of the string

For performance reasons, search & category filters are mutually exclusive. If category is specified, search filter will be ignored in order to do fast matches for typeahead. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
filter_search = 'filter_search_example' # str | Filter for tags starting with the given text (optional)
filter_category = 'filter_category_example' # str | Filter for tags on questions from a specific category (optional)
filter_import_id = 789 # int | Filter for tags on questions from a specific import job (optional)

try: 
    # List and search tags by the beginning of the string
    api_response = api_instance.search_question_tags(filter_search=filter_search, filter_category=filter_category, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->search_question_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_search** | **str**| Filter for tags starting with the given text | [optional] 
 **filter_category** | **str**| Filter for tags on questions from a specific category | [optional] 
 **filter_import_id** | **int**| Filter for tags on questions from a specific import job | [optional] 

### Return type

**list[str]**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_import_job**
> ImportJobResource update_import_job(id, request=request)

Update an import job

Changes should be made before process is started for there to be any effect. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 789 # int | The id of the job
request = knetik_cloud.ImportJobResource() # ImportJobResource | The updated job (optional)

try: 
    # Update an import job
    api_response = api_instance.update_import_job(id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->update_import_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the job | 
 **request** | [**ImportJobResource**](ImportJobResource.md)| The updated job | [optional] 

### Return type

[**ImportJobResource**](ImportJobResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_question**
> QuestionResource update_question(id, question=question)

Update a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the question
question = knetik_cloud.QuestionResource() # QuestionResource | The updated question (optional)

try: 
    # Update a question
    api_response = api_instance.update_question(id, question=question)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->update_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 
 **question** | [**QuestionResource**](QuestionResource.md)| The updated question | [optional] 

### Return type

[**QuestionResource**](QuestionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_question_answer**
> update_question_answer(question_id, id, answer=answer)

Update an answer for a question

<b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
question_id = 'question_id_example' # str | The id of the question
id = 'id_example' # str | The id of the answer
answer = knetik_cloud.AnswerResource() # AnswerResource | The updated answer (optional)

try: 
    # Update an answer for a question
    api_instance.update_question_answer(question_id, id, answer=answer)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->update_question_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **str**| The id of the question | 
 **id** | **str**| The id of the answer | 
 **answer** | [**AnswerResource**](AnswerResource.md)| The updated answer | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_question_template**
> QuestionTemplateResource update_question_template(id, question_template_resource=question_template_resource)

Update a question template

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
question_template_resource = knetik_cloud.QuestionTemplateResource() # QuestionTemplateResource | The question template resource object (optional)

try: 
    # Update a question template
    api_response = api_instance.update_question_template(id, question_template_resource=question_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->update_question_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **question_template_resource** | [**QuestionTemplateResource**](QuestionTemplateResource.md)| The question template resource object | [optional] 

### Return type

[**QuestionTemplateResource**](QuestionTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_questions_in_bulk**
> int update_questions_in_bulk(question=question, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)

Bulk update questions

Will update all questions that match filters used (or all questions in system if no filters used). Body should match a question resource with only those properties you wish to set. Null values will be ignored. Returned number is how many were updated. <br><br><b>Permissions Needed:</b> TRIVIA_ADMIN

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
api_instance = knetik_cloud.GamificationTriviaApi(knetik_cloud.ApiClient(configuration))
question = knetik_cloud.QuestionResource() # QuestionResource | New values for a set of question fields (optional)
filter_search = 'filter_search_example' # str | Filter for documents whose question, answers or tags contains provided string (optional)
filter_idset = 'filter_idset_example' # str | Filter for documents whose id is in the comma separated list provided (optional)
filter_category = 'filter_category_example' # str | Filter for questions with specified category, by id (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for questions with specified tags (separated by comma) (optional)
filter_type = 'filter_type_example' # str | Filter for questions with specified type.  Allowable values: ('TEXT', 'IMAGE', 'VIDEO', 'AUDIO') (optional)
filter_published = true # bool | Filter for questions currenctly published or not (optional)
filter_import_id = 789 # int | Filter for questions from a specific import job (optional)

try: 
    # Bulk update questions
    api_response = api_instance.update_questions_in_bulk(question=question, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->update_questions_in_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | [**QuestionResource**](QuestionResource.md)| New values for a set of question fields | [optional] 
 **filter_search** | **str**| Filter for documents whose question, answers or tags contains provided string | [optional] 
 **filter_idset** | **str**| Filter for documents whose id is in the comma separated list provided | [optional] 
 **filter_category** | **str**| Filter for questions with specified category, by id | [optional] 
 **filter_tagset** | **str**| Filter for questions with specified tags (separated by comma) | [optional] 
 **filter_type** | **str**| Filter for questions with specified type.  Allowable values: (&#39;TEXT&#39;, &#39;IMAGE&#39;, &#39;VIDEO&#39;, &#39;AUDIO&#39;) | [optional] 
 **filter_published** | **bool**| Filter for questions currenctly published or not | [optional] 
 **filter_import_id** | **int**| Filter for questions from a specific import job | [optional] 

### Return type

**int**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

