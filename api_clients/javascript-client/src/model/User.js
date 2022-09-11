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

/**
 * The User model module.
 * @module model/User
 * @version 1.0.0
 */
export class User {
  /**
   * Constructs a new <code>User</code>.
   * @alias module:model/User
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>User</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/User} obj Optional instance to populate.
   * @return {module:model/User} The populated <code>User</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new User();
      if (data.hasOwnProperty('id'))
        obj.id = ApiClient.convertToType(data['id'], 'Number');
      if (data.hasOwnProperty('login'))
        obj.login = ApiClient.convertToType(data['login'], 'String');
      if (data.hasOwnProperty('full_name'))
        obj.fullName = ApiClient.convertToType(data['full_name'], 'String');
      if (data.hasOwnProperty('avatar_url'))
        obj.avatarUrl = ApiClient.convertToType(data['avatar_url'], 'String');
      if (data.hasOwnProperty('username'))
        obj.username = ApiClient.convertToType(data['username'], 'String');
    }
    return obj;
  }
}

/**
 * @member {Number} id
 */
User.prototype.id = undefined;

/**
 * @member {String} login
 */
User.prototype.login = undefined;

/**
 * @member {String} fullName
 */
User.prototype.fullName = undefined;

/**
 * @member {String} avatarUrl
 */
User.prototype.avatarUrl = undefined;

/**
 * @member {String} username
 */
User.prototype.username = undefined;

