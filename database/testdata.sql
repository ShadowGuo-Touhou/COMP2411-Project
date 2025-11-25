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

-- Generated 30 more Managers
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (9, 'Anthony Carroll', 73111, 35745913, 7);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (10, 'David Woods', 46114, 21854488, 1);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (11, 'Mary Stanley', 65630, 4592308, 10);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (12, 'Cameron Garcia', 71445, 37886966, 5);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (13, 'Christy Garcia', 55902, 49962254, 5);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (14, 'Natalie Russo', 59387, 72169023, 9);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (15, 'Patricia Bishop', 64844, 86748966, 14);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (16, 'Jodi Taylor', 69917, 38345580, 14);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (17, 'Linda Simmons', 72910, 64055311, 2);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (18, 'Brianna Waters', 48807, 15967223, 8);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (19, 'Judith Warner', 57597, 77300212, 3);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (20, 'Catherine Ellis', 67445, 75382076, 18);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (21, 'Dorothy Johnson', 62348, 17609195, 10);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (22, 'Anthony Rivera', 78673, 74905921, 4);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (23, 'Lisa Bond', 60710, 99542754, 8);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (24, 'Jeffrey Wagner', 71909, 53039299, 19);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (25, 'Angela Flores', 65509, 38334471, 17);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (26, 'Matthew Cherry', 59212, 90130571, 12);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (27, 'Kelly Hernandez', 67059, 76700082, 4);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (28, 'Jessica Lee', 56452, 15243976, 6);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (29, 'Christopher Hardy', 67332, 50719765, 2);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (30, 'Carrie Hicks', 77802, 21563075, 29);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (31, 'Robin Cowan', 51049, 54517704, 19);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (32, 'Samuel Walsh', 62513, 89061953, 7);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (33, 'Cindy Brown', 51386, 60922765, 20);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (34, 'Mrs. Regina Farrell MD', 48210, 98283282, 32);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (35, 'Karla Garrett', 76728, 27939382, 19);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (36, 'Amber Weeks', 47702, 82711072, 15);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (37, 'Daniel Hester', 46145, 92809020, 35);
INSERT INTO Manager (MID, Name, Salary, Contact, Supervisor) VALUES (38, 'Crystal Morgan', 79317, 12697394, 12);


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

