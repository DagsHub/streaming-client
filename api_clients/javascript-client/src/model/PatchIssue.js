/*
 * DagsHub API
 * This API is used to interact with DagsHub. 
 *
 * OpenAPI spec version: 1.0.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.35
 *
 * Do not edit the class manually.
 *
 */
import {ApiClient} from '../ApiClient';
import {Assignee} from './Assignee';
import {Body} from './Body';
import {Milestone} from './Milestone';
import {State} from './State';
import {Title} from './Title';

/**
 * The PatchIssue model module.
 * @module model/PatchIssue
 * @version 1.0.0
 */
export class PatchIssue {
  /**
   * Constructs a new <code>PatchIssue</code>.
   * @alias module:model/PatchIssue
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>PatchIssue</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/PatchIssue} obj Optional instance to populate.
   * @return {module:model/PatchIssue} The populated <code>PatchIssue</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new PatchIssue();
      if (data.hasOwnProperty('title'))
        obj.title = Title.constructFromObject(data['title']);
      if (data.hasOwnProperty('body'))
        obj.body = Body.constructFromObject(data['body']);
      if (data.hasOwnProperty('assignee'))
        obj.assignee = Assignee.constructFromObject(data['assignee']);
      if (data.hasOwnProperty('milestone'))
        obj.milestone = Milestone.constructFromObject(data['milestone']);
      if (data.hasOwnProperty('state'))
        obj.state = State.constructFromObject(data['state']);
    }
    return obj;
  }
}

/**
 * @member {module:model/Title} title
 */
PatchIssue.prototype.title = undefined;

/**
 * @member {module:model/Body} body
 */
PatchIssue.prototype.body = undefined;

/**
 * @member {module:model/Assignee} assignee
 */
PatchIssue.prototype.assignee = undefined;

/**
 * @member {module:model/Milestone} milestone
 */
PatchIssue.prototype.milestone = undefined;

/**
 * @member {module:model/State} state
 */
PatchIssue.prototype.state = undefined;

