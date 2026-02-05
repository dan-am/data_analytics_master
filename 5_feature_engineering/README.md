# Phase 5: Feature Engineering

## Overview
This phase focuses on creating and selecting features that will improve model performance.

## Objectives
- Create new meaningful features
- Transform existing features
- Select most relevant features
- Encode categorical variables
- Scale/normalize numerical features

## Feature Engineering Techniques

### 1. Feature Creation

#### Interaction Features
```python
# Create interaction between features
df['feature_interaction'] = df['feature1'] * df['feature2']
```

#### Aggregation Features
```python
# Create aggregate features
df['total_score'] = df[score_columns].sum(axis=1)
df['average_metric'] = df[metric_columns].mean(axis=1)
```

#### Binning/Discretization
```python
# Create categorical bins from numerical features
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 50, 65, 100], 
                          labels=['child', 'young_adult', 'adult', 'senior', 'elderly'])
```

#### Domain-Specific Features
- Create features based on healthcare domain knowledge
- Risk scores, severity indices
- Time-based features (if temporal data available)

### 2. Feature Transformation

#### Scaling
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Standardization (z-score normalization)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[numerical_cols])

# Min-Max scaling
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df[numerical_cols])
```

#### Encoding Categorical Variables
```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Label encoding for ordinal variables
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])

# One-hot encoding for nominal variables
df_encoded = pd.get_dummies(df, columns=['category'], drop_first=True)
```

#### Mathematical Transformations
```python
# Log transformation (for skewed data)
df['feature_log'] = np.log1p(df['feature'])

# Square root transformation
df['feature_sqrt'] = np.sqrt(df['feature'])

# Box-Cox transformation
from scipy.stats import boxcox
df['feature_boxcox'], _ = boxcox(df['feature'] + 1)
```

### 3. Feature Selection

#### Correlation-based Selection
```python
# Remove highly correlated features
corr_matrix = df.corr().abs()
upper_triangle = corr_matrix.where(
    np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
)
to_drop = [col for col in upper_triangle.columns 
           if any(upper_triangle[col] > 0.95)]
```

#### Variance-based Selection
```python
from sklearn.feature_selection import VarianceThreshold

# Remove low variance features
selector = VarianceThreshold(threshold=0.01)
selected_features = selector.fit_transform(df)
```

#### Statistical Tests
```python
from sklearn.feature_selection import SelectKBest, f_classif, chi2

# For classification
selector = SelectKBest(score_func=f_classif, k=10)
selected_features = selector.fit_transform(X, y)
```

#### Model-based Selection
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

# Use Random Forest for feature importance
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X, y)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)
```

## Feature Engineering Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

# Define transformers for different column types
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(drop='first', handle_unknown='ignore'))
])

# Combine transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Create full pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('feature_selection', SelectKBest(k=20))
])
```

## Best Practices

1. **Document all transformations** - Keep track of feature engineering decisions
2. **Avoid data leakage** - Fit transformers only on training data
3. **Create reproducible pipelines** - Use sklearn pipelines
4. **Validate new features** - Check if they improve model performance
5. **Keep it simple** - Start with simple features, add complexity as needed
6. **Domain knowledge** - Leverage healthcare expertise for feature creation

## Evaluation Metrics

- Feature importance scores
- Correlation with target (if supervised)
- Variance explained
- Model performance improvement

## Deliverables

- [ ] Feature creation scripts
- [ ] Feature selection analysis
- [ ] Feature engineering pipeline
- [ ] Feature documentation (data dictionary)
- [ ] Comparison of feature sets

## Next Steps

After feature engineering:
1. Finalize feature set
2. Create preprocessing pipeline
3. Save transformed datasets
4. Proceed to Phase 6: Modeling
