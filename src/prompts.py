query_template = """Given the topic "{topic}",generate diverse top search queries covering:
    - Definitions and Technical explanations
    - Latest developments(do not include dates)
    - 4 to 5 Practical applications
    - one real use case implemented in any industry or company
    -  If the topic is related to data preprocessing steps, include two additional applications specific to machine learning and data science
    Note: all these diverse query needs to be help in finding applications of given topic"""


report_prompt = """
Generate a report based on the following outline or format strictly:

# Introduction
  - Provide a brief introduction of topic in 50 to 100 words.

## Real world applicatio of the topics
### Application Name
       - Description(min 150 to 200 words).
### Application Name 
       - Description(min 150 to 200 words).
### Application Name
      - Description(min 150 to 200 words).
### Application Name  
      - Description(min 150 to 200 words).

      so on...  (4 to 5 applications)

## Industry case study with comapny (if available)
    - Provide a case study description related to given topic.(150 to 200 words)

### Additional resources.
    -  [Link](url)
    -  [Link](url)
    -  [Link](url)
    -  [Link](url)
Note: Do not include source links of edutech website like GeeksforGeeks, udemy, Javapoint, Byjus, Analyticsvidhya, etc.
Note: Bold the important keywords and sentences in the report.
<"end-of-sequence">.
"""