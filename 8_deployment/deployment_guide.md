# Phase 8: Deployment

## Overview
This phase focuses on preparing the patient segmentation model for production deployment.

## Objectives
- Document deployment strategy
- Create inference pipeline
- Develop API (if needed)
- Plan monitoring and maintenance
- Create user documentation

## Deployment Strategy

### 1. Model Deployment Options

#### Option A: Batch Predictions
- Run model on scheduled intervals
- Process patient data in batches
- Update segmentation periodically

#### Option B: Real-time API
- REST API for on-demand predictions
- Integrate with healthcare systems
- Low-latency predictions

#### Option C: Embedded in Application
- Package model with application
- Local predictions
- No external API calls required

### 2. Deployment Checklist

- [ ] Model artifacts saved and versioned
- [ ] Preprocessing pipeline documented
- [ ] Dependencies documented (requirements.txt)
- [ ] Inference script tested
- [ ] API endpoints designed (if applicable)
- [ ] Performance benchmarks established
- [ ] Monitoring plan defined
- [ ] Rollback strategy prepared

## Inference Script Example

```python
"""
Patient Segmentation Inference Script
"""

import joblib
import pandas as pd
import numpy as np
from pathlib import Path

class PatientSegmentationPredictor:
    """Class to handle patient segmentation predictions."""
    
    def __init__(self, model_path, scaler_path=None):
        """
        Initialize predictor.
        
        Args:
            model_path: Path to saved model
            scaler_path: Path to saved scaler (optional)
        """
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path) if scaler_path else None
        
    def preprocess(self, data):
        """Preprocess input data."""
        # Apply same preprocessing as training
        if self.scaler:
            data_scaled = self.scaler.transform(data)
            return data_scaled
        return data
    
    def predict(self, data):
        """
        Predict patient segments.
        
        Args:
            data: DataFrame with patient features
            
        Returns:
            Array of segment predictions
        """
        # Preprocess
        data_processed = self.preprocess(data)
        
        # Predict
        predictions = self.model.predict(data_processed)
        
        return predictions
    
    def predict_with_confidence(self, data):
        """
        Predict with confidence scores (if model supports it).
        
        Returns:
            predictions, confidence_scores
        """
        data_processed = self.preprocess(data)
        predictions = self.model.predict(data_processed)
        
        if hasattr(self.model, 'predict_proba'):
            confidence = np.max(self.model.predict_proba(data_processed), axis=1)
            return predictions, confidence
        
        return predictions, None
    
    def get_segment_profile(self, segment_id):
        """Return characteristics of a specific segment."""
        # Load segment profiles (could be stored separately)
        segment_profiles = {
            0: "High-risk patients requiring intensive care",
            1: "Moderate-risk patients with chronic conditions",
            2: "Low-risk patients with preventive care needs",
            3: "Healthy patients requiring routine check-ups"
        }
        return segment_profiles.get(segment_id, "Unknown segment")


def main():
    """Example usage."""
    # Initialize predictor
    predictor = PatientSegmentationPredictor(
        model_path='../models/patient_segmentation_model.pkl',
        scaler_path='../models/scaler.pkl'
    )
    
    # Load new patient data
    new_patients = pd.read_csv('new_patients.csv')
    
    # Make predictions
    segments = predictor.predict(new_patients)
    
    # Add to dataframe
    new_patients['segment'] = segments
    
    # Get segment descriptions
    new_patients['segment_description'] = new_patients['segment'].apply(
        predictor.get_segment_profile
    )
    
    # Save results
    new_patients.to_csv('patient_segments_output.csv', index=False)
    print(f"Segmented {len(new_patients)} patients")


if __name__ == '__main__':
    main()
```

## REST API Example (Flask)

