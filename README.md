# SIV-Web-Interface

# SIV Web Interface: Live Prototype

A secure, web-based prototype demonstrating the Speaker Identification and Verification (SIV) Convolutional Neural Network (CNN) in real-time.

## 🌐 Live Demo
**Access the live application here:** [INSERT_YOUR_STREAMLIT_URL_HERE]

## Overview
This repository hosts the front-end interface and inference engine for our text-independent SIV model. Built with **Streamlit**, the application processes raw `.ogg` or `.wav` acoustic samples, extracts 2D Mel-spectrogram spatial features via `librosa`, and performs real-time identity verification utilizing a pre-trained `TensorFlow` CNN.

## 🛡️ Security & Architecture
* **Resource Management:** Utilizes `@st.cache_resource` for optimized CNN memory allocation.
* **Secure File Handling:** Implements `tempfile` with guaranteed cleanup protocols (`try...finally`) to prevent Denial of Service (DoS) via resource exhaustion.
* **Data Normalization:** Applies global mean/std scaling dynamically during runtime inference.

## Tech Stack
* **Frontend:** Streamlit
* **Backend Engine:** Python
* **Machine Learning:** TensorFlow (CPU-optimized), scikit-learn
* **Acoustic Processing:** Librosa

## Associated Research & Dataset
This prototype is part of a broader research initiative on biometric security in low-resource language environments (Central Kurdish).

* **Dataset Access:** [10.17632/7rv22xjmdx.3](https://doi.org/10.17632/7rv22xjmdx.3)
* **Citation:**
    > Abdulrahman, Ayub Othman; Ali, Ahmad; jamal, Muhamad Jamal; Bakr, Zhyar (2026), “A Comprehensive Kurdish Speech Corpus for Speaker Identification and Verification in a Low-Resource Language Environment”, Mendeley Data, V3, doi: 10.17632/7rv22xjmdx.3

## License
Distributed under the MIT License.
