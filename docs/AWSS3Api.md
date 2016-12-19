# swagger_client.AWSS3Api

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pre_sign_url_using_get**](AWSS3Api.md#pre_sign_url_using_get) | **GET** /amazon/s3/signedposturl | Get a signed S3 URL


# **pre_sign_url_using_get**
> AmazonS3Activity pre_sign_url_using_get(filename=filename, content_type=content_type)

Get a signed S3 URL

Requires the file name and file content type (i.e., 'video/mpeg')

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
api_instance = swagger_client.AWSS3Api()
filename = 'filename_example' # str | The file name (optional)
content_type = 'content_type_example' # str | The content type (optional)

try: 
    # Get a signed S3 URL
    api_response = api_instance.pre_sign_url_using_get(filename=filename, content_type=content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AWSS3Api->pre_sign_url_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| The file name | [optional] 
 **content_type** | **str**| The content type | [optional] 

### Return type

[**AmazonS3Activity**](AmazonS3Activity.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

