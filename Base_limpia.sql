/*
Navicat MySQL Data Transfer

Source Server         : Localhost
Source Server Version : 50525
Source Host           : localhost:3306
Source Database       : audith2

Target Server Type    : MYSQL
Target Server Version : 50525
File Encoding         : 65001

Date: 2012-11-01 15:31:50
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `ar`
-- ----------------------------
DROP TABLE IF EXISTS `ar`;
CREATE TABLE `ar` (
`ID`  int(11) NOT NULL AUTO_INCREMENT ,
`ID_GENERAL`  int(11) NOT NULL ,
`N`  int(11) NULL DEFAULT NULL ,
`CUP`  varchar(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PACIENTE`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`TIPO_PACIENTE`  varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`LINEA_BIOLOGICOS`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`ENTIDAD`  varchar(200) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
PRIMARY KEY (`ID`, `ID_GENERAL`),
FOREIGN KEY (`ID_GENERAL`) REFERENCES `generales` (`ID_PRINCIPAL`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `AR_2` (`ID_GENERAL`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='AR; InnoDB free: 109568 kB; (`ID_GENERAL`) REFER `audith/generales`(`ID_PRINCIPA'
AUTO_INCREMENT=29901

;

-- ----------------------------
-- Records of ar
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for `dhepatitis`
-- ----------------------------
DROP TABLE IF EXISTS `dhepatitis`;
CREATE TABLE `dhepatitis` (
`id_pac`  int(11) NOT NULL AUTO_INCREMENT ,
`id_general`  int(11) NOT NULL ,
`num_pac`  int(11) NOT NULL ,
`px_nom`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`tip_pac`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`nom_ltra`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`nom_hep`  varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`nom_gen`  varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
PRIMARY KEY (`id_pac`),
FOREIGN KEY (`id_general`) REFERENCES `dhepatitis` (`id_general`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `id_general` (`id_general`) USING BTREE ,
INDEX `hepa` (`id_general`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='InnoDB free: 109568 kB; (`id_general`) REFER `audith/dhepatitis`(`id_general`) O'
AUTO_INCREMENT=1

;

-- ----------------------------
-- Records of dhepatitis
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for `generales`
-- ----------------------------
DROP TABLE IF EXISTS `generales`;
CREATE TABLE `generales` (
`ID_PRINCIPAL`  int(11) NOT NULL AUTO_INCREMENT ,
`ID_UNICO`  varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`FOLIO`  int(11) NULL DEFAULT NULL ,
`TEMA`  varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`TEMA_COD`  int(11) NULL DEFAULT NULL ,
`FECHA`  date NOT NULL ,
`MEDICO_COD`  varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`MEDICO_DES`  varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`ESPE_DES`  varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`INSTITUCION`  varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`SECTOR`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`HOSPITAL`  varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`CLUE`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`ESTADO`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`ZONA`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`NUM_PACIENTES`  int(11) NULL DEFAULT NULL ,
`USUARIO`  varchar(15) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`TIPO_MEDICO`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`MEDICO_ADSCRITO`  varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`NUM_PACIENTES_BIOLOGICOS`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
PRIMARY KEY (`ID_PRINCIPAL`, `FECHA`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='Tabla con variables generales en OncoAudith'
AUTO_INCREMENT=9096

;

-- ----------------------------
-- Records of generales
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for `hemato`
-- ----------------------------
DROP TABLE IF EXISTS `hemato`;
CREATE TABLE `hemato` (
`ID`  int(11) NOT NULL AUTO_INCREMENT ,
`ID_GENERAL`  int(11) NOT NULL ,
`N`  int(11) NULL DEFAULT NULL ,
`CUP`  varchar(3) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PACIENTE`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`TIPO_PACIENTE`  varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`TIPO_DE_CANCER`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT '' ,
`TIPO_HISTOLOGICO`  varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT '' ,
`SUBTIPO_HISTOLOGICO`  varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT '' ,
`VARIEDAD_HISTO`  varchar(259) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' ,
`COD_ENF`  varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '\'\'' ,
PRIMARY KEY (`ID`, `ID_GENERAL`),
FOREIGN KEY (`ID_GENERAL`) REFERENCES `generales` (`ID_PRINCIPAL`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `Hemato_2` (`ID_GENERAL`) USING BTREE ,
INDEX `hemato` (`ID_GENERAL`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='Pacientes hematologia\r\n; InnoDB free: 12288 kB; (`ID_GENERAL'
AUTO_INCREMENT=44811

;

-- ----------------------------
-- Records of hemato
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for `oncologia`
-- ----------------------------
DROP TABLE IF EXISTS `oncologia`;
CREATE TABLE `oncologia` (
`ID`  int(11) NOT NULL AUTO_INCREMENT ,
`ID_GENERAL`  int(11) NOT NULL ,
`FECHA_GENERAL`  date NOT NULL DEFAULT '0000-00-00' ,
`N`  int(11) NULL DEFAULT NULL ,
`CUP`  varchar(25) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PACIENTE`  varchar(25) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`TIPO_PACIENTE`  varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,
`DX_1`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`DX_1_COD`  varchar(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`DX_2`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`DX_2_COD`  varchar(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`TRATAMIENTO`  varchar(25) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`ESTADIO`  varchar(25) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`SUB_ETAPA`  varchar(25) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
PRIMARY KEY (`ID`, `ID_GENERAL`),
FOREIGN KEY (`ID_GENERAL`) REFERENCES `generales` (`ID_PRINCIPAL`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `ID_GENERAL` (`ID_GENERAL`) USING BTREE ,
INDEX `oncologia_ibfk_1` (`ID_GENERAL`, `FECHA_GENERAL`) USING BTREE ,
INDEX `onco` (`ID_GENERAL`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='InnoDB free: 5120 kB; (`ID_GENERAL`) REFER `audith/generales'
AUTO_INCREMENT=240047

;

-- ----------------------------
-- Records of oncologia
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for `prod_ar`
-- ----------------------------
DROP TABLE IF EXISTS `prod_ar`;
CREATE TABLE `prod_ar` (
`ID`  int(11) NOT NULL AUTO_INCREMENT ,
`ID_PACIENTE_AR`  int(11) NOT NULL ,
`PROD_COD`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PROD_DES`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PRINCIPIO_COD`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PRINCIPIO_DES`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`MANU_DES`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
PRIMARY KEY (`ID`),
FOREIGN KEY (`ID_PACIENTE_AR`) REFERENCES `ar` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `Audith_ar_3` (`ID_PACIENTE_AR`) USING BTREE ,
INDEX `ar_prod` (`ID_PACIENTE_AR`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='Productos AR; InnoDB free: 109568 kB; (`ID_PACIENTE_AR`) REFER `audith/ar`(`ID`)'
AUTO_INCREMENT=55040

;

-- ----------------------------
-- Records of prod_ar
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for `prod_hemato`
-- ----------------------------
DROP TABLE IF EXISTS `prod_hemato`;
CREATE TABLE `prod_hemato` (
`ID`  int(11) NOT NULL AUTO_INCREMENT ,
`ID_PACIENTE_HEMATO`  int(11) NOT NULL ,
`PROD_COD`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PROD_DES`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PRINCIPIO_COD`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PRINCIPIO_DES`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`MANU_DES`  varchar(45) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
PRIMARY KEY (`ID`),
FOREIGN KEY (`ID_PACIENTE_HEMATO`) REFERENCES `hemato` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `Audith_hemato_3` (`ID_PACIENTE_HEMATO`) USING BTREE ,
INDEX `hemato_prod` (`ID_PACIENTE_HEMATO`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='Productos hemato\n; InnoDB free: 11264 kB; (`ID_PACIENTE_HEMA'
AUTO_INCREMENT=104067

;

-- ----------------------------
-- Records of prod_hemato
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for `prod_hepa`
-- ----------------------------
DROP TABLE IF EXISTS `prod_hepa`;
CREATE TABLE `prod_hepa` (
`id_pro`  int(11) NOT NULL AUTO_INCREMENT ,
`id_pac`  int(11) NOT NULL ,
`prod_cod`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`prod_des`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`principio_cod`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`principio_des`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`manu_des`  varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
PRIMARY KEY (`id_pro`),
FOREIGN KEY (`id_pac`) REFERENCES `dhepatitis` (`id_pac`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `id_pac` (`id_pac`) USING BTREE ,
INDEX `hepa_prod` (`id_pac`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='InnoDB free: 109568 kB; (`id_pac`) REFER `audith/dhepatitis`(`id_pac`) ON UPDATE'
AUTO_INCREMENT=1

;

-- ----------------------------
-- Records of prod_hepa
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for `prod_onco`
-- ----------------------------
DROP TABLE IF EXISTS `prod_onco`;
CREATE TABLE `prod_onco` (
`ID`  int(11) NOT NULL AUTO_INCREMENT ,
`ID_PACIENTE`  int(11) NOT NULL ,
`PROD_COD`  varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PROD_DES`  varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PRINCIPIO_COD`  varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`PRINCIPIO_DES`  varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`MANU_DES`  varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
PRIMARY KEY (`ID`),
FOREIGN KEY (`ID_PACIENTE`) REFERENCES `oncologia` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
INDEX `Productos` (`ID_PACIENTE`) USING BTREE ,
INDEX `onco_prod` (`ID_PACIENTE`) USING BTREE 
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='InnoDB free: 5120 kB; (`ID_PACIENTE`) REFER `audith/oncologi'
AUTO_INCREMENT=424171

;

-- ----------------------------
-- Records of prod_onco
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Auto increment value for `ar`
-- ----------------------------
ALTER TABLE `ar` AUTO_INCREMENT=29901;

-- ----------------------------
-- Auto increment value for `dhepatitis`
-- ----------------------------
ALTER TABLE `dhepatitis` AUTO_INCREMENT=1;

-- ----------------------------
-- Auto increment value for `generales`
-- ----------------------------
ALTER TABLE `generales` AUTO_INCREMENT=9096;

-- ----------------------------
-- Auto increment value for `hemato`
-- ----------------------------
ALTER TABLE `hemato` AUTO_INCREMENT=44811;

-- ----------------------------
-- Auto increment value for `oncologia`
-- ----------------------------
ALTER TABLE `oncologia` AUTO_INCREMENT=240047;

-- ----------------------------
-- Auto increment value for `prod_ar`
-- ----------------------------
ALTER TABLE `prod_ar` AUTO_INCREMENT=55040;

-- ----------------------------
-- Auto increment value for `prod_hemato`
-- ----------------------------
ALTER TABLE `prod_hemato` AUTO_INCREMENT=104067;

-- ----------------------------
-- Auto increment value for `prod_hepa`
-- ----------------------------
ALTER TABLE `prod_hepa` AUTO_INCREMENT=1;

-- ----------------------------
-- Auto increment value for `prod_onco`
-- ----------------------------
ALTER TABLE `prod_onco` AUTO_INCREMENT=424171;
