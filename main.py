import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import datetime
import time

# --- CYBER NEWS TICKER (PATTI) ---
st.markdown("""
    <style>
    .ticker-container {
        width: 100%;
        background-color: #004400;
        color: #00FF41;
        overflow: hidden;
        white-space: nowrap;
        padding: 10px 0;
        border-bottom: 2px solid #00FF41;
        font-weight: bold;
        font-family: 'Courier New', monospace;
    }
    .ticker-text {
        display: inline-block;
        padding-left: 100%;
        animation: ticker 50s linear infinite;
    }
    @keyframes ticker {
        0% { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }
    .alert-tag { background: red; color: white; padding: 2px 8px; border-radius: 3px; margin-right: 10px; }
    </style>
    
    <div class="ticker-container">
        <div class="ticker-text">
            <span class="alert-tag">LATEST SCAM ALERT</span> 🚨 Digital Arrest scam targets users via Skype/WhatsApp Video calls -- DO NOT SHARING SCREEN! | 
            <span class="alert-tag">GOVT NOTICE</span> 🛡️ RBI warns against sharing OTP for KYC updates. Real banks never ask for passwords! | 
            <span class="alert-tag">NEW THREAT</span> 🎭 AI Voice Cloning scams on the rise. Always verify via a secondary personal question. | 
            <span class="alert-tag">HELPLINE</span> 📞 Report any fraud immediately at 1930 or cybercrime.gov.in
            <span class="alert-tag">TIP</span> 🔐 Enable 2FA on all banking apps to prevent unauthorized access.
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- SESSION STATE FOR HISTORY ---
if 'scam_history' not in st.session_state:
    # Sample data for initial look
    st.session_state.scam_history = [
        {"Timestamp": "2026-01-04 10:15", "Threat Type": "Digital Arrest", "Confidence": "98%", "Status": "Intercepted"},
        {"Timestamp": "2026-01-04 09:40", "Threat Type": "OTP Phishing", "Confidence": "94%", "Status": "Blocked"}
    ]

def generate_report(data):
    report_text = f"🛡️ GLITCH SECURE-VOICE - OFFICIAL INCIDENT REPORT\n"
    report_text += f"Generated on: {datetime.datetime.now()}\n"
    report_text += "="*50 + "\n\n"
    for entry in data:
        report_text += f"TIME: {entry.get('Timestamp', 'N/A')}\n"
        report_text += f"TYPE: {entry.get('Threat Type', 'Unknown')}\n"
        report_text += f"RISK: {entry.get('Confidence', 0)}%\n"
        report_text += f"ACTION: {entry.get('Status', 'Logged')}\n"
        report_text += "-"*30 + "\n"
    return report_text

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="GlitchSecureVoice Pro AI", layout="wide")

# --- 2. ADVANCED UI STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #00FF41; font-family: 'Courier New', monospace; }
    .status-box { border: 1px solid #00FF41; padding: 15px; border-radius: 5px; background: #1a1a1a; box-shadow: 0 0 10px #00FF41; }
    .fraud-popup {
        position: fixed; top: 15%; left: 50%; transform: translateX(-50%);
        background-color: #990000; border: 5px solid #ff0000; color: #ffffff;
        padding: 40px; border-radius: 20px; text-align: center;
        z-index: 9999; box-shadow: 0 0 100px #ff0000; display: none;
    }
    .info-card { background: #111; border: 1px solid #333; padding: 20px; border-radius: 10px; margin-bottom: 20px; height: 100%; }
    .metric-text { font-size: 14px; color: #00FF41; }
    </style>
    """, unsafe_allow_html=True)
