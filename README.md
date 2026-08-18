# CAP 931 - Sales Agent Prototype Using Multi-Agent GPT Models

## Project Overview

This project is a prototype AI-powered Sales Assistant Agent designed to help a sales representative research a prospective account, understand competitor positioning, identify relevant leadership, and generate strategic sales insights.

The prototype uses a multi-agent architecture powered by GPT models and a Streamlit user interface. Each specialized agent performs a different part of the sales research process, and the final Report Agent combines the results into an Executive Sales Intelligence Brief.

For the prototype scenario, the product being sold is an **AI-Powered Talent Acquisition Platform**, and the prospective account is **Microsoft**.

---

## Project Objectives

The application was designed to:

* Collect sales opportunity information through a Streamlit interface.
* Research a prospective company using current publicly available web information.
* Analyze competitors relevant to the sales opportunity.
* Identify current company leaders and stakeholders.
* Connect the product value proposition to the prospect's business priorities.
* Generate a concise Executive Sales Intelligence Brief.
* Distinguish confirmed facts from sales inference.
* Preserve relevant source names and URLs.
* Accept an optional product overview document for additional context.

---

## Technology Stack

* Python 3.12
* Streamlit
* OpenAI API
* GPT model through the OpenAI Responses API
* OpenAI web search tools
* python-dotenv
* PyPDF
* Requests
* BeautifulSoup4
* uv for Python environment and dependency management

---

## Project Structure

```text
CAP-931-Sales-Agent/
│
├── app.py
├── agents.py
├── test_openai.py
├── product_overview.txt
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .python-version
└── .env
```

### app.py

The main Streamlit application.

Responsibilities include:

* displaying the user interface
* collecting sales opportunity inputs
* accepting optional PDF or TXT product documents
* extracting document text
* sending context to the agents
* displaying the final Executive Sales Intelligence Brief
* displaying individual agent outputs in expandable sections

### agents.py

Contains the multi-agent GPT workflow.

The system includes the following agents:

#### 1. Company Research Agent

Researches the prospective company using current publicly available web information.

It focuses on:

* company strategy
* AI and technology initiatives
* workforce strategy
* HR and talent priorities
* relevant executive statements
* recent official announcements

The agent is instructed to prefer official company sources, investor information, annual reports, press releases, and reputable publications.

#### 2. Competitor Intelligence Agent

Researches the competitors entered by the sales representative.

It analyzes:

* competitor products
* recruiting and talent-management capabilities
* AI capabilities
* recent product announcements
* competitive strengths
* possible weaknesses
* implications for the sales opportunity

Confirmed facts are separated from sales inference.

#### 3. Leadership Research Agent

Identifies current leaders relevant to the sales opportunity.

Areas of focus include:

* Human Resources
* People leadership
* Talent Acquisition
* HR Technology
* People Analytics
* Corporate Transformation
* Responsible AI
* Privacy
* Legal and governance

The agent avoids inventing names or titles when reliable public evidence is unavailable.

#### 4. Sales Strategy Agent

Connects the product's capabilities and value proposition to the prospective customer's likely needs.

It develops:

* potential pain points
* opportunity areas
* discovery questions
* recommended talking points
* competitive positioning
* sales approach

#### 5. Executive Report Agent

Combines the findings from the other agents into a concise account intelligence brief.

The report includes:

* Company Strategy
* Competitor Insights
* Leadership Priorities
* Sales Opportunity
* Recommended Talking Points
* Risks or Unknowns
* Sources

---

## Streamlit Inputs

The application accepts the following sales opportunity information:

* Product Name
* Prospective Company URL
* Product Category
* Competitor names or URLs
* Value Proposition
* Target Customer
* Optional Product Overview document

The prototype supports optional `.pdf` and `.txt` product documents.

---

## Prototype Sales Scenario

### Product

AI-Powered Talent Acquisition Platform

### Product Category

AI Recruiting & Talent Analytics

### Prospective Account

Microsoft

### Competitors

* Workday
* Oracle

### Target Customer

Chief Human Resources Officer / Head of Talent Acquisition

### Value Proposition

An AI-powered recruiting platform that helps enterprises identify qualified candidates faster, automate repetitive recruiting tasks, and use talent analytics to improve hiring decisions.

---

## Multi-Agent Workflow

The prototype follows this process:

```text
Sales Rep Inputs
      ↓
Company Research Agent
      ↓
Competitor Intelligence Agent
      ↓
Leadership Research Agent
      ↓
Sales Strategy Agent
      ↓
Executive Report Agent
      ↓
Executive Sales Intelligence Brief
```

