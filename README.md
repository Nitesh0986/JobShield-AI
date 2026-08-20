# JobShield-AI
AI-powered recruitment scam detection platform that analyzes job postings, recruiter details, URLs, and suspicious signals to provide an explainable scam risk score.
# 🛡️ JobShield AI

### AI-Powered Fake Job & Recruitment Scam Detection System

> **Don't just trust a job. Let JobShield investigate it.**

JobShield AI is an AI-powered recruitment scam detection platform designed to help students, freshers, and job seekers identify potentially fraudulent job opportunities before they apply, share sensitive information, or make payments.

Instead of simply classifying a job as **Fake** or **Genuine**, JobShield AI analyzes multiple risk signals and provides a **Scam Risk Score, evidence-based explanation, and safety recommendations**.

---

## 🚨 Problem

Online recruitment has become increasingly vulnerable to:

* Fake job postings
* Impersonated recruiters
* Fraudulent offer letters
* Fake company websites
* Registration/processing fee scams
* Suspicious recruiter emails
* Phishing links
* Unrealistic job offers

Students and freshers are particularly vulnerable because they may not have enough experience to identify these warning signs.

The key problem is not only:

> **“Is this job fake?”**

but also:

> **“Why does this job look suspicious?”**

JobShield AI aims to answer both.

---

## 💡 Our Solution

JobShield AI treats recruitment verification as an **investigation rather than a simple classification problem**.

Users can provide:

* Job description
* Recruiter email
* Company website / URL
* Offer-letter content

The system analyzes multiple signals using:

```text
Job Information
       ↓
NLP / ML Analysis
       +
Rule-Based Risk Detection
       +
Email & Domain Analysis
       ↓
Risk Scoring Engine
       ↓
Scam Risk Score
       ↓
Evidence & Explanation
       ↓
Safety Recommendation
```

The final result provides an understandable risk assessment instead of a simple **Fake/Real** label.

---

# ⭐ Key Features

## 🎯 Scam Risk Score

Provides a risk percentage and category:

* 🟢 Low Risk
* 🟡 Medium Risk
* 🔴 High Risk

Example:

```text
SCAM RISK: 87%
RISK LEVEL: HIGH
```

---

## 🔍 Evidence-Based Detection

JobShield AI explains the signals responsible for the risk score.

Example:

```text
Detected Red Flags:

🔴 Recruiter email does not match company domain
🔴 Payment request detected
🔴 Suspicious URL
🟠 Unrealistic salary claim
🟠 Urgency-based language
```

---

## 📧 Recruiter & Email Analysis

Analyzes recruiter information and identifies potential inconsistencies between:

* Recruiter identity
* Claimed organization
* Email domain
* Contact information

---

## 🌐 Domain & URL Analysis

Analyzes submitted company/job URLs for suspicious characteristics and inconsistencies.

---

## 🧠 NLP / ML Scam Detection

Analyzes job descriptions and recruitment messages for:

* Suspicious language
* Unrealistic promises
* Manipulation patterns
* Payment-related signals
* Other recruitment scam indicators

---

## 💬 Explainable AI

Instead of providing only a prediction, JobShield AI converts detected signals into a human-readable explanation.

Example:

> **Why is this opportunity risky?**
>
> The opportunity has been classified as high risk because multiple independent indicators were detected, including a recruiter-domain mismatch and a request for payment.

---

## 🛡️ Safety Recommendations

The system provides actionable guidance such as:

* Verify the employer through its official website
* Avoid paying recruitment fees
* Do not share sensitive financial information
* Verify recruiter identity before proceeding
* Cross-check the job with official career pages

---

# 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │      USER       │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ React Frontend  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ FastAPI Backend │
                    └────────┬────────┘
                             ↓
             ┌───────────────────────────────┐
             │ JobShield Investigation Engine│
             ├───────────────────────────────┤
             │                               │
             │  NLP / ML Analysis            │
             │  Rule-Based Detection         │
             │  Email Analysis               │
             │  Domain / URL Analysis        │
             │                               │
             └──────────────┬────────────────┘
                            ↓
                   ┌──────────────────┐
                   │ Risk Scoring     │
                   │ Engine           │
                   └────────┬─────────┘
                            ↓
                   ┌──────────────────┐
                   │ AI Explanation   │
                   │ & Recommendation  │
                   └────────┬─────────┘
                            ↓
                   ┌──────────────────┐
                   │ Evidence         │
                   │ Dashboard        │
                   └──────────────────┘