```python
"""
Flask API for Patient Segmentation
"""

from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model at startup
model = joblib.load('models/patient_segmentation_model.pkl')
scaler = joblib.load('models/scaler.pkl')

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'model': 'loaded'})

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict patient segment.
    
    Expected JSON format:
    {
        "patients": [
            {"age": 45, "feature1": value1, ...},
            {"age": 60, "feature2": value2, ...}
        ]
    }
    """
    try:
        data = request.get_json()
        patients_df = pd.DataFrame(data['patients'])
        
        # Preprocess
        patients_scaled = scaler.transform(patients_df)
        
        # Predict
        segments = model.predict(patients_scaled)
        
        # Format response
        results = []
        for i, segment in enumerate(segments):
            results.append({
                'patient_id': i,
                'segment': int(segment),
                'segment_name': f'Segment_{segment}'
            })
        
        return jsonify({'predictions': results})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/segments', methods=['GET'])
def get_segments():
    """Return information about available segments."""
    segments_info = {
        '0': 'High-risk patients',
        '1': 'Moderate-risk patients',
        '2': 'Low-risk patients',
        '3': 'Healthy patients'
    }
    return jsonify(segments_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## Monitoring Plan

### Key Metrics to Monitor

1. **Model Performance:**
   - Prediction accuracy (if ground truth available)
   - Segment distribution over time
   - Model confidence scores

2. **System Performance:**
   - Response time / latency
   - Throughput (predictions per second)
   - Error rates
   - Resource usage (CPU, memory)

3. **Data Quality:**
   - Input data distribution
   - Missing value rates
   - Out-of-range values
   - Data drift detection

### Monitoring Implementation

```python
import logging
from datetime import datetime

class PredictionMonitor:
    """Monitor predictions for quality and drift."""
    
    def __init__(self, log_file='predictions.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)
        self.logger = logging.getLogger('predictions')
    
    def log_prediction(self, input_data, prediction, confidence=None):
        """Log each prediction."""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'prediction': prediction,
            'confidence': confidence,
            'input_features': input_data.to_dict()
        }
        self.logger.info(log_entry)
    
    def detect_drift(self, recent_data, reference_data):
        """Detect data drift."""
        # Compare distributions
        from scipy.stats import ks_2samp
        
        drift_detected = False
        for col in recent_data.columns:
            statistic, p_value = ks_2samp(recent_data[col], reference_data[col])
            if p_value < 0.05:
                self.logger.warning(f"Drift detected in {col}: p={p_value}")
                drift_detected = True
        
        return drift_detected
```

## Maintenance Plan

### Regular Tasks

1. **Weekly:**
   - Review prediction logs
   - Check error rates
   - Monitor segment distributions

2. **Monthly:**
   - Evaluate model performance
   - Check for data drift
   - Review segment profiles

3. **Quarterly:**
   - Retrain model with new data
   - Update segment definitions if needed
   - Performance benchmarking

### Model Retraining Triggers

- Significant data drift detected
- Performance degradation
- New data patterns emerge
- Business requirements change

## Documentation

### User Guide Topics

1. **For Data Scientists:**
   - Model architecture and algorithms
   - Training process and hyperparameters
   - Feature engineering steps
   - Evaluation metrics

2. **For Developers:**
   - API documentation
   - Integration guide
   - Error handling
   - Example code

3. **For End Users:**
   - Segment interpretations
   - Use cases and applications
   - Limitations and caveats
   - Contact for support

## Deliverables

- [ ] Deployment guide (this document)
- [ ] Inference script
- [ ] API implementation (if applicable)
- [ ] API documentation
- [ ] Monitoring implementation
- [ ] User guide
- [ ] Maintenance plan

## Security and Privacy Considerations

- **Data Privacy:** Ensure HIPAA/GDPR compliance
- **Access Control:** Implement authentication and authorization
- **Data Encryption:** Encrypt data in transit and at rest
- **Audit Logging:** Log all predictions and access
- **Model Security:** Protect model from adversarial attacks

## Next Steps

1. Review deployment strategy with stakeholders
2. Implement chosen deployment option
3. Set up monitoring and logging
4. Create user documentation
5. Plan model maintenance schedule
6. Conduct pilot deployment
7. Full production rollout

## Success Criteria

- [ ] Model deployed successfully
- [ ] Predictions are accurate and timely
- [ ] Monitoring is in place
- [ ] Documentation is complete
- [ ] Users are trained
- [ ] Maintenance plan is active
