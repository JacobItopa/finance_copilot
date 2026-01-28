# SME Financial Intelligence Copilot

A tailored financial assistant for Small and Medium Enterprises (SMEs) to automate transaction categorization and generate financial insights.

## Features
- **Transaction Upload**: Upload CSV files containing financial transactions.
- **Auto-Categorization**: Automatically categorizes transactions using Rule-Based and LLM-Based logic.
- **Contextual Awareness**: Uses RAG (Retrieval-Augmented Generation) to understand company-specific context for better categorization.
- **Financial Summary**: Generates a financial summary including Total Income, Total Expense, and Net Cash Flow.
- **Actionable Insights**:
    - **Anomaly Detection**: Flags transactions that deviate significantly from category averages.
    - **Cash Runway**: Estimates how long the business can survive based on critical burn rate.
- **Smart Recommendations**: translates financial insights into clear, actionable advice (e.g., "Reduce discretionary spending").
- **Daily Digest**: Aggregates insights, key metrics, and alerts into a daily report.
- **Email Notifications**: Sends daily financial digests via email using Resend.
- **Database Storage**: Stores all transactions in a SQLite database.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/JacobItopa/finance_copilot.git
    cd finance_copilot
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables**:
    Create a `.env` file in the root directory and add your OpenAI API Key:
    ```
    OPENAI_API_KEY=your_api_key_here
    RESEND_API_KEY=your_resend_api_key
    SENDER_EMAIL=your_verified_sender_email
    ```

4.  **Initialize Database**:
    ```bash
    python -m app.db.init_db
    ```

5.  **Run the Application**:
    ```bash
    uvicorn app.main:app --reload
    ```

## API Endpoints
- `POST /upload/`: Upload a CSV file for processing.
- `GET /summary/`: Get the financial summary of all transactions.
- `GET /insights/`: Get AI-generated financial insights (anomalies, cash runway).
- `GET /recommendations/`: Get prioritized, actionable financial recommendations.
- `GET /digest/`: Get a daily financial digest including metrics and alerts.
- `POST /email-digest/`: Trigger a daily digest email to a specified recipient (Query param: `email`).

## Tech Stack
- **Backend**: FastAPI
- **Database**: SQLite, SQLAlchemy
- **AI/LLM**: OpenAI GPT-4o-mini
