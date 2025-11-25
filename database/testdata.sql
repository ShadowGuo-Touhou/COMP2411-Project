PRAGMA foreign_keys = ON;

BEGIN TRANSACTION;

-- Executive Officer
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (1, 'Alex Chan', 65000, 90000001, NULL);

-- Managers
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (2, 'Betty Wong', 52000, 90000002, 1);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (3, 'Charlie Lee', 51000, 90000003, 1);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (4, 'David Ho', 50000, 90000004, 1);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (5, 'Emily Lam', 48000, 90000005, 2);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (6, 'Frank Yu', 47000, 90000006, 2);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (7, 'Grace Ng', 46000, 90000007, 3);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (8, 'Henry Lau', 45500, 90000008, 4);

-- Workers
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (1, 'Jason Li', 18000, 91000001, 2);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (2, 'Kelly Tam', 19000, 91000002, 3);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (3, 'Michael Chan', 20000, 91000003, 4);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (4, 'Nancy Fong', 21000, 91000004, 5);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (5, 'Oscar Yip', 22000, 91000005, 6);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (6, 'Peter Wong', 18000, 91000006, 7);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (7, 'Queenie Choi', 19000, 91000007, 8);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (8, 'Raymond Luk', 20000, 91000008, 2);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (9, 'Sandy Cheung', 21000, 91000009, 3);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (10, 'Tony Leung', 22000, 91000010, 4);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (11, 'Ursula Hui', 18000, 91000011, 5);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (12, 'Victor Lau', 19000, 91000012, 6);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (13, 'Wendy Poon', 20000, 91000013, 7);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (14, 'Xavier Aankhein Khuli', 21000, 91000014, 8);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (15, 'Yvonne Luk', 22000, 91000015, 2);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (16, 'Zoe Lee', 18000, 91000016, 3);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (17, 'Brian Ng', 19000, 91000017, 4);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (18, 'Carmen Ho', 20000, 91000018, 5);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (19, 'Derek Chan', 21000, 91000019, 6);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (20, 'Iris Lam', 22000, 91000020, 7);

-- Locations
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('PQ200', 'Corridor', 5);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('PQ604', 'Laboratory', 5);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('PQ209', 'Washroom', 5);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('QT302', 'Washroom', 5);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('Z211', 'Classroom', 6);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('Z209', 'Classroom', 6);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('QT412', 'Laboratory', 7);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('PQ806', 'Lobby', 2);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('P202', 'Gate', 2);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('QT200', 'Square', 3);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('N102', 'Classroom', 3);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('X001', 'Swimming Pool', 4);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('Block L', 'Library', 8);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('Main Garden', 'Garden', 8);
INSERT INTO Location (Name, Facility, Supervisor) VALUES ('Staff Carpark', 'Carpark', 4);

-- Activities
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (1, 'Daily corridor cleaning', '2025-01-01', '2025-01-01');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (2, 'Night-time washroom deep clean', '2025-01-03', '2025-01-05');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (3, 'Classroom floor waxing', '2025-01-05', '2025-02-05');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (4, 'Lab fume hood inspection', '2025-01-07', '2025-01-07');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (5, 'Lobby glass cleaning', '2025-01-09', '2025-01-11');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (6, 'Entrance pressure washing', '2025-01-11', '2025-01-11');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (7, 'Square drainage clearing after rainstorm', '2025-01-13', '2025-01-15');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (8, 'Garden tree pruning', '2025-01-15', '2025-01-30');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (9, 'Pool deck anti-slip treatment', '2025-01-17', '2025-01-17');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (10, 'Library carpet vacuum', '2025-01-19', '2025-01-21');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (11, 'Library air filter replacement', '2025-01-21', '2025-01-21');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (12, 'Carpark oil stain removal', '2025-01-23', '2025-01-25');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (13, 'Window seal repair PQ604', '2025-01-25', '2025-02-01');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (14, 'Roof leak inspection Z209', '2025-01-27', '2025-01-27');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (15, 'Typhoon debris clean-up', '2025-01-29', '2025-01-31');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (16, 'Mold treatment in washroom', '2025-01-31', '2025-02-04');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (17, 'Pest control in classroom', '2025-02-02', '2025-02-02');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (18, 'Emergency water leak cleanup', '2025-02-04', '2025-02-06');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (19, 'Fire drill equipment check', '2025-02-06', '2025-02-06');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (20, 'Annual façade inspection', '2025-02-08', '2025-02-10');

-- Companies
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (1, 'CleanPro Services Ltd.', '12/F, Tech Plaza, Kowloon', 93000001);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (2, 'Sparkle Facility Mgmt', '8/F, Harbour Centre, Hong Kong', 93000002);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (3, 'GreenLeaf Gardening Co.', 'Shop 3, Garden Street, Kowloon', 93000003);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (4, 'SafeLab Engineering', 'Unit 502, Science Park, New Territories', 93000004);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (5, 'Skyline Façade Repair', 'Unit 2101, Industrial Centre', 93000005);

