# Mentor GPT - Student Mentorship App

## Overview
Mentor GPT is a Streamlit-based web application designed to gather detailed information about students and mentor them through their academic projects and capstones. It uses OpenAI's GPT models to provide tailored mentorship based on the student's profile, technical skills, areas of interest, and project details.

The application enables students to upload project reports, fill out key academic and project-related information, and receive guidance on their projects. The AI mentor provides constructive feedback, plans project milestones, and assists with technical challenges, ensuring the student achieves their academic goals.

---

## Features
- **User-Friendly Form**: Collects student details such as name, degree, department, technical skills, areas of interest, and project phase.
- **File Upload**: Accepts project reports in PDF, DOCX, and TXT formats, extracting and processing the content for mentorship.
- **Dynamic Mentorship**: Uses OpenAI's GPT models to mentor students based on their profile and project requirements.
- **Customizable Input Fields**: Tile-based inputs for user data collection, including dropdowns and text fields.
- **Styling and Layout**: Modern UI with wide layout and optional background styling.
- **Interactive Chat**: Students can engage with the AI mentor for further guidance or clarifications.

---

## Installation and Setup
### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/mentor-gpt.git
   cd mentor-gpt
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure OpenAI API:
   - Create a `config.py` file in the root directory.
   - Add the following:
     ```python
     openai_key = "your_openai_api_key"
     ```

4. Run the application:
   ```bash
   streamlit run mentor_gpt_1.py
   ```

5. Access the app:
   Open the provided local URL in your browser.

---

## How It Works

### Student Information Form
- **Inputs**:
  - Student's name, degree, department, year of admission.
  - Technical skills, areas of interest, and preferred learning style.
  - Current project phase and technology access.
- **File Upload**:
  - Supports PDF, DOCX, and TXT formats for project reports.

### AI Mentorship
- **Profile-Based Guidance**:
  - Generates a tailored prompt using the student's inputs.
  - Creates milestones, resources, and actionable suggestions for the student's project.
- **Interactive Chat**:
  - Students can ask additional questions or clarify doubts.
  - AI responds with beginner-friendly, concise advice.

---

## Key Components

### Input and Form Functions
- **`create_tile_input`**: Generates a labeled input field with optional helper text.
- **`create_tile_important`**: Similar to `create_tile_input` but marks the field as required.
- **`create_dropdown`**: Creates a dropdown with customizable options.

### File Handling
- **`handle_uploaded_file`**:
  - Reads uploaded files and extracts text based on file type (PDF, DOCX, or TXT).

### Mentorship Logic
- **System Prompt**:
  - The AI mentor uses a dynamically created system prompt containing student information to provide personalized guidance.

### Styling
- **`app_custom_style`**:
  - Custom CSS for background styling and layout adjustments.

---

## Example Use Case

1. **Step 1**: The student opens the app and fills out the form with their details.
2. **Step 2**: They upload their project report for review.
3. **Step 3**: Submit the form to generate a tailored mentorship profile.
4. **Step 4**: Interact with the AI mentor for project planning, technical guidance, or general advice.

---

## Future Improvements
- **Add Analytics**: Track mentorship interactions and provide progress reports.
- **Enhanced File Support**: Include support for other document types like PPTX or XLSX.
- **Resource Suggestions**: Integrate links to articles, tutorials, or courses based on student inputs.
- **Multi-User Support**: Enable account creation and personalized sessions for multiple users.

---

## Technologies Used
- **Frontend**: Streamlit for UI and interaction.
- **Backend**: OpenAI GPT models for generating mentorship responses.
- **File Handling**: PyMuPDF and `python-docx` for extracting text from uploaded documents.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author
For any questions or feedback, feel free to reach out to:
- **Name**: Arun Vignesh Nedunchezhian
--- 

Happy mentoring!
