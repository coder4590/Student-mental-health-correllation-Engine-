# 🧠 MindGuard — Student Mental Health Correlation Engine

> *"I'm fine."*

That's what you said when your friend asked. That's what you typed in the group chat. That's what you told yourself this morning.

But at 3 AM, staring at the ceiling, you know you're not fine. The pressure is crushing. Sleep isn't coming. Social media scrolls don't help anymore. You're not alone in this — but it feels like you are.

What if there was something that could listen? Not judge. Not prescribe. Just listen, analyze, and tell you: "Here's what might be going on. Here's what you can do. And here's a number to call if it gets worse."

That's MindGuard.

---

## ❤️ What This Actually Is

MindGuard is a full-stack AI system that takes a 19-question assessment covering sleep, academic pressure, financial stress, social media use, physical activity, and more. It runs a trained ML model to predict depression risk based on real student data. It generates a personalized report feature by feature, explaining what's helping and what's hurting your mental health. It provides an AI companion chatbot trained to respond to depression, anxiety, loneliness, academic stress, and crisis situations. And it offers one-click crisis support with direct access to Kaan Pete Roi and National Mental Health helplines.

It's not a diagnosis. It's a conversation starter. With yourself.

---

## 📊 The Data — And Its Brutal Limitation

| What We Had | What It Means |
|---|---|
| 496 student records | Tiny. In ML terms, almost microscopic. |
| 63 original features | Only 20 kept after cleaning. 43 were individual scale items that would cause data leakage. |
| Target variable | PHQ-9 depression severity converted to binary (At Risk / Not At Risk) |

Why binary? With 496 rows and a multi-class target, the model couldn't learn meaningful patterns for 5 severity levels. Switching to binary was the honest choice — the data simply couldn't support more.

Did we try other datasets? Yes. We searched UCI, Kaggle, government repositories. The CDC YRBS has 278k rows but requires formal request. WHO GSHS has aggregated data, not individual records. We took what was available, acknowledged the limitation, and built the best system the data could support.

---

## 🧪 The Model — Finding Signal in Small Data

| Algorithm | Best Score | Verdict |
|---|---|---|
| Logistic Regression | 0.68 | Too simple. Missed non-linear patterns. |
| XGBoost | 0.75 | Good, but small data limited boosting potential. |
| Random Forest | 0.79 | Winner. Bagging handles small data better than boosting. |

Why Random Forest won: With 496 rows, boosting amplifies noise. Bagging averages it out. The result is a model that correctly identifies at-risk students 79% of the time using only pre-diagnostic, screening-level features.

Is 79% good enough? For a screening tool with 496 training examples? Yes. It's better than random guessing and close to validated clinical screening instruments. It's honest. Nothing was leaked. Nothing was faked.

---

## 🏗️ The Pipeline — What We Actually Built

**Data Cleaning:** Remove 43 leakage features. Fix typos in categoricals. Handle chronic illness column. Create binary target from PHQ-9 severity score.

**Feature Engineering:** Extract chronic illness values from Bangla/English mixed column. Select final 19 features covering demographics, academic life, living conditions, finances, lifestyle, and mental health indicators.

**ML Pipeline:** ColumnTransformer with StandardScaler for numeric features and OneHotEncoder with handle_unknown='ignore' for categorical features. RandomForestClassifier with tuned n_estimators and class_weight='balanced' to handle class imbalance.

**API Layer:** FastAPI with three working endpoints. /predict accepts the 19-feature form and returns depression risk with personalized NLP-generated report. /chat accepts free-text messages and returns therapeutic responses from the knowledge base. /health returns system status.

**NLP Engine:** Four dedicated Python modules. prompts.py contains 12 categories of therapeutic responses. nlp_engine.py generates full personalized reports by mapping each feature value to its corresponding insight. chatbot.py provides intelligent pattern matching with fuzzy scoring, crisis detection, typo handling, and nonsense recovery. mental_health_knowledge.py stores 500+ query patterns across 7 major categories including depression symptoms, suicidal ideation, self-harm, academic stress, loneliness, anxiety, and relationship issues.

