# DagsHubApi.ContentApi

All URIs are relative to *http://localhost:3000/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getArchive**](ContentApi.md#getArchive) | **GET** /repos/{username}/{repo}/archive/{ref}/{format} | Download archive
[**getContent**](ContentApi.md#getContent) | **GET** /repos/{owner}/{repo}/content/{branch}/{treePath} | Get data from a folder in repository
[**getRaw**](ContentApi.md#getRaw) | **GET** /repos/{username}/{repo}/raw/{ref}/{path} | Download raw content
[**uploadContent**](ContentApi.md#uploadContent) | **PUT** /repos/{owner}/{repo}/content/{branch}/{treePath} | Upload data to a repository

<a name="getArchive"></a>
# **getArchive**
> getArchive(username, repo, ref, format)

Download archive

This method returns archive by given format.

### Example
```javascript
import {DagsHubApi} from 'dags_hub_api';
let defaultClient = DagsHubApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

// Configure API key authorization: tokenAuth
let tokenAuth = defaultClient.authentications['tokenAuth'];
tokenAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.apiKeyPrefix = 'Token';

let apiInstance = new DagsHubApi.ContentApi();
let username = "username_example"; // String | A DagsHub username
let repo = "repo_example"; // String | name of the repository
let ref = "ref_example"; // String | The name of the commit/branch/tag
let format = "format_example"; // String | The format of archive, either .zip or .tar.gz

apiInstance.getArchive(username, repo, ref, format, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| A DagsHub username | 
 **repo** | **String**| name of the repository | 
 **ref** | **String**| The name of the commit/branch/tag | 
 **format** | **String**| The format of archive, either .zip or .tar.gz | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="getContent"></a>
# **getContent**
> Files getContent(owner, repo, branch, treePath, opts)

Get data from a folder in repository

### Example
```javascript
import {DagsHubApi} from 'dags_hub_api';
let defaultClient = DagsHubApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

// Configure API key authorization: tokenAuth
let tokenAuth = defaultClient.authentications['tokenAuth'];
tokenAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.apiKeyPrefix = 'Token';

let apiInstance = new DagsHubApi.ContentApi();
let owner = "owner_example"; // String | owner of the repository
let repo = "repo_example"; // String | name of the repository
let branch = "branch_example"; // String | branch of the repository
let treePath = "treePath_example"; // String | path of a folter in the repository
let opts = { 
  'includeSize': false // Boolean | 
};
apiInstance.getContent(owner, repo, branch, treePath, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| owner of the repository | 
 **repo** | **String**| name of the repository | 
 **branch** | **String**| branch of the repository | 
 **treePath** | **String**| path of a folter in the repository | 
 **includeSize** | **Boolean**|  | [optional] [default to false]

### Return type

[**Files**](Files.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getRaw"></a>
# **getRaw**
> getRaw(username, repo, ref, path)

Download raw content

This method returns the raw content of a file.

### Example
```javascript
import {DagsHubApi} from 'dags_hub_api';
let defaultClient = DagsHubApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

// Configure API key authorization: tokenAuth
let tokenAuth = defaultClient.authentications['tokenAuth'];
tokenAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.apiKeyPrefix = 'Token';

let apiInstance = new DagsHubApi.ContentApi();
let username = "username_example"; // String | A DagsHub username
let repo = "repo_example"; // String | name of the repository
let ref = "ref_example"; // String | The name of the commit/branch/tag
let path = "path_example"; // String | The content path

apiInstance.getRaw(username, repo, ref, path, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| A DagsHub username | 
 **repo** | **String**| name of the repository | 
 **ref** | **String**| The name of the commit/branch/tag | 
 **path** | **String**| The content path | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="uploadContent"></a>
# **uploadContent**
> Object uploadContent(owner, repo, branch, treePath, opts)

Upload data to a repository

last_commit - If the tip of the branch differs on the server at the moment of processing the request, the request is denied.

### Example
```javascript
import {DagsHubApi} from 'dags_hub_api';
let defaultClient = DagsHubApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

// Configure API key authorization: tokenAuth
let tokenAuth = defaultClient.authentications['tokenAuth'];
tokenAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.apiKeyPrefix = 'Token';

let apiInstance = new DagsHubApi.ContentApi();
let owner = "owner_example"; // String | owner of the repository
let repo = "repo_example"; // String | name of the repository
let branch = "branch_example"; // String | branch of the repository
let treePath = "treePath_example"; // String | path of a folter in the repository
let opts = { 
  'commitSummary': "commitSummary_example", // String | 
  'commitMessage': "commitMessage_example", // String | 
  'commitChoice': "commitChoice_example", // String | 
  'lastCommit': "lastCommit_example", // String | 
  'newBranchName': "newBranchName_example", // String | 
  'versioning': "versioning_example", // String | 
  'files': null // [Object] | 
};
apiInstance.uploadContent(owner, repo, branch, treePath, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| owner of the repository | 
 **repo** | **String**| name of the repository | 
 **branch** | **String**| branch of the repository | 
 **treePath** | **String**| path of a folter in the repository | 
 **commitSummary** | **String**|  | [optional] 
 **commitMessage** | **String**|  | [optional] 
 **commitChoice** | **String**|  | [optional] 
 **lastCommit** | **String**|  | [optional] 
 **newBranchName** | **String**|  | [optional] 
 **versioning** | **String**|  | [optional] 
 **files** | [**[Object]**](Object.md)|  | [optional] 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

