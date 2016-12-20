# swagger_client.GamificationTriviaApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_answers_using_post**](GamificationTriviaApi.md#add_answers_using_post) | **POST** /trivia/questions/{question_id}/answers | Add an answer to a question
[**add_tag_using_post**](GamificationTriviaApi.md#add_tag_using_post) | **POST** /trivia/questions/{id}/tags | Add a tag to a question
[**batch_add_tag_using_post**](GamificationTriviaApi.md#batch_add_tag_using_post) | **POST** /trivia/questions/tags | Add a tag to a batch of questions
[**batch_remove_tag_using_delete**](GamificationTriviaApi.md#batch_remove_tag_using_delete) | **DELETE** /trivia/questions/tags/{tag} | Remove a tag from a batch of questions
[**bulk_update_using_put**](GamificationTriviaApi.md#bulk_update_using_put) | **PUT** /trivia/questions | Bulk update questions
[**count_questions_using_get**](GamificationTriviaApi.md#count_questions_using_get) | **GET** /trivia/questions/count | Count questions based on filters.
[**create_question_template_using_post**](GamificationTriviaApi.md#create_question_template_using_post) | **POST** /trivia/questions/templates | Create a question template
[**create_question_using_post**](GamificationTriviaApi.md#create_question_using_post) | **POST** /trivia/questions | Create a question
[**create_using_post**](GamificationTriviaApi.md#create_using_post) | **POST** /trivia/import | Create an import job
[**delete_question_template_using_delete**](GamificationTriviaApi.md#delete_question_template_using_delete) | **DELETE** /trivia/questions/templates/{id} | Delete a question template
[**delete_question_using_delete**](GamificationTriviaApi.md#delete_question_using_delete) | **DELETE** /trivia/questions/{id} | Delete a question
[**delete_using_delete**](GamificationTriviaApi.md#delete_using_delete) | **DELETE** /trivia/import/{id} | Delete an import job
[**get_answer_using_get**](GamificationTriviaApi.md#get_answer_using_get) | **GET** /trivia/questions/{question_id}/answers/{id} | Get an answer for a question
[**get_answers_using_get**](GamificationTriviaApi.md#get_answers_using_get) | **GET** /trivia/questions/{question_id}/answers | List the answers available for a question
[**get_list_using_get1**](GamificationTriviaApi.md#get_list_using_get1) | **GET** /trivia/import | Get a list of import job
[**get_question_template_using_get**](GamificationTriviaApi.md#get_question_template_using_get) | **GET** /trivia/questions/templates/{id} | Get a single question template
[**get_question_templates_using_get**](GamificationTriviaApi.md#get_question_templates_using_get) | **GET** /trivia/questions/templates | List and search question templates
[**get_question_using_get**](GamificationTriviaApi.md#get_question_using_get) | **GET** /trivia/questions/{id} | Get a single question
[**get_questions_delta_using_get**](GamificationTriviaApi.md#get_questions_delta_using_get) | **GET** /trivia/questions/delta | List question deltas in ascending order of updated date
[**get_questions_using_get**](GamificationTriviaApi.md#get_questions_using_get) | **GET** /trivia/questions | List and search questions
[**get_tags_using_get1**](GamificationTriviaApi.md#get_tags_using_get1) | **GET** /trivia/questions/{id}/tags | List the tags for a question
[**get_tags_using_get2**](GamificationTriviaApi.md#get_tags_using_get2) | **GET** /trivia/tags | List and search tags by the beginning of the string
[**get_using_get**](GamificationTriviaApi.md#get_using_get) | **GET** /trivia/import/{id} | Get an import job
[**remove_answers_using_delete**](GamificationTriviaApi.md#remove_answers_using_delete) | **DELETE** /trivia/questions/{question_id}/answers/{id} | Remove an answer from a question
[**remove_tag_using_delete**](GamificationTriviaApi.md#remove_tag_using_delete) | **DELETE** /trivia/questions/{id}/tags/{tag} | Remove a tag from a question
[**start_process_using_post**](GamificationTriviaApi.md#start_process_using_post) | **POST** /trivia/import/{id}/process | Start processing an import job
[**update_answer_using_put**](GamificationTriviaApi.md#update_answer_using_put) | **PUT** /trivia/questions/{question_id}/answers/{id} | Update an answer for a question
[**update_question_template_using_put**](GamificationTriviaApi.md#update_question_template_using_put) | **PUT** /trivia/questions/templates/{id} | Update a question template
[**update_question_using_put**](GamificationTriviaApi.md#update_question_using_put) | **PUT** /trivia/questions/{id} | Update a question
[**update_using_put**](GamificationTriviaApi.md#update_using_put) | **PUT** /trivia/import/{id} | Update an import job


# **add_answers_using_post**
> AnswerResource add_answers_using_post(question_id, answer=answer)

Add an answer to a question

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
api_instance = swagger_client.GamificationTriviaApi()
question_id = 'question_id_example' # str | The id of the question
answer = swagger_client.AnswerResource() # AnswerResource | The new answer (optional)

try: 
    # Add an answer to a question
    api_response = api_instance.add_answers_using_post(question_id, answer=answer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->add_answers_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **str**| The id of the question | 
 **answer** | [**AnswerResource**](AnswerResource.md)| The new answer | [optional] 

### Return type

[**AnswerResource**](AnswerResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tag_using_post**
> add_tag_using_post(id, tag=tag)

Add a tag to a question

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
api_instance = swagger_client.GamificationTriviaApi()
id = 'id_example' # str | The id of the question
tag = 'tag_example' # str | The new tag (optional)

try: 
    # Add a tag to a question
    api_instance.add_tag_using_post(id, tag=tag)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->add_tag_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 
 **tag** | **str**| The new tag | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_add_tag_using_post**
> int batch_add_tag_using_post(tag=tag, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)

Add a tag to a batch of questions

All questions that dont't have the tag and match filters will have it added. The returned number is the number of questions updated.

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
api_instance = swagger_client.GamificationTriviaApi()
tag = 'tag_example' # str | The tag to add (optional)
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
    api_response = api_instance.batch_add_tag_using_post(tag=tag, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->batch_add_tag_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| The tag to add | [optional] 
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_remove_tag_using_delete**
> int batch_remove_tag_using_delete(tag, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)

Remove a tag from a batch of questions

ll questions that have the tag and match filters will have it removed. The returned number is the number of questions updated.

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
api_instance = swagger_client.GamificationTriviaApi()
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
    api_response = api_instance.batch_remove_tag_using_delete(tag, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->batch_remove_tag_using_delete: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_using_put**
> int bulk_update_using_put(question=question, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)

Bulk update questions

Will update all questions that match filters used (or all questions in system if no filters used). Body should match a question resource with only those properties you wish to set. Null values will be ignored. Returned number is how many were updated.

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
api_instance = swagger_client.GamificationTriviaApi()
question = swagger_client.QuestionResource() # QuestionResource | New values for a set of question fields (optional)
filter_search = 'filter_search_example' # str | Filter for documents whose question, answers or tags contains provided string (optional)
filter_idset = 'filter_idset_example' # str | Filter for documents whose id is in the comma separated list provided (optional)
filter_category = 'filter_category_example' # str | Filter for questions with specified category, by id (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for questions with specified tags (separated by comma) (optional)
filter_type = 'filter_type_example' # str | Filter for questions with specified type.  Allowable values: ('TEXT', 'IMAGE', 'VIDEO', 'AUDIO') (optional)
filter_published = true # bool | Filter for questions currenctly published or not (optional)
filter_import_id = 789 # int | Filter for questions from a specific import job (optional)

try: 
    # Bulk update questions
    api_response = api_instance.bulk_update_using_put(question=question, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->bulk_update_using_put: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_questions_using_get**
> int count_questions_using_get(filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published)

Count questions based on filters.

This is also provided by the list endpoint so you don't need to call this for pagination purposes

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
api_instance = swagger_client.GamificationTriviaApi()
filter_search = 'filter_search_example' # str | Filter for documents whose question, answers or tags contains provided string (optional)
filter_idset = 'filter_idset_example' # str | Filter for documents whose id is in the comma separated list provided (optional)
filter_category = 'filter_category_example' # str | Filter for questions with specified category, by id (optional)
filter_tag = 'filter_tag_example' # str | Filter for questions with specified tag (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for questions with specified tags (separated by comma) (optional)
filter_type = 'filter_type_example' # str | Filter for questions with specified type.  Allowable values: ('TEXT', 'IMAGE', 'VIDEO', 'AUDIO') (optional)
filter_published = true # bool | Filter for questions currenctly published or not (optional)

try: 
    # Count questions based on filters.
    api_response = api_instance.count_questions_using_get(filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tag=filter_tag, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->count_questions_using_get: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_question_template_using_post**
> QuestionTemplateResource create_question_template_using_post(question_template_resource=question_template_resource)

Create a question template

Question templates define a type of question and the properties they have

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
api_instance = swagger_client.GamificationTriviaApi()
question_template_resource = swagger_client.QuestionTemplateResource() # QuestionTemplateResource | The question template resource object (optional)

try: 
    # Create a question template
    api_response = api_instance.create_question_template_using_post(question_template_resource=question_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->create_question_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_template_resource** | [**QuestionTemplateResource**](QuestionTemplateResource.md)| The question template resource object | [optional] 

### Return type

[**QuestionTemplateResource**](QuestionTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_question_using_post**
> QuestionResource create_question_using_post(question=question)

Create a question

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
api_instance = swagger_client.GamificationTriviaApi()
question = swagger_client.QuestionResource() # QuestionResource | The new question (optional)

try: 
    # Create a question
    api_response = api_instance.create_question_using_post(question=question)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->create_question_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question** | [**QuestionResource**](QuestionResource.md)| The new question | [optional] 

### Return type

[**QuestionResource**](QuestionResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_using_post**
> ImportJobResource create_using_post(request=request)

Create an import job

Set up a job to import a set of trivia questions from a cvs file at a remote url. the file will be validated asynchronously but will not be processed until started manually with the process endpoint.

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
api_instance = swagger_client.GamificationTriviaApi()
request = swagger_client.ImportJobResource() # ImportJobResource | The new import job (optional)

try: 
    # Create an import job
    api_response = api_instance.create_using_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->create_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ImportJobResource**](ImportJobResource.md)| The new import job | [optional] 

### Return type

[**ImportJobResource**](ImportJobResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_question_template_using_delete**
> delete_question_template_using_delete(id, cascade=cascade)

Delete a question template

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
api_instance = swagger_client.GamificationTriviaApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a question template
    api_instance.delete_question_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->delete_question_template_using_delete: %s\n" % e)
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

# **delete_question_using_delete**
> delete_question_using_delete(id)

Delete a question

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
api_instance = swagger_client.GamificationTriviaApi()
id = 'id_example' # str | The id of the question

try: 
    # Delete a question
    api_instance.delete_question_using_delete(id)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->delete_question_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete**
> delete_using_delete(id)

Delete an import job

Also deletes all questions that were imported by it

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
api_instance = swagger_client.GamificationTriviaApi()
id = 789 # int | The id of the job

try: 
    # Delete an import job
    api_instance.delete_using_delete(id)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the job | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_answer_using_get**
> AnswerResource get_answer_using_get(question_id, id)

Get an answer for a question

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
api_instance = swagger_client.GamificationTriviaApi()
question_id = 'question_id_example' # str | The id of the question
id = 'id_example' # str | The id of the answer

try: 
    # Get an answer for a question
    api_response = api_instance.get_answer_using_get(question_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_answer_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **str**| The id of the question | 
 **id** | **str**| The id of the answer | 

### Return type

[**AnswerResource**](AnswerResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_answers_using_get**
> list[AnswerResource] get_answers_using_get(question_id)

List the answers available for a question

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
api_instance = swagger_client.GamificationTriviaApi()
question_id = 'question_id_example' # str | The id of the question

try: 
    # List the answers available for a question
    api_response = api_instance.get_answers_using_get(question_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_answers_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **str**| The id of the question | 

### Return type

[**list[AnswerResource]**](AnswerResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_using_get1**
> PageImportJobResource get_list_using_get1(filter_vendor=filter_vendor, filter_category=filter_category, filter_name=filter_name, filter_status=filter_status, size=size, page=page, order=order)

Get a list of import job

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
api_instance = swagger_client.GamificationTriviaApi()
filter_vendor = 'filter_vendor_example' # str | Filter for jobs by vendor id (optional)
filter_category = 'filter_category_example' # str | Filter for jobs by category id (optional)
filter_name = 'filter_name_example' # str | Filter for jobs which name *STARTS* with the given string (optional)
filter_status = 'filter_status_example' # str | Filter for jobs that are in a specific set of statuses (comma separated) (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get a list of import job
    api_response = api_instance.get_list_using_get1(filter_vendor=filter_vendor, filter_category=filter_category, filter_name=filter_name, filter_status=filter_status, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_list_using_get1: %s\n" % e)
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

[**PageImportJobResource**](PageImportJobResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_template_using_get**
> QuestionTemplateResource get_question_template_using_get(id)

Get a single question template

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
api_instance = swagger_client.GamificationTriviaApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single question template
    api_response = api_instance.get_question_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question_template_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**QuestionTemplateResource**](QuestionTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_templates_using_get**
> PageQuestionTemplateResource get_question_templates_using_get(size=size, page=page, order=order)

List and search question templates

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
api_instance = swagger_client.GamificationTriviaApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search question templates
    api_response = api_instance.get_question_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question_templates_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageQuestionTemplateResource**](PageQuestionTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_question_using_get**
> QuestionResource get_question_using_get(id)

Get a single question

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
api_instance = swagger_client.GamificationTriviaApi()
id = 'id_example' # str | The id of the question

try: 
    # Get a single question
    api_response = api_instance.get_question_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_question_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 

### Return type

[**QuestionResource**](QuestionResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_questions_delta_using_get**
> list[DeltaResource] get_questions_delta_using_get(since=since)

List question deltas in ascending order of updated date

The 'since' parameter is important to avoid getting a full list of all questions. Implementors should make sure they pass the updated date of the last resource loaded, not the date of the last request, in order to avoid gaps

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
api_instance = swagger_client.GamificationTriviaApi()
since = 789 # int | Timestamp in seconds (optional)

try: 
    # List question deltas in ascending order of updated date
    api_response = api_instance.get_questions_delta_using_get(since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_questions_delta_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| Timestamp in seconds | [optional] 

### Return type

[**list[DeltaResource]**](DeltaResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_questions_using_get**
> PageQuestionResource get_questions_using_get(size=size, page=page, order=order, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)

List and search questions

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
api_instance = swagger_client.GamificationTriviaApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)
filter_search = 'filter_search_example' # str | Filter for documents whose question, answers or tags contains provided string (optional)
filter_idset = 'filter_idset_example' # str | Filter for documents whose id is in the comma separated list provided (optional)
filter_category = 'filter_category_example' # str | Filter for questions with specified category, by id (optional)
filter_tagset = 'filter_tagset_example' # str | Filter for questions with specified tags (separated by comma) (optional)
filter_type = 'filter_type_example' # str | Filter for questions with specified type.  Allowable values: ('TEXT', 'IMAGE', 'VIDEO', 'AUDIO') (optional)
filter_published = true # bool | Filter for questions currenctly published or not (optional)
filter_import_id = 789 # int | Filter for questions from a specific import job (optional)

try: 
    # List and search questions
    api_response = api_instance.get_questions_using_get(size=size, page=page, order=order, filter_search=filter_search, filter_idset=filter_idset, filter_category=filter_category, filter_tagset=filter_tagset, filter_type=filter_type, filter_published=filter_published, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_questions_using_get: %s\n" % e)
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
 **filter_type** | **str**| Filter for questions with specified type.  Allowable values: (&#39;TEXT&#39;, &#39;IMAGE&#39;, &#39;VIDEO&#39;, &#39;AUDIO&#39;) | [optional] 
 **filter_published** | **bool**| Filter for questions currenctly published or not | [optional] 
 **filter_import_id** | **int**| Filter for questions from a specific import job | [optional] 

### Return type

[**PageQuestionResource**](PageQuestionResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_using_get1**
> list[str] get_tags_using_get1(id)

List the tags for a question

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
api_instance = swagger_client.GamificationTriviaApi()
id = 'id_example' # str | The id of the question

try: 
    # List the tags for a question
    api_response = api_instance.get_tags_using_get1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_tags_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 

### Return type

**list[str]**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_using_get2**
> Collectionstring get_tags_using_get2(filter_search=filter_search, filter_category=filter_category, filter_import_id=filter_import_id)

List and search tags by the beginning of the string

For performance reasons, search & category filters are mutually exclusive. If category is specified, search filter will be ignored in order to do fast matches for typeahead.

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
api_instance = swagger_client.GamificationTriviaApi()
filter_search = 'filter_search_example' # str | Filter for tags starting with the given text (optional)
filter_category = 'filter_category_example' # str | Filter for tags on questions from a specific category (optional)
filter_import_id = 789 # int | Filter for tags on questions from a specific import job (optional)

try: 
    # List and search tags by the beginning of the string
    api_response = api_instance.get_tags_using_get2(filter_search=filter_search, filter_category=filter_category, filter_import_id=filter_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_tags_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_search** | **str**| Filter for tags starting with the given text | [optional] 
 **filter_category** | **str**| Filter for tags on questions from a specific category | [optional] 
 **filter_import_id** | **int**| Filter for tags on questions from a specific import job | [optional] 

### Return type

[**Collectionstring**](Collectionstring.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get**
> ImportJobResource get_using_get(id)

Get an import job

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
api_instance = swagger_client.GamificationTriviaApi()
id = 789 # int | The id of the job

try: 
    # Get an import job
    api_response = api_instance.get_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the job | 

### Return type

[**ImportJobResource**](ImportJobResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_answers_using_delete**
> remove_answers_using_delete(question_id, id)

Remove an answer from a question

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
api_instance = swagger_client.GamificationTriviaApi()
question_id = 'question_id_example' # str | The id of the question
id = 'id_example' # str | The id of the answer

try: 
    # Remove an answer from a question
    api_instance.remove_answers_using_delete(question_id, id)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->remove_answers_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **str**| The id of the question | 
 **id** | **str**| The id of the answer | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tag_using_delete**
> remove_tag_using_delete(id, tag)

Remove a tag from a question

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
api_instance = swagger_client.GamificationTriviaApi()
id = 'id_example' # str | The id of the question
tag = 'tag_example' # str | The tag to remove

try: 
    # Remove a tag from a question
    api_instance.remove_tag_using_delete(id, tag)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->remove_tag_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 
 **tag** | **str**| The tag to remove | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_process_using_post**
> ImportJobResource start_process_using_post(id, publish_now)

Start processing an import job

Will process the CSV file and add new questions asynchronously. The status of the job must be 'VALID'.

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
api_instance = swagger_client.GamificationTriviaApi()
id = 789 # int | The id of the job
publish_now = true # bool | Whether the new questions should be published live immediately

try: 
    # Start processing an import job
    api_response = api_instance.start_process_using_post(id, publish_now)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->start_process_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the job | 
 **publish_now** | **bool**| Whether the new questions should be published live immediately | 

### Return type

[**ImportJobResource**](ImportJobResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_answer_using_put**
> update_answer_using_put(question_id, id, answer=answer)

Update an answer for a question

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
api_instance = swagger_client.GamificationTriviaApi()
question_id = 'question_id_example' # str | The id of the question
id = 'id_example' # str | The id of the answer
answer = swagger_client.AnswerResource() # AnswerResource | The updated answer (optional)

try: 
    # Update an answer for a question
    api_instance.update_answer_using_put(question_id, id, answer=answer)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->update_answer_using_put: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_question_template_using_put**
> update_question_template_using_put(id, question_template_resource=question_template_resource)

Update a question template

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
api_instance = swagger_client.GamificationTriviaApi()
id = 'id_example' # str | The id of the template
question_template_resource = swagger_client.QuestionTemplateResource() # QuestionTemplateResource | The question template resource object (optional)

try: 
    # Update a question template
    api_instance.update_question_template_using_put(id, question_template_resource=question_template_resource)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->update_question_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **question_template_resource** | [**QuestionTemplateResource**](QuestionTemplateResource.md)| The question template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_question_using_put**
> QuestionResource update_question_using_put(id, question=question)

Update a question

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
api_instance = swagger_client.GamificationTriviaApi()
id = 'id_example' # str | The id of the question
question = swagger_client.QuestionResource() # QuestionResource | The updated question (optional)

try: 
    # Update a question
    api_response = api_instance.update_question_using_put(id, question=question)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->update_question_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the question | 
 **question** | [**QuestionResource**](QuestionResource.md)| The updated question | [optional] 

### Return type

[**QuestionResource**](QuestionResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put**
> ImportJobResource update_using_put(id, request=request)

Update an import job

Changes should be made before process is started for there to be any effect.

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
api_instance = swagger_client.GamificationTriviaApi()
id = 789 # int | The id of the job
request = swagger_client.ImportJobResource() # ImportJobResource | The updated job (optional)

try: 
    # Update an import job
    api_response = api_instance.update_using_put(id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationTriviaApi->update_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the job | 
 **request** | [**ImportJobResource**](ImportJobResource.md)| The updated job | [optional] 

### Return type

[**ImportJobResource**](ImportJobResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

