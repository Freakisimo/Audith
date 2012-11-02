/* AR */
ALTER TABLE `audith`.`ar` DROP FOREIGN KEY `AR`;

ALTER TABLE `audith`.`ar` 
  ADD CONSTRAINT `AR`
  FOREIGN KEY (`ID_GENERAL`)
  REFERENCES `audith`.`generales` (`ID_PRINCIPAL`)
  ON DELETE CASCADE
  ON UPDATE CASCADE
, ADD INDEX `AR` (`ID_GENERAL` ASC);

/* Hemato */
ALTER TABLE `audith`.`hemato` DROP FOREIGN KEY `hemato` ;

ALTER TABLE `audith`.`hemato` 
  ADD CONSTRAINT `hemato`
  FOREIGN KEY (`ID_GENERAL`)
  REFERENCES `audith`.`generales` (`ID_PRINCIPAL`)
  ON DELETE CASCADE
  ON UPDATE CASCADE
, ADD INDEX `hemato` (`ID_GENERAL` ASC) ;

/* Hepatitis */
ALTER TABLE `audith`.`dhepatitis` DROP FOREIGN KEY `hepa` ;

ALTER TABLE `audith`.`dhepatitis` 
  ADD CONSTRAINT `hepa`
  FOREIGN KEY (`id_general` )
  REFERENCES `audith`.`dhepatitis` (`id_general` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, ADD INDEX `hepa` (`id_general` ASC) ;

/* Oncologia */
ALTER TABLE `audith`.`oncologia` DROP FOREIGN KEY `onco` ;

ALTER TABLE `audith`.`oncologia` 
  ADD CONSTRAINT `onco`
  FOREIGN KEY (`ID_GENERAL` )
  REFERENCES `audith`.`generales` (`ID_PRINCIPAL` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, ADD INDEX `onco` (`ID_GENERAL` ASC) ;

/* Prod_ar */
ALTER TABLE `audith`.`prod_ar` DROP FOREIGN KEY `ar_prod` ;

ALTER TABLE `audith`.`prod_ar` 
  ADD CONSTRAINT `ar_prod`
  FOREIGN KEY (`ID_PACIENTE_AR` )
  REFERENCES `audith`.`ar` (`ID` )
  ON DELETE CASCADE
  ON UPDATE CASCADE;

/* Prod_hemato */
ALTER TABLE `audith`.`prod_hemato` DROP FOREIGN KEY `hemato_prod` ;

ALTER TABLE `audith`.`prod_hemato` 
  ADD CONSTRAINT `hemato_prod`
  FOREIGN KEY (`ID_PACIENTE_HEMATO` )
  REFERENCES `audith`.`hemato` (`ID` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, ADD INDEX `hemato_prod` (`ID_PACIENTE_HEMATO` ASC) ;

/* Prod_hepa */
ALTER TABLE `audith`.`prod_hepa` DROP FOREIGN KEY `hepa_prod` ;

ALTER TABLE `audith`.`prod_hepa` 
  ADD CONSTRAINT `hepa_prod`
  FOREIGN KEY (`id_pac` )
  REFERENCES `audith`.`dhepatitis` (`id_pac` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, ADD INDEX `hepa_prod` (`id_pac` ASC) ;

/* Prod_onco */
ALTER TABLE `audith`.`prod_onco` DROP FOREIGN KEY `onco_prod` ;

ALTER TABLE `audith`.`prod_onco` 
  ADD CONSTRAINT `onco_prod`
  FOREIGN KEY (`ID_PACIENTE` )
  REFERENCES `audith`.`oncologia` (`ID` )
  ON DELETE CASCADE
  ON UPDATE CASCADE
, ADD INDEX `onco_prod` (`ID_PACIENTE` ASC) ;