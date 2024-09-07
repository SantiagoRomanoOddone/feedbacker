# Feedbacker

## Project Overview

Feedbacker is designed to analyze feedback and generate actionable recommendations using **Natural Language Processing (NLP)** and **Reinforcement Learning (RL)**. The system processes feedback, identifies key topics, and suggests actions to improve  engagement. Over time, the system learns which actions are most effective, with input from human experts.

## Key Components

1. **Data Collection Agent**: Collects feedback from sources like surveys or emails.
2. **Sentiment Analysis Agent**: Classifies feedback sentiment (positive, negative, or neutral) using NLP.
3. **Topic Analysis Agent**: Extracts key issues or topics from feedback (e.g., “processo de compra”).
4. **Current State Agent**: Retrieves relevant process documentation related to identified issues.
5. **Recommendation Agent (RL)**: Suggests actions to address issues and learns from their outcomes using RL.
6. **Human-in-the-loop**: Allows human intervention to refine actions and improve the learning process.
7. **Control Agent**: Tracks the effectiveness of implemented actions and monitors progress.

## How it Works

1. **Collect Feedback**: Feedback is gathered and analyzed for sentiment and topics.
2. **Current State**: The system looks at relevant process documentation.
3. **Recommend Actions**: The RL agent suggests actions based on feedback and learns from outcomes.
4. **Human Review**: A human expert can review and modify action suggestions.
5. **Monitor Success**: The Control Agent checks if the actions led to improvements.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SantiagoRomanoOddone/feedbacker.git