The agents work sequentially so that the final Report Agent can combine research, competitive intelligence, stakeholder information, and sales strategy into one output.

---

## Web Research and Data Integration

The Company Research Agent, Competitor Intelligence Agent, and Leadership Research Agent use web search to retrieve current public information.

The agents are instructed to prioritize sources such as:

* official company websites
* annual reports
* investor relations materials
* company leadership pages
* product documentation
* press releases
* official corporate blogs
* reputable publications

The prompts specifically instruct the agents not to invent facts.

The system also separates:

**Confirmed facts** – information supported by research sources.

**Sales inference** – conclusions or recommendations derived from confirmed information but not presented as verified company facts.

---

## Example Research Findings

During testing with Microsoft, the system generated research covering topics such as:

* Microsoft's AI transformation strategy
* enterprise cloud and AI priorities
* HR transformation
* responsible AI
* workforce analytics
* Microsoft leadership
* Workday Talent Acquisition
* Workday HiredScore and AI recruiting capabilities
* Oracle Fusion Cloud Recruiting
* Oracle Recruiting Booster
* recruiting AI and talent analytics
* sales positioning opportunities and risks

The system also preserved source URLs in the final Executive Sales Intelligence Brief.

---

## Optional Product Document Processing

The Streamlit application allows the sales representative to upload a product overview document.

Supported formats:

* PDF
* TXT

The system extracts the document text and adds it to the sales context given to the agents.

This allows the agents to use additional product information when generating:

* sales positioning
* product differentiation
* competitor analysis
* recommended talking points
* opportunity insights

---

## Model Selection

The prototype uses a GPT model through the OpenAI API.

The model was selected because it provides strong capabilities for:

* natural language understanding
* summarization
* research synthesis
* multi-step reasoning
* sales strategy generation
* structured business writing
* tool-enabled web research

### Strengths

* High-quality natural language generation
* Strong context understanding
* Effective synthesis across multiple research outputs
* Support for web search
* Effective prompt chaining
* Strong business-oriented responses

### Considerations

* API usage has a financial cost.
* Web research increases processing time.
* LLM outputs still require grounding and source verification.
* The system must distinguish confirmed information from inference.
* Sensitive use cases such as AI in hiring require attention to fairness, privacy, transparency, and governance.

---

## Prompt Engineering Approach

Several prompt engineering techniques were used.

### Role Prompting

Each agent receives a specialized professional role, such as:

* Company Research Agent
* Competitor Intelligence Agent
* Leadership Research Agent
* Sales Strategy Agent
* Executive Sales Report Agent

### Context Setting

Each agent receives the same core sales opportunity context.

### Prompt Constraints

Agents are instructed to:

* remain focused on B2B sales intelligence
* avoid unrelated responses
* avoid inventing facts
* identify uncertainty
* use reliable sources
* distinguish confirmed facts from inference

### Prompt Chaining

The outputs of multiple specialized agents are passed into the final Executive Report Agent.

This allows the final response to combine multiple perspectives instead of relying on a single prompt.

---

## Experiments and Improvements

Several iterations were performed while developing the prototype.

### Experiment 1 – Basic Multi-Agent Generation

The first version used separate company, competitor, leadership, sales strategy, and reporting agents.

Result:

The structure of the report was strong, but some company and competitor information was based on general model knowledge rather than verified current research.

### Experiment 2 – Web-Enabled Company Research

The Company Research Agent was upgraded to use web search.

Result:

The output became more evidence-based and included official Microsoft sources, executive statements, workforce information, and current company strategy.

### Experiment 3 – Web-Enabled Competitor Research

The Competitor Agent was upgraded to research Workday and Oracle through current public sources.

Result:

The agent produced more detailed comparisons of recruiting products, AI capabilities, strengths, weaknesses, and positioning opportunities.

### Experiment 4 – Web-Enabled Leadership Research

The Leadership Agent was upgraded to identify actual company leaders through current public sources.

Result:

The system identified relevant executives when evidence was available and explicitly avoided naming leaders when the information could not be reliably confirmed.

### Experiment 5 – Source Preservation

The Executive Report Agent was updated to preserve important research URLs.

Result:

The final Executive Sales Intelligence Brief included a Sources section that allowed the sales representative to review the underlying evidence.

### Experiment 6 – Product Document Upload

PDF and TXT document parsing were added to the Streamlit application.

Result:

The application successfully accepted a product overview document and included the extracted information in the agent context.

---

## Challenges and Solutions

### Challenge 1 – Environment Configuration

PowerShell initially prevented virtual environment activation because script execution was disabled.

Solution:

