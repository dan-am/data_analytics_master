# Patientensegmentierung – Analyseprojekt

## Projektübersicht
Dieses Projekt implementiert einen umfassenden Data-Analytics-Workflow zur Patientensegmentierung unter Verwendung des [Patient Segmentation Dataset von Kaggle](https://www.kaggle.com/datasets/nudratabbas/patient-segmentation-data).

## 📚 Ressourcen

### Datensatz-Empfehlungen
Auf der Suche nach interessanten Datensätzen für Ihre Seminararbeit? Unser umfassender Leitfaden hilft weiter:

**[Datensatz-Empfehlungen](dataset_recommendations.md)** – Kuratierte Datensätze für:
- 🔍 Clustering-Analyse
- 🛒 Warenkorbanalyse
- 💰 Finanzdaten & KYC-Analyse
- 🎯 Klassifikationsaufgaben

**[Schnellübersicht](DATASETS_QUICK_REFERENCE.md)** – Kompakte Zusammenfassung der wichtigsten Datensätze.

## Data-Science-Lebenszyklus

Dieses Projekt folgt einem strukturierten Ansatz basierend auf dem Data-Science-Lebenszyklus:

### Phase 1: Geschäftsverständnis
**Ziel:** Geschäftsproblem und Projektziele definieren.
- **Ordner:** `1_business_understanding/`
- **Zweck:** Anforderungen der Patientensegmentierung für Gesundheitsdienstleister verstehen
- **Ergebnisse:** Problemdefinition, Erfolgskriterien, Projektcharta

### Phase 2: Datenanschaffung
**Ziel:** Relevante Daten sammeln und speichern.
- **Ordner:** `2_data_acquisition/`
- **Zweck:** Patientensegmentierungs-Datensatz herunterladen und organisieren
- **Ergebnisse:** Rohdaten, Datenquellen-Dokumentation, Download-Skripte

### Phase 3: Datenvorbereitung
**Ziel:** Daten bereinigen und vorverarbeiten.
- **Ordner:** `3_data_preparation/`
- **Zweck:** Fehlende Werte, Ausreißer und Datenqualitätsprobleme behandeln
- **Ergebnisse:** Bereinigte Datensätze, Datenqualitätsberichte, Vorverarbeitungsskripte

### Phase 4: Explorative Datenanalyse (EDA)
**Ziel:** Datenmuster und Zusammenhänge verstehen.
- **Ordner:** `4_exploratory_analysis/`
- **Zweck:** Verteilungen, Korrelationen und wichtige Erkenntnisse visualisieren
- **Ergebnisse:** EDA-Notebooks, Visualisierungsberichte, statistische Zusammenfassungen

### Phase 5: Feature Engineering
**Ziel:** Relevante Features erstellen und auswählen.
- **Ordner:** `5_feature_engineering/`
- **Zweck:** Features für Patientensegmentierungsmodelle entwickeln
- **Ergebnisse:** Feature-Erstellungsskripte, Feature-Selektionsanalyse

### Phase 6: Modellierung
**Ziel:** Machine-Learning-Modelle erstellen und trainieren.
- **Ordner:** `6_modeling/`
- **Zweck:** Clustering-/Klassifikationsmodelle für Patientensegmentierung entwickeln
- **Ergebnisse:** Trainierte Modelle, Trainingsskripte, Hyperparameter-Tuning-Ergebnisse

### Phase 7: Evaluation
**Ziel:** Modellleistung bewerten.
- **Ordner:** `7_evaluation/`
- **Zweck:** Segmentierungsqualität und Modellmetriken evaluieren
- **Ergebnisse:** Evaluationsberichte, Leistungsmetriken, Modellvergleich

### Phase 8: Deployment
**Ziel:** Produktionsbereitstellung vorbereiten.
- **Ordner:** `8_deployment/`
- **Zweck:** Deployment-Strategie dokumentieren und Inferenz-Skripte erstellen
- **Ergebnisse:** Deployment-Leitfaden, API-Spezifikationen, Monitoring-Plan

## Projektstruktur

```
data_analytics_master/
├── README.md                          # Diese Datei
├── requirements.txt                   # Python-Abhängigkeiten
├── 1_business_understanding/          # Geschäftsproblem-Definition
│   ├── project_charter.md
│   └── success_criteria.md
├── 2_data_acquisition/                # Datensammlung
│   ├── raw_data/                      # Originaldaten (gitignored)
│   ├── processed_data/                # Verarbeitete Daten (gitignored)
│   ├── data_sources/                  # Datenquellen-Dokumentation
│   └── download_data.py               # Download-Skript
├── 3_data_preparation/                # Datenbereinigung
│   ├── data_cleaning.py
│   ├── data_validation.py
│   └── preprocessing_pipeline.py
├── 4_exploratory_analysis/            # EDA
│   ├── eda_notebook.ipynb
│   ├── statistical_analysis.py
│   └── visualization.py
├── 5_feature_engineering/             # Feature-Erstellung
│   ├── feature_creation.py
│   ├── feature_selection.py
│   └── feature_engineering_pipeline.py
├── 6_modeling/                        # Modellentwicklung
│   ├── train_model.py
│   ├── hyperparameter_tuning.py
│   └── clustering_models.py
├── 7_evaluation/                      # Modellevaluation
│   ├── evaluate_model.py
│   ├── performance_metrics.py
│   └── model_comparison.py
├── 8_deployment/                      # Deployment
│   ├── deployment_guide.md
│   ├── inference_script.py
│   └── api_documentation.md
├── notebooks/                         # Jupyter-Notebooks
├── reports/                           # Generierte Analyseberichte
├── scripts/                           # Hilfsskripte
├── models/                            # Gespeicherte Modelle (gitignored)
└── references/                        # Referenzmaterialien
```

## Erste Schritte

### Voraussetzungen
- Python 3.8+
- Kaggle-Konto für den Daten-Download
- Benötigte Python-Pakete (siehe requirements.txt)

### Installation

1. Repository klonen:
```bash
git clone https://github.com/dan-am/data_analytics_master.git
cd data_analytics_master
```

2. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

3. Kaggle-API-Zugangsdaten einrichten:
   - Kaggle-Konto erstellen unter https://www.kaggle.com
   - Kontoeinstellungen → API → Neuen API-Token erstellen
   - Die heruntergeladene `kaggle.json` in `~/.kaggle/` ablegen

4. Datensatz herunterladen:
```bash
python 2_data_acquisition/download_data.py
```

### Verwendung

Die Phasen der Reihe nach durcharbeiten:

1. **Geschäftsverständnis:** Dokumentation in `1_business_understanding/` lesen
2. **Daten beschaffen:** Download-Skript in `2_data_acquisition/` ausführen
3. **Daten vorbereiten:** Bereinigungsskripte in `3_data_preparation/` ausführen
4. **Daten explorieren:** EDA-Notebooks in `4_exploratory_analysis/` ausführen
5. **Features erstellen:** Feature-Skripte in `5_feature_engineering/` nutzen
6. **Modelle erstellen:** Modelle mit Skripten in `6_modeling/` trainieren
7. **Evaluieren:** Leistung mit Skripten in `7_evaluation/` bewerten
8. **Bereitstellen:** Deployment-Leitfaden in `8_deployment/` befolgen

## Datensatz-Informationen

**Quelle:** [Kaggle – Patient Segmentation Data](https://www.kaggle.com/datasets/nudratabbas/patient-segmentation-data)

**Beschreibung:** Dieser Datensatz enthält Patienteninformationen für Segmentierungsanalysen und eignet sich für Healthcare-Analytics und Patienten-Clustering.

## Mitwirken

Beiträge sind willkommen! Bitte die bestehende Projektstruktur und die Phasen des Data-Science-Lebenszyklus einhalten.

## Lizenz

Dieses Projekt ist Teil des DAMI01/DATA01 Data Analytics Masterstudiengangs.

## Kontakt

Bei Fragen oder Problemen bitte ein Issue im Repository erstellen.
