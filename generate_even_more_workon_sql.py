import random

# --- GENERATE 40 MORE WorkOn ---
# Company IDs: 1 to 15 (We added 10 more recently, total 15)
# Activities: 1 to 70
# Existing WorkOn: ~30 entries (original 10 + 20 generated)
# Need 40 more.

# Let's try to assign work to activities that don't have a WorkOn entry yet if possible, 
# or just random ones (Primary Key is AID, CompanyID - so an activity can have multiple companies working on it).

company_ids = list(range(1, 16)) # 1 to 15
activity_ids = list(range(1, 71)) # 1 to 70

sql_statements = []
sql_statements.append("\n-- Generated 40 more WorkOn")

count = 0
attempts = 0
generated_pairs = set()

# Pre-populate generated_pairs with likely existing ones to avoid primary key collisions if we were parsing the file,
# but since we are just appending, we rely on randomness. 
# To be safer, let's just pick random pairs and rely on the high number of combinations (70 * 15 = 1050) vs ~70 used.

while count < 40 and attempts < 1000:
    aid = random.choice(activity_ids)
    cid = random.choice(company_ids)
    
    # Simple check to avoid duplicates within this batch
    if (aid, cid) not in generated_pairs:
        generated_pairs.add((aid, cid))
        
        payment = random.randint(10000, 80000)
        quarter = f"2025-Q{random.randint(1, 4)}"
        
        stmt = f"INSERT INTO WorkOn (AID, CompanyID, ContractedPayment, ContractedTime) VALUES ({aid}, {cid}, {payment}, '{quarter}');"
        sql_statements.append(stmt)
        count += 1
    attempts += 1

print("\n".join(sql_statements))

