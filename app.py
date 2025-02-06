from symptom_checker import SymptomChecker  # Assuming the Jupyter Notebook code is converted into a module

import streamlit as st

def main():
    st.title("Symptom Checker")
    
    st.write("Please enter your symptoms below:")
    
    symptoms_input = st.text_input("Symptoms (comma-separated):")
    
    if st.button("Check Symptoms"):
        if symptoms_input:
            symptoms = [symptom.strip() for symptom in symptoms_input.split(",")]
            checker = SymptomChecker()
            result = checker.check_symptoms(symptoms)  # Assuming check_symptoms is a method in the SymptomChecker class
            
            st.write("Possible conditions:")
            st.write(result)
        else:
            st.warning("Please enter at least one symptom.")

if __name__ == "__main__":
    main()