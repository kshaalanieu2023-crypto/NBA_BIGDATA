#Do the following in MySQL Workbench before running code:
#CREATE DATABASE IF NOT EXISTS nba_data;

# ---------- REQUIRED LIBRARIES ----------
import pandas as pd
from sqlalchemy import create_engine

# ---------- 1. DATABASE CONNECTION ----------
USER = "root"          # your MySQL username
PASS = "Here you just put the password for MySQL Workbenhch" # your MySQL password
HOST = "localhost"     # your MySQL host (localhost for local setup)
DB   = "nba_data"      # database name you created in Workbench

# create connection engine
engine = create_engine(f"mysql+pymysql://{USER}:{PASS}@{HOST}:3306/{DB}", future=True)

# ---------- 2. FILE PATHS ----------
base_path = "/Users/rayanmerhi/Downloads/bigdatanba"

players_path = f"{base_path}/players_2005_2025.csv"
teams_path   = f"{base_path}/teams_2005_2025.json"

# ---------- 3. LOAD & INSERT PLAYERS ----------
print("Loading players data...")
players_df = pd.read_csv(players_path)

# insert DataFrame into MySQL (auto-creates table)
players_df.to_sql("players", engine, if_exists="replace", index=False)
print(f" Inserted {len(players_df)} player records into 'players' table.")

# ---------- 4. LOAD & INSERT TEAMS ----------
print("Loading teams data...")
teams_df = pd.read_json(teams_path)

teams_df.to_sql("teams", engine, if_exists="replace", index=False)
print(f" Inserted {len(teams_df)} team records into 'teams' table.")

# ---------- 5. CONFIRMATION ----------
print("\n All data successfully integrated into MySQL database 'nba_data'!")
print("Tables created: players, teams")



#Do this in MySQL Workbench to check data integration is correct
#USE nba_data;
#SELECT * FROM players LIMIT 5;
#SELECT * FROM teams LIMIT 5;
