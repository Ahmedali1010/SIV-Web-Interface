import streamlit as st
import os
import tempfile
import numpy as np
import librosa
import joblib
import tensorflow as tf

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Voice Biometrics SIV", page_icon="🎙️", layout="centered")

# --- GLOBAL VARIABLES ---
SAMPLE_RATE = 22050
DURATION = 1.0 
N_MELS = 64
MAX_PAD_LEN = 44
SECURITY_THRESHOLD = 97.60  # The EER threshold established in research

# --- 1. CACHING THE MODEL (CRITICAL FOR WEB PERFORMANCE) ---
@st.cache_resource
def load_ai_assets():
    # Load model and preprocessors securely
    model = tf.keras.models.load_model('Ultimate_Mel_CNN_New.h5')
    preprocessors = joblib.load('Mel_Preprocessors_New.pkl')
    return model, preprocessors

try:
    model, preprocessors = load_ai_assets()
    le = preprocessors['label_encoder']
    saved_mean = preprocessors['mean']
    saved_std = preprocessors['std']
except Exception as e:
    st.error("Critical System Failure: Unable to load AI models. Please contact the administrator.")
    st.stop()

# --- 2. THE EXTRACTION ENGINE ---
def process_and_predict(audio_path):
    # Load and truncate/pad audio
    audio, sr = librosa.load(audio_path, sr=SAMPLE_RATE, duration=DURATION)
    
    # Extract Mel-Spectrogram
    mel = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=N_MELS)
    mel_db = librosa.power_to_db(mel, ref=np.max)
    
    # Spatial padding to exactly 44 frames
    if mel_db.shape[1] > MAX_PAD_LEN:
        mel_db = mel_db[:, :MAX_PAD_LEN]
    else:
        pad_width = MAX_PAD_LEN - mel_db.shape[1]
        mel_db = np.pad(mel_db, ((0, 0), (0, pad_width)), mode='constant')
        
    mel_db = mel_db.astype(np.float32)
    
    # Global Normalization
    mel_normalized = (mel_db - saved_mean) / saved_std
    
    # Expand dimensions for 2D-CNN (Batch, Height, Width, Channel)
    cnn_input = np.expand_dims(mel_normalized, axis=0)
    cnn_input = np.expand_dims(cnn_input, axis=-1)
    
    # Inference
    prediction_probs = model.predict(cnn_input, verbose=0)
    predicted_class = np.argmax(prediction_probs)
    
    speaker_name = le.inverse_transform([predicted_class])[0]
    confidence = prediction_probs[0][predicted_class] * 100
    
    return speaker_name, confidence

# --- 3. FRONTEND INTERFACE ---
st.title("🎙️ Speaker Verification System")
st.markdown("Upload a 1-second `.ogg` or `.wav` audio sample to verify the speaker's identity against the neural network.")

st.divider()

# File Uploader Widget
uploaded_file = st.file_uploader("Select Audio File", type=['ogg', 'wav', 'mp3'])

if uploaded_file is not None:
    # Audio Player Widget
    st.audio(uploaded_file, format='audio/ogg')
    
    # Trigger Button
    if st.button("Authenticate Identity", type="primary", use_container_width=True):
        
        # Display loading animation while processing
        with st.spinner("Extracting 2D Mel-Spectrogram and analyzing spatial features..."):
            
            # Secure temporary file handling
            tmp_path = None
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".ogg") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_path = tmp_file.name
                
                # Execute prediction
                predicted_speaker, confidence_score = process_and_predict(tmp_path)
                
                # --- 4. DISPLAY RESULTS ---
                st.divider()
                
                # Columns for side-by-side metric display
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric(label="👤 Identified Speaker", value=predicted_speaker)
                    
                with col2:
                    st.metric(label="📊 Confidence Score", value=f"{confidence_score:.2f}%")
                
                # Security Threshold Logic
                st.write("### Authentication Status")
                if confidence_score >= SECURITY_THRESHOLD:
                    st.success(f"✅ **ACCESS GRANTED:** Identity verified successfully (Threshold > {SECURITY_THRESHOLD}%).")
                else:
                    st.error(f"❌ **ACCESS DENIED:** Confidence too low for secure verification.")
                    
                # Visual Progress Bar for Confidence
                st.progress(int(confidence_score) / 100.0)

            except Exception as e:
                # Catch processing errors cleanly without exposing stack trace
                st.error("Authentication failed. Please ensure the audio file is not corrupted and contains valid speech data.")
                
            finally:
                # Guaranteed cleanup to prevent Resource Exhaustion (DoS)
                if tmp_path and os.path.exists(tmp_path):
                    os.remove(tmp_path)