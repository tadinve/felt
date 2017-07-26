SELECT 
	Product,
	Check_Column,
	`PO_Create_to_PO_Release`,
	`PO_Release_to_PKG_Start`,
	`PKG_Start_to_PKG_Finish`,
	`PKG_Finish_to_PKG_Final_Check`,
	`Final_Check_to_BRR_Begin`,
	`BRR_Begin_to_BRR_Finish`,
	`BRR_Finish_to_QP_Release`
FROM 
	roche_felt_tb
WHERE
	Check_Column != 'TRUE' 
	OR `PO_Create_to_PO_Release` < 0
	OR `PO_Release_to_PKG_Start` < 0
	OR `PKG_Start_to_PKG_Finish` < 0
	OR `PKG_Finish_to_PKG_Final_Check` < 0
	OR `Final_Check_to_BRR_Begin` < 0
	OR `BRR_Begin_to_BRR_Finish` < 0
	OR `BRR_Finish_to_QP_Release` < 0;

-----------------------------------------------
DELETE 
FROM 
	roche_felt_tb
WHERE
	Check_Column != 'TRUE' 
	OR `PO_Create_to_PO_Release` < 0
	OR `PO_Release_to_PKG_Start` < 0
	OR `PKG_Start_to_PKG_Finish` < 0
	OR `PKG_Finish_to_PKG_Final_Check` < 0
	OR `Final_Check_to_BRR_Begin` < 0
	OR `BRR_Begin_to_BRR_Finish` < 0
	OR `BRR_Finish_to_QP_Release` < 0;