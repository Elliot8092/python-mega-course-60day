import streamlit as st
import functions

file_path = "todos.txt"
todo_list = functions.read_file(file_path)

def add_todo():
    todo = st.session_state["new_todo"]
    todo_list.append(f"{todo}\n")
    functions.write_file(todo_list, file_path)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This appis to increase your productivity.")

# Print checkboxes and remove is checked
for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox == True:
        todo_list.pop(index)
        functions.write_file(todo_list, file_path)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Todo input", placeholder="Enter todo: ", 
              on_change=add_todo, key="new_todo", label_visibility="hidden")