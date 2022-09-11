# DagsHub API
#
# This API is used to interact with DagsHub. 
#
# OpenAPI spec version: 1.0.0
# 
# Generated by: https://github.com/swagger-api/swagger-codegen.git

#' WebhookConfig Class
#'
#' @field url 
#' @field content_type 
#' @field secret 
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
WebhookConfig <- R6::R6Class(
  'WebhookConfig',
  public = list(
    `url` = NULL,
    `content_type` = NULL,
    `secret` = NULL,
    initialize = function(`url`, `content_type`, `secret`){
      if (!missing(`url`)) {
        stopifnot(is.character(`url`), length(`url`) == 1)
        self$`url` <- `url`
      }
      if (!missing(`content_type`)) {
        stopifnot(is.character(`content_type`), length(`content_type`) == 1)
        self$`content_type` <- `content_type`
      }
      if (!missing(`secret`)) {
        stopifnot(is.character(`secret`), length(`secret`) == 1)
        self$`secret` <- `secret`
      }
    },
    toJSON = function() {
      WebhookConfigObject <- list()
      if (!is.null(self$`url`)) {
        WebhookConfigObject[['url']] <- self$`url`
      }
      if (!is.null(self$`content_type`)) {
        WebhookConfigObject[['content_type']] <- self$`content_type`
      }
      if (!is.null(self$`secret`)) {
        WebhookConfigObject[['secret']] <- self$`secret`
      }

      WebhookConfigObject
    },
    fromJSON = function(WebhookConfigJson) {
      WebhookConfigObject <- jsonlite::fromJSON(WebhookConfigJson)
      if (!is.null(WebhookConfigObject$`url`)) {
        self$`url` <- WebhookConfigObject$`url`
      }
      if (!is.null(WebhookConfigObject$`content_type`)) {
        self$`content_type` <- WebhookConfigObject$`content_type`
      }
      if (!is.null(WebhookConfigObject$`secret`)) {
        self$`secret` <- WebhookConfigObject$`secret`
      }
    },
    toJSONString = function() {
       sprintf(
        '{
           "url": %s,
           "content_type": %s,
           "secret": %s
        }',
        self$`url`,
        self$`content_type`,
        self$`secret`
      )
    },
    fromJSONString = function(WebhookConfigJson) {
      WebhookConfigObject <- jsonlite::fromJSON(WebhookConfigJson)
      self$`url` <- WebhookConfigObject$`url`
      self$`content_type` <- WebhookConfigObject$`content_type`
      self$`secret` <- WebhookConfigObject$`secret`
    }
  )
)
