# 💼 genAI Cold Email Generator

A generative AI-powered tool that creates personalized cold emails to Human Resources (HR) professionals, showcasing how a candidate's skills align with a specific job role. Built using Python, LangChain, ChromaDB, and Streamlit, this project streamlines professional outreach for job seekers.

## 🚀 Project Objective

This tool aims to simplify the job search process by generating compelling, customized emails that reflect the user’s qualifications and target specific roles. By combining natural language processing with semantic search, the generator ensures the emails feel human-written and relevant.

## 🔧 Tech Stack

- **Python** – Core scripting language
- **LangChain** – Orchestrates prompt engineering and language model workflows
- **ChromaDB** – Enables vector-based storage and semantic search of skills/job descriptions
- **Streamlit** – Provides an interactive and user-friendly web interface

## ✨ Key Features

- Input your **skills** and **target job description**
- Retrieve similar skill matches using **vector embeddings**
- Generate customized cold emails tailored to HR
- Simple and intuitive **web interface** using Streamlit

## 🧠 How It Works

1. **Skill & Job Input**: User enters their relevant skills and target job summary.
2. **Semantic Retrieval**: ChromaDB fetches job-skill matches using embeddings.
3. **Prompt Generation**: LangChain builds a prompt aligned to HR communication tone.
4. **Output**: A polished, human-like cold email is generated for copy or download.

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/Bikram-lab/genAI-cold-email-generator.git
cd genAI-cold-email-generator
