# knetik_cloud.AmazonWebServicesS3Api

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_download_url**](AmazonWebServicesS3Api.md#get_download_url) | **GET** /amazon/s3/downloadurl | Get a temporary signed S3 URL for download
[**get_signed_s3_url**](AmazonWebServicesS3Api.md#get_signed_s3_url) | **GET** /amazon/s3/signedposturl | Get a signed S3 URL for upload


# **get_download_url**
> str get_download_url(bucket=bucket, path=path, expiration=expiration)

Get a temporary signed S3 URL for download

To give access to files in your own S3 account, you will need to grant KnetikcCloud access to the file by adjusting your bucket policy accordingly. See S3 documentation for details. <br><br><b>Permissions Needed:</b> S3_ADMIN

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
api_instance = knetik_cloud.AmazonWebServicesS3Api(knetik_cloud.ApiClient(configuration))
bucket = 'bucket_example' # str | S3 bucket name (optional)
path = 'path_example' # str | The path to the file relative to the bucket (the s3 object key) (optional)
expiration = 60 # int | The number of seconds this URL will be valid. Default to 60 (optional) (default to 60)

try: 
    # Get a temporary signed S3 URL for download
    api_response = api_instance.get_download_url(bucket=bucket, path=path, expiration=expiration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmazonWebServicesS3Api->get_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| S3 bucket name | [optional] 
 **path** | **str**| The path to the file relative to the bucket (the s3 object key) | [optional] 
 **expiration** | **int**| The number of seconds this URL will be valid. Default to 60 | [optional] [default to 60]

### Return type

**str**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signed_s3_url**
> AmazonS3Activity get_signed_s3_url(filename=filename, content_type=content_type)

Get a signed S3 URL for upload

Requires the file name and file content type (i.e., 'video/mpeg'). Make a PUT to the resulting url to upload the file and use the cdn_url to retrieve it after. <br><br><b>Permissions Needed:</b> S3_USER or S3_ADMIN

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
api_instance = knetik_cloud.AmazonWebServicesS3Api(knetik_cloud.ApiClient(configuration))
filename = 'filename_example' # str | The file name (optional)
content_type = 'content_type_example' # str | The content type (optional)

try: 
    # Get a signed S3 URL for upload
    api_response = api_instance.get_signed_s3_url(filename=filename, content_type=content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AmazonWebServicesS3Api->get_signed_s3_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| The file name | [optional] 
 **content_type** | **str**| The content type | [optional] 

### Return type

[**AmazonS3Activity**](AmazonS3Activity.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

