# {{classname}}

All URIs are relative to *http://localhost:3000/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetArchive**](ContentApi.md#GetArchive) | **Get** /repos/{username}/{repo}/archive/{ref}/{format} | Download archive
[**GetContent**](ContentApi.md#GetContent) | **Get** /repos/{owner}/{repo}/content/{branch}/{treePath} | Get data from a folder in repository
[**GetRaw**](ContentApi.md#GetRaw) | **Get** /repos/{username}/{repo}/raw/{ref}/{path} | Download raw content
[**UploadContent**](ContentApi.md#UploadContent) | **Put** /repos/{owner}/{repo}/content/{branch}/{treePath} | Upload data to a repository

# **GetArchive**
> GetArchive(ctx, username, repo, ref, format)
Download archive

This method returns archive by given format.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **username** | **string**| A DagsHub username | 
  **repo** | **string**| name of the repository | 
  **ref** | **string**| The name of the commit/branch/tag | 
  **format** | **string**| The format of archive, either .zip or .tar.gz | 

### Return type

 (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetContent**
> []*os.File GetContent(ctx, owner, repo, branch, treePath, optional)
Get data from a folder in repository

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **owner** | **string**| owner of the repository | 
  **repo** | **string**| name of the repository | 
  **branch** | **string**| branch of the repository | 
  **treePath** | **string**| path of a folter in the repository | 
 **optional** | ***ContentApiGetContentOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ContentApiGetContentOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **includeSize** | **optional.Bool**|  | [default to false]

### Return type

[**[]*os.File**](array.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetRaw**
> GetRaw(ctx, username, repo, ref, path)
Download raw content

This method returns the raw content of a file.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **username** | **string**| A DagsHub username | 
  **repo** | **string**| name of the repository | 
  **ref** | **string**| The name of the commit/branch/tag | 
  **path** | **string**| The content path | 

### Return type

 (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UploadContent**
> Object UploadContent(ctx, owner, repo, branch, treePath, optional)
Upload data to a repository

last_commit - If the tip of the branch differs on the server at the moment of processing the request, the request is denied.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **owner** | **string**| owner of the repository | 
  **repo** | **string**| name of the repository | 
  **branch** | **string**| branch of the repository | 
  **treePath** | **string**| path of a folter in the repository | 
 **optional** | ***ContentApiUploadContentOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a ContentApiUploadContentOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------




 **commitSummary** | **optional.**|  | 
 **commitMessage** | **optional.**|  | 
 **commitChoice** | **optional.**|  | 
 **lastCommit** | **optional.**|  | 
 **newBranchName** | **optional.**|  | 
 **versioning** | **optional.**|  | 
 **files** | [**optional.Interface of []interface{}**](interface{}.md)|  | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

