MemoryGuard

AI-Powered Early Cognitive Decline Risk Stratification and Longitudinal Decision Support

MemoryGuard is an AI-assisted healthcare system designed to help identify and track possible cognitive changes over time.

Instead of focusing only on a single risk score, MemoryGuard analyzes previous and current assessments to understand how a person's cognitive profile is changing.

MemoryGuard is a decision-support and risk-stratification system. It does not provide a medical diagnosis or replace healthcare professionals.

Problem Statement

Cognitive decline associated with Alzheimer's disease can develop gradually, making early changes difficult to notice.

A single clinical assessment provides only a snapshot of a person's condition and may not clearly show how their cognitive abilities are changing over time.

Existing prediction systems may provide a risk score without clearly showing previous assessment trends, important contributing factors, or useful next steps.

MemoryGuard addresses this problem by analyzing patient information over time and presenting meaningful changes in an easy-to-understand format.

Proposed Solution

MemoryGuard uses machine learning to analyze patient demographic and cognitive assessment information.

The system provides:

Cognitive decline risk stratification

Previous vs. current assessment comparison

Important contributing factors

Risk trajectory and changes over time

Cognitive Digital Timeline

Supportive lifestyle suggestions

Clinical follow-up prompts

Unique Feature: Personal Cognitive Fingerprint

The main innovation of MemoryGuard is the Personal Cognitive Fingerprint.

Instead of looking only at a patient's current score, MemoryGuard creates a baseline profile of the individual's cognitive performance and compares future assessments with their own previous baseline.

How It Works

Patient Assessment
        ↓
Personal Cognitive Fingerprint
        ↓
Personal Baseline
        ↓
New Assessment
        ↓
Compare With Previous Baseline
        ↓
Detect Meaningful Changes
        ↓
Identify What Changed
        ↓
Risk and Trend Analysis
        ↓
Clinical Follow-up Support

The Personal Cognitive Fingerprint can represent areas such as:

Memory

Attention

Executive function

Cognitive performance

Functional ability

Example

Previous assessment:

Memory              80
Attention           75
Executive Function  70
Daily Function      85

Later assessment:

Memory              72
Attention           73
Executive Function  62
Daily Function      82

MemoryGuard compares the new assessment with the individual's previous baseline and highlights the areas where meaningful changes occurred.

Example Output

Meaningful change detected.

Main areas of change:
- Executive function
- Memory

Suggested action:
Consider clinical review.

This allows healthcare professionals to quickly understand what changed, rather than seeing only a single risk score.

What Makes MemoryGuard Different?

Traditional Approach

Patient Data
     ↓
AI Model
     ↓
Risk Score

MemoryGuard

Previous Assessments
        ↓
Personal Cognitive Fingerprint
        ↓
Personal Baseline
        ↓
New Assessment
        ↓
Change Detection
        ↓
"What Changed?"
        ↓
Risk and Trend Analysis
        ↓
Clinical Follow-up Support

Our Key Idea

Our focus is not just prediction, but understanding the patient's change over time.

Key Features

1. AI-Based Risk Stratification

The system analyzes cognitive and functional assessment data to classify cognitive decline risk.

2. Personal Cognitive Fingerprint

Creates an individual's baseline cognitive profile.

3. Change Detection

Compares new assessments with previous assessments to identify meaningful changes.

4. Cognitive Digital Timeline

Displays previous and current assessments using easy-to-understand charts.

5. "What Changed?" Analysis

Highlights the areas that changed between assessments.

6. Contributing Factors

Shows important factors that influence the risk assessment.

7. Risk Trajectory

Helps visualize how the estimated risk changes over time.

8. Supportive Guidance

Provides general healthy lifestyle suggestions such as:

Regular physical activity

Healthy sleep

Cognitive activities

Social engagement

Healthy daily habits

9. Clinical Follow-up Support

Provides prompts that may help healthcare professionals decide when additional clinical review should be considered.

How MemoryGuard Works

Patient Information
        ↓
Data Collection
        ↓
Data Preprocessing
        ↓
AI / Machine Learning Analysis
        ↓
Risk Stratification
        ↓
Personal Cognitive Fingerprint
        ↓
Previous vs. Current Comparison
        ↓
Change Detection
        ↓
Cognitive Digital Timeline
        ↓
Contributing Factors
        ↓
Supportive Guidance
        ↓
Clinical Follow-up Support

AI Technology

MemoryGuard uses:

Python

Machine Learning

Pandas

NumPy

Scikit-learn

Streamlit

Data Visualization

The machine-learning model analyzes patterns in cognitive and functional assessment data to support risk stratification.

Dataset

The project uses cognitive assessment data containing demographic, cognitive, and functional assessment information.

Example attributes include:

Age

Sex

Cognitive assessment scores

Memory-related scores

Functional assessment scores

Previous assessment information

Note: Sensitive or personally identifiable patient information should not be uploaded to this public repository.

Intended Users

Healthcare Professionals

MemoryGuard can help healthcare professionals:

Review assessment information

Compare previous and current assessments

Identify changes over time

Understand contributing factors

Support follow-up decisions

Patients

Patients can benefit from clearer visualization of changes in their cognitive assessment history.

Caregivers and Families

The system can help communicate changes and trends more clearly.

Safety and Limitations

MemoryGuard is not a diagnostic system.

It does not replace:

Medical diagnosis

Clinical examination

Healthcare professionals

Professional medical judgment

AI predictions may contain errors. Therefore, the system should be used as supportive information and not as the sole basis for medical decisions.

Lifestyle suggestions are general supportive recommendations and are not presented as medical treatment or a guarantee of preventing disease.

Project Workflow

                    MEMORYGUARD
                         |
                         ↓
                Patient Information
                         |
                         ↓
                 Data Preprocessing
                         |
                         ↓
                  AI Risk Analysis
                         |
             +-----------+-----------+
             ↓                       ↓
      Risk Stratification     Personal Cognitive
                                  Fingerprint
             |                       |
             +-----------+-----------+
                         ↓
                  Change Detection
                         ↓
                    What Changed?
                         ↓
                Cognitive Timeline
                         ↓
                Risk and Trend Analysis
                         ↓
             Clinical Follow-up Support

Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/MemoryGuard.git

Move into the project folder:

cd MemoryGuard

Install the required packages:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

Project Structure

MemoryGuard/
|
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
|
├── data/
|   └── memoryguard_dataset.csv
|
├── model/
|   └── memoryguard_model.pkl
|
├── assets/
|   └── screenshots/
|
└── docs/
    ├── problem_statement.pdf
    └── presentation.pdf

Team

CODE CREW

Team Members

Monica N. G.

Janani T. S.

Kanimozhi J.

Domain

Healthcare

Hackathon

Innovision 2.0

Our Innovation

MemoryGuard goes beyond a single prediction by creating a Personal Cognitive Fingerprint and detecting meaningful changes from an individual's own baseline over time.

Our goal is to help healthcare professionals understand:

"What changed?"

rather than simply asking:

"What is the current risk?"

Disclaimer

MemoryGuard is an AI-assisted research and prototype project developed for the Innovision 2.0 hackathon.

It is intended for decision-support and educational/prototype purposes and should not be used as a substitute for professional medical diagnosis or treatment.
