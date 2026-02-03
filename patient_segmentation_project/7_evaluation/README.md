# Phase 7: Evaluation

## Overview
This phase focuses on comprehensive evaluation of the patient segmentation models.

## Objectives
- Assess model performance
- Validate segmentation quality
- Compare different models
- Analyze segment characteristics
- Generate evaluation reports

## Evaluation Framework

### 1. Clustering Evaluation (Unsupervised)

#### Internal Validation Metrics

```python
from sklearn.metrics import (
    silhouette_score,
    silhouette_samples,
    davies_bouldin_score,
    calinski_harabasz_score
)

# Silhouette Analysis
silhouette_avg = silhouette_score(X_scaled, cluster_labels)
sample_silhouette_values = silhouette_samples(X_scaled, cluster_labels)

# Davies-Bouldin Index (lower is better)
db_index = davies_bouldin_score(X_scaled, cluster_labels)

# Calinski-Harabasz Index (higher is better)
ch_index = calinski_harabasz_score(X_scaled, cluster_labels)

print(f"Silhouette Score: {silhouette_avg:.3f}")
print(f"Davies-Bouldin Index: {db_index:.3f}")
print(f"Calinski-Harabasz Index: {ch_index:.3f}")
```

#### Silhouette Plot
```python
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fig, ax = plt.subplots(figsize=(10, 7))
y_lower = 10

for i in range(n_clusters):
    cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
    cluster_silhouette_values.sort()
    
    size_cluster_i = cluster_silhouette_values.shape[0]
    y_upper = y_lower + size_cluster_i
    
    color = cm.nipy_spectral(float(i) / n_clusters)
    ax.fill_betweenx(np.arange(y_lower, y_upper),
                     0, cluster_silhouette_values,
                     facecolor=color, edgecolor=color, alpha=0.7)
    
    y_lower = y_upper + 10

ax.axvline(x=silhouette_avg, color="red", linestyle="--")
plt.title('Silhouette Plot for Patient Segments')
plt.xlabel('Silhouette Coefficient')
plt.ylabel('Cluster')
plt.show()
```

#### Elbow Method
```python
from sklearn.cluster import KMeans

inertias = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K_range, inertias, 'bx-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()
```

### 2. Classification Evaluation (Supervised)

```python
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)

# Basic metrics
accuracy = accuracy_score(y_test, y_pred)
precision, recall, f1, _ = precision_recall_fscore_support(
    y_test, y_pred, average='weighted'
)

# Classification report
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()

# ROC curve (for binary or multi-class)
if hasattr(model, 'predict_proba'):
    y_proba = model.predict_proba(X_test)
    # For multi-class, calculate ROC for each class
```

### 3. Segment Analysis

#### Segment Profiles
```python
# Add cluster labels to dataframe
df['segment'] = cluster_labels

# Analyze segment characteristics
segment_profiles = df.groupby('segment').agg({
    'numerical_col1': ['mean', 'std'],
    'numerical_col2': ['mean', 'std'],
    'categorical_col': lambda x: x.mode()[0]
})

print(segment_profiles)

# Segment sizes
segment_sizes = df['segment'].value_counts().sort_index()
print("\nSegment Sizes:")
print(segment_sizes)

# Visualize segment distribution
segment_sizes.plot(kind='bar')
plt.title('Patient Distribution Across Segments')
plt.xlabel('Segment')
plt.ylabel('Number of Patients')
plt.show()
```

#### Feature Importance per Segment
```python
# Calculate mean feature values per segment
feature_means = df.groupby('segment')[numerical_features].mean()

# Normalize for comparison
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
feature_means_normalized = pd.DataFrame(
    scaler.fit_transform(feature_means),
    columns=feature_means.columns,
    index=feature_means.index
)

# Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(feature_means_normalized.T, annot=True, cmap='RdYlGn', center=0)
plt.title('Feature Profiles by Segment (Normalized)')
plt.xlabel('Segment')
plt.ylabel('Feature')
plt.show()
```

### 4. Cluster Visualization

#### PCA Visualization
```python
from sklearn.decomposition import PCA

# Reduce to 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot clusters
plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], 
                     c=cluster_labels, cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Cluster')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%} variance)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%} variance)')
plt.title('Patient Segments Visualization (PCA)')
plt.show()
```

#### t-SNE Visualization
```python
from sklearn.manifold import TSNE

# Reduce to 2D
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

# Plot
plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], 
                     c=cluster_labels, cmap='viridis', alpha=0.6)
plt.colorbar(scatter, label='Cluster')
plt.title('Patient Segments Visualization (t-SNE)')
plt.show()
```

### 5. Model Comparison

```python
# Compare multiple models
results = []

for model_name, model in models.items():
    score = silhouette_score(X_scaled, model.labels_)
    db_score = davies_bouldin_score(X_scaled, model.labels_)
    ch_score = calinski_harabasz_score(X_scaled, model.labels_)
    
    results.append({
        'Model': model_name,
        'Silhouette': score,
        'Davies-Bouldin': db_score,
        'Calinski-Harabasz': ch_score
    })

comparison_df = pd.DataFrame(results)
print(comparison_df)
```

## Evaluation Checklist

- [ ] Internal validation metrics calculated
- [ ] Silhouette analysis performed
- [ ] Segment profiles created
- [ ] Cluster visualization generated
- [ ] Model comparison completed
- [ ] Best model selected and justified
- [ ] Segments are interpretable
- [ ] Segment sizes are reasonable

## Deliverables

- [ ] Evaluation report with all metrics
- [ ] Segment profiles and characteristics
- [ ] Visualization plots
- [ ] Model comparison table
- [ ] Recommendations for segment use

## Success Criteria

### Metric Thresholds
- **Silhouette Score:** > 0.5 (good separation)
- **Davies-Bouldin Index:** < 1.0 (compact clusters)
- **Segment Balance:** No segment < 5% of total patients
- **Interpretability:** Clear differentiating features identified

## Next Steps

After evaluation:
1. Document final model selection
2. Create segment interpretation guide
3. Prepare deployment recommendations
4. Proceed to Phase 8: Deployment
