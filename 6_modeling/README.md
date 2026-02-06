# Phase 6: Modellierung

## Überblick
Diese Phase konzentriert sich auf den Aufbau und das Training von Machine-Learning-Modellen zur Patientensegmentierung.

## Ziele
- Geeignete Algorithmen auswählen
- Modelle trainieren
- Hyperparameter optimieren
- Modellleistung vergleichen
- Bestes Modell auswählen

## Modellierungsansätze für Patientensegmentierung

### Unüberwachtes Lernen (Clustering)

#### 1. K-Means-Clustering
```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Optimale Clusteranzahl bestimmen (Elbow-Methode)
inertias = []
silhouette_scores = []
K_bereich = range(2, 11)

for k in K_bereich:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_skaliert)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_skaliert, kmeans.labels_))

# Elbow-Kurve plotten
plt.plot(K_bereich, inertias, 'bx-')
plt.xlabel('Anzahl Cluster (k)')
plt.ylabel('Trägheit')
plt.title('Elbow-Methode')
plt.show()

# Endgültiges Modell trainieren
bestes_k = 4  # aus Elbow-Plot bestimmt
kmeans = KMeans(n_clusters=bestes_k, random_state=42)
cluster = kmeans.fit_predict(X_skaliert)
```

#### 2. Hierarchisches Clustering
```python
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Linkage-Matrix erstellen
linkage_matrix = linkage(X_skaliert, method='ward')

# Dendrogramm plotten
plt.figure(figsize=(12, 6))
dendrogram(linkage_matrix)
plt.title('Dendrogramm – Hierarchisches Clustering')
plt.show()

# Clustering anwenden
hierarchisch = AgglomerativeClustering(n_clusters=4, linkage='ward')
cluster = hierarchisch.fit_predict(X_skaliert)
```

#### 3. DBSCAN
```python
from sklearn.cluster import DBSCAN

# DBSCAN-Clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
cluster = dbscan.fit_predict(X_skaliert)
```

#### 4. Gaussian-Mixture-Modelle
```python
from sklearn.mixture import GaussianMixture

# GMM-Clustering
gmm = GaussianMixture(n_components=4, random_state=42)
cluster = gmm.fit_predict(X_skaliert)
```

### Überwachtes Lernen (falls Labels vorhanden)

#### Klassifikationsalgorithmen
```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Daten aufteilen
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Modelle trainieren
modelle = {
    'Logistische Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(n_estimators=100),
    'Gradient Boosting': GradientBoostingClassifier(),
    'SVM': SVC(kernel='rbf')
}

for name, modell in modelle.items():
    modell.fit(X_train, y_train)
    print(f"{name} trainiert")
```

## Hyperparameter-Tuning

### Grid Search
```python
from sklearn.model_selection import GridSearchCV

# Parameter-Grid definieren
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}

# Grid Search durchführen
grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train, y_train)

print(f"Beste Parameter: {grid_search.best_params_}")
print(f"Bester Score: {grid_search.best_score_}")
```

### Random Search
```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Parameterverteilungen definieren
param_dist = {
    'n_estimators': randint(50, 200),
    'max_depth': randint(5, 20),
    'min_samples_split': randint(2, 11)
}

# Random Search durchführen
random_search = RandomizedSearchCV(
    RandomForestClassifier(),
    param_distributions=param_dist,
    n_iter=50,
    cv=5,
    random_state=42
)
random_search.fit(X_train, y_train)
```

## Modellpersistenz

```python
import joblib

# Modell speichern
joblib.dump(modell, '../models/patient_segmentation_model.pkl')

# Modell laden
geladenes_modell = joblib.load('../models/patient_segmentation_model.pkl')
```

## Best Practices

1. **Einfach beginnen** – Mit Baseline-Modellen starten
2. **Kreuzvalidierung** – k-Fold-Kreuzvalidierung verwenden
3. **Feature-Skalierung** – Features vor dem Clustering skalieren
4. **Zufallsseeds** – Für Reproduzierbarkeit setzen
5. **Modellversionierung** – Modellversionen und Konfigurationen nachverfolgen
6. **Dokumentation** – Modellentscheidungen und Begründungen dokumentieren

## Ergebnisse

- [ ] Trainierte Modelle (gespeichert im models/-Verzeichnis)
- [ ] Modelltrainingsskripte
- [ ] Hyperparameter-Tuning-Ergebnisse
- [ ] Modellvergleichsbericht
- [ ] Begründung der Modellauswahl

## Nächste Schritte

Nach der Modellierung:
1. Bestes Modell auswählen
2. Modelleigenschaften dokumentieren
3. Endgültiges Modell speichern
4. Weiter zu Phase 7: Evaluation
