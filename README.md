# Deep-Fake Detection

A Django-based web application that leverages deep learning models to detect and classify deepfake content in videos and images. This project implements multiple state-of-the-art neural network architectures including **InceptionV3**, **EfficientNet**, and a **Hybrid Model** to provide robust deepfake detection capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Architecture](#project-architecture)
- [Models Used](#models-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Models](#database-models)
- [API Endpoints](#api-endpoints)
- [Performance Metrics](#performance-metrics)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project is designed to detect deepfake videos and images using advanced deep learning techniques. It provides a web-based interface for users and administrators to upload datasets, train models, and analyze detection results with comparative performance graphs.

## ✨ Features

- **Multiple Detection Models**: Implements three different neural network architectures for redundancy and accuracy
  - InceptionV3: 98.74% accuracy
  - EfficientNet: 66% accuracy
  - Hybrid Model: 69.7% accuracy

- **Admin Dashboard**: Manage users, datasets, and model performance
- **User Management**: Accept/reject new user registrations
- **Dataset Upload**: Upload custom datasets for model training
- **Performance Visualization**: Comparative graphs showing model accuracy metrics
- **Train-Test Split Analysis**: View training and validation statistics
- **Database Integration**: Persistent storage of model performance metrics

## 🏗️ Project Architecture

```
Deep-Fake-Detection/
├── models.py                 # Django ORM models
├── views.py                  # View logic and handlers
├── admin.py                  # Admin interface configuration
├── apps.py                   # App configuration
├── inceptionv3.h5           # Pre-trained InceptionV3 model
├── deepfakedatabase         # Dataset storage
├── migrations/              # Database migration files
│   ├── 0001_initial.py
│   ├── 0002_comparison_graph_...
│   ├── 0003_delete_inceptionv3_model.py
│   ├── 0004_inceptionv3_model.py
│   ├── 0005_delete_comparison_graph_...
│   ├── 0006_initial.py
│   └── 0007_graph_model.py
└── tests.py                 # Unit tests
```

## 🧠 Models Used

### 1. **InceptionV3**
- **Accuracy**: 98.74%
- **Status**: Completed
- Pre-trained model file: `inceptionv3.h5`
- Best performing model in the suite

### 2. **EfficientNet**
- **Accuracy**: 66%
- **Status**: Completed
- Lightweight model with good efficiency

### 3. **Hybrid Model**
- **Accuracy**: 69.7%
- **Status**: Completed
- Combines features from multiple architectures

## 📦 Installation

### Prerequisites

- Python 3.7+
- Django 3.0+
- TensorFlow/Keras
- OpenCV
- NumPy
- Pandas

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bhavagna27/Deep-Fake-detection.git
   cd Deep-Fake-detection
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Web Interface: `http://localhost:8000/`
   - Admin Panel: `http://localhost:8000/admin/`

## 🚀 Usage

### For Administrators

1. **Dashboard**: View total users, accepted, and pending registrations
2. **Manage Users**: Accept or reject user registration requests
3. **Upload Dataset**: Upload training datasets for model improvement
4. **View Model Performance**: Check individual model metrics (InceptionV3, EfficientNet, Hybrid)
5. **Compare Models**: Visualize performance comparison graphs
6. **Train-Test Analysis**: View dataset split statistics

### For Regular Users

1. **Register**: Create an account (requires admin approval)
2. **Submit Media**: Upload videos/images for deepfake detection
3. **View Results**: Get detection results and confidence scores

## 📁 Project Structure

### Database Models

#### `Dataset`
- Stores uploaded datasets
- Fields: title, file, uploaded_at

#### `InceptionV3_model`
- Tracks InceptionV3 model performance
- Fields: model_name, model_accuracy, model_executed

#### `EfficientNet_model`
- Tracks EfficientNet model performance
- Fields: model_name, model_accuracy, model_executed

#### `Hybrid_model`
- Tracks Hybrid model performance
- Fields: model_name, model_accuracy, model_executed

#### `Comparison_graph`
- Stores comparative metrics
- Fields: S_No, Inception, EfficientNet, Hybrid

#### `graph_model`
- Tracks fake vs. real image statistics
- Fields: Fake_details, Real_details

#### `Train_test_split_model`
- Stores dataset split information
- Fields: S_No, Images_training, Images_validation, Images_classes

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/admin/` | GET | Admin dashboard |
| `/admin/users/` | GET | List all users |
| `/admin/upload/` | POST | Upload dataset |
| `/admin/train-test/` | GET | Train-test split view |
| `/admin/cnnmodel/` | GET | InceptionV3 model performance |
| `/admin/efficientnet/` | GET | EfficientNet model performance |
| `/admin/hybrid/` | GET | Hybrid model performance |
| `/admin/graph/` | GET | Fake vs Real statistics |
| `/admin/comparison/` | GET | Model comparison graph |
| `/admin/accept-user/<id>/` | POST | Accept user registration |
| `/admin/reject-user/<id>/` | POST | Reject user registration |
| `/admin/delete-user/<id>/` | POST | Delete user |

## 📊 Performance Metrics

### Current Model Performance

| Model | Accuracy | Status |
|-------|----------|--------|
| InceptionV3 | 98.74% | ✅ Completed |
| EfficientNet | 66% | ✅ Completed |
| Hybrid Model | 69.7% | ✅ Completed |

### Dataset Statistics

- **Training Images**: 2,041
- **Validation Images**: 2,041
- **Number of Classes**: 2 (Real/Fake)

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License. See the LICENSE file for more details.

## 📧 Contact

For any queries or suggestions, please reach out to the project maintainer:
- **GitHub**: [@Bhavagna27](https://github.com/Bhavagna27)

## 🔬 Future Enhancements

- [ ] Implement real-time video processing
- [ ] Add more advanced detection models
- [ ] Integrate face recognition for enhanced detection
- [ ] Improve EfficientNet model accuracy
- [ ] Add REST API for external integrations
- [ ] Deploy on cloud platforms (AWS, Azure, GCP)
- [ ] Add comprehensive logging and monitoring
- [ ] Implement model versioning

---

**Last Updated**: September 2024
