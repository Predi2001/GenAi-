import streamlit as st

quiz_categories = {
    "Computer Science": [
       {
            "question": "1.What does CPU stand for?",
            "options": ["Central Processing Unit", "Central Process Unit", "Computer Personal Unit", "Central Processor Unit"],
            "answer": "Central Processing Unit"
        },
        {
            "question": "2.What is the brain of the computer?",
            "options": ["Motherboard", "RAM", "CPU", "Hard Drive"],
            "answer": "CPU"
        },
        {
            "question": "3.Which of the following is an example of an input device?",
            "options": ["Printer", "Monitor", "Keyboard", "Speaker"],
            "answer": "Keyboard"
        },
        {
            "question": "4.What is the main function of the ALU?",
            "options": ["Store data", "Perform arithmetic and logic operations", "Control computer operations", "Manage memory"],
            "answer": "Perform arithmetic and logic operations"
        },
        {
            "question": "5.What does 'HTTP' stand for?",
            "options": ["Hypertext Transfer Protocol", "Hypertext Transfer Program", "Hypertext Transmission Protocol", "Hyper Transfer Text Protocol"],
            "answer": "Hypertext Transfer Protocol"
        },
        {
            "question": "6.Which language is considered the mother of all programming languages?",
            "options": ["C", "Java", "Assembly", "FORTRAN"],
            "answer": "Assembly"
        },
        {
            "question": "7.What is the permanent memory built into your computer called?",
            "options": ["RAM", "ROM", "CPU", "Hard Drive"],
            "answer": "ROM"
        },
        {
            "question": "8.Which part of the computer is used for long-term data storage?",
            "options": ["CPU", "RAM", "Hard Drive", "Motherboard"],
            "answer": "Hard Drive"
        },
        {
            "question": "9.What does GPU stand for?",
            "options": ["Graphics Processing Unit", "General Processing Unit", "Gaming Processing Unit", "Graphical Processing Unit"],
            "answer": "Graphics Processing Unit"
        },
        {
            "question": "10.Which company developed Python programming language?",
            "options": ["Google", "Facebook", "Microsoft", "Dropbox"],
            "answer": "Dropbox"
        },
       
    ],
    "General Knowledge": [
        {
            "question": "1.What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "answer": "Paris"
        },
        {
            "question": "2.What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Jupiter"
        },
   
    ]
}

if 'quiz_state' not in st.session_state:
    st.session_state.quiz_state = {
        "current_question": 0,
        "score": 0,
        "selected_category": None
    }

def main():
    st.title("Quiz App")
    

    selected_category = st.selectbox("Choose quiz category:", options=["Computer Science", "General Knowledge"])
    st.session_state.quiz_state["selected_category"] = selected_category

 
    if selected_category:
        quiz_questions = quiz_categories[selected_category]
        current_question = st.session_state.quiz_state["current_question"]
        question = quiz_questions[current_question]

     
        st.header(question["question"])

       
        options = question["options"]
        selected_option = st.radio("Choose your answer:", options)

   
        if st.button("Submit"):
            if selected_option == question["answer"]:
                st.session_state.quiz_state["score"] += 1
                st.success("Correct!")
            else:
                st.error("Incorrect!")

        
            if current_question + 1 < len(quiz_questions):
                st.session_state.quiz_state["current_question"] += 1
            else:
                st.write(f"Quiz Completed! Your final score is {st.session_state.quiz_state['score']}/{len(quiz_questions)}.")
                st.session_state.quiz_state["current_question"] = 0
                st.session_state.quiz_state["score"] = 0
                st.session_state.quiz_state["selected_category"] = None

 
    if st.session_state.quiz_state["selected_category"] is None:
        if st.button("Retry Quiz"):
            st.session_state.quiz_state["current_question"] = 0
            st.session_state.quiz_state["score"] = 0

if __name__ == "__main__":
    main()
