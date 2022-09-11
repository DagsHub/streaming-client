/*
 * DagsHub API
 *
 * This API is used to interact with DagsHub. 
 *
 * API version: 1.0.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type HooksIdBody struct {
	Config *WebhookConfig `json:"config,omitempty"`
	Events *[]interface{} `json:"events,omitempty"`
	// Weather the hook is actually triggered on pushes or not. Ignore this field to leave it unchanged.
	Active bool `json:"active,omitempty"`
}
