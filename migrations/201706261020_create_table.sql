CREATE TABLE IF NOT EXISTS `roche_felt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Roche_Key` varchar(125) DEFAULT NULL,
  `PO_Number` varchar(255) DEFAULT NULL,
  `Order_Type` varchar(255) DEFAULT NULL COMMENT 'packaging or repackaging',
  `Material_Number` varchar(255) DEFAULT NULL,
  `Product_Name` text,
  `PO_creation_date` date DEFAULT NULL,
  `Batch_Number` varchar(255) DEFAULT NULL,
  `PO_Release_Date` datetime DEFAULT NULL,
  `Packaging_Line_Start` date DEFAULT NULL,
  `Packaging_Line_Finish` date DEFAULT NULL,
  `Packaging_Final_Check_Date` date DEFAULT NULL,
  `BRR_Start_Date` date DEFAULT NULL,
  `BRR_End_Date` date DEFAULT NULL,
  `QA_Release_Date` date DEFAULT NULL,
  `Product` varchar(255) DEFAULT NULL,
  `Batch_Status` int(11) DEFAULT NULL,
  `PO_Create_to_PO_Release` int(11) DEFAULT NULL,
  `PO_Release_to_PKG_Start` int(11) DEFAULT NULL,
  `PKG_Start_to_PKG_Finish` int(11) DEFAULT NULL,
  `PKG_Finish_to_PKG_Final_Check` int(11) NOT NULL,
  `Final_Check_to_BRR_Begin` int(11) DEFAULT NULL,
  `BRR_Begin_to_BRR_Finish` int(11) DEFAULT NULL,
  `BRR_Finish_to_QP_Release` int(11) DEFAULT NULL,
  `FG_E2E` int(11) DEFAULT NULL,
  `Check_Column` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1;