A temporary PowerShell execution-policy bypass was used for the active terminal session.

### Challenge 2 – API Environment Variable

The OpenAI API key was initially not loading from the `.env` file.

Solution:

The `.env` file was corrected to use:

```text
OPENAI_API_KEY=<secret-key>
```

The application was then able to load the API key successfully.

### Challenge 3 – API Credits

The first API connection returned an insufficient quota error.

Solution:

API credits were added and the connection was tested successfully.

### Challenge 4 – Streamlit and Environment Loading

The OpenAI client was initially created before the `.env` file was loaded.

Solution:

`load_dotenv()` was added before initializing the OpenAI client.

### Challenge 5 – Python Syntax and Indentation Errors

During development, some functions produced syntax or indentation errors while being edited.

Solution:

Python's compile check was used repeatedly:

```powershell
uv run python -m py_compile agents.py
```

and:

```powershell
uv run python -m py_compile app.py
```

This allowed syntax problems to be identified before restarting Streamlit.

### Challenge 6 – Unsupported LLM Assumptions

Early outputs included sales assumptions without enough current evidence.

Solution:

Web-enabled research agents were added and prompted to distinguish confirmed facts from sales inference.

---

## Time Management

The development work was divided into major phases:

### Phase 1 – Environment Setup

* Created Python project
* Created virtual environment
* Installed dependencies
* Configured API access

### Phase 2 – Streamlit Interface

* Created required input fields
* Added product information
* Added optional file upload

### Phase 3 – Multi-Agent Development

* Built Company Research Agent
* Built Competitor Agent
* Built Leadership Agent
* Built Sales Strategy Agent
* Built Report Agent

### Phase 4 – Research Enhancement

* Added web search
* Added source links
* Improved factual grounding
* Added confirmed fact vs. inference labeling

### Phase 5 – Testing and Debugging

* Tested API connectivity
* Tested Streamlit
* Corrected environment loading
* Corrected syntax and indentation issues
* Tested document upload
* Reviewed final sales intelligence reports

### Phase 6 – Documentation and Submission Preparation

* Created technical documentation
* Documented experiments
* Documented challenges and solutions
* Prepared project for final submission

---

## Running the Project

### 1. Navigate to the project

```powershell
cd "C:\Users\Lydia Nyambura\CAP-931-Sales-Agent"
```

### 2. Activate the virtual environment

If PowerShell blocks script execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Create a `.env` file

The `.env` file should contain:

```text
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

Never upload the `.env` file or expose the API key publicly.

### 4. Run the Streamlit application

```powershell
uv run streamlit run app.py
```

### 5. Open the Local URL

Example:

```text
http://localhost:8501
```

The exact port may change if another Streamlit server is already running.

---

## Security

The OpenAI API key is stored in `.env`.

The `.gitignore` file excludes:

```text
.env
.venv/
__pycache__/
*.pyc
```

This helps prevent secret credentials and unnecessary local files from being committed to GitHub.

---

## Production Deployment Considerations

A production version of this application would require additional improvements.

### Security

* Store secrets in a secure secret-management system.
* Use authentication and role-based access.
* Encrypt sensitive customer and candidate information.
* Implement secure logging.
* Apply data-retention controls.

### Scalability

* Move research and agent workflows to backend services.
* Use asynchronous processing for long-running research.
* Add caching to reduce repeated API and web-search requests.
* Use a scalable cloud hosting environment.

### Reliability

* Add structured error handling.
* Add API retry logic.
* Add monitoring and logging.
* Add source validation.
* Add automated testing.

### Responsible AI

Because this prototype involves recruiting technology, a production system should include:

* human oversight
* bias monitoring
* fairness testing
* transparency
* explainability
* privacy protections
* auditability
* compliance review

---

## Potential Future Enhancements

Future versions could include:

* automated email alerts for new company announcements
* monitoring of competitor product releases
* monitoring of relevant job postings
* PDF export of the Executive Sales Intelligence Brief
* PowerPoint sales meeting deck generation
* CRM integration
* saved account histories
* automated account comparison
* scoring and prioritization of sales opportunities
* deeper product-document analysis
* additional specialized agents

---

## Conclusion

The CAP 931 Sales Agent Prototype demonstrates how a multi-agent GPT architecture can support B2B sales research.

Instead of relying on one large prompt, the application divides the work among specialized agents responsible for company research, competitor intelligence, leadership research, sales strategy, and executive reporting.

The prototype combines Streamlit, GPT models, web research, prompt engineering, document processing, and source-aware reporting to help a sales representative quickly understand a prospective account and prepare a more informed sales approach.
