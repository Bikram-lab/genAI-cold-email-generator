import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

print("Starting the script...")


class Chain:
    def __init__(self):
        load_dotenv()
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-8b-instant",
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """ Scraped text from website
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing
            following keys: 'role', 'experience', 'skills' and 'description'.
            Only return the valid JSON.
            ### VALID Json (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            json_res = json_parser.parse(res.content)
        except OutputParserException as e:
            print("Parsing failed with message:", e)
            raise OutputParserException("Content too big. Unable to parse jobs.")
        return json_res

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ###JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Bikramjeet Singh, an experienced Data Engineer at TCS(an IT Consultant company) with 3 years of experience. 
            You job is to write mail to the Hiring manager for the job at their company to consider you for the the role at their company.
            Do not provide preamble.
            ### EMAIL (NO PREAMBLE)

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


if __name__ == "__main__":
    print("Running test extract_jobs...")
    #print(os.getenv("GROQ_API_KEY"))
