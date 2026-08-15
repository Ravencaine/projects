---
title: "How to Tell a Data Story"
source: "https://medium.com/@jjr8888/how-to-tell-a-data-story-651edd4c5b4a"
author:
  - "[[Jesse Ruiz (she/they)]]"
published: 2024-08-05
created: 2026-08-11
description: "My Process for Creating Data Visualizations"
Processed: "Unprocessed"
---
## My Process for Creating Data Visualizations

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*L5P68HfvyU-MaV2s)

Photo by Isaac Smith on Unsplash

What is your process for creating a data visualization?

In my experience, it *depends* on many factors but there are general considerations to ensure thorough and effective data storytelling. I frame my own process as a series of questions that each reflects complex topics such as process and information gathering, data modeling, exploratory data analysis, statistical analysis, design and user experience/interaction, as well as data visualization. Given that there is no “one-size-fits-all” rule in data visualization, I made this article as generalized as possible. Different industries may require adjustments or other (additional) considerations.

Here are the questions to ask when creating a data visualization end-to-end:

1\. What is the data?

2\. Who is the data/report for?

3\. Where does the data come from and where do you store it?

4\. Is the data accurate and true?

5\. What is the data telling you?

6\. What does the data look like?

7\. What works and doesn’t work?

8\. How do you maintain this data visualization or how does someone else maintain it?

