from chain import Chain
from jobpost import Jobpost
from util import clean_text
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

def create_streamlit_app(llm, jobpost, clean_text):
    st.title("Cold Mail Generator")
    url_input = st.text_input(
        "Enter a URL:",
        value="Provide the job weblink....",
    )
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            jobpost.load_jobpost()
            jobs = llm.extract_jobs(data)
            for i, job in enumerate(jobs, 1):
                skills = job.get("skills", [])
                links = jobpost.query_links(skills)

                email = llm.write_mail(job, links)
                st.markdown("**Generated Email:**")
                st.code(email, language="markdown")
                st.markdown("---")
                st.subheader(f"Job {i}: {job.get('role', 'Unknown Role')}")
                st.write("**Experience:**", job.get("experience", "N/A"))
                st.write("**Skills:**", ", ".join(job.get("skills", [])))
                st.write("**Description:**", job.get("description", "N/A"))
                if links:
                    st.write("**Matched Links:**")
                    for link in links:
                        st.markdown(f"- [{link}]({link})")
                else:
                    st.write("No matching links found.")

        except Exception as e:
            st.error(f"An Error Occured: {e}")


if __name__ == "__main__":
    chain = Chain()
    jobpost = Jobpost()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, jobpost, clean_text)