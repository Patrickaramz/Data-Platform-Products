# Inlämning: Data Platform 26 - ETL-flöde med python & docker

## Projektbeskrivning
Detta projekt är en kompletteringsuppgift som demonstrerar ett grundläggande ETL-flöde
(Extract, Transform, Load) samt gör ett simulerat händelseflöde. Programmet läser in produktdata från en CSV-fil, genomför statistiska beräkningar med hjälp av pandas och presenterar resultatet via ett FastApi

## Installation & Uppstart

### Alternativ 1 Docker

1. Bygg imagen:
   ```bash
   docker build -t min-dataplatform . 
   ```


2. Starta containern
   ```bash
   docker run -p 8000:8000 min-dataplattform 
   ```

3. Besök API: http://localhost:8000/api/stats

### Alternativt 2 Lokalt

1. Installera nödvändiga bibliotek:
 pip install fastapi uvicorn pandas

2. Kör applikationen:
python main.py

## API Endpoints

1. GET /api/stats: Visar transformerad statistik (medelpris per kategori)

2. GET /api/stream: Simulerar ett händelseflöde som loggar händelser i realtid


## Arbetsprocess

1. Sprint 1: Setup av FastApi och grundläggande struktur

2. Sprint 2: Implementering av Pandas logik för statistik och simulering av händelseflöde

3. Sprint 3: Docker konfiguration och felsökning samt tester.


## Reflektion

Genom att dela upp arbetet i delar har jag kunnat isolera problem tidigt. Ett exempel från detta var kolumnnamnen i csv-filen måste matcha koden i main.py för att pandas beräkningarna skulle fungera korrekt. Genom att använda docker i slutskedet har jag säkertsälllt att applikationen är obereoende av den lokala miljön vilket gör lösningen redo för en riktig data plattform.