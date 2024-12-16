import streamlit as st
from openai import OpenAI
import io
import fitz  # PyMuPDF
from docx import Document
from datetime import datetime
import config

# Function to create a single tile for input with a label above and helper text below
def create_tile_input(label, helper, key):
    st.write("**"+label+"**")
    value = st.text_input("", key=key, help=helper, placeholder="Enter " + label.lower())
    return value
def create_tile_important(label, helper, key):
    st.write("**"+label+"** *")
    value = st.text_input("", key=key, help=helper, placeholder="Enter " + label.lower())
    return value
def create_dropdown(label, options, helper, key):
    st.write("**"+label+"** *")
    # Assuming options is a list of four options you want to show in the dropdown
    value = st.selectbox("", options, key=key, help=helper)
    return value

def handle_uploaded_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        with fitz.open(stream=uploaded_file.getvalue(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(io.BytesIO(uploaded_file.getvalue()))
        text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    elif uploaded_file.type == "text/plain":
        text = str(uploaded_file.getvalue(), "utf-8")
    else:
        text = "Unsupported file type."
    return text

# Get today's date in the specified format
today_date = datetime.now().strftime("%B %d, %Y")

def app_custom_style():
    # Example of injecting raw CSS
    st.set_page_config(layout="wide")
    st.markdown("""
        <style>
        /* Background image */
        .stApp {
            background-image: url('');
            background-size: cover;
        }        
        </style>
    """, unsafe_allow_html=True)

# Call the function at the beginning of your app to apply the styles
app_custom_style()


# Main app function
def app():
    # st.set_page_config(layout="wide")

    # Begin a form context
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "submit" not in st.session_state:
        st.session_state.submit = True
    if "sys_prompt" not in st.session_state:
        st.session_state.sys_prompt = True
        
    if "student_name" not in st.session_state:
        st.session_state.student_name = ""
    if "degree" not in st.session_state:
        st.session_state.skills = ""
    if "department" not in st.session_state:
        st.session_state.department = ""
    if "year_of_admission" not in st.session_state:
        st.session_state.skills = ""
    if "technical_skills" not in st.session_state:
        st.session_state.skills = ""
    if "area_of_interest" not in st.session_state:
        st.session_state.area_of_interest = ""
        
    # if "problem_statement" not in st.session_state:
    #     st.session_state.problem_statement = ""
    if "project_title" not in st.session_state:
        st.session_state.project_title = ""
    if "project_phase" not in st.session_state:
        st.session_state.project_phase = ""
    if "preferred_learning_style" not in st.session_state:
        st.session_state.preferred_learning_style = ""
    if "project_report" not in st.session_state:
        st.session_state.project_report = ""
    if "technology_access" not in st.session_state:
        st.session_state.project_phase = ""
        
    if "today_date" not in st.session_state:
        st.session_state.today_date = today_date
    
    if "greeted" not in st.session_state:
        st.session_state.greeted = False
     # Check if file has been processed
    if "file_processed" not in st.session_state:
        st.session_state.file_processed = False
    degree = ["","B.A","M.A","B.Sc","M.Sc","B.Phil","M.Phil"]   
    department = ["","Maths","Computer Science","IT","Tamil","Computer Applications"]  
    if st.session_state.submit:
        st.title('Project Information Form')
        with st.form(key='project_info_form'):
            # Create two columns for the input fields
            col1, col2 = st.columns(2)

            # First column for inputs
            with col1:
                create_tile_important('Student Name', 'Enter the full name of the student.', 'student_name')
                st.write("---------------")
                create_dropdown('Department',department, 'Enter the department name or code.', 'department')
                st.write("---------------")
                create_tile_important('Technical Skills', 'List the skills relevant to the project.', 'technical_skills')
                st.write("---------------")
                create_tile_input('Project Title', 'Provide a title for your project if you have decided on one or else leave it blank.', 'project_title')
                st.write("---------------")
                create_tile_important('Preferred Learning Style', 'Describe how you prefer to learn new things.', 'preferred_learning_style')
                st.write("---------------")
            # Second column for inputs
            with col2:
                create_dropdown('Degree',degree, 'e.g., BA, BSc, etc.', 'degree')
                st.write("---------------")
                create_tile_important('Year of Admission', 'Year of joining the course', 'year_of_admission')
                st.write("---------------")
                create_tile_important('Areas of Interest', 'Describe your main areas of interest.', 'area_of_interest')
                st.write("---------------")
                create_tile_input('Project Phase', 'Indicate the current phase of the project. e.g., Planning, Design, Implementation, etc.', 'project_phase')
                st.write("---------------")
                create_tile_input('Technology Access', 'Information on the devices and software the you have access to', 'technology_access')
                st.write("---------------")
                
                
            # File uploader widget
            st.write("\n")
            uploaded_file = st.file_uploader("**Upload Project Report (PDF, DOCX, TXT)**", type=['pdf', 'docx', 'txt'])
            if uploaded_file is not None and not st.session_state.file_processed:
                file_text = handle_uploaded_file(uploaded_file)
                st.session_state.project_report = file_text
                st.session_state.file_processed = True  # Mark file as processed

            # Submit button for the form
            submitted = st.form_submit_button('Submit')
            if submitted:
                st.session_state.sys_prompt = f"""You are an AI mentor designed to guide students through their academic projects and capstones. Your role is to assist with the bottlenecks faced by the students in academic projects and capstones.Consider yourself as an academic who is thorough and systematic in your thought process. Your responses will be beginner friendly, to-the-point and brief. You will help in planning project milestones for different phases of the project. You will offer mentorship, suggest resources, assist with technical challenges, and provide constructive feedback. Your goal is to facilitate the student's learning process, helping them to achieve success in their academic endeavors. Dont explicitly write any code unless the student asks.
The end of the responses should be showing your readiness to guide the student to the next steps (e.g., Pick one of the choices suggested above or give me a preference, I would be happy to guide you through your next steps. Or something like this).

The profile of the student that you are currently guiding is as follows,
    Student Name: {st.session_state.student_name}
    Degree: {st.session_state.degree}
    Department: {st.session_state.department}
    Year of Admission: {st.session_state.year_of_admission}
    Technical Skills : {st.session_state.technical_skills}
    Areas of Interest : {st.session_state.area_of_interest}
    Project Title : {st.session_state.project_title}
    Project Phase : {st.session_state.project_phase}
    Preferred Learning Style : {st.session_state.preferred_learning_style}
    Technology Access: {st.session_state.technology_access}
    Project Report: {st.session_state.project_report}
    Today's Date: {st.session_state.today_date}"""
                print(st.session_state.sys_prompt)
                st.session_state.submit = False
                # You can handle the submitted data here, such as saving to a database or file
                
    
    else:
        st.title('MENTOR GPT')
        client = OpenAI(api_key=config.openai_key)
        
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-4o"
            
        st.session_state.messages.append({"role": "system", "content": st.session_state.sys_prompt }) 
        if not st.session_state.greeted:
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": "assistant", "content": f"""you are an AI mentor,make a one line greeting for a student with his/her details.
Student Name: {st.session_state.student_name}
Degree: {st.session_state.degree}
Department: {st.session_state.department}
Technical Skills : {st.session_state.technical_skills}
Areas of Interest : {st.session_state.area_of_interest}
"""}
                ],
            )
            response = str(stream.choices[0].message.content)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.greeted = True
        
        for message in st.session_state.messages:
            if not (message["role"] == "system"):
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        
        

# Run the app
if __name__ == '__main__':
    app()
