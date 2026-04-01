from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd
import time
import os   
import json


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
    conn = sqlite3.connect('platform.db')
    if os.path.exists('products_100.csv'):
        df = pd.read_csv('products_100.csv')

        df.columns = ['products_name', 'category', 'price', 'stock_quantity', 'extra']
        df = df.drop(columns=['extra'])

        df.to_sql('products', conn, if_exists='replace', index=False)
        print("Ingest: Data har lästs in och städats via Pandas.")
        conn.close()

# 2. TRANSFORM - Nu med pandas istället för sql enligt kraven
@app.get("/api/stats")
def get_stats():
    conn = sqlite3.connect('platform.db')
    df = pd.read_sql("SELECT * FROM products", conn)
    conn.close()

    if df.empty:
        return {"Error": "Inget data tillgänglig"}
    
    # Transformering med pandas groupby
    stats = df.groupby('category')['price'].mean().round(2).reset_index()
    stats.columns = ['category', 'avg-price']

    return {
        "beskrivning": "Statistik transformerad med Pandas",
        "data": stats.to_dict(orient='records')
    }

# 3. LOAD / STREAM (Simulerat händelseflöde för kafka)
@app.get("/api/stream")
def stream_products():
    conn = sqlite3.connect('platform.db')
    df = pd.read_sql("SELECT product_name, price FROM products ORDER BY price DESC LIMIT 5", conn)
    conn.close()

    products = df.to_dict(orient='records')

    print("\n--- STARTAR HÖBDEKSEFKLDE (KAFKA.FORMAT) ---")
    for p in products:
        event = json.dumps(p)
        print(f"PRODUCER -> Skickar händelse: {event}")
        time.sleep(0.8)

    return{"status": "Success", "message": "Data printad stegvis"}


if __name__ == "__main__":
    import uvicorn 
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)     # För docker container


