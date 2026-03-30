from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd
import time
import os

app = FastAPI()


# Inställningar för CORS så att 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# Databashantering

def init_db():
    # Skapar tablleen och importerar data från CSV 
    conn = sqlite3.connect('platform.db')
    cursor = conn.cursor()

    # Skapa tabell för produkterna
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            category TEXT,
            price REAL, 
            stock_quantity INTEGER            
        )
    """)


# Ingest: Läs CSV med Pandas och spara till sqlite
    # Vi kollar om filen finns först så det inte kraschar
    if os.path.exists('products_100.csv'):
        df = pd.read_csv('products_100.csv')
        df.to_sql('products', conn, if_exists='replace', index=False)
        print("Databasen är aktiv och CSV-data har importerats!")
    else:
        print("Hittade inte products_100.csv - kontrollera filnamnet.")

    conn.commit()
    conn.close()

# Kör funktionen så att databasen skapas direkt
init_db()

@app.get("/")
def root():
    return {"message": "Data Platform API - Ingest klart"}