CREATE DATABASE  IF NOT EXISTS `livetracking` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `livetracking`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: livetracking
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `location` (
  `locationID` int NOT NULL AUTO_INCREMENT,
  `CurrentLocation` varchar(255) NOT NULL,
  `LastUpdated` datetime DEFAULT NULL,
  `BatteryStatus` int DEFAULT NULL,
  `empID` int DEFAULT NULL,
  PRIMARY KEY (`locationID`),
  KEY `empID` (`empID`),
  CONSTRAINT `location_ibfk_1` FOREIGN KEY (`empID`) REFERENCES `user` (`empID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `locationdetails`
--

DROP TABLE IF EXISTS `locationdetails`;
/*!50001 DROP VIEW IF EXISTS `locationdetails`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8 */;
/*!50001 CREATE VIEW `locationdetails` AS SELECT 
 1 AS `empId`,
 1 AS `name`,
 1 AS `email`,
 1 AS `phoneno`,
 1 AS `dob`,
 1 AS `sex`,
 1 AS `CurrentLocation`,
 1 AS `LastUpdated`,
 1 AS `BatteryStatus`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `empID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phoneno` varchar(15) NOT NULL,
  `password` varchar(45) NOT NULL,
  `dob` date NOT NULL,
  `sex` varchar(1) NOT NULL,
  PRIMARY KEY (`empID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'livetracking'
--

--
-- Dumping routines for database 'livetracking'
--

--
-- Final view structure for view `locationdetails`
--

/*!50001 DROP VIEW IF EXISTS `locationdetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `locationdetails` AS select `u`.`empID` AS `empId`,`u`.`name` AS `name`,`u`.`email` AS `email`,`u`.`phoneno` AS `phoneno`,`u`.`dob` AS `dob`,`u`.`sex` AS `sex`,`l`.`CurrentLocation` AS `CurrentLocation`,`l`.`LastUpdated` AS `LastUpdated`,`l`.`BatteryStatus` AS `BatteryStatus` from (`user` `u` join `location` `l` on((`u`.`empID` = `l`.`empID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-14  0:39:28