**Frontend:** Three HTML pages with a unified dark glassmorphism theme. Landing page with gradient accents and floating cards. Assessment page with 19-field form, progress bar, and dynamic results display. Chatbot page with sidebar topics, message bubbles, typing indicator, suggested prompts, and persistent crisis button.

**Containerization:** Docker Compose with two services. FastAPI backend container with Python 3.11 and all dependencies. Nginx frontend container serving static files. One command to build and run everything.

---

## 🤖 The AI Chatbot — From Scratch, No External API

The chatbot is not connected to OpenAI or any external LLM. Every response was written based on clinical knowledge, crisis intervention protocols, and empathetic communication principles.

| Category | Patterns | What It Handles |
|---|---|---|
| Depression Symptoms | 50+ | Emptiness, worthlessness, hopelessness, crying, fatigue, anhedonia |
| Suicide & Crisis | 30+ | Active ideation, passive ideation, self-harm urges |
| Academic Stress | 20+ | Can't study, failing, pressure, overwhelm |
| Loneliness | 15+ | No friends, isolation, no one understands |
| Anxiety | 15+ | Racing thoughts, panic, constant worry |
| Relationships & Family | 20+ | Breakups, toxic family, pressure |
| Nonsense / Typos | 25+ | Keyboard smashing, misspellings |
| Crisis Detection | 15+ keywords | Immediate helpline response |

How it works: Pattern matching with fuzzy scoring. Crisis keywords get priority. Typos get gentle correction. Nonsense gets a caring "Are you okay?" prompt. Vague messages get help identifying emotions through physical sensations.

Built from scratch. No shortcuts.

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| Data | Pandas, NumPy |
| ML | Scikit-learn (RandomForestClassifier, Pipeline, ColumnTransformer, StandardScaler, OneHotEncoder) |
| API | FastAPI, Pydantic, Uvicorn |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Container | Docker, Docker Compose, Nginx |
| Version Control | Git, GitHub |

---

## 🚀 How To Run

