/*
Navicat MySQL Data Transfer

Source Server         : 139mariadb_main
Source Server Version : 50505
Source Host           : 192.168.1.139:3306
Source Database       : ams

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2017-07-06 16:10:46
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for apis
-- ----------------------------
DROP TABLE IF EXISTS `apis`;
CREATE TABLE `apis` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `schemes` varchar(10) DEFAULT NULL COMMENT '请求协议\r\n- http\r\n- https\r\n- ws\r\n- wss',
  `host` varchar(255) DEFAULT NULL COMMENT '提供接口的主机\r\n格式\r\n    api.example.com\r\n    example.com:8089\r\n    93.184.216.34\r\n    93.184.216.34:8089',
  `base_path` varchar(255) DEFAULT '' COMMENT '接口根路径',
  `title` varchar(255) DEFAULT NULL COMMENT '接口名称',
  `description` varchar(255) DEFAULT NULL COMMENT '接口描述',
  `version` varchar(255) DEFAULT NULL COMMENT '接口版本',
  `produces` varchar(255) DEFAULT NULL COMMENT '默认响应 content-type',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for operation_parameter
-- ----------------------------
DROP TABLE IF EXISTS `operation_parameter`;
CREATE TABLE `operation_parameter` (
  `operation_id` bigint(20) NOT NULL,
  `parameter_id` bigint(20) NOT NULL,
  PRIMARY KEY (`parameter_id`,`operation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for operation_tag
-- ----------------------------
DROP TABLE IF EXISTS `operation_tag`;
CREATE TABLE `operation_tag` (
  `operation_id` bigint(20) NOT NULL,
  `tag_id` bigint(255) NOT NULL,
  PRIMARY KEY (`operation_id`,`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for parameters
-- ----------------------------
DROP TABLE IF EXISTS `parameters`;
CREATE TABLE `parameters` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `source` varchar(255) DEFAULT NULL COMMENT '参数来源',
  `name` varchar(255) DEFAULT NULL COMMENT '参数名称',
  `type` varchar(255) DEFAULT NULL COMMENT '参数类型',
  `required` tinyint(4) DEFAULT '1',
  `format` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `default` varchar(255) DEFAULT NULL,
  `minimum` double DEFAULT NULL,
  `maximum` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='参数';

-- ----------------------------
-- Table structure for path_operation
-- ----------------------------
DROP TABLE IF EXISTS `path_operation`;
CREATE TABLE `path_operation` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `operation` varchar(255) DEFAULT NULL COMMENT '请求方式get, post, put, patch, delete, head, options,defaut',
  `path_id` bigint(20) NOT NULL,
  `summary` varchar(255) DEFAULT NULL COMMENT '简述',
  `description` varchar(5000) DEFAULT NULL COMMENT '描述',
  `secure` tinyint(4) NOT NULL DEFAULT '0' COMMENT '需要的权限',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for paths
-- ----------------------------
DROP TABLE IF EXISTS `paths`;
CREATE TABLE `paths` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `path_url` varchar(500) DEFAULT NULL COMMENT '接口路径',
  `doc_id` bigint(20) NOT NULL COMMENT '所属文档ID',
  `secure` tinyint(4) NOT NULL DEFAULT '0' COMMENT '是否需要权限检测',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for response_model
-- ----------------------------
DROP TABLE IF EXISTS `response_model`;
CREATE TABLE `response_model` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL COMMENT '模型名称，类名',
  `type` varchar(255) DEFAULT NULL,
  `doc_id` bigint(20) DEFAULT NULL,
  `child_model_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for response_model_prop
-- ----------------------------
DROP TABLE IF EXISTS `response_model_prop`;
CREATE TABLE `response_model_prop` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `format` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `model_id` bigint(20) NOT NULL,
  `prop_model_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for responses
-- ----------------------------
DROP TABLE IF EXISTS `responses`;
CREATE TABLE `responses` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(255) DEFAULT NULL,
  `description` varchar(600) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `response_model_id` bigint(20) DEFAULT NULL,
  `operation_id` bigint(20) DEFAULT NULL,
  `wrapper_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for tags
-- ----------------------------
DROP TABLE IF EXISTS `tags`;
CREATE TABLE `tags` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `tag` varchar(255) DEFAULT NULL COMMENT '标签名',
  `description` varchar(1000) DEFAULT NULL COMMENT '标签描述',
  `doc_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