-- Generated 20 more Workers
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (21, 'Eric Williams', 22073, 13909295, 36);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (22, 'Barbara Perkins', 26436, 8164528, 23);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (23, 'Stacy Williams', 22606, 23849894, 37);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (24, 'Nicolas Weber', 20095, 98041633, 2);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (25, 'Debbie Brown', 24271, 14571512, 32);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (26, 'Rebecca Burns', 22381, 60261806, 24);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (27, 'Ashley Barron', 25012, 52654771, 31);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (28, 'Shelby Russo', 26432, 61257015, 36);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (29, 'Mary Mitchell', 19674, 9202573, 37);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (30, 'Linda Hayes', 19601, 7802215, 19);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (31, 'Lisa Hernandez', 18211, 60892683, 19);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (32, 'Barbara Barr', 15973, 90531985, 4);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (33, 'Destiny Torres', 17454, 79144274, 4);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (34, 'Zoe Johnston', 21233, 48657644, 23);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (35, 'Katie Kennedy', 24538, 46277891, 16);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (36, 'Anna Duke', 25748, 3940237, 13);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (37, 'Jeffrey Smith', 15360, 46282450, 4);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (38, 'Janice Lin', 15074, 69931966, 22);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (39, 'Alicia Martinez', 21767, 37690156, 11);
INSERT INTO Worker (WID, Name, Salary, Contact, Supervisor) VALUES (40, 'Nathan Ward', 20129, 8149676, 28);


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
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (21, 'Elevator safety inspection', '2025-02-12', '2025-02-12');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (22, 'HVAC system overhaul', '2025-02-15', '2025-02-20');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (23, 'Emergency lighting battery test', '2025-02-22', '2025-02-22');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (24, 'Water tank cleaning', '2025-02-25', '2025-02-27');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (25, 'Lawn mowing and edging', '2025-03-01', '2025-03-02');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (26, 'CCTV camera lens cleaning', '2025-03-05', '2025-03-06');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (27, 'Lecture hall upholstery cleaning', '2025-03-08', '2025-03-10');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (28, 'Fire alarm system testing', '2025-03-12', '2025-03-12');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (29, 'Graffiti removal on exterior walls', '2025-03-15', '2025-03-16');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (30, 'Air conditioner coil cleaning', '2025-03-20', '2025-03-25');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (31, 'Stairwell repainting', '2025-03-28', '2025-04-02');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (32, 'Basement sump pump check', '2025-04-05', '2025-04-05');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (33, 'Solar panel dust removal', '2025-04-08', '2025-04-09');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (34, 'Termite inspection', '2025-04-12', '2025-04-12');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (35, 'Swimming pool filter sand change', '2025-04-15', '2025-04-16');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (36, 'Gym equipment sanitization', '2025-04-20', '2025-04-20');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (37, 'Parking lot restriping', '2025-04-25', '2025-04-28');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (38, 'Generator load bank testing', '2025-05-02', '2025-05-02');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (39, 'Window blind ultrasonic cleaning', '2025-05-05', '2025-05-08');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (40, 'Kitchen grease trap pumping', '2025-05-12', '2025-05-12');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (41, 'Automatic door sensor calibration', '2025-05-15', '2025-05-15');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (42, 'Roof gutter clearing', '2025-05-20', '2025-05-21');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (43, 'Drinking fountain filter replacement', '2025-05-25', '2025-05-25');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (44, 'Conference room carpet shampooing', '2025-06-01', '2025-06-02');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (45, 'Exterior signage repair', '2025-06-05', '2025-06-07');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (46, 'Server room dust control', '2025-06-10', '2025-06-10');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (47, 'Playground safety surface repair', '2025-06-15', '2025-06-18');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (48, 'Irrigation system maintenance', '2025-06-22', '2025-06-23');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (49, 'Waste recycling center organization', '2025-06-28', '2025-06-29');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (50, 'Locker room deep clean', '2025-07-05', '2025-07-07');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (51, 'Ceiling tile replacement', '2025-07-12', '2025-07-14');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (52, 'Electrical distribution panel thermography', '2025-07-18', '2025-07-18');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (53, 'Fountain pump repair', '2025-07-22', '2025-07-23');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (54, 'Cafeteria exhaust hood cleaning', '2025-07-28', '2025-07-28');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (55, 'Walkway pressure washing', '2025-08-02', '2025-08-04');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (56, 'Tree health assessment', '2025-08-10', '2025-08-12');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (57, 'Plumbing backflow preventer test', '2025-08-15', '2025-08-15');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (58, 'Archive room humidity check', '2025-08-20', '2025-08-20');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (59, 'Security gate mechanism lubrication', '2025-08-25', '2025-08-25');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (60, 'Marble floor crystallization', '2025-09-01', '2025-09-05');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (61, 'Fall season gutter guard installation', '2025-09-10', '2025-09-12');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (62, 'Laboratory spill kit replenishment', '2025-09-15', '2025-09-15');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (63, 'Auditorium lighting rig inspection', '2025-09-20', '2025-09-21');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (64, 'Vending machine area sanitation', '2025-09-25', '2025-09-25');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (65, 'Bicycle rack rust treatment', '2025-10-02', '2025-10-03');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (66, 'Heating boiler startup check', '2025-10-10', '2025-10-11');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (67, 'Leaf clearance from pathways', '2025-10-15', '2025-10-20');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (68, 'Access control system audit', '2025-10-25', '2025-10-26');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (69, 'Emergency exit sign repair', '2025-11-05', '2025-11-05');
INSERT INTO Activity (AID, Name, startDate, endDate) VALUES (70, 'Year-end inventory check', '2025-12-28', '2025-12-30');
-- Companies
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (1, 'CleanPro Services Ltd.', '12/F, Tech Plaza, Kowloon', 93000001);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (2, 'Sparkle Facility Mgmt', '8/F, Harbour Centre, Hong Kong', 93000002);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (3, 'GreenLeaf Gardening Co.', 'Shop 3, Garden Street, Kowloon', 93000003);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (4, 'SafeLab Engineering', 'Unit 502, Science Park, New Territories', 93000004);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (5, 'Skyline Façade Repair', 'Unit 2101, Industrial Centre', 93000005);