```bash
git clone https://github.com/yourusername/mindguard.git
cd mindguard
docker compose up --build# 🧠 MindGuard — Student Mental Health Correlation Engine

> *"I'm fine."*

That's what you said when your friend asked. That's what you typed in the group chat. That's what you told yourself this morning.

But at 3 AM, staring at the ceiling, you know you're not fine. The pressure is crushing. Sleep isn't coming. Social media scrolls don't help anymore. You're not alone in this — but it feels like you are.

What if there was something that could listen? Not judge. Not prescribe. Just listen, analyze, and tell you: "Here's what might be going on. Here's what you can do. And here's a number to call if it gets worse."

That's MindGuard.

---

## ❤️ What This Actually Is

MindGuard is a full-stack AI system that takes a 19-question assessment covering sleep, academic pressure, financial stress, social media use, physical activity, and more. It runs a trained ML model to predict depression risk based on real student data. It generates a personalized report feature by feature, explaining what's helping and what's hurting your mental health. It provides an AI companion chatbot trained to respond to depression, anxiety, loneliness, academic stress, and crisis situations. And it offers one-click crisis support with direct access to Kaan Pete Roi and National Mental Health helplines.

It's not a diagnosis. It's a conversation starter. With yourself.

---

## 📊 The Data — And Its Brutal Limitation

| What We Had | What It Means |
|---|---|
| 496 student records | Tiny. In ML terms, almost microscopic. |
| 63 original features | Only 20 kept after cleaning. 43 were individual scale items that would cause data leakage. |
| Target variable | PHQ-9 depression severity converted to binary (At Risk / Not At Risk) |

Why binary? With 496 rows and a multi-class target, the model couldn't learn meaningful patterns for 5 severity levels. Switching to binary was the honest choice — the data simply couldn't support more.

Did we try other datasets? Yes. We searched UCI, Kaggle, government repositories. The CDC YRBS has 278k rows but requires formal request. WHO GSHS has aggregated data, not individual records. We took what was available, acknowledged the limitation, and built the best system the data could support.

---

## 🧪 The Model — Finding Signal in Small Data

| Algorithm | Best Score | Verdict |
|---|---|---|
| Logistic Regression | 0.68 | Too simple. Missed non-linear patterns. |
| XGBoost | 0.75 | Good, but small data limited boosting potential. |
| Random Forest | 0.79 | Winner. Bagging handles small data better than boosting. |

Why Random Forest won: With 496 rows, boosting amplifies noise. Bagging averages it out. The result is a model that correctly identifies at-risk students 79% of the time using only pre-diagnostic, screening-level features.

Is 79% good enough? For a screening tool with 496 training examples? Yes. It's better than random guessing and close to validated clinical screening instruments. It's honest. Nothing was leaked. Nothing was faked.

---

## 🏗️ The Pipeline — What We Actually Built

**Data Cleaning:** Remove 43 leakage features. Fix typos in categoricals. Handle chronic illness column. Create binary target from PHQ-9 severity score.

**Feature Engineering:** Extract chronic illness values from Bangla/English mixed column. Select final 19 features covering demographics, academic life, living conditions, finances, lifestyle, and mental health indicators.

**ML Pipeline:** ColumnTransformer with StandardScaler for numeric features and OneHotEncoder with handle_unknown='ignore' for categorical features. RandomForestClassifier with tuned n_estimators and class_weight='balanced' to handle class imbalance.

**API Layer:** FastAPI with three working endpoints. /predict accepts the 19-feature form and returns depression risk with personalized NLP-generated report. /chat accepts free-text messages and returns therapeutic responses from the knowledge base. /health returns system status.

**NLP Engine:** Four dedicated Python modules. prompts.py contains 12 categories of therapeutic responses. nlp_engine.py generates full personalized reports by mapping each feature value to its corresponding insight. chatbot.py provides intelligent pattern matching with fuzzy scoring, crisis detection, typo handling, and nonsense recovery. mental_health_knowledge.py stores 500+ query patterns across 7 major categories including depression symptoms, suicidal ideation, self-harm, academic stress, loneliness, anxiety, and relationship issues.

**Frontend:** Three HTML pages with a unified dark glassmorphism theme. Landing page with gradient accents and floating cards. Assessment page with 19-field form, progress bar, and dynamic results display. Chatbot page with sidebar topics, message bubbles, typing indicator, suggested prompts, and persistent crisis button.

**Containerization:** Docker Compose with two services. FastAPI backend container with Python 3.11 and all dependencies. Nginx frontend container serving static files. One command to build and run everything.

---

## 🤖 The AI Chatbot — From Scratch, No External API

The chatbot is not connected to OpenAI or any external LLM. Every response was written based on clinical knowledge, crisis intervention protocols, and empathetic communication principles.

| Category | Patterns | What It Handles |
|---|---|---|
| Depression Symptoms | 50+ | Emptiness, worthlessness, hopelessness, crying, fatigue, anhedonia |
| Suicide & Crisis | 30+ | Active ideation, passive ideation, self-harm urges |
| Academic Stress | 20+ | Can't study, failing, pressure, overwhelm |
| Loneliness | 15+ | No friends, isolation, no one understands |
| Anxiety | 15+ | Racing thoughts, panic, constant worry |
| Relationships & Family | 20+ | Breakups, toxic family, pressure |
| Nonsense / Typos | 25+ | Keyboard smashing, misspellings |
| Crisis Detection | 15+ keywords | Immediate helpline response |

How it works: Pattern matching with fuzzy scoring. Crisis keywords get priority. Typos get gentle correction. Nonsense gets a caring "Are you okay?" prompt. Vague messages get help identifying emotions through physical sensations.

Built from scratch. No shortcuts.

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| Data | Pandas, NumPy |
| ML | Scikit-learn (RandomForestClassifier, Pipeline, ColumnTransformer, StandardScaler, OneHotEncoder) |
| API | FastAPI, Pydantic, Uvicorn |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Container | Docker, Docker Compose, Nginx |
| Version Control | Git, GitHub |

---

## 🚀 How To Run

```bash
git clone https://github.com/yourusername/mindguard.git
cd mindguard
docker compose up --build
