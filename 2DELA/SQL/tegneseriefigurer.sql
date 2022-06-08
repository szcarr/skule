-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema tegneseriefigurer
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tegneseriefigurer
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tegneseriefigurer` DEFAULT CHARACTER SET utf8 ;
USE `tegneseriefigurer` ;

-- -----------------------------------------------------
-- Table `tegneseriefigurer`.`blad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tegneseriefigurer`.`blad` (
  `blad_id` INT NOT NULL AUTO_INCREMENT,
  `bladnavn` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`blad_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tegneseriefigurer`.`figur`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tegneseriefigurer`.`figur` (
  `figur_id` INT NOT NULL AUTO_INCREMENT,
  `figurnavn` VARCHAR(45) NOT NULL,
  `aarstall` INT NOT NULL,
  `blad_id` INT NOT NULL,
  PRIMARY KEY (`figur_id`),
  INDEX `fk_figur_blad_idx` (`blad_id` ASC),
  CONSTRAINT `fk_figur_blad`
    FOREIGN KEY (`blad_id`)
    REFERENCES `tegneseriefigurer`.`blad` (`blad_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