-- Tasks
INSERT INTO Task (AID, Name, Equipment) VALUES (1, 'Sweep & mop', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (1, 'Disinfect handrails', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (2, 'Toilet descaling', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (2, 'Floor scrubbing', 'Scrubber');
INSERT INTO Task (AID, Name, Equipment) VALUES (2, 'Mirror polishing', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (3, 'Strip old wax', 'Floor Maintaince Machines');
INSERT INTO Task (AID, Name, Equipment) VALUES (3, 'Apply new wax', 'Floor Buffers');
INSERT INTO Task (AID, Name, Equipment) VALUES (4, 'Check airflow', 'Inspection tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (4, 'Replace filters', 'Inspection tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (5, 'Clean glass panels', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (5, 'Polish metal frames', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (6, 'High-pressure wash', 'Pressure washer');
INSERT INTO Task (AID, Name, Equipment) VALUES (6, 'Apply anti-slip coating', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (7, 'Clear leaves from drains', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (7, 'Flush drainage channels', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (8, 'Trim branches', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (8, 'Collect and dispose trimmings', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (9, 'Clean tiles', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (9, 'Apply anti-slip chemical', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (10, 'Vacuum carpets', 'Vacuum cleaner');
INSERT INTO Task (AID, Name, Equipment) VALUES (10, 'Spot stain removal', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (11, 'Remove old filters', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (11, 'Install new filters', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (12, 'Degrease floor', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (12, 'Remove oil stains', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (13, 'Inspect window seals', 'Inspection tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (13, 'Apply new sealant', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (14, 'Inspect roof', 'Inspection tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (14, 'Seal minor cracks', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (15, 'Collect debris', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (15, 'Wash affected areas', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (16, 'Spray anti-mold chemical', 'Sprayer');
INSERT INTO Task (AID, Name, Equipment) VALUES (16, 'Scrub walls', 'Scrubber');
INSERT INTO Task (AID, Name, Equipment) VALUES (17, 'Set up bait stations', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (17, 'Spray insecticide', 'Sprayer');
INSERT INTO Task (AID, Name, Equipment) VALUES (18, 'Wet vacuum standing water', 'Vacuum cleaner');
INSERT INTO Task (AID, Name, Equipment) VALUES (18, 'Set up drying fans', 'Standard tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (19, 'Check extinguishers', 'Inspection tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (19, 'Inspect hose reels', 'Inspection tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (20, 'Inspect façade', 'Inspection tools');
INSERT INTO Task (AID, Name, Equipment) VALUES (20, 'Repair cracked tiles', 'Standard tools');

-- TaskChemicals
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (1, 'Disinfect handrails', 'Bleach solution');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (1, 'Disinfect handrails', 'Alcohol-based disinfectant');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (2, 'Toilet descaling', 'Acidic descaler');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (2, 'Floor scrubbing', 'Neutral floor cleaner');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (3, 'Strip old wax', 'Wax stripper');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (3, 'Apply new wax', 'Floor wax');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (6, 'Apply anti-slip coating', 'Anti-slip coating');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (9, 'Apply anti-slip chemical', 'Anti-slip chemical');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (12, 'Degrease floor', 'Degreaser');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (12, 'Remove oil stains', 'Solvent cleaner');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (16, 'Spray anti-mold chemical', 'Anti-mold spray');
INSERT INTO TaskChemicals (AID, TaskName, Chemicals) VALUES (17, 'Spray insecticide', 'Low-toxicity insecticide');

-- HoldIn
INSERT INTO HoldIn (AID, LocationName) VALUES (1, 'PQ200');
INSERT INTO HoldIn (AID, LocationName) VALUES (2, 'PQ209');
INSERT INTO HoldIn (AID, LocationName) VALUES (2, 'QT302');
INSERT INTO HoldIn (AID, LocationName) VALUES (3, 'Z211');
INSERT INTO HoldIn (AID, LocationName) VALUES (4, 'QT412');
INSERT INTO HoldIn (AID, LocationName) VALUES (4, 'PQ604');
INSERT INTO HoldIn (AID, LocationName) VALUES (5, 'PQ806');
INSERT INTO HoldIn (AID, LocationName) VALUES (6, 'P202');
INSERT INTO HoldIn (AID, LocationName) VALUES (7, 'QT200');
INSERT INTO HoldIn (AID, LocationName) VALUES (8, 'Main Garden');
INSERT INTO HoldIn (AID, LocationName) VALUES (9, 'X001');
INSERT INTO HoldIn (AID, LocationName) VALUES (10, 'Block L');
INSERT INTO HoldIn (AID, LocationName) VALUES (11, 'Block L');
INSERT INTO HoldIn (AID, LocationName) VALUES (12, 'Staff Carpark');
INSERT INTO HoldIn (AID, LocationName) VALUES (13, 'PQ604');
INSERT INTO HoldIn (AID, LocationName) VALUES (14, 'Z209');
INSERT INTO HoldIn (AID, LocationName) VALUES (15, 'Main Garden');
INSERT INTO HoldIn (AID, LocationName) VALUES (16, 'QT302');
INSERT INTO HoldIn (AID, LocationName) VALUES (17, 'N102');
INSERT INTO HoldIn (AID, LocationName) VALUES (18, 'Staff Carpark');
INSERT INTO HoldIn (AID, LocationName) VALUES (19, 'Z209');
INSERT INTO HoldIn (AID, LocationName) VALUES (20, 'Block L');

-- WorkOn
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (2, 3, 23000, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (4, 5, 26000, '2025-Q1');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (6, 2, 29000, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (8, 4, 32000, '2025-Q1');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (10, 1, 35000, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (12, 3, 38000, '2025-Q1');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (14, 5, 41000, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (16, 2, 44000, '2025-Q1');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (18, 4, 47000, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (20, 1, 50000, '2025-Q1');

-- Assigned（很多，我给你一批，已经避免主键冲突）
INSERT INTO Assigned (WID, AID, TaskName) VALUES (1, 1, 'Sweep & mop');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (2, 1, 'Sweep & mop');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (3, 1, 'Disinfect handrails');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (4, 1, 'Disinfect handrails');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (5, 2, 'Toilet descaling');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (6, 2, 'Toilet descaling');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (7, 2, 'Floor scrubbing');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (8, 2, 'Floor scrubbing');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (9, 2, 'Mirror polishing');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (10, 2, 'Mirror polishing');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (11, 3, 'Strip old wax');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (12, 3, 'Strip old wax');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (13, 3, 'Apply new wax');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (14, 3, 'Apply new wax');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (15, 4, 'Check airflow');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (16, 4, 'Check airflow');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (17, 4, 'Replace filters');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (18, 4, 'Replace filters');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (19, 5, 'Clean glass panels');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (20, 5, 'Clean glass panels');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (1, 5, 'Polish metal frames');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (2, 5, 'Polish metal frames');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (3, 6, 'High-pressure wash');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (4, 6, 'High-pressure wash');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (5, 6, 'Apply anti-slip coating');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (6, 6, 'Apply anti-slip coating');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (7, 7, 'Clear leaves from drains');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (8, 7, 'Clear leaves from drains');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (9, 7, 'Flush drainage channels');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (10, 7, 'Flush drainage channels');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (11, 8, 'Trim branches');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (12, 8, 'Trim branches');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (13, 8, 'Collect and dispose trimmings');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (14, 8, 'Collect and dispose trimmings');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (15, 9, 'Clean tiles');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (16, 9, 'Clean tiles');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (17, 9, 'Apply anti-slip chemical');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (18, 9, 'Apply anti-slip chemical');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (19, 10, 'Vacuum carpets');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (20, 10, 'Vacuum carpets');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (1, 10, 'Spot stain removal');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (2, 10, 'Spot stain removal');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (3, 11, 'Remove old filters');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (4, 11, 'Remove old filters');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (5, 11, 'Install new filters');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (6, 11, 'Install new filters');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (7, 12, 'Degrease floor');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (8, 12, 'Degrease floor');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (9, 12, 'Remove oil stains');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (10, 12, 'Remove oil stains');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (11, 13, 'Inspect window seals');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (12, 13, 'Inspect window seals');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (13, 13, 'Apply new sealant');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (14, 13, 'Apply new sealant');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (15, 14, 'Inspect roof');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (16, 14, 'Inspect roof');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (17, 14, 'Seal minor cracks');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (18, 14, 'Seal minor cracks');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (19, 15, 'Collect debris');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (20, 15, 'Collect debris');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (1, 15, 'Wash affected areas');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (2, 15, 'Wash affected areas');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (3, 16, 'Spray anti-mold chemical');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (4, 16, 'Spray anti-mold chemical');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (5, 16, 'Scrub walls');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (6, 16, 'Scrub walls');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (7, 17, 'Set up bait stations');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (8, 17, 'Set up bait stations');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (9, 17, 'Spray insecticide');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (10, 17, 'Spray insecticide');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (11, 18, 'Wet vacuum standing water');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (12, 18, 'Wet vacuum standing water');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (13, 18, 'Set up drying fans');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (14, 18, 'Set up drying fans');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (15, 19, 'Check extinguishers');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (16, 19, 'Check extinguishers');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (17, 19, 'Inspect hose reels');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (18, 19, 'Inspect hose reels');

INSERT INTO Assigned (WID, AID, TaskName) VALUES (19, 20, 'Inspect façade');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (20, 20, 'Inspect façade');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (1, 20, 'Repair cracked tiles');
INSERT INTO Assigned (WID, AID, TaskName) VALUES (2, 20, 'Repair cracked tiles');

COMMIT;
