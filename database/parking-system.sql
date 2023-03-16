SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cars
-- ----------------------------
DROP TABLE IF EXISTS `cars`;
CREATE TABLE `cars`  (
  `ID` int(0) NOT NULL AUTO_INCREMENT,
  `CarID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '车辆id，可认为车牌号',
  `StartTime` datetime(0) NULL DEFAULT NULL COMMENT '入场时间',
  `EndTime` datetime(0) NULL DEFAULT NULL COMMENT '出场时间',
  `TotalTime` int(0) NULL DEFAULT NULL COMMENT '停车总时间，按小时算',
  `AnyCard` int(0) NULL DEFAULT NULL COMMENT '车辆办卡情况，0为未办卡，1为月卡，2为年卡',
  `Fee` float(255, 0) NULL DEFAULT NULL COMMENT '该次停车需要缴纳的费用',
  `ParkingID` int(0) NULL DEFAULT NULL COMMENT '车位id',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 107 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cars
-- ----------------------------
INSERT INTO `cars` VALUES (78, '晋L T4788', '2023-03-13 18:40:31', '2023-03-13 21:52:38', 3, 2, 240, 65);
INSERT INTO `cars` VALUES (79, '沪N 80D65', '2023-03-13 15:45:11', NULL, NULL, 1, NULL, 158);
INSERT INTO `cars` VALUES (81, '云T F9920', '2023-03-13 14:54:24', NULL, NULL, 1, NULL, 113);
INSERT INTO `cars` VALUES (83, '甘N 642R3', '2023-03-13 21:58:10', NULL, NULL, 1, NULL, 165);
INSERT INTO `cars` VALUES (85, '闽T 2R664', '2023-03-13 10:45:41', NULL, NULL, 1, NULL, 199);
INSERT INTO `cars` VALUES (86, '吉C 7L837', '2023-03-13 15:51:17', NULL, NULL, 2, NULL, 105);
INSERT INTO `cars` VALUES (87, '冀J 345P8', '2023-03-13 07:31:59', NULL, NULL, 0, NULL, 49);
INSERT INTO `cars` VALUES (88, '鲁Y 508R4', '2023-03-13 09:27:32', '2023-03-13 09:57:32', 0, 1, 0, 20);
INSERT INTO `cars` VALUES (89, '云U G4820', '2023-03-13 16:33:30', '2023-03-13 21:42:28', 5, 1, 450, 49);
INSERT INTO `cars` VALUES (90, '皖U 959B3', '2023-03-13 22:11:10', '2023-03-13 22:47:29', 0, 2, 0, 51);
INSERT INTO `cars` VALUES (91, '湘N 3Y378', '2023-03-13 16:31:08', '2023-03-13 20:17:59', 3, 1, 270, 97);
INSERT INTO `cars` VALUES (92, '冀V M5547', '2023-03-13 20:16:47', '2023-03-13 21:43:47', 1, 1, 90, 197);
INSERT INTO `cars` VALUES (93, '苏R 6X373', '2023-03-13 14:13:22', NULL, NULL, 0, NULL, 143);
INSERT INTO `cars` VALUES (95, '新R 7J279', '2023-03-13 18:33:42', NULL, NULL, 1, NULL, 178);
INSERT INTO `cars` VALUES (99, '新F 28Y76', '2023-03-13 15:43:37', NULL, NULL, 2, NULL, 193);
INSERT INTO `cars` VALUES (100, '辽S 98Z25', '2023-03-13 10:23:58', NULL, NULL, 1, NULL, 146);
INSERT INTO `cars` VALUES (101, '粤R 4P638', '2023-03-13 12:02:03', '2023-03-13 19:57:50', 7, 1, 630, 3);
INSERT INTO `cars` VALUES (102, '鲁C H3775', '2023-03-13 13:41:03', '2023-03-13 14:02:19', 0, 0, 0, 5);
INSERT INTO `cars` VALUES (103, '赣Q W4466', '2023-03-13 07:06:11', '2023-03-13 13:33:34', 6, 1, 540, 66);
INSERT INTO `cars` VALUES (104, '鄂E 864H3', '2023-03-13 10:46:25', '2023-03-13 22:03:22', 11, 2, 880, 71);
INSERT INTO `cars` VALUES (105, '鲁X 849J5', '2023-03-13 20:12:42', '2023-03-13 21:09:51', 0, 1, 0, 103);
INSERT INTO `cars` VALUES (106, '闽S 872J0', '2023-03-13 07:31:01', NULL, NULL, 0, NULL, 161);

-- ----------------------------
-- Table structure for login
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login`  (
  `UserName` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户名',
  `Email` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '邮箱',
  `Password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '密码',
  `Salt` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '盐值',
  PRIMARY KEY (`UserName`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for parking
-- ----------------------------
DROP TABLE IF EXISTS `parking`;
CREATE TABLE `parking`  (
  `ParkingID` int(0) NOT NULL COMMENT '车位id(0~100)',
  `CarID` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '车辆ID',
  `StartTime` datetime(0) NULL DEFAULT NULL COMMENT '入场时间',
  `AnyCard` int(0) NULL DEFAULT NULL COMMENT '车辆办卡情况，0为未办卡，1为月卡，2为年卡',
  PRIMARY KEY (`ParkingID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of parking
-- ----------------------------
INSERT INTO `parking` VALUES (105, '吉C 7L837', '2023-03-13 15:51:17', 2);
INSERT INTO `parking` VALUES (113, '云T F9920', '2023-03-13 14:54:24', 1);
INSERT INTO `parking` VALUES (143, '苏R 6X373', '2023-03-13 14:13:22', 0);
INSERT INTO `parking` VALUES (146, '辽S 98Z25', '2023-03-13 10:23:58', 1);
INSERT INTO `parking` VALUES (158, '沪N 80D65', '2023-03-13 15:45:11', 1);
INSERT INTO `parking` VALUES (161, '闽S 872J0', '2023-03-13 07:31:01', 0);
INSERT INTO `parking` VALUES (165, '甘N 642R3', '2023-03-13 21:58:10', 1);
INSERT INTO `parking` VALUES (178, '新R 7J279', '2023-03-13 18:33:42', 1);
INSERT INTO `parking` VALUES (193, '新F 28Y76', '2023-03-13 15:43:37', 2);
INSERT INTO `parking` VALUES (199, '闽T 2R664', '2023-03-13 10:45:41', 1);

SET FOREIGN_KEY_CHECKS = 1;
