# {{classname}}

All URIs are relative to *http://localhost:3000/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateIssue**](IssuesApi.md#CreateIssue) | **Post** /repos/{owner}/{repo}/issues | Create an issue
[**EditIssue**](IssuesApi.md#EditIssue) | **Patch** /repos/{owner}/{repo}/issues | Edit an issue
[**GetIssue**](IssuesApi.md#GetIssue) | **Get** /repos/{owner}/{repo}/issues/{index} | Get a single issue
[**ListRepoIssues**](IssuesApi.md#ListRepoIssues) | **Get** /repos/{owner}/{repo}/issues | List issues for a repository

# **CreateIssue**
> Issue CreateIssue(ctx, owner, repo, optional)
Create an issue

Any user with read access to a repository can create an issue.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **owner** | **string**| owner of the repository | 
  **repo** | **string**| name of the repository | 
 **optional** | ***IssuesApiCreateIssueOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a IssuesApiCreateIssueOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of PostIssue**](PostIssue.md)|  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **EditIssue**
> Issue EditIssue(ctx, owner, repo, optional)
Edit an issue

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **owner** | **string**| owner of the repository | 
  **repo** | **string**| name of the repository | 
 **optional** | ***IssuesApiEditIssueOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a IssuesApiEditIssueOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **body** | [**optional.Interface of PatchIssue**](PatchIssue.md)|  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetIssue**
> Issue GetIssue(ctx, owner, repo, index)
Get a single issue

This endpoint may also return pull requests in the response. If an issue is a pull request, the object will include a pull_request key.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **owner** | **string**| owner of the repository | 
  **repo** | **string**| name of the repository | 
  **index** | **int32**| the index of an issue or a pull request | 

### Return type

[**Issue**](Issue.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListRepoIssues**
> []Issue ListRepoIssues(ctx, owner, repo)
List issues for a repository

This endpoint may also return pull requests in the response. If an issue is a pull request, the object will include a pull_request key.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **owner** | **string**| owner of the repository | 
  **repo** | **string**| name of the repository | 

### Return type

[**[]Issue**](array.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

