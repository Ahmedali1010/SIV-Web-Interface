<div align="center">

# 🎙️ SIV Web Interface: Live Prototype

**A secure, web-based prototype demonstrating a Speaker Identification and Verification (SIV) Convolutional Neural Network in real time.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-CPU--Optimized-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

**[🌐 Launch the Live Demo](https://kurdish-siv-prototype.streamlit.app/)**

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Security & Architecture](#️-security--architecture)
- [Tech Stack](#️-tech-stack)
- [Associated Research & Dataset](#-associated-research--dataset)
- [Citation](#-citation)
- [License](#-license)

---

## 📖 Overview

This repository hosts the front-end interface and inference engine for a **text-independent SIV model**. Built with **Streamlit**, the application:

1. Processes raw `.ogg` or `.wav` acoustic samples
2. Extracts 2D Mel-spectrogram spatial features via `librosa`
3. Performs real-time identity verification using a pre-trained `TensorFlow` CNN

---

## 🌐 Live Demo

| | |
|---|---|
| **URL** | [kurdish-siv-prototype.streamlit.app](https://kurdish-siv-prototype.streamlit.app/) |
| **Input** | `.ogg` / `.wav` audio sample |
| **Output** | Verified speaker identity + confidence score |

---

## 🛡️ Security & Architecture

| Component | Implementation |
|---|---|
| **Resource Management** | `@st.cache_resource` for optimized CNN memory allocation across sessions |
| **Secure File Handling** | `tempfile` with guaranteed cleanup via `try...finally`, mitigating DoS via resource exhaustion |
| **Data Normalization** | Global mean/std scaling applied dynamically during runtime inference |

---

## 🛠️ Tech Stack

| Layer | Technologies |
|---|---|
| **Frontend** | Streamlit |
| **Backend Engine** | Python |
| **Machine Learning** | TensorFlow (CPU-optimized), scikit-learn |
| **Acoustic Processing** | Librosa |

---

## 🔬 Associated Research & Dataset

This prototype is part of a broader research initiative on **biometric security in low-resource language environments** (Central Kurdish).

| | |
|---|---|
| **Dataset** | *A Comprehensive Kurdish Speech Corpus for Speaker Identification and Verification in a Low-Resource Language Environment* |
| **Repository** | Mendeley Data, V3 |
| **DOI** | [10.17632/7rv22xjmdx.3](https://doi.org/10.17632/7rv22xjmdx.3) |

### Citation

If you use this dataset or prototype in your research, please cite:

```
Abdulrahman, Ayub Othman; Ali, Ahmad; Jamal, Muhamad Jamal; Bakr, Zhyar (2026),
"A Comprehensive Kurdish Speech Corpus for Speaker Identification and Verification
in a Low-Resource Language Environment", Mendeley Data, V3,
doi: 10.17632/7rv22xjmdx.3
```

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

<div align="center">

*Advancing biometric security research for low-resource language communities.*

</div>
