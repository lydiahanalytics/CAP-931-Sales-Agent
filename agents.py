from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def run_agent(role, task, context):
    prompt = f"""
You are the {role} in a multi-agent sales intelligence system.

Your task:
{task}

Context:
{context}

Instructions:
- Stay focused on B2B sales intelligence.
- Be concise, factual, and useful to a sales representative.
- Do not invent facts.
- Clearly state when information is uncertain or unavailable.
"""

    response = client.responses.create(
        model="gpt-5.4",
        input=prompt
    )

    return response.output_text


def company_research_agent(context):
    prompt = f"""
You are the Company Research Agent in a multi-agent sales intelligence system.

Research the prospective company using current publicly available web information.

Sales context:
{context}

Find evidence related to:
- company strategy
- AI and technology initiatives
- hiring or workforce strategy
- HR or talent priorities
- relevant executive statements
- recent press releases or official company announcements

Instructions:
- Use current web sources.
- Prefer official company sources, annual reports, investor materials,
  press releases, and reputable publications.
- Do not invent facts.
- Distinguish confirmed information from inference.
- Include source names and URLs in your answer.
- Focus only on information relevant to the sales opportunity.
"""

    response = client.responses.create(
        model="gpt-5.4",
        tools=[{"type": "web_search"}],
        input=prompt
    )

    return response.output_text

def competitor_agent(context):
    prompt = f"""
You are the Competitor Intelligence Agent in a multi-agent
sales intelligence system.

Sales context:
{context}

Research the competitors named in the sales context using current
publicly available web information.

Research:
- competitor products and services
- relevant AI capabilities
- recruiting, HR, or talent-management capabilities
- recent product announcements
- competitive strengths
- possible weaknesses or gaps
- how each competitor affects this sales opportunity

Instructions:
- Use current web sources.
- Prefer official competitor websites, product documentation,
  press releases, investor materials, and reputable publications.
- Do not invent facts.
- Clearly distinguish confirmed facts from sales inference.
- Do not claim the prospective company uses a competitor unless
  there is evidence.
- Include source names and URLs.
- End with a concise competitive positioning recommendation.
"""

    response = client.responses.create(
        model="gpt-5.4",
        tools=[{"type": "web_search"}],
        input=prompt
    )

    return response.output_text

def leadership_agent(context):
    prompt = f"""
You are the Leadership Research Agent in a multi-agent sales intelligence system.

Sales context:
{context}

Research the prospective company's current leadership using publicly available web information.

Focus on leaders relevant to:
- Human Resources / People
- Talent Acquisition
- HR Technology / People Systems
- People Analytics / Workforce Strategy
- Corporate Strategy / Transformation
- AI governance, privacy, or security when relevant to the sale

Instructions:
- Use current web sources.
- Prefer the prospective company's official leadership pages,
  press releases, annual reports, and reputable publications.
- Identify actual current leaders by name and title when evidence is available.
- Explain why each leader or role matters to this sales opportunity.
- Do not invent names or titles.
- Clearly label anything uncertain or inferred.
- Include source names and URLs.
- End with a prioritized stakeholder map for the sales representative.
"""

    response = client.responses.create(
        model="gpt-5.4",
        tools=[{"type": "web_search"}],
        input=prompt
    )

    return response.output_text


def sales_strategy_agent(context):
    return run_agent(
        role="Sales Strategy Agent",
        task=(
            "Connect the product value proposition to the prospective company's "
            "likely needs. Identify potential pain points, opportunities, and "
            "recommended sales talking points."
        ),
        context=context
    )

def report_agent(company, competitors, leadership, sales_strategy, context):
    combined_context = f"""
ORIGINAL SALES CONTEXT:
{context}

COMPANY RESEARCH:
{company}

COMPETITOR ANALYSIS:
{competitors}

LEADERSHIP ANALYSIS:
{leadership}

SALES STRATEGY:
{sales_strategy}
"""

    return run_agent(
        role="Executive Sales Report Agent",
        task=(
            "Create a professional one-page account intelligence brief. "
            "Use the sections: Company Strategy, Competitor Insights, "
            "Leadership Priorities, Sales Opportunity, Recommended Talking Points, "
            "Risks or Unknowns, and Sources. "
            "Use only facts supported by the agent outputs provided in the context. "
            "Preserve the most relevant source names and URLs from the research. "
            "Clearly distinguish confirmed facts from inference. "
            "Do not invent sources, leaders, competitor usage, or company technology. "
            "Keep the brief concise and useful to a sales representative."
        ),
        context=combined_context
    )