```

---

# 🔥 What Makes JobShield Different?

A conventional system may simply produce:

```text
Fake Job — 91%
```

JobShield AI aims to provide:

```text
HIGH RISK — 91%

Evidence:
✓ Recruiter identity mismatch
✓ Payment request detected
✓ Suspicious URL
✓ Unrealistic compensation claim
✓ Urgency-based language

Recommendation:
Verify the employer through its official career channel
before proceeding.
```

### Core USP

> **JobShield AI is not just a fake-job classifier; it is an AI-powered recruitment scam investigator that provides evidence behind its decision.**

---

# 🧠 Technology Stack

### Frontend

* React.js
* JavaScript
* HTML5
* CSS3
* Tailwind CSS

### Backend

* Python
* FastAPI
* REST APIs

### AI / Machine Learning

* Python
* Scikit-learn
* NLP
* Pandas
* NumPy

### AI Explanation

* Gemini API / LLM

### Database

* MongoDB / Firebase

### Supporting Technologies

* Regular Expressions
* URL / Domain Analysis
* Git
* GitHub

### Deployment

* Cloud Deployment

> The final implementation will use only the technologies required for a reliable MVP.

---

# 📂 Project Structure

```text
JobShield-AI/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── utils/
│   │
│   └── requirements.txt
│
├── ml/
│   ├── data/
│   ├── models/
│   ├── preprocessing/
│   └── training/
│
├── docs/
│
├── .gitignore
├── README.md
└── LICENSE
```

---

# 👥 Team

* **Riyanshika** — Frontend & Full Stack
* **Nitesh Barnwal** — AI/ML & NLP

---

# 🎯 Hackathon

## OmniKon National Hackathon 2026

**Problem Statement ID:** `Omni_CyberTech_10`

**Project:** JobShield AI

**Domain:** Cybersecurity / AI / Fraud Detection

---

# 🚀 Implementation Roadmap

### Phase 1 — Research & Dataset

* Study recruitment scam patterns
* Collect legitimate and suspicious job examples
* Identify important scam indicators
* Define risk-scoring methodology

### Phase 2 — AI/ML Engine

* Text preprocessing
* Feature extraction
* NLP analysis
* Train scam detection model
* Evaluate model performance

### Phase 3 — Investigation Engine

* Rule-based red-flag detection
* Recruiter/email consistency checks
* URL/domain analysis
* Evidence generation

### Phase 4 — AI Explanation

* Integrate LLM
* Generate human-readable explanations
* Generate safety recommendations

### Phase 5 — Full-Stack Integration

* Build React interface
* Develop FastAPI endpoints
* Connect AI engine
* Build risk-analysis dashboard

### Phase 6 — Testing & Deployment

* Test legitimate and suspicious cases
* Improve false-positive handling
* Deploy prototype
* Prepare final demonstration

---

# 📊 Expected Output

For every submitted opportunity, JobShield AI aims to generate:

```text
┌──────────────────────────────────────┐
│         JOBSHIELD ANALYSIS           │
├──────────────────────────────────────┤
│ Scam Risk:       87%                 │
│ Risk Level:      HIGH                │
│                                      │
│ Red Flags:                           │
│ 🔴 Email mismatch                    │
│ 🔴 Payment request                   │
│ 🟠 Suspicious URL                    │
│ 🟠 Unrealistic salary                │
│                                      │
│ AI Explanation:                      │
│ Multiple independent risk indicators │
│ suggest this opportunity should be   │
│ verified before proceeding.          │
│                                      │
│ Recommendation:                      │
│ Verify through the official company  │
│ career channel.                      │
└──────────────────────────────────────┘
```

---

# 🌱 Future Scope

JobShield AI can be extended with:

* 🌐 Browser extension for real-time job checking
* 💼 Job portal integration
* 💬 WhatsApp / Telegram message analysis
* 📄 Offer-letter verification
* 🏢 Company identity verification
* 🔄 Continuous scam-pattern learning
* 📱 Mobile application
* 📊 Organization-level fraud analytics

---

# ⚠️ Disclaimer

JobShield AI provides a risk assessment based on available signals.

It should **not** be treated as an absolute determination that an organization or job opportunity is legitimate or fraudulent.

Users should independently verify important employment opportunities through official company channels.

---

# 🌟 Vision

> **Make online recruitment safer by turning hidden scam signals into clear, understandable evidence.**

### 🛡️ JobShield AI

**Investigate before you apply.**