-- Generated 10 more Companies
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (6, 'EnergyStill Solutions', 'Unit 1064 Box 5637, DPO AA 81956', 30736082);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (7, 'HimSection Services Ltd.', '768 Hansen Vista, Lake Benjamin, OH 84316', 75733022);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (8, 'ChallengeOpportunity Services Ltd.', '4763 Lisa Walk, Santosborough, TX 58347', 59116845);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (9, 'MeetingRed Engineering', '872 Charles Village Suite 128, Ryanville, AK 83095', 74681009);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (10, 'ManagePiece Gardening Co.', 'PSC 2030, Box 7108, APO AP 88318', 90989124);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (11, 'WeDrug Engineering', '7039 Baker Parkway Suite 359, Lake Patrickland, FM 29400', 76430430);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (12, 'DirectionKeep Works', 'PSC 1242, Box 0216, APO AA 86405', 30021895);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (13, 'PeaceRequire Facility Mgmt', 'Unit 0554 Box 2695, DPO AP 81895', 89249701);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (14, 'LiveOwner Holdings', '078 Isaac Hollow Apt. 766, North Kayla, PR 83130', 80156530);
INSERT INTO Company (CompanyID, Name, Address, Contact) VALUES (15, 'EveryoneSpecial Services Ltd.', '315 Gerald Forest Suite 676, West Jennifer, AL 17769', 26492054);


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