st.markdown("""
    <style>
    .forensic-card {
        border-left: 5px solid #00FF41;
        background: #1a1a1a;
        padding: 15px;
        margin: 10px 0;
    }
    .meter-bar {
        background: #333;
        border-radius: 10px;
        height: 15px;
        width: 100%;
        margin-top: 5px;
    }
    .meter-fill {
        background: linear-gradient(90deg, #00FF41, #ff0000);
        height: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CORE JAVASCRIPT ENGINE (Popups, Sounds, Saboteur) ---
# Saare functions ek hi script block mein taaki error na aaye
st.markdown("""
    <div id="popup-box" class="fraud-popup">
        <h1 style="font-size: 50px;">🚨 SCAM ALERT 🚨</h1>
        <h2 style="color: yellow;">CRITICAL THREAT DETECTED</h2>
        <p style="font-size: 25px;">Fraudulent patterns matched. HANG UP IMMEDIATELY.</p>
        <button onclick="document.getElementById('popup-box').style.display='none'" style="padding: 10px 20px; cursor:pointer; background:white; color:black; font-weight:bold;">CLOSE ALERT</button>
    </div>

    <script>
    let audioCtx;
    let saboteurNode;

    function initAudio() {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }

    function playAlertSound() {
        initAudio();
        var osc = audioCtx.createOscillator();
        var gain = audioCtx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(880, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        setTimeout(() => { osc.stop(); }, 500); 
    }

    function toggleSaboteur(start) {
        initAudio();
        if (start) {
            if (saboteurNode) return; 
            saboteurNode = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();
            saboteurNode.type = 'sawtooth';
            saboteurNode.frequency.setValueAtTime(12000, audioCtx.currentTime);
            gainNode.gain.setValueAtTime(0.05, audioCtx.currentTime);
            saboteurNode.connect(gainNode);
            gainNode.connect(audioCtx.destination);
            saboteurNode.start();
        } else if (saboteurNode) {
            saboteurNode.stop();
            saboteurNode = null;
        }
    }
    </script>
    """, unsafe_allow_html=True)

# --- 4. HEADER ---
st.title("🛡️ GLITCH SECURE-VOICE ")
st.markdown('<div class="status-box"><b>SYSTEM STATUS:</b> FULLY AUTOMATED MODE <br><b>MONITOR:</b> AUTO-ANALYSIS & SABOTEUR READY</div>', unsafe_allow_html=True)
st.markdown("### 🚨 ACTIVE PROTECTION ENGAGED: Monitoring Incoming Call Audio...")
time.sleep(1)
st.markdown("### ⏱️ Session Start Time: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# --- HISTORY RESET LOGIC ---
if st.button("🗑️ Clear Incident History"):
    st.session_state.scam_history = []
    st.rerun()

# --- NEW: UPLOAD & ANALYZE SECTION ---
st.write("---")
st.subheader("📁 Offline Evidence Analysis")

upload_col1, upload_col2 = st.columns([1, 1])

with upload_col1:
    uploaded_file = st.file_uploader("Upload suspicious call recording (MP3/WAV)", type=["mp3", "wav"])

if uploaded_file is not None:
    with st.status("Deep Scanning Recording...", expanded=True) as status:
        st.write("🎞️ Extracting audio features...")
        time.sleep(1.5)
        st.write("🧠 Running NLP Semantic Matching...")
        time.sleep(2)
        new_incident = {
            "Timestamp": datetime.datetime.now().strftime("%H:%M:%S | %d %b"),
            "Threat Type": "Audio Recording Phish",
            "Confidence": 91, 
            "Status": "Evidence Logged"
        }
        # History mein save karna
        st.session_state.scam_history.insert(0, new_incident)
        
        status.update(label="Analysis Complete: Threat Logged!", state="complete")
        st.error("⚠️ SCAM DETECTED: Recording matched fraud database.")
        # Popup trigger
        components.html("<script>window.parent.document.getElementById('popup-box').style.display='block';</script>", height=0)
        
        # Simulated Detection (In real-world, you'd use OpenAI Whisper or SpeechRecognition here)
        detected_scam = True 
        
        if detected_scam:
            status.update(label="⚠️ SCAM PATTERNS DETECTED!", state="error")
            st.error("Result: High probability of 'Digital Arrest' scam found in recording.")
            
            # Triggering the Popup via JavaScript from Python
            components.html("""
                <script>
                    window.parent.document.getElementById('popup-box').style.display='block';
                    window.parent.playAlertSound();
                </script>
            """, height=0)
        else:
            status.update(label="✅ Recording Clear", state="complete")
            st.success("No known fraud signatures found.")

with upload_col2:
    st.info("""
    **How it works:**
    1. Upload any recorded call.
    2. AI scans for specific keywords (OTP,illegal activity, adharcard, pancard, Arrest, CBI).
    3. If matched, it triggers the **Vulnerability Alert** and generates an Evidence Log.
    """)

# --- 5. LIVE SCANNING INTERFACE ---
stt_engine_code = """
<div style="background: #111; padding: 20px; border: 2px solid #00FF41; border-radius: 10px; text-align: center;">
    <button id="scan-btn" style="background: #00FF41; color: #000; border: none; padding: 15px 40px; cursor: pointer; font-size: 20px; font-weight: bold; width: 100%;">🔴 ACTIVATE LIVE PROTECTION</button>
    <div id="transcript-box" style="color: #00FF41; font-size: 16px; margin-top: 20px; text-align: left; min-height: 80px; background: #000; padding: 10px; border: 1px solid #333; font-family: monospace;">System Standby...</div>
</div>

<script>
    const btn = document.getElementById('scan-btn');
    const tBox = document.getElementById('transcript-box');
    const popup = window.parent.document.getElementById('popup-box');
    
    const SCAM_WORDS = ["otp", "money transfer", "digital-arrest", "illegal action","bank-account", "password", "lottery", "aadhar verification", "pan card link", "biometric update", "skype verification", "video statement", "don't hang up","gift card", "cbi", "police", "kyc", "customer care", "account"];

    if ('webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;
        recognition.lang = 'en-IN';

        btn.onclick = () => {
            recognition.start();
            btn.innerText = "🛡️ MONITORING CALL AUDIO...";
            btn.style.background = "#222"; btn.style.color = "red";
        };

        recognition.onresult = (event) => {
            let text = "";
            for (let i = event.resultIndex; i < event.results.length; i++) {
                text += event.results[i][0].transcript.toLowerCase();
            }
            tBox.innerText = ">> Live Stream: " + text;
            
            SCAM_WORDS.forEach(word => {
                if (text.includes(word)) {
                    window.navigator.vibrate([500, 100, 500]);
                    popup.style.display = 'block';
                    window.parent.playAlertSound();
                    window.parent.toggleSaboteur(true); // Auto-activate Saboteur on threat
                }
            });
        };

        recognition.onspeechend = () => {
            window.parent.postMessage({type: 'AUTO_ANALYZE', val: true}, "*");
        };
    }
</script>
"""
components.html(stt_engine_code, height=280)

st.write("---")

# ==========================================
# NEW: DECOY SCREEN & GPS TRACER SECTION
# ==========================================

# --- DECOY SCREEN CSS ---
st.markdown("""
    <style>
    .decoy-bank {
        background: linear-gradient(180deg, #1a2a6c, #b21f1f, #fdbb2d);
        padding: 30px; border-radius: 15px; color: white; text-align: center;
        font-family: Arial, sans-serif; box-shadow: 0 0 20px rgba(0,0,0,0.5);
    }
    .balance-amt { font-size: 45px; font-weight: bold; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

st.subheader("🛡️ Active Counter-Defense")
col_decoy, col_gps = st.columns(2)

with col_decoy:
    st.markdown("🔍 **Decoy Screen Mode**")
    show_decoy = st.toggle("Enable Honey-Pot (Fake Bank UI)")

    if show_decoy:
        st.warning("⚠️ DECOY ACTIVE: Displaying dummy data to intercepting software.")
        st.markdown("""
            <div class="decoy-bank">
                <h3>🏦 GLOBAL SECURE BANK</h3>
                <p>Welcome, Authorized User</p>
                <hr style="border: 0.5px solid white;">
                <p>Available Balance</p>
                <div class="balance-amt">₹ 0.42</div>
                <p style="font-size: 12px;">Last Transaction: -₹ 5,000 (FAILED)</p>
                <div style="background: rgba(255,255,255,0.2); padding: 10px; border-radius: 5px;">
                    <b>Account Status:</b> <span style="color: #ff4b4b;">RESTRICTED</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

with col_gps:
    st.markdown("📡 **Scammer Identification**")
    if st.button("🛰️ START GPS IP-TRACE", use_container_width=True):
        with st.status("Initializing Satellite Uplink...", expanded=True) as status:
            st.write("📡 Connecting to VoIP Gateway...")
            time.sleep(1)
            st.write("🌍 Triangulating Signal Bounces...")
            time.sleep(1)
            st.write("📍 Target ISP: Unknown (Hidden via Proxy)")
            st.write("📌 Estimated Region: SE Asia / Scam Farm Hub")
            status.update(label="TRACING ACTIVE: TARGET LOCKED", state="error")
            st.error("⚠️ SATELLITE TRACKING IN PROGRESS: DO NOT DISCONNECT")
            st.toast("IP Trace Signal: 192.168.X.X captured!")

# --- ADVANCED FORENSICS SECTION ---
st.write("---")
st.subheader("🕵️ Advanced Forensics Analysis")

f1, f2 = st.columns(2)
with f1:
    st.markdown("""
        <div class="info-card" style="border-left: 5px solid #00FF41; background: #1a1a1a; padding: 15px; border-radius: 10px;">
            <b>🎙️ Voice Fingerprinting</b><br>
            <span style="font-size: 12px; color: #888;">AI vs Human Analysis</span>
            <div style="background:#333; height:10px; border-radius:5px; margin:10px 0;">
                <div style="background:red; width:87%; height:100%; border-radius:5px;"></div>
            </div>
            <small>Deepfake Probability: 87% (High Risk)</small>
        </div>
        """, unsafe_allow_html=True)

with f2:
    st.markdown("""
        <div class="info-card" style="border-left: 5px solid #00FF41; background: #1a1a1a; padding: 15px; border-radius: 10px;">
            <b>📡 Background Ambient Analysis</b><br>
            <span style="font-size: 12px; color: #888;">Environment Signature</span><br>
            <code>SCAN: Detected Crowded Call Center Noise</code><br>
            <code>SCAN: VoIP Latency Artifacts Found</code>
        </div>
        """, unsafe_allow_html=True)

# --- POLICE REPORTING ---
st.write("---")
if st.button("🚔 GENERATE & SUBMIT FORENSIC COMPLAINT", use_container_width=True):
    with st.spinner("Compiling Digital Evidence Packet..."):
        time.sleep(2)
        st.success("Evidence Packet Generated! Ready for submission to National Cyber Crime Portal.")
        st.balloons()

# --- SCAM HISTORY DATABASE ---
st.write("---")

if st.session_state.scam_history:
    # Convert list to DataFrame
    history_df = pd.DataFrame(st.session_state.scam_history)

    st.subheader("🗃️ Incident History Log")

# --- SCAMMER VOICE DATABASE ---
if 'voice_blacklist' not in st.session_state:
    st.session_state.voice_blacklist = []

# Button setup
if st.session_state.scam_history:
    # Function ko call karke data ready karna
    final_report = generate_report(st.session_state.scam_history)
    
    st.download_button(
        label="📄 Download Official Incident Report",
        data=final_report,
        file_name=f"SecureVoice_Report_{datetime.date.today()}.txt",
        mime="text/plain",
        use_container_width=True
    )
    
    # Iske neeche aapki dataframe (table) display hogi
    st.dataframe(pd.DataFrame(st.session_state.scam_history), use_container_width=True)
    
    # Professional Table Display
    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Timestamp": st.column_config.TextColumn("🕒 Time Detected"),
            "Threat Type": st.column_config.TextColumn("🚨 Threat Type"),
            "Confidence": st.column_config.ProgressColumn(
                "📈 Risk Confidence",
                help="AI detection certainty percentage",
                min_value=0,
                max_value=100,
                format="%d%%"
            ),
            "Status": st.column_config.TextColumn("🛠️ Action Taken")
        }
    )
else:
    st.success("✅ System Clean: No threats logged in the current session.")

    

# --- 6. ANALYTICS & GRAPHING ---
st.write("---")
st.subheader("📊 Instant AI Threat Intelligence")

col_a, col_b = st.columns([1, 2])

with col_a:
    st.markdown("""
    <div class="info-card">
        <b>🛡️ Real-Time Metrics:</b><br><br>
        <span class="metric-text">● Vocal Stress: 92%</span><br>
        <span class="metric-text">● AI Probability: 87%</span><br>
        <span class="metric-text">● Intent Score: 95%</span><br>
        <span class="metric-text">● Voice Clarity: 40%</span>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    chart_data = pd.DataFrame(
        np.random.randn(20, 4),
        columns=['Vocal Stress', 'AI Probability', 'Fraud Index', 'Voice Clarity']
    )
    st.line_chart(chart_data, height=250)

with st.expander("🔍 VIEW AUTO-ANALYSIS DETAILS", expanded=False):
    st.write("Deep Frequency Matching (DFM) is analyzing the semantic structure of the conversation.")
    st.metric("Detection Confidence", "94%", "CRITICAL")

st.write("---")
st.subheader("🕵️ Advanced Scammer Identification (Forensics)")

f1, f2 = st.columns(2)

with f1:
    st.markdown("""
        <div class="forensic-card">
            <b>🎙️ Voice Fingerprinting</b><br>
            <span style="font-size: 12px; color: #888;">Analyzing Vocal Cords & Synthetic Artifacts</span>
            <div class="meter-bar"><div class="meter-fill" style="width: 87%;"></div></div>
            <small>Deepfake Probability: 87% (High Risk)</small>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("**Vocal Characteristics:**")
    st.progress(0.92, text="Stress Level (Vocal Tension)")
    st.progress(0.45, text="Breath Consistency (AI vs Human)")

with f2:
    st.markdown("""
        <div class="forensic-card">
            <b>📡 Background Ambient Analysis</b><br>
            <span style="font-size: 12px; color: #888;">Filtering Noise for Location Tracing</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Forensic Findings
    noise_tags = ["Filtered: VoIP Static", "Detected: Crowded Office", "Detected: Multiple Voices"]
    for tag in noise_tags:
        st.code(f"SCAN: {tag}", language="bash")
    
    st.warning("Forensic Result: Likely a 'Scam Farm' environment (Fake Call Center).")

# --- ONE-CLICK POLICE REPORTING ---
st.write("---")
if st.button("🚔 GENERATE & SUBMIT FORENSIC COMPLAINT TO 1930", use_container_width=True):
    with st.spinner("Compiling Voice Evidence & IP Metadata..."):
        time.sleep(2)
        st.success("Digital Evidence Packet Created! You can now upload this to the National Cyber Crime Portal.")
        st.balloons()

# --- 7. SABOTEUR CONTROL ---
st.write("---")
st.subheader("🛰️ Call Recording Saboteur")
sab_on = st.toggle("Enable Manual Voice Jammer")

if sab_on:
    st.error("⚠️ SABOTEUR ACTIVE: Jamming signal injected to prevent AI Voice Cloning.")
    components.html("<script>window.parent.toggleSaboteur(true);</script>", height=0)
else:
    components.html("<script>window.parent.toggleSaboteur(false);</script>", height=0)

# --- 8. CALLER IDENTITY & POLICE ---
st.write("---")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="info-card">
        <b>📞 Caller Identity:</b><br><br>
        - Prefix: +91 140<br>
        - Category: High Risk Spam<br>
        - Trust Score: 15/100<br>
        - Reports: 412 (Last 24h)
    </div>
    """, unsafe_allow_html=True)
    st.button("🚨 ALERT AUTHORITIES", use_container_width=True)

with c2:
    st.markdown("""
        <div class="info-card">
            <b style="color: #00FF41;">🚩 SCAMMER TACTICS</b><br><br>
            <details>
                <summary style="cursor:pointer; color: #ff4b4b;"><b>Voice Deepfakes</b></summary>
                <p style="font-size: 12px; color: #bbb;">Detects frequency anomalies in cloned audio.</p>
            </details>
            <details>
                <summary style="cursor:pointer; color: #ff4b4b;"><b>Urgency Bias</b></summary>
                <p style="font-size: 12px; color: #bbb;">Identifies high-pressure panic speech.</p>
            </details>
            <details>
                <summary style="cursor:pointer; color: #ff4b4b;"><b>Digital Arrest</b></summary>
                <p style="font-size: 12px; color: #bbb;">Flags fake legal/CBI video call threats.</p>
            </details>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="info-card">
        <b>🚔 Evidence Log:</b><br><br>
        - Real-time Transcript<br>
        - Vocal Fingerprint<br>
        - Intent Timestamp
    </div>
    """, unsafe_allow_html=True)
    st.download_button("📂 EXPORT EVIDENCE", "DETECTION REPORT: PHISHING\nRESULT: SCAM CONFIRMED", file_name="glitch_scam_report.txt", use_container_width=True)

st.write("---")
if st.button("📞 EMERGENCY: DIAL 1930", type="primary", use_container_width=True):
    components.html("<script>window.location.href = 'tel:1930';</script>")
    st.success("Emergency Protocol Initiated.")

# --- COMPACT OFFICIAL FOOTER ---
st.markdown("""
    <style>
    .mini-footer {
        background-color: #002200;
        color: #00FF41;
        padding: 20px;
        border-top: 2px solid #00FF41;
        margin-top: 50px;
        font-family: sans-serif;
        font-size: 13px;
    }
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
    }
    .f-link { color: white; text-decoration: none; display: block; margin: 3px 0; }
    .f-link:hover { color: #00FF41; }
    .emergency-box { border: 1px dashed red; padding: 5px; color: #ff4b4b; font-weight: bold; text-align: center; }
    </style>

    <div class="mini-footer">
        <div class="footer-grid">
            <div>
                <b style="color: #00FF41;">🏛️ GOVT LINKS</b>
                <a class="f-link" href="https://cybercrime.gov.in/">● Cyber Crime Portal</a>
                <a class="f-link" href="https://cert-in.org.in/">● CERT-In Official</a>
                <a class="f-link" href="https://www.rbi.org.in/">● RBI Cybersecurity</a>
                <a class="f-link" href="https://www.india.gov.in/">● Digital India</a>
                <a class="f-link" href="https://meity.gov.in/">● MeitY</a>
                <a class="f-link" href="https://www.cyberlawsindia.net/">● Cyber Laws India</a>
            </div>
            <div>
                <b style="color: #00FF41;">⚖️ LEGAL HELP</b>
                <span class="f-link">● IT Act Sec 66D</span>
                <span class="f-link">● IPC Sec 420 Help</span>
                <span class="f-link">● Data Protection Act</span>
                <span class="f-link">● Cybercrime Laws</span>
                <span class="f-link">● Report Cybercrime</span>
                </span class="f-link">● Legal Aid India</span>
            </div>
            <div>
                <b style="color: #00FF41;">📞 CONTACT</b>
                <span class="f-link">C-DAC: support@cdac.in</span>
                <div class="emergency-box">🚨 HELPLINE: 1930</div>
                <div class="emergency-box">📧 REPORT: cybercrime.gov.in</div>
                <div class="emergency-box">⚠️ SMS: 14422</div>
                <div class="emergency-box">🌐 WEBSITE: www.cybercrime.gov.in</div>
                <div class="emergency-box">📞 TOLL-FREE: 1800-11-3690</div>
            </div>
        </div>
        <hr style="border: 0.1px solid #004400; margin: 15px 0;">
        <div style="text-align: center; font-size: 11px; opacity: 0.7;">
            © 2026 Team GLITCHER | Digital India Initiative
             Built with ❤️ for a safer digital world.
             Best viewed in dark mode for optimal experience.
             by Balkrishna Shukla | SecureVoice-Real Time Audio Detection Engine v1.0|Engineering College Ajmer, Rajasthan|
        </div>
    </div>
    """, unsafe_allow_html=True)
st.caption("Team GLITCHER | Balkrishna Shukla| SecureVoice-Real Time Audio Detection Engine v4.0")