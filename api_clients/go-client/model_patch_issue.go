/*
 * DagsHub API
 *
 * This API is used to interact with DagsHub. 
 *
 * API version: 1.0.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type PatchIssue struct {
	Title string `json:"title,omitempty"`
	Body string `json:"body,omitempty"`
	Assignee string `json:"assignee,omitempty"`
	Milestone int32 `json:"milestone,omitempty"`
	State *State `json:"state,omitempty"`
}