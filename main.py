from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd
import time
import os

app = FastAPI()


# Inställningar för CORS, detta tillåter frontend att anropa vårat API från alla källor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# 1. INGEST / EXTRACT 
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

        df.columns = ['product_name', 'category', 'price', 'stock_quantity', 'extra']

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


# TRANSFORM

@app.get("/api/stats")
def get_stats():
    conn = sqlite3.connect('platform.db')
    cursor = conn.cursor()
    
    # SQL-fråga som räknar ut medelvärdet (AVG) grupperat på kategori
    cursor.execute("SELECT category, AVG(price) FROM products GROUP BY category")
    stats_data = cursor.fetchall()
    conn.close()

    resultat = []
    for s in stats_data:
        resultat.append({
            "kategori": s[0],
            "medelpris": round(s[1], 2)
        })
    
    return {"beskrivning": "Medelpris per produktkategori", "data": resultat}


# 3. LOAD
@app.get("/api/stream")
def stream_products():
    conn = sqlite3.connect('platform.db')
    cursor = conn.cursor()
    
    # Vi hämtar de 5 dyraste produkterna för att visa ett urval
    cursor.execute("SELECT product_name, price FROM products ORDER BY price DESC LIMIT 5")
    products = cursor.fetchall()
    conn.close()

    print("\n--- STARTAR DATASTRÖM (SIMULERING) ---")
    for p in products:
        # Här sker det "stegvisa" flödet
        print(f"Skickar produkt: {p[0]} | Pris: {p[1]} kr")
        time.sleep(0.8) # Pausar kort för att simulera realtidsflöde
    
    return {"status": "Success", "message": "5 produkter har streamats till terminalen"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)