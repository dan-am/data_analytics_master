# Phase 7: Evaluation

## Überblick
Diese Phase konzentriert sich auf die umfassende Bewertung der Patientensegmentierungsmodelle.

## Ziele
- Modellleistung bewerten
- Segmentierungsqualität validieren
- Verschiedene Modelle vergleichen
- Segmenteigenschaften analysieren
- Evaluationsberichte erstellen

## Evaluationsrahmen

### 1. Clustering-Evaluation (unüberwacht)

#### Interne Validierungsmetriken

```python
from sklearn.metrics import (
    silhouette_score,
    silhouette_samples,
    davies_bouldin_score,
    calinski_harabasz_score
)

# Silhouette-Analyse
silhouette_avg = silhouette_score(X_skaliert, cluster_labels)
sample_silhouette_werte = silhouette_samples(X_skaliert, cluster_labels)

# Davies-Bouldin-Index (niedriger ist besser)
db_index = davies_bouldin_score(X_skaliert, cluster_labels)

# Calinski-Harabasz-Index (höher ist besser)
ch_index = calinski_harabasz_score(X_skaliert, cluster_labels)

print(f"Silhouette-Score: {silhouette_avg:.3f}")
print(f"Davies-Bouldin-Index: {db_index:.3f}")
print(f"Calinski-Harabasz-Index: {ch_index:.3f}")
```

#### Silhouette-Plot
```python
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fig, ax = plt.subplots(figsize=(10, 7))
y_unten = 10

for i in range(n_cluster):
    cluster_silhouette_werte = sample_silhouette_werte[cluster_labels == i]
    cluster_silhouette_werte.sort()
    
    groesse_cluster_i = cluster_silhouette_werte.shape[0]
    y_oben = y_unten + groesse_cluster_i
    
    farbe = cm.nipy_spectral(float(i) / n_cluster)
    ax.fill_betweenx(np.arange(y_unten, y_oben),
                     0, cluster_silhouette_werte,
                     facecolor=farbe, edgecolor=farbe, alpha=0.7)
    
    y_unten = y_oben + 10

ax.axvline(x=silhouette_avg, color="red", linestyle="--")
plt.title('Silhouette-Plot für Patientensegmente')
plt.xlabel('Silhouette-Koeffizient')
plt.ylabel('Cluster')
plt.show()
```

#### Elbow-Methode
```python
from sklearn.cluster import KMeans

inertias = []
K_bereich = range(2, 11)

for k in K_bereich:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_skaliert)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_bereich, inertias, 'bx-')
plt.xlabel('Anzahl Cluster (k)')
plt.ylabel('Trägheit')
plt.title('Elbow-Methode für optimales k')
plt.show()
```

### 2. Klassifikations-Evaluation (überwacht)

```python
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)

# Basismetriken
genauigkeit = accuracy_score(y_test, y_pred)
praezision, recall, f1, _ = precision_recall_fscore_support(
    y_test, y_pred, average='weighted'
)

# Klassifikationsbericht
print(classification_report(y_test, y_pred))

# Konfusionsmatrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Konfusionsmatrix')
plt.ylabel('Wahrer Wert')
plt.xlabel('Vorhergesagter Wert')
plt.show()
```

### 3. Segmentanalyse

#### Segmentprofile
```python
# Cluster-Labels zum DataFrame hinzufügen
df['segment'] = cluster_labels

# Segmenteigenschaften analysieren
segment_profile = df.groupby('segment').agg({
    'numerische_spalte1': ['mean', 'std'],
    'numerische_spalte2': ['mean', 'std'],
    'kategorische_spalte': lambda x: x.mode()[0]
})

print(segment_profile)

# Segmentgrößen
segment_groessen = df['segment'].value_counts().sort_index()
print("\nSegmentgrößen:")
print(segment_groessen)

# Segmentverteilung visualisieren
segment_groessen.plot(kind='bar')
plt.title('Patientenverteilung über Segmente')
plt.xlabel('Segment')
plt.ylabel('Anzahl Patienten')
plt.show()
```

#### Feature-Importance pro Segment
```python
# Durchschnittliche Feature-Werte pro Segment berechnen
feature_mittelwerte = df.groupby('segment')[numerische_features].mean()

# Für Vergleich normalisieren
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
feature_mittelwerte_normalisiert = pd.DataFrame(
    scaler.fit_transform(feature_mittelwerte),
    columns=feature_mittelwerte.columns,
    index=feature_mittelwerte.index
)

# Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(feature_mittelwerte_normalisiert.T, annot=True, cmap='RdYlGn', center=0)
plt.title('Feature-Profile nach Segment (normalisiert)')
plt.xlabel('Segment')
plt.ylabel('Feature')
plt.show()
```

### 4. Cluster-Visualisierung

#### PCA-Visualisierung
```python
from sklearn.decomposition import PCA

# Auf 2D reduzieren
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_skaliert)

# Cluster plotten
plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], 
                     c=cluster_labels, cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Cluster')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} Varianz)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} Varianz)')
plt.title('Patientensegmente – Visualisierung (PCA)')
plt.show()
```

#### t-SNE-Visualisierung
```python
from sklearn.manifold import TSNE

# Auf 2D reduzieren
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_skaliert)

# Plotten
plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], 
                     c=cluster_labels, cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Cluster')
plt.title('Patientensegmente – Visualisierung (t-SNE)')
plt.show()
```

### 5. Modellvergleich

```python
# Mehrere Modelle vergleichen
ergebnisse = []

for modell_name, modell in modelle.items():
    score = silhouette_score(X_skaliert, modell.labels_)
    db_score = davies_bouldin_score(X_skaliert, modell.labels_)
    ch_score = calinski_harabasz_score(X_skaliert, modell.labels_)
    
    ergebnisse.append({
        'Modell': modell_name,
        'Silhouette': score,
        'Davies-Bouldin': db_score,
        'Calinski-Harabasz': ch_score
    })

vergleichs_df = pd.DataFrame(ergebnisse)
print(vergleichs_df)
```

## Evaluations-Checkliste

- [ ] Interne Validierungsmetriken berechnet
- [ ] Silhouette-Analyse durchgeführt
- [ ] Segmentprofile erstellt
- [ ] Cluster-Visualisierung erstellt
- [ ] Modellvergleich abgeschlossen
- [ ] Bestes Modell ausgewählt und begründet
- [ ] Segmente sind interpretierbar
- [ ] Segmentgrößen sind angemessen

## Ergebnisse

- [ ] Evaluationsbericht mit allen Metriken
- [ ] Segmentprofile und -eigenschaften
- [ ] Visualisierungsplots
- [ ] Modellvergleichstabelle
- [ ] Empfehlungen zur Segmentnutzung

## Erfolgskriterien

### Schwellenwerte
- **Silhouette-Score:** > 0.5 (gute Trennung)
- **Davies-Bouldin-Index:** < 1.0 (kompakte Cluster)
- **Segmentbalance:** Kein Segment < 5 % der Gesamtpatienten
- **Interpretierbarkeit:** Klare Unterscheidungsmerkmale identifiziert

## Nächste Schritte

Nach der Evaluation:
1. Endgültige Modellauswahl dokumentieren
2. Leitfaden zur Segmentinterpretation erstellen
3. Deployment-Empfehlungen vorbereiten
4. Weiter zu Phase 8: Deployment
