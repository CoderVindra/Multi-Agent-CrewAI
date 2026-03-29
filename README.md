# 📊 Multi-Agent Stock Analysis System using CrewAI

A powerful **multi-agent AI system** built using CrewAI that analyzes stock data and makes trading decisions using real-time information.

---

## 🚀 Features

- 🤖 Multi-agent collaboration (Analyst + Trader)
- 📊 Real-time stock data using Yahoo Finance
- 🧠 LLM-powered reasoning (Groq - LLaMA 3.3 70B)
- 🔍 Automated stock analysis
- 💼 Smart trading decisions (Buy / Sell / Hold)

---

## 🏗️ Project Structure

```
Multi-Agent-CrewAI/
│── agents/
│   ├── analyst_agent.py
│   ├── trader_agent.py
│
│── tasks/
│   ├── analyst_task.py
│   ├── trade_task.py
│
│── tools/
│   ├── stock_research_tool.py
│
│── crew.py
│── main.py
│── requirements.txt
│── README.md
```

---

## ⚙️ How It Works

### 🧠 Analyst Agent
- Fetches live stock data
- Analyzes price, change %, and trends
- Generates structured insights

### 💼 Trader Agent
- Uses analysis to make decisions
- Evaluates risk and momentum
- Outputs: **Buy / Sell / Hold**

### 🔗 Crew Workflow
1. Analyze stock performance  
2. Make trading decision  

---

## 🧰 Tech Stack

- CrewAI  
- Groq (LLaMA 3.3 - 70B)  
- yFinance  
- Python  

---

## 🧪 Setup

### 1. Clone Repo
```bash
git clone https://github.com/CoderVindra/Multi-Agent-CrewAI.git
cd Multi-Agent-CrewAI
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API Key
Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run

```bash
python main.py
```

Example:
```python
run("AAPL")
```

---

## 📌 Output

- 📊 Stock Analysis Summary  
- 📈 Trading Recommendation  

---

## 💡 Learnings

- Multi-agent system design  
- Tool integration with LLMs  
- Real-time AI decision workflows  

---

## 🙌 Author

**Ravindra Pawar**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
