import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres", password = "HanZawNyine015062@#&", host = "db.aaiiskwuasvabzyrxvxy.supabase.co", port = "5432")
print ("Opened database successfully")