To discuss each question in length, I will use an example data visualization project, which was a Makeover Monday data visualization challenge in collaboration with Operation Fistula. This project involved survey data from a study about a global health issue called fistula. You can view my original visualization [here](https://public.tableau.com/views/ViolenceAgainstWomenandGirlsSurveybyOperationFistula/Violenceagainstwomen?%3Alanguage=en-US&%3Asid=&%3Adisplay_count=n&%3Aorigin=viz_share_link) and you can read more about the project here: [https://opfistula.org/](https://opfistula.org/).

![Data dashboard built with Tableau showing stacked bar chart and survey questions.](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WcCex64ltuv97Q6CHVwmgA.png)

My data visualization for Operation Fistula for Makeover Monday challenge on Week 10 of 2020

### Step 1 — What is the data or understanding your data

Whatever the data is, you must first understand it in depth. This entails deciphering the features and what each row of data represents (if relational). Completing this sentence is an absolute minimum: “This data is in the form of \_\_\_ (a table, an image file, a web response, a json file, etc.) and each observation, file or row represents \_\_\_. Its features or characteristics are \_\_\_.” As a novice, it is great practice to ask this question repeatedly and discuss it out loud.

Having a complete picture of your data is hard work. It requires knowledge of databases, database design, data dictionaries, data governance, availability, and data quality. Each of these topics are deep and complex. But don’t let the complexity deter you or confuse you. If the data visualization project is as simple as this year’s school budget, then let it be simple.

My data visualization on Operation Fistula started with a clean csv file and data dictionary that was provided by Makeover Monday. The nature of the data was survey data or questions and answers about topics. This kind of qualitative data is difficult to simplify and visually represent but more on that later. Having read through the project mission, the data dictionary and the csv file, I knew that: “This data is in the form of a csv file and each observation represents an aggregated value based on a group of survey respondents answers to a specific question. Its features are a record id, the survey question, country, gender, date of survey and the aggregated value representing the percentage of people who agree with the question.”

Please feel free to take a peek at the data here:

[https://data.world/makeovermonday/2020w10](https://data.world/makeovermonday/2020w10)

### Step 2 — Who is the data and report for, or understanding your audience

Next, we need to examine who is consuming this data and report, what they need it for, what it represents for them. In trying to understand your audience, identify who will be looking at this data and visualization. What’s at stake for them? How do they usually interact with this data? Are they producing this data? Very often in industry, data visualizations or data reports are for the boss, the executives, or the decision makers. They are consuming data reports to understand the health and the current state of things within the business. And that’s a very simple and easy data reporting assignment. The business drives needs and requirements through key performance indicators, or KPIs. And your audience is simply the people in charge or people responsible for these KPIs.

You can see how survey data is more complex than business metrics. There’s both qualitative and quantitative information and both are dependent upon the chosen methodology for their integrity. Survey data has more considerations than most data, including survey methodology, ethical considerations, and context.

When I worked on the Operation Fistula data visualization, I came to understand the audience included global health actors including world health ministers, other researchers, and potential funders. In addition, I know that the audience is also a group of data science and visualization enthusiasts on the internet. Therefore, I made the assumption that most of the audience that was in the latter group would not be familiar with this global health crisis nor with survey methodologies in the global health arena. More on this important assumption later.

### Step 3 — Where does the data come from and where do you store it?

Understanding the origin and storage of your data is crucial for several reasons. It helps you assess the data’s reliability, potential biases, and limitations. It also informs how you might need to process or clean the data before visualization. In the case of the Operation Fistula project, the data came from a survey conducted by the organization. It was provided as a clean CSV file through the Makeover Monday challenge. In real-world scenarios, data sources can be much more complex, including:

- Internal databases
- APIs
- Web scraping
- IoT devices
- Third-party data providers

For storage, the choice depends on factors like data volume, update frequency, and access requirements. Options range from simple flat files to complex distributed systems.

### Step 4 — Is the data accurate and true?

Data quality is paramount in creating meaningful visualizations. This step involves:

1. Checking for missing or null values
2. Identifying outliers or anomalies
3. Verifying data types and formats
4. Cross-referencing with other sources, if possible

Many considerations abound when it comes to data integrity. In terms of the issues it presents for data visualization, it requires thorough validations of accuracy, completeness, validity, consistency, timeliness, and uniqueness. I know this sounds like a bunch of words that all mean the same thing, but they don’t. Completeness means the data has all the required fields and values, validity means the data conforms to certain formats, consistency means the data is coherent and compatible, timeliness means the data is available and updated within a certain timeframe, accuracy means the data reflects the true state and uniqueness means the data does not have duplicates.

For the most part, if you work at a large company, the data quality may fall under the duties of a separate team like data engineering. However, the due diligence to check for all of these is mandatory nevertheless.

For the Operation Fistula data, the cleanliness of the provided CSV file simplified this step. As I did not conduct the survey myself, I trusted that the authors of the study completed quality checks. However, it’s still important to verify the survey methodology and consider potential biases in the data collection process.

### Step 5 — What is the data telling you?

The most paramount job of a data visualization is to tell as story. It’s very easy to get muddled here. In order to tell a story, you must know your data thoroughly. This is where exploratory data analysis (EDA) comes into play. EDA involves:

1. Calculating summary statistics
2. Identifying trends and patterns
3. Exploring relationships between variables
4. Formulating hypotheses about the data

In truth, this step is also done hand in hand with step 4, data validations. That is, they inform each other but have different scopes.

In the Operation Fistula project, the data revealed insights about awareness, attitudes, and experiences related to fistula across different countries and demographics. Key findings included variations in awareness levels between countries or gender-based differences in attitudes towards the condition. These key findings were important to keep in mind when thinking about the story I want to tell the audience.

### Step 6 — What does the data look like?

So now that I have done validation, explored and found insights, what types of charts are best suited for the data story. How can we guide to user through a story with charts without exhausting them with useless information. This step involves choosing appropriate visualization types based on:

1. The nature of the data (categorical, numerical, time-series, etc.)
2. The story you want to tell
3. The audience’s familiarity with different chart types

For the Operation Fistula data, I sought to create the visualization as an exploratory tool. I wanted the visualization to feel like the original survey itself because I determined that the audience was likely unfamiliar with this data and topic of global health. Beginning with the idea of presenting the visualization as a mock survey, I included the questions in a column with form buttons next to them to mimic the original survey. I wanted to pull the audience into the data by confronting them with the survey questions directly. In my visualization design process, I considered the following but ultimately decided for a simple matrix design to summarize the findings:

- Bar charts for comparing percentages across countries or questions
- Heatmaps to show variations across multiple dimensions
- Treemaps to represent hierarchical data
- Interactive elements to allow exploration of different survey questions

### Step 7 — What works and doesn’t work?

This stage involves iterative refinement of your visualization. Consider:

1. Clarity: Is the main message immediately apparent?
2. Aesthetics: Is the design visually appealing without distracting from the data?
3. Interactivity: Does it enhance understanding or overwhelm the user?
4. Accessibility: Is it readable for all users, including those with visual impairments?

In the Operation Fistula visualization, I went through several iterations, testing different chart types and layouts to find the most effective way to communicate the survey results. I included the key findings in a text box on the bottom of the frame with a heading of “Key Findings” and included links to more information about the project. As I worked through finding the best design for composing the elements, I knew that the top left quadrant was the most important one and therefore where I placed the survey questions with form buttons.

### Step 8 — How do you maintain this data visualization or how does someone else maintain it?

It sometimes happens that you work on a data visualization and never return to it after you deliver it. But it’s not good practice to leave your work undocumented or without any consideration for how it will be used in the future. Maintenance considerations include:

1. Documentation: Clear explanations of data sources, processing steps, and visualization choices
2. Version control: Tracking changes over time
3. Reproducibility: Ensuring others can recreate or update the visualization
4. Scalability: Designing for potential increases in data volume or complexity

For the Operation Fistula project, as a one-time challenge, maintenance was not a major concern. However, in a real-world scenario, you need to consider how to update the visualization as new survey data becomes available, and how to hand off the project to other team members if necessary. By addressing these questions thoroughly, you create a robust process for developing effective and impactful data visualizations, regardless of the specific project or domain. Always be sure to include links to data sources as well as your own name and contact information in your data visualizations.

In enterprise settings, a major facet of the job of a data visualization specialist is maintaining existing dashboards. In this case, iterating through all of the above steps are required but in reality less concern is given to design over time. More concern and attention is given to data validation and accuracy and timeliness in these situations.

### Conclusion

In conclusion, the process of creating effective data visualizations is multifaceted and requires a structured approach to ensure that the final product communicates the intended message clearly and accurately. By systematically addressing key questions — from understanding the nature of the data and its audience to ensuring data quality and appropriate visualization techniques — data storytellers can craft compelling narratives that resonate with viewers. It’s less common to have to build a data visualization end-to-end and so perhaps all the steps I addressed here will not matter. But it’s helpful to understand the big picutre.

The example of the Operation Fistula data visualization illustrates the importance of tailoring the visualization to meet the needs of diverse stakeholders, including health professionals and researchers. It highlights the necessity of iterative refinement and the role of aesthetics and clarity in enhancing user engagement.

Ultimately, a well-maintained data visualization not only serves its immediate purpose but also lays the groundwork for future updates and adaptations, ensuring that it remains relevant and useful over time. Embracing this comprehensive approach will empower you to transform complex datasets into insightful stories that drive informed decision-making and foster greater understanding of critical issues.

Thanks for reading!