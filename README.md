# 9CT_Task_3
### Mind Map
 put the photo in here


# Requirements Outline
### Mind Map 

### Functional Requirements
- Loading: The system should be able to load the correct files and display an error message if the file is missing
- Cleaning: The system should be able to handle missing values in the data
- Analysis: The system should be able to handle statistical analysis in the form of calculating the mean and median for the data
- Visualisation: The data should be clearly visualised in different forms including matplotlib charts which display the difference between female and male performance
- Reporting: The final data will need to be stored in a .csv file
### Non-Functional Requirements
- Usability: The user should be able to navigate the UI and access data/data visualisations with ease, and understand the purpose, scope, and origins of data used in the project from the README.md
- Reliability: The data used for the project should be a truthful representation of the students' performance and recent
### Use Case
#### Actor: User
#### Goal: For the user to interact and access with collected data and visualisations through the UI
#### Preconditions:
- The dataset has already been preloaded into the system by an administrator / programmer. 
- The user can acess the UI
#### Main Flow:
1. The user opens the program and sees a text-based menu
2. The menu gives them the option to view:
    - A visualisation of the performance of female and male students in the most recent english NAPLAN and HSC results
    - Search or filter data from different states, demographics, language backgrounds, etc.
    - Update a data entry to change a value or correct an error
3. The program performs the user's selected action
#### Postconditions:
- The user has accessed and interacted with the data
- The updates the user has made to the data are saved
- The data is still accessible

# Research
### Relevant Sources
#### International Sources:
- https://today.ucsd.edu/story/girls-excel-in-language-arts-early-which-may-explain-the-stem-gender-gap-in-adults
- https://ed.stanford.edu/news/new-stanford-education-study-shows-where-boys-and-girls-do-better-math-english
- https://news.griffith.edu.au/2018/09/21/girls-better-readers-and-writers-than-boys-study/
- https://www.cambridgeassessment.org.uk/Images/gender-differences-cambridge-english.pdf
#### Australian Sources:
- https://www.theguardian.com/education/2009/apr/21/girls-boys-english-grades
- https://www.smh.com.au/national/nsw/girls-now-out-performing-boys-in-nearly-every-hsc-subject-20221209-p5c56d.html
- https://www.unsw.edu.au/newsroom/news/2018/09/study-reveals-patterns-in-stem-grades-of-girls-versus-boys

### SEE-I Paragraph
#### Planning
- Girls seem to routinely outperform boys in english as well as other humanities subjects.

# Data Dictionary
| Field | Datatype     | Format For Display   |  Description | Example  | Validation  |
|---------- |---------- |----------------   |--------------- | ------ | --------- |
|  Year   |   year  |   YYYY | The year the NAPLAN test was taken  | 2018 | Must be a 4 digit number |
|  Male Reading Mean / (S.D.) |  float64 | NNN.NN (NN.N)  | The average of male year 7 NAPLAN results for the reading test and the standard deviation of their scores in brackets | 540.8 (68.6) |
|  Male Reading % at or above NMS | float64 | NN.N | ??? | 83.7 |  |
| Female Reading Mean / (S.D.) | float64 | NNN.NN (NN.N) | The average of female year 7 NAPLAN results for the reading test and the standard deviation of their scores in brackets | 571.9 (57.9) |

# Evaluation
### SEE-I Paragraph
Analyse your findings and make note of areas that might need more research, provide a conclusion on your hypothesis.
### Peer PMI Verification
Chart
#### Evaluate your system and results in relation to your Requirements Outline
My system is able to calculate the means of the data, fulfilling the analysis aspect of the requirements outline but doesn't calculate the median because I decided that wasn't necessary for understanding the data. My system also effectively visualises the data in the form of different matplotlib charts that display the differences between female and male performance, also giving the project a high readibility. However, the UI isn't able to be navigated with ease and I didn't get time to code an error message if the data is missing, failing the loading aspect of the requirements outline.
#### Evaluate your system in relation to peer feedback
#### Evaluate your project in relation to project management
I don't believe I managed my time as effectively as possible during this project. I procrastinated on a lot of the research aspects and ended up having to do them all towards the end of the project. However, I don't believe my github commits are a good measure of this because github desktop wasn't downloaded on my PC originally, meaning I had to do my theory in a seperate file which I later transferred to my project, so my github commits make it look much worse than it actually was. In the future I'd want to front load the theory work to give myself more time for the coding which I did entirely on one weekend which is less than ideal.
#### Evaluate your system in in relation to its data and security
- Is the data valid, accurate, and timely? The dataset doesn't include data from 2023, 2024, or 2025 because of a change in the reporting of NAPLAN results which limits the timeliness of the data. The data is all accurate though, and reliable as it comes from Australian Curriculum, Assessment and Reporting Authority.
- Is it unbiased? The data is complete and paints an accurate picture of female and male performance, but the visualisations are somewhat misleading as they don't start at 0 which makes the gap in performance seem much larger than it actually is.
- Do we need to improve its security – if so, how? The system isn't secure at all but I don't think it needs to be. If I were to improve the security I would ???
- Could the UX be more accessible – if so, how? The UX 