-- Generated 10 more HoldIn
INSERT INTO HoldIn (AID, LocationName) VALUES (30, 'PQ806');
INSERT INTO HoldIn (AID, LocationName) VALUES (27, 'Z211');
INSERT INTO HoldIn (AID, LocationName) VALUES (21, 'N102');
INSERT INTO HoldIn (AID, LocationName) VALUES (31, 'PQ209');
INSERT INTO HoldIn (AID, LocationName) VALUES (37, 'PQ806');
INSERT INTO HoldIn (AID, LocationName) VALUES (64, 'Staff Carpark');
INSERT INTO HoldIn (AID, LocationName) VALUES (52, 'Main Garden');
INSERT INTO HoldIn (AID, LocationName) VALUES (29, 'PQ209');
INSERT INTO HoldIn (AID, LocationName) VALUES (59, 'PQ604');
INSERT INTO HoldIn (AID, LocationName) VALUES (53, 'Z211');
INSERT INTO HoldIn (AID, LocationName) VALUES (21, 'PQ806');
INSERT INTO HoldIn (AID, LocationName) VALUES (22, 'Block L');
INSERT INTO HoldIn (AID, LocationName) VALUES (23, 'PQ200');
INSERT INTO HoldIn (AID, LocationName) VALUES (24, 'Block L');
INSERT INTO HoldIn (AID, LocationName) VALUES (25, 'Main Garden');
INSERT INTO HoldIn (AID, LocationName) VALUES (26, 'P202');
INSERT INTO HoldIn (AID, LocationName) VALUES (27, 'N102');
INSERT INTO HoldIn (AID, LocationName) VALUES (28, 'PQ200');
INSERT INTO HoldIn (AID, LocationName) VALUES (29, 'QT200');
INSERT INTO HoldIn (AID, LocationName) VALUES (30, 'Z209');
INSERT INTO HoldIn (AID, LocationName) VALUES (31, 'PQ200');
INSERT INTO HoldIn (AID, LocationName) VALUES (32, 'Staff Carpark');
INSERT INTO HoldIn (AID, LocationName) VALUES (33, 'Block L');
INSERT INTO HoldIn (AID, LocationName) VALUES (34, 'Main Garden');
INSERT INTO HoldIn (AID, LocationName) VALUES (35, 'X001');
INSERT INTO HoldIn (AID, LocationName) VALUES (36, 'Z211');
INSERT INTO HoldIn (AID, LocationName) VALUES (37, 'Staff Carpark');
INSERT INTO HoldIn (AID, LocationName) VALUES (38, 'Staff Carpark');
INSERT INTO HoldIn (AID, LocationName) VALUES (39, 'Z211');
INSERT INTO HoldIn (AID, LocationName) VALUES (40, 'PQ200');
INSERT INTO HoldIn (AID, LocationName) VALUES (41, 'PQ806');
INSERT INTO HoldIn (AID, LocationName) VALUES (42, 'Block L');
INSERT INTO HoldIn (AID, LocationName) VALUES (43, 'PQ200');
INSERT INTO HoldIn (AID, LocationName) VALUES (44, 'N102');
INSERT INTO HoldIn (AID, LocationName) VALUES (45, 'P202');
INSERT INTO HoldIn (AID, LocationName) VALUES (46, 'PQ604');
INSERT INTO HoldIn (AID, LocationName) VALUES (47, 'QT200');
INSERT INTO HoldIn (AID, LocationName) VALUES (48, 'Main Garden');
INSERT INTO HoldIn (AID, LocationName) VALUES (49, 'Staff Carpark');
INSERT INTO HoldIn (AID, LocationName) VALUES (50, 'QT302');
INSERT INTO HoldIn (AID, LocationName) VALUES (51, 'Z209');
INSERT INTO HoldIn (AID, LocationName) VALUES (52, 'PQ604');
INSERT INTO HoldIn (AID, LocationName) VALUES (53, 'QT200');
INSERT INTO HoldIn (AID, LocationName) VALUES (54, 'PQ200');
INSERT INTO HoldIn (AID, LocationName) VALUES (55, 'QT200');
INSERT INTO HoldIn (AID, LocationName) VALUES (56, 'Main Garden');
INSERT INTO HoldIn (AID, LocationName) VALUES (57, 'PQ209');
INSERT INTO HoldIn (AID, LocationName) VALUES (58, 'Block L');
INSERT INTO HoldIn (AID, LocationName) VALUES (59, 'P202');
INSERT INTO HoldIn (AID, LocationName) VALUES (60, 'PQ806');
INSERT INTO HoldIn (AID, LocationName) VALUES (61, 'Block L');
INSERT INTO HoldIn (AID, LocationName) VALUES (62, 'QT412');
INSERT INTO HoldIn (AID, LocationName) VALUES (63, 'N102');
INSERT INTO HoldIn (AID, LocationName) VALUES (64, 'PQ200');
INSERT INTO HoldIn (AID, LocationName) VALUES (65, 'P202');
INSERT INTO HoldIn (AID, LocationName) VALUES (66, 'Staff Carpark');
INSERT INTO HoldIn (AID, LocationName) VALUES (67, 'Main Garden');
INSERT INTO HoldIn (AID, LocationName) VALUES (68, 'P202');
INSERT INTO HoldIn (AID, LocationName) VALUES (69, 'PQ200');
INSERT INTO HoldIn (AID, LocationName) VALUES (70, 'Block L');


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

-- Generated 20 more WorkOn
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (48, 4, 43233, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (27, 4, 59057, '2025-Q1');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (36, 4, 37395, '2025-Q2');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (52, 1, 15409, '2025-Q2');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (25, 4, 23772, '2025-Q1');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (26, 1, 29487, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (34, 1, 20277, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (35, 5, 56330, '2025-Q2');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (31, 2, 17648, '2025-Q2');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (42, 2, 15176, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (57, 4, 48770, '2025-Q4');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (40, 4, 12633, '2025-Q4');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (37, 3, 36951, '2025-Q3');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (47, 1, 23701, '2025-Q4');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (21, 5, 28075, '2025-Q4');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (49, 4, 15101, '2025-Q2');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (64, 3, 50816, '2025-Q4');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (46, 4, 20519, '2025-Q2');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (58, 1, 45471, '2025-Q1');
INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES (32, 4, 42930, '2025-Q4');


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
