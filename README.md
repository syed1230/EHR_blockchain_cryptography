# 🔐 EHR Blockchain Security System with ML-Based Access Analysis

A Python-based security system for protecting Electronic Health Records (EHRs) using **AES-256-GCM encryption, SHA-256 hashing, blockchain integrity verification, and Machine Learning-based suspicious access detection**.

The project combines cryptographic techniques with security log analysis to demonstrate how sensitive healthcare records can be protected and how potentially suspicious access activity can be identified.

## 🎯 Project Objectives

- **Patient Data Security:** Protect sensitive patient records using AES-256-GCM encryption.
- **Data Integrity:** Generate SHA-256 hashes to verify data integrity.
- **Tamper Detection:** Use blockchain hash linking to detect unauthorized modifications.
- **Secure Authentication:** Provide authenticated access with Admin and Doctor roles.
- **Suspicious Access Detection:** Apply Decision Tree Classification to analyze access patterns recorded in security logs.
- **Security Auditing:** Maintain logs of security-related events to support monitoring and analysis.

## ✨ Key Features

### 🔒 1. Patient Data Encryption
- Encrypt patient records using AES-256-GCM.
- Protect sensitive information from unauthorized disclosure.
- Decrypt records for authorized users using the correct encryption key and authentication information.

### ⛓️ 2. Blockchain-Based Record Storage
- Store encrypted patient records in blockchain blocks.
- Maintain block indexes and timestamps.
- Store data hashes, current block hashes, and previous block hashes.
- Link blocks through their previous hashes.

### 🛡️ 3. Automatic Integrity Verification
The system verifies blockchain integrity by checking:

- SHA-256 hashes of encrypted data.
- Current block hashes.
- Connections between consecutive blocks.

If verification identifies an inconsistency, the application can report a potential tampering attempt.

### 👤 4. User Authentication and Role Management
- Authenticate users before granting access.
- Support Admin and Doctor roles.
- Verify passwords using PBKDF2 with SHA-256.
- Restrict sensitive operations to authorized users.

### 🧠 5. ML-Based Suspicious Access Detection
The project includes a Decision Tree Classification model for analyzing security access patterns.

The model uses access-related features such as:

- Access hour.
- Number of failed attempts.
- Number of records accessed.
- Unusual location indicator.

The model classifies access activity based on patterns learned from its training dataset and helps identify potentially suspicious events.

**Note:** ML-based classification is intended to support security monitoring. Its predictions are not proof that an activity is malicious.

### 📋 6. Security Logs and Audit Trails
- Maintain security-related event logs.
- Record access and authentication events where implemented.
- Store audit information for reviewing application activity.
- Support analysis of logged events through the security analysis components.

### 🆔 7. Patient Record Management
The application supports patient record entry with fields such as:

- Patient ID
- Patient Name
- Age
- Gender
- Blood Group
- Diagnosis

The system checks for duplicate Patient IDs before storing new records.

### 💾 8. Persistent CSV Storage
CSV files are used to maintain patient records, security logs, and related application data.

This provides simple persistent storage for the academic demonstration.

## 🔄 System Workflow

```text
User Login
    ↓
Patient Record Entry
    ↓
AES-256-GCM Encryption
    ↓
SHA-256 Hash Generation
    ↓
Blockchain Storage
    ↓
Blockchain Integrity Verification
    ↓
Tamper Detection
    ↓
Authorized Decryption
```

### ML Security Analysis Workflow

```text
Security Access Logs
        ↓
Feature Preparation
        ↓
Trained Decision Tree Model
        ↓
Access Pattern Classification
        ↓
Potentially Suspicious Activity Identification
```

The cryptographic workflow protects patient records, while the ML workflow analyzes security access patterns. They serve different security purposes.

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application implementation |
| Streamlit | Interactive web application interface |
| AES-256-GCM | Patient data encryption and authentication |
| SHA-256 | Cryptographic hashing and integrity verification |
| PBKDF2-SHA256 | Password-based key derivation for authentication |
| Blockchain | Hash-linked record storage and integrity checking |
| Scikit-learn | Decision Tree Classification model |
| Pandas | Data handling and analysis, where used |
| CSV | Persistent storage for records and logs |
| Cryptography Library | Encryption and cryptographic operations |

## 📂 Project Structure

```text
ehr-blockchain-cryptography/
│
├── app.py
├── auth.py
├── blockchain.py
├── crypto_utils.py
├── storage.py
├── audit_log.py
│
├── security_ml.py
├── access_detection.py
├── analyze_security_logs.py
│
├── access_training_data.csv
├── access_logs.csv
├── security_logs.csv
├── security_audit.csv
├── ehr_data.csv
│
├── test_blockchain.py
├── test_security_ml.py
│
├── README.md
└── .gitignore
```

**Additional generated or local files may include:**

- `access_model.pkl` — saved machine learning model.
- `aes_key.key` — encryption key file.
- `__pycache__/` — Python-generated cache files.

These files may be created or used by the application depending on its configuration. Secret keys must be kept out of public repositories.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/syed1230/ehr-blockchain-cryptography.git
```

### 2. Navigate to the Project Directory

```bash
cd ehr-blockchain-cryptography
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install streamlit cryptography pandas scikit-learn
```

Install any additional dependencies required by your project files.

### 5. Run the Application

```bash
streamlit run app.py
```

The Streamlit application will provide a local URL in the terminal. Open that URL in your browser.

## 🧪 Testing

The repository includes test files for blockchain integrity and machine learning functionality.

Run the blockchain tests:

```bash
python -m pytest test_blockchain.py
```

Run the ML security tests:

```bash
python -m pytest test_security_ml.py
```

Install `pytest` if necessary:

```bash
pip install pytest
```

The tests should be run against the current project implementation to verify that the expected functionality works correctly.

## 🔐 Security Considerations

- Encryption keys must be protected and should never be committed to a public GitHub repository.
- Use `.gitignore` to exclude secret keys, virtual environments, generated cache files, and other sensitive local artifacts.
- ML classifications can produce false positives and false negatives.
- CSV storage is suitable for an academic prototype but does not provide the access controls, concurrency guarantees, and operational safeguards required for production healthcare systems.
- The project demonstrates blockchain concepts; it should not be described as a distributed blockchain network unless a distributed implementation exists.

## 🚀 Future Improvements

- Integrate with real healthcare information systems.
- Introduce secure, scalable database storage.
- Improve ML-based suspicious access detection with larger and validated datasets.
- Add role-based audit reports and security dashboards.
- Explore distributed blockchain architecture.
- Strengthen encryption-key management and deployment security.

## 🎓 Project Scope

This project is developed for **academic demonstration purposes**. It demonstrates cryptographic protection of electronic health records, blockchain-based integrity verification, authenticated access, security logging, and machine learning-based access pattern analysis.

It is not intended for storing real patient information or for production healthcare deployment without further security testing, privacy safeguards, and regulatory compliance.

## 👩‍💻 Author

**Shaguftha Syed**  
B.Tech Computer Science and Engineering  
Amrita Vishwa Vidyapeetham

GitHub: [@syed1230](https://github.com/syed1230)
