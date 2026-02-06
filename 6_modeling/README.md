# Phase 6: Modeling

## Overview
This phase focuses on building and training machine learning models for patient segmentation.

## Objectives
- Select appropriate algorithms
- Train models
- Tune hyperparameters
- Compare model performance
- Select best model

## Modeling Approaches for Patient Segmentation

### Unsupervised Learning (Clustering)

#### 1. K-Means Clustering
```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Determine optimal number of clusters (Elbow method)
inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Plot elbow curve
plt.plot(K_range, inertias, 'bx-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# Train final model
best_k = 4  # determined from elbow plot
kmeans = KMeans(n_clusters=best_k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
```

#### 2. Hierarchical Clustering
```python
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Create linkage matrix
linkage_matrix = linkage(X_scaled, method='ward')

# Plot dendrogram
plt.figure(figsize=(12, 6))
dendrogram(linkage_matrix)
plt.title('Hierarchical Clustering Dendrogram')
plt.show()

# Apply clustering
hierarchical = AgglomerativeClustering(n_clusters=4, linkage='ward')
clusters = hierarchical.fit_predict(X_scaled)
```

#### 3. DBSCAN
```python
from sklearn.cluster import DBSCAN

# DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(X_scaled)
```

#### 4. Gaussian Mixture Models
```python
from sklearn.mixture import GaussianMixture

# GMM clustering
gmm = GaussianMixture(n_components=4, random_state=42)
clusters = gmm.fit_predict(X_scaled)
```

### Supervised Learning (if labels available)

#### Classification Algorithms
```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

# Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train models
models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(n_estimators=100),
    'Gradient Boosting': GradientBoostingClassifier(),
    'SVM': SVC(kernel='rbf')
}

for name, model in models.items():
    model.fit(X_train, y_train)
    print(f"{name} trained")
```

## Hyperparameter Tuning

### Grid Search
```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}

# Grid search
grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")
```

### Random Search
```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Define parameter distributions
param_dist = {
    'n_estimators': randint(50, 200),
    'max_depth': randint(5, 20),
    'min_samples_split': randint(2, 11)
}

# Random search
random_search = RandomizedSearchCV(
    RandomForestClassifier(),
    param_distributions=param_dist,
    n_iter=50,
    cv=5,
    random_state=42
)
random_search.fit(X_train, y_train)
```

## Model Evaluation Metrics

### Clustering Metrics
```python
from sklearn.metrics import (
    silhouette_score, 
    davies_bouldin_score, 
    calinski_harabasz_score
)

# Calculate metrics
silhouette = silhouette_score(X_scaled, clusters)
davies_bouldin = davies_bouldin_score(X_scaled, clusters)
calinski_harabasz = calinski_harabasz_score(X_scaled, clusters)

print(f"Silhouette Score: {silhouette:.3f}")
print(f"Davies-Bouldin Index: {davies_bouldin:.3f}")
print(f"Calinski-Harabasz Score: {calinski_harabasz:.3f}")
```

### Classification Metrics
```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# Predictions
y_pred = model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(classification_report(y_test, y_pred))
```

## Model Persistence

```python
import joblib
import pickle

# Save model
joblib.dump(model, '../models/patient_segmentation_model.pkl')

# Load model
loaded_model = joblib.load('../models/patient_segmentation_model.pkl')
```

## Best Practices

1. **Start simple** - Begin with baseline models
2. **Cross-validation** - Use k-fold cross-validation
3. **Feature scaling** - Scale features before clustering
4. **Random seeds** - Set random seeds for reproducibility
5. **Model versioning** - Track model versions and configurations
6. **Documentation** - Document model choices and rationale

## Deliverables

- [ ] Trained models (saved in models/ directory)
- [ ] Model training scripts
- [ ] Hyperparameter tuning results
- [ ] Model comparison report
- [ ] Best model selection justification

## Next Steps

After modeling:
1. Select best performing model
2. Document model characteristics
3. Save final model
4. Proceed to Phase 7: Evaluation
