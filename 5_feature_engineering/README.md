# Phase 5: Feature Engineering

## Überblick
Diese Phase konzentriert sich auf die Erstellung und Auswahl von Features zur Verbesserung der Modellleistung.

## Ziele
- Neue aussagekräftige Features erstellen
- Vorhandene Features transformieren
- Relevanteste Features auswählen
- Kategorische Variablen kodieren
- Numerische Features skalieren/normalisieren

## Feature-Engineering-Techniken

### 1. Feature-Erstellung

#### Interaktions-Features
```python
# Interaktion zwischen Features erstellen
df['feature_interaktion'] = df['feature1'] * df['feature2']
```

#### Aggregations-Features
```python
# Aggregierte Features erstellen
df['gesamt_score'] = df[score_spalten].sum(axis=1)
df['durchschnitt_metrik'] = df[metrik_spalten].mean(axis=1)
```

#### Binning/Diskretisierung
```python
# Kategorische Bins aus numerischen Features erstellen
df['altersgruppe'] = pd.cut(df['alter'], bins=[0, 18, 35, 50, 65, 100], 
                             labels=['kind', 'junger_erwachsener', 'erwachsener', 'senior', 'aelterer'])
```

#### Domänenspezifische Features
- Features basierend auf Healthcare-Fachwissen erstellen
- Risikoscores, Schweregradindizes
- Zeitbasierte Features (falls Zeitdaten verfügbar)

### 2. Feature-Transformation

#### Skalierung
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Standardisierung (Z-Score-Normalisierung)
scaler = StandardScaler()
df_skaliert = scaler.fit_transform(df[numerische_spalten])

# Min-Max-Skalierung
scaler = MinMaxScaler()
df_skaliert = scaler.fit_transform(df[numerische_spalten])
```

#### Kodierung kategorischer Variablen
```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Label-Kodierung für ordinale Variablen
le = LabelEncoder()
df['kategorie_kodiert'] = le.fit_transform(df['kategorie'])

# One-Hot-Kodierung für nominale Variablen
df_kodiert = pd.get_dummies(df, columns=['kategorie'], drop_first=True)
```

#### Mathematische Transformationen
```python
# Log-Transformation (für schiefe Daten)
df['feature_log'] = np.log1p(df['feature'])

# Quadratwurzel-Transformation
df['feature_sqrt'] = np.sqrt(df['feature'])

# Box-Cox-Transformation
from scipy.stats import boxcox
df['feature_boxcox'], _ = boxcox(df['feature'] + 1)
```

### 3. Feature-Selektion

#### Korrelationsbasierte Selektion
```python
# Hoch korrelierte Features entfernen
korr_matrix = df.corr().abs()
oberes_dreieck = korr_matrix.where(
    np.triu(np.ones(korr_matrix.shape), k=1).astype(bool)
)
zu_entfernen = [col for col in oberes_dreieck.columns 
                if any(oberes_dreieck[col] > 0.95)]
```

#### Varianzbasierte Selektion
```python
from sklearn.feature_selection import VarianceThreshold

# Features mit geringer Varianz entfernen
selector = VarianceThreshold(threshold=0.01)
ausgewaehlte_features = selector.fit_transform(df)
```

#### Statistische Tests
```python
from sklearn.feature_selection import SelectKBest, f_classif, chi2

# Für Klassifikation
selector = SelectKBest(score_func=f_classif, k=10)
ausgewaehlte_features = selector.fit_transform(X, y)
```

#### Modellbasierte Selektion
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

# Random Forest für Feature-Importance verwenden
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X, y)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'wichtigkeit': rf.feature_importances_
}).sort_values('wichtigkeit', ascending=False)
```

## Feature-Engineering-Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

# Transformer für verschiedene Spaltentypen definieren
numerischer_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

kategorischer_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore'))
])

# Transformer kombinieren
vorverarbeitung = ColumnTransformer(
    transformers=[
        ('num', numerischer_transformer, numerische_spalten),
        ('kat', kategorischer_transformer, kategorische_spalten)
    ])

# Vollständige Pipeline erstellen
pipeline = Pipeline(steps=[
    ('vorverarbeitung', vorverarbeitung),
    ('feature_selektion', SelectKBest(k=20))
])
```

## Best Practices

1. **Alle Transformationen dokumentieren** – Feature-Engineering-Entscheidungen nachverfolgen
2. **Datenleck vermeiden** – Transformer nur auf Trainingsdaten fitten
3. **Reproduzierbare Pipelines erstellen** – sklearn-Pipelines verwenden
4. **Neue Features validieren** – Prüfen, ob sie die Modellleistung verbessern
5. **Einfach beginnen** – Mit einfachen Features starten, Komplexität bei Bedarf erhöhen
6. **Fachwissen nutzen** – Healthcare-Expertise für Feature-Erstellung einsetzen

## Ergebnisse

- [ ] Feature-Erstellungsskripte
- [ ] Feature-Selektionsanalyse
- [ ] Feature-Engineering-Pipeline
- [ ] Feature-Dokumentation (Datenwörterbuch)
- [ ] Vergleich der Feature-Sets

## Nächste Schritte

Nach dem Feature Engineering:
1. Feature-Set finalisieren
2. Vorverarbeitungs-Pipeline erstellen
3. Transformierte Datensätze speichern
4. Weiter zu Phase 6: Modellierung
