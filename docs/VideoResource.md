# VideoResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the video is available, based on various factors | [optional] 
**author** | [**SimpleReferenceResourcelong**](SimpleReferenceResourcelong.md) | The original artist of the media | [optional] 
**authored** | **int** | The date the media was created as a unix timestamp in seconds | [optional] 
**banned** | **bool** | Whether the video has been banned or not | [optional] 
**category** | [**SimpleReferenceResourcestring**](SimpleReferenceResourcestring.md) | The category of the video | 
**comments** | [**list[CommentResource]**](CommentResource.md) | The comments of the video | [optional] 
**contributors** | [**list[ContributionResource]**](ContributionResource.md) | Artists that contributed to the creation. See separate endpoint to add to list | [optional] 
**created_date** | **int** | The date/time this resource was created in seconds since unix epoch | [optional] 
**embed** | **str** | The country of an embedable version | [optional] 
**extension** | **str** | The file extension of the media file. 1-5 characters | 
**height** | **int** | The height of the video in px | 
**id** | **int** | The unique ID for that resource | [optional] 
**length** | **int** | The length of the video in seconds | 
**location** | **str** | The country of the media. Typically a url. Cannot be blank | 
**long_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**mime_type** | **str** | The mime-type of the media | [optional] 
**name** | **str** | The user friendly name of that resource | 
**priority** | **int** | The sort order of the video. default: 100 | [optional] 
**privacy** | **str** | The privacy setting. default: private | [optional] 
**published** | **bool** | Whether the video has been made public. Default true | [optional] 
**short_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**size** | **int** | The size of the media. Minimum 0 if supplied | [optional] 
**tags** | **list[str]** | The tags for the video | [optional] 
**thumbnail** | **str** | The country of a thumbnail version. Typically a url | [optional] 
**updated_date** | **int** | The date/time this resource was last updated in seconds since unix epoch | [optional] 
**uploader** | [**SimpleUserResource**](SimpleUserResource.md) | The user the media was uploaded by. May be null for system uploaded media. May only be set to a user other than the current caller if VIDEOS_ADMIN permission. Null will mean the caller is the uploader unless the caller has VIDEOS_ADMIN permission, in which case it will be set to null | [optional] 
**views** | **int** | The view count of the video | [optional] 
**width** | **int** | The width of the video in px | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


