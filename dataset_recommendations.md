# Interessante Datensätze für Data Analytics Projekte

Dieser Leitfaden enthält kuratierte Datensätze für verschiedene Data Analytics Themen, die für Seminararbeiten und akademische Projekte geeignet sind. Die Auswahl fokussiert sich auf weniger häufig verwendete, aber umfangreiche und interessante Datasets.

## 📊 Inhaltsverzeichnis

1. [Clustering-Analyse](#clustering-analyse)
2. [Warenkorbanalyse (Market Basket Analysis)](#warenkorbanalyse)
3. [Finanzdaten für KYC-Analyse](#finanzdaten-für-kyc-analyse)
4. [Klassifikationsaufgaben](#klassifikationsaufgaben)
5. [Allgemeine Hinweise](#allgemeine-hinweise)

---

## 🔍 Clustering-Analyse

### 1. Online Retail Dataset (erweiterte Version)
**Quelle:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/502/online+retail+ii  
**Größe:** ~1 Million Transaktionen  
**Beschreibung:** Transaktionsdaten eines Online-Händlers aus UK (2009-2011). Ideal für Customer Segmentation und RFM-Analyse.

**Warum interessant:**
- Echte E-Commerce Daten mit internationalen Transaktionen
- Erlaubt komplexe Segmentierungsstrategien
- Enthält Rückgaben und negative Mengen (realistische Daten)
- Gut geeignet für RFM (Recency, Frequency, Monetary) Clustering

**Analyseansätze:**
- Customer Lifetime Value Segmentierung
- Geografische Kundencluster
- Produktaffinitäts-Clustering
- Zeitbasierte Verhaltenscluster

---

### 2. Seoul Bike Sharing Demand Dataset
**Quelle:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand  
**Größe:** 8.760 Stunden Daten  
**Beschreibung:** Stündliche Fahrradvermietungsdaten aus Seoul mit Wetter- und Kalenderdaten.

**Warum interessant:**
- Zeitreihen-Clustering möglich
- Multivariate Daten (Wetter, Zeit, Feiertage)
- Nicht-westlicher Kontext (Seoul, Südkorea)
- Clustering von Nutzungsmustern über verschiedene Bedingungen

**Analyseansätze:**
- Clustering von Wettermustern und deren Einfluss
- Zeitbasierte Nutzungsmuster (Wochentage vs. Wochenende)
- Saisonale Cluster-Bildung
- Anomalie-Detektion in Nutzungsmustern

---

### 3. Wholesale Customers Dataset
**Quelle:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/292/wholesale+customers  
**Größe:** 440 Kunden, 8 Features  
**Beschreibung:** Jahresausgaben von Großhandelskunden für verschiedene Produktkategorien.

**Warum interessant:**
- B2B-Kontext (weniger häufig als B2C)
- Verschiedene Produktkategorien (Frisch, Milch, Lebensmittel, Frozen, etc.)
- Gut dokumentiert und überschaubar für tiefe Analysen
- Erlaubt Vergleich verschiedener Clustering-Algorithmen

**Analyseansätze:**
- K-Means, Hierarchical, DBSCAN Vergleich
- Dimensionsreduktion mit PCA/t-SNE
- Geschäftstyp-Segmentierung (Hotel, Retail, Café)
- Ausgabenmuster-Analyse

---

### 4. Credit Card Dataset for Clustering
**Quelle:** Kaggle  
**URL:** https://www.kaggle.com/datasets/arjunbhasin2013/ccdata  
**Größe:** 8.950 Kreditkarteninhaber, 18 Features  
**Beschreibung:** Nutzungsverhalten von Kreditkarteninhabern über 6 Monate.

**Warum interessant:**
- Finanzverhalten-Segmentierung
- Mehrere Dimensionen: Käufe, Cash Advances, Zahlungsverhalten
- Reale Bankdaten (anonymisiert)
- Gut für Kundenprofilierung

**Analyseansätze:**
- Risikosegmentierung von Kunden
- Produktempfehlungs-Cluster
- Zahlungsverhalten-Muster
- Cross-Selling Potenzial-Analyse

---

## 🛒 Warenkorbanalyse

### 1. Instacart Market Basket Analysis
**Quelle:** Kaggle  
**URL:** https://www.kaggle.com/c/instacart-market-basket-analysis  
**Größe:** 3+ Millionen Bestellungen, 200.000+ Produkte  
**Beschreibung:** Anonymisierte Online-Lebensmittel-Bestelldaten von Instacart.

**Warum interessant:**
- Sehr umfangreich für robuste Assoziationsregeln
- Echte Sequenzen von Bestellungen pro Kunde
- Zeitliche Dimension (Bestellhistorie)
- Produkthierarchie verfügbar

**Analyseansätze:**
- Apriori/FP-Growth Algorithmen
- Zeitbasierte Assoziationen (was wird nach was gekauft)
- Produktempfehlungssysteme
- Saisonalität in Produktkombinationen

---

### 2. Belgian Retail Dataset
**Quelle:** Kaggle/BRDS  
**URL:** https://www.kaggle.com/datasets/mittalvishesh/the-belgian-retail-dataset  
**Größe:** 88.162 Transaktionen, 16.470 Produkte  
**Beschreibung:** Transaktionsdaten eines belgischen Einzelhändlers über 3 Jahre.

**Warum interessant:**
- Europäischer Markt (nicht US-zentrisch)
- Mehrjährige Daten für Trend-Analyse
- Produktkategorien und Preise enthalten
- Weniger bekannt als andere Retail-Datasets

**Analyseansätze:**
- Cross-Category Assoziationen
- Preissensitivitäts-Analyse in Warenkörben
- Saisonale Produktbündel
- Kundensegment-spezifische Regeln

---

### 3. Bakery Sales Dataset
**Quelle:** Kaggle  
**URL:** https://www.kaggle.com/datasets/mittalvishesh/transaction-data-for-a-bakery  
**Größe:** 20.507 Transaktionen  
**Beschreibung:** Verkaufstransaktionen einer französischen Bäckerei.

**Warum interessant:**
- Nischen-Einzelhandel (Bäckerei)
- Zeitstempel für Tageszeit-Analysen
- Kleinere Warenkörbe, aber häufige Käufe
- Food-Service Kontext

**Analyseansätze:**
- Tageszeit-basierte Assoziationen (Frühstück vs. Nachmittag)
- Getränke-Gebäck Kombinationen
- Wochentag-spezifische Muster
- Bundle-Pricing Optimierung

---

### 4. Ta Feng Grocery Dataset
**Quelle:** UCI/Kaggle  
**URL:** https://www.kaggle.com/datasets/chiranjivdas09/ta-feng-grocery-dataset  
**Größe:** 800.000+ Transaktionen  
**Beschreibung:** Transaktionsdaten einer taiwanesischen Supermarktkette.

**Warum interessant:**
- Asiatischer Markt (andere Produktkategorien)
- Enthält Kundendemografiedaten
- Produkthierarchie mit Sub-Kategorien
- Wenig verwendet in akademischen Arbeiten

**Analyseansätze:**
- Demografie-spezifische Warenkörbe
- Cross-Cultural Market Basket Patterns
- Produkthierarchie-basierte Regeln
- Kundenlebenszyklus-Analyse

---

## 💰 Finanzdaten für KYC-Analyse

### 1. Synthetic Financial Datasets for Fraud Detection (PaySim)
**Quelle:** Kaggle  
**URL:** https://www.kaggle.com/datasets/ealaxi/paysim1  
**Größe:** 6+ Millionen Transaktionen  
**Beschreibung:** Synthetische Mobile-Money-Transaktionen basiert auf echten afrikanischen Daten.

**Warum interessant:**
- KYC-relevante Transaktionsmuster
- Fraud-Labels für überwachtes Lernen
- Mobile Money Kontext (moderne Finanzen)
- Verschiedene Transaktionstypen (CASH_OUT, TRANSFER, etc.)

**Analyseansätze:**
- Verdächtige Transaktionsmuster-Erkennung
- Kundenrisiko-Profiling
- Network Analysis (Geldflüsse)
- Anomalie-Detektion für KYC

---

### 2. AML (Anti-Money Laundering) Synthetic Dataset
**Quelle:** IBM/Kaggle  
**URL:** https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml  
**Größe:** 180.000+ synthetische Transaktionen  
**Beschreibung:** Synthetische Banktransaktionen mit AML-Labels.

**Warum interessant:**
- Spezifisch für AML/KYC Compliance
- Verschiedene verdächtige Muster eingebaut
- Kundenprofile und Transaktionsnetzwerke
- Realistic für Bankkontext

**Analyseansätze:**
- KYC Risk Scoring
- Transaktions-Pattern Recognition
- Graph-basierte Geldwäsche-Erkennung
- Regelbasierte vs. ML-basierte KYC

---

### 3. Credit Card Fraud Detection Dataset
**Quelle:** Kaggle/ULB  
**URL:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud  
**Größe:** 284.807 Transaktionen  
**Beschreibung:** Europäische Kreditkartentransaktionen mit Fraud-Labels (PCA-transformiert).

**Warum interessant:**
- Echte Bankdaten (anonymisiert)
- Stark unbalanciert (wie reale KYC-Daten)
- PCA-Features (Privacy-preserving)
- Benchmark-Dataset für Fraud Detection

**Analyseansätze:**
- Imbalanced Classification Techniken
- KYC-Alerting Systems
- Threshold Optimization
- Ensemble Methods für Detection

---

### 4. Bank Marketing Dataset
**Quelle:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/222/bank+marketing  
**Größe:** 45.211 Kundenkontakte  
**Beschreibung:** Direktmarketing-Kampagnen einer portugiesischen Bank mit Kundenattributen.

**Warum interessant:**
- Umfangreiche Kundendemografie (KYC-relevant)
- Sozioökonomische Indikatoren
- Kontakthistorie und Kampagnenerfolg
- Gut für Customer Due Diligence Analysen

**Analyseansätze:**
- Customer Risk Profiling
- Segment-basierte KYC-Anforderungen
- Propensity Modeling
- Feature Importance für KYC-Entscheidungen

---

### 5. Lending Club Loan Data
**Quelle:** Kaggle  
**URL:** https://www.kaggle.com/datasets/wordsforthewise/lending-club  
**Größe:** 2+ Millionen Kredite  
**Beschreibung:** Peer-to-Peer Lending Daten mit detaillierten Kreditnehmer-Informationen.

**Warum interessant:**
- Umfangreiche Kreditnehmer-Attribute (KYC-ähnlich)
- Kreditperformance über Zeit
- Alternative Lending Daten
- Risikobewertungs-Features

**Analyseansätze:**
- Credit Risk Modeling für KYC
- Alternative Data in Customer Due Diligence
- Default Prediction Models
- Portfolio Risk Analysis

---

## 🎯 Klassifikationsaufgaben

### 1. Covertype Dataset
**Quelle:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/31/covertype  
**Größe:** 581.012 Instanzen, 54 Features, 7 Klassen  
**Beschreibung:** Waldbedeckungstypen basierend auf kartografischen Variablen.

**Warum interessant:**
- Multi-Klassen Klassifikation (7 Typen)
- Große Datenmenge für robuste Modelle
- Mix aus kategorischen und kontinuierlichen Features
- Geospatiale Daten

**Analyseansätze:**
- Random Forest, Gradient Boosting
- Feature Engineering für Geo-Daten
- Class Imbalance Handling
- Ensemble Methods Vergleich

---

### 2. Human Activity Recognition (HAR) Dataset
**Quelle:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones  
**Größe:** 10.299 Instanzen, 561 Features  
**Beschreibung:** Smartphone-Sensordaten für Aktivitätserkennung (Gehen, Stehen, etc.).

**Warum interessant:**
- Zeitreihen-Features aus Sensordaten
- Multi-Klassen Problem (6 Aktivitäten)
- IoT/Wearables Kontext
- Feature Engineering aus Rohdaten

**Analyseansätze:**
- SVM, Neural Networks
- Feature Selection bei hochdimensionalen Daten
- Time-Series Classification
- Signal Processing Techniken

---

### 3. Room Occupancy Detection Dataset
**Quelle:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/357/occupancy+detection  
**Größe:** 20.560 Messungen  
**Beschreibung:** Raumbelegung basierend auf Temperatur, Luftfeuchtigkeit, Licht, CO2.

**Warum interessant:**
- IoT/Smart Building Anwendung
- Umweltsensordaten
- Binary Classification mit Zeitstempel
- Energieeffizienz-Kontext

**Analyseansätze:**
- Logistic Regression, Decision Trees
- Time-based Feature Engineering
- Threshold-based vs. ML Approaches
- Real-time Classification Simulation

---

### 4. Wine Quality Dataset
**Quelle:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/186/wine+quality  
**Größe:** 6.497 Weine (Rot und Weiß)  
**Beschreibung:** Physikochemische Eigenschaften und Qualitätsbewertungen von Wein.

**Warum interessant:**
- Ordinal Classification (Qualität 0-10)
- Chemische Features
- Zwei Varianten (Rot/Weiß Wein)
- Weinproduktions-Kontext

**Analyseansätze:**
- Ordinal vs. Multi-Class Classification
- Feature Importance Analysis
- Regression vs. Classification Approach
- Ensemble Methods

---

### 5. Dry Bean Dataset
**Quelle:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/602/dry+bean+dataset  
**Größe:** 13.611 Bohnen, 16 Features, 7 Klassen  
**Beschreibung:** Morphologische Features verschiedener Bohnensorten.

**Warum interessant:**
- Computer Vision Features (aber kein Bildverarbeitung nötig)
- Landwirtschafts-/Food-Tech Kontext
- Gut balancierte Klassen
- Neueres Dataset (2020)

**Analyseansätze:**
- Multi-Class Classification
- Dimensionality Reduction
- Feature Engineering aus Morphologie
- Agricultural Data Science

---

### 6. Bank Customer Churn Prediction
**Quelle:** Kaggle  
**URL:** https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction  
**Größe:** 10.000 Kunden  
**Beschreibung:** Kundenabwanderung bei einer Bank mit demografischen und Konto-Features.

**Warum interessant:**
- Business-relevantes Problem
- Imbalanced Classification
- Mix aus numerischen und kategorischen Features
- CRM/Marketing Kontext

**Analyseansätze:**
- Churn Prediction Models
- Cost-Sensitive Learning
- Feature Importance für Retention
- Uplift Modeling

---

## 📋 Allgemeine Hinweise

### Datensatz-Auswahl Kriterien

Bei der Auswahl eines Datensatzes für Ihre Seminararbeit, beachten Sie:

1. **Größe und Komplexität**
   - Mindestens 1.000 Datenpunkte für statistische Signifikanz
   - Ausreichend Features für meaningful Analysis (>5)
   - Nicht zu groß für Ihre Computing-Ressourcen

2. **Dokumentation**
   - Gute Beschreibung der Features
   - Bekannte Datenqualitätsprobleme dokumentiert
   - Verwendungsbeispiele oder Papers verfügbar

3. **Relevanz**
   - Passt zum gewählten Analysetyp
   - Interessanter Business/Research Context
   - Erlaubt mehrere Analyseansätze

4. **Lizenz und Ethik**
   - Klare Nutzungsrechte für akademische Arbeiten
   - Keine sensitiven persönlichen Daten (oder gut anonymisiert)
   - Ethisch vertretbare Datensammlung

### Download und Vorbereitung

#### UCI ML Repository
```python
# Beispiel für Online Retail Dataset
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
df = pd.read_excel(url)
df.to_csv('online_retail.csv', index=False)
```

#### Kaggle Datasets
```bash
# Kaggle CLI installieren
pip install kaggle

# API Token konfigurieren (~/.kaggle/kaggle.json)
# Dataset herunterladen
kaggle datasets download -d <dataset-path>
```

### Best Practices für Seminararbeit

1. **Explorative Datenanalyse (EDA)**
   - Verstehen Sie Ihre Daten gründlich
   - Dokumentieren Sie Datenqualitätsprobleme
   - Visualisieren Sie wichtige Zusammenhänge

2. **Reproduzierbarkeit**
   - Versionieren Sie Ihre Daten (oder dokumentieren Sie Download-Quelle)
   - Nutzen Sie Seeds für Random Operations
   - Dokumentieren Sie Dependencies (requirements.txt)

3. **Methodologie**
   - Verwenden Sie Train/Test Split
   - Cross-Validation für robuste Ergebnisse
   - Vergleichen Sie mehrere Ansätze

4. **Dokumentation**
   - Begründen Sie Ihre Datensatz-Wahl
   - Dokumentieren Sie alle Preprocessing-Schritte
   - Interpretieren Sie Ihre Ergebnisse im Business-Kontext

### Zusätzliche Ressourcen

- **UCI Machine Learning Repository:** https://archive.ics.uci.edu/
- **Kaggle Datasets:** https://www.kaggle.com/datasets
- **Google Dataset Search:** https://datasetsearch.research.google.com/
- **Data.gov:** https://data.gov/ (US Government Data)
- **European Data Portal:** https://data.europa.eu/
- **Papers with Code:** https://paperswithcode.com/datasets (mit Benchmarks)
- **AWS Open Data:** https://registry.opendata.aws/
- **Awesome Public Datasets (GitHub):** https://github.com/awesomedata/awesome-public-datasets

### Kontakt und Fragen

Für Fragen zur Datensatz-Auswahl oder Projektplanung:
- Nutzen Sie die Issue-Tracker des Repositories
- Diskutieren Sie mit Kommilitonen und Dozenten
- Konsultieren Sie die Referenz-Papers zu den Datasets

---

**Letzte Aktualisierung:** Februar 2026  
**Erstellt für:** DAMI01 / DATA01 Data Analytics Masters Course

