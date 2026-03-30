# Inlämning: Data Platform 26 - ETL-flöde med python

## Projektbeskrivning
Detta projekt är en kompletteringsuppgift som demonstrerar ett grundläggande ETL-flöde
(Extract, Transform, Load). Programmet läser in produktdata från en CSV-fil, genomför statistiska beräkningar och presenterar resultatet stegvis.

## Installation & Uppstart
För att köra detta projekt lokalt:

1. Installera nödvändiga bibliotek:
   ```bash
   pip install fastapi uvicorn pandas

2. Kör applikationen:
   ```bash
   python main.py


## Arbetsprocess

1. Sprint 1: Grundläggande setup av FastAPI och databaskoppling

2. Sprint 2: Implementering av logik för statistik och simulering av flödet.

3. Spring 3: Dokumentation och finslipning av felhantering, exempelvis hantering av kolumnnamn i CSV-filen.

# Reflektion

Genom att dela upp arbetet i mindre testbara delar har jag kunnat identifiera och lösa problem tidigt i arbetsprocessen. Ett exempel på detta var nör kolumnnamnen i CSV-filen inte matchade mina SQL frågor. Pågrund av att jag testade varje delmoment i koden kunde jag snabbt justera den och verifiera att allt fungerade innan jag gick vidare till nästa moment. Detta arbetssätt har gjort projektet mer stabilt samt lätt att jobba med i samband med att jag inte hade flera fel i slutet av koden. 