# Retail Security Knife Detection Using Azure Custom Vision AI

## Project Overview

Retail theft and violent incidents pose serious safety risks to both customers and staff. Rapid detection of weapons like knives in surveillance footage can help security teams respond faster and prevent harm.

This project leverages **Microsoft Azure Custom Vision AI** to build and deploy a real-time knife detection system on retail surveillance videos, enhancing security monitoring through AI-powered alerts.

---

## Features

- Custom-trained object detection model to identify knives in video frames.
- Reasonable precision and recall to reduce false alarms.
- Cloud-based deployment using Azure Custom Vision for scalability and ease of use.
- Real-time alerts via text SMS if any potential threat encountered.

---

## Approach

1. **Data Collection & Annotation:**  
   Gathered a diverse dataset of surveillance video frames containing knives in various lighting and angles. Annotated knife locations using Azure Custom Vision’s labeling tool.

2. **Model Training:**  
   Used Azure Custom Vision’s object detection service to train a deep learning model tailored to the knife detection task. Leveraged transfer learning and iterative model refinement to improve accuracy.

3. **Deployment & Integration:**  
   Exported the trained model and integrated it into a video processing pipeline that analyzes recorded surveillance feeds. The system flags potential knife detections and generates real-time alerts.

---
