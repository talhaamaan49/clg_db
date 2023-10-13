import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector as mysql

connection = mysql.Connect(
    host = '192.168.56.1',
    user = 'webdatabase',
    password = 'webdatabase',
    database = 'college'
)

cursor = connection.cursor()


with st.sidebar:
    selected = option_menu(
        menu_title='College Database',
        options=['Admin','Student','Professor','Department','Courses','Interested?','Contact'],
        icons=['person-check-fill','person-circle','mortarboard-fill','buildings','book','pencil-fill','telephone-forward'],
        default_index=0
        
)
    
def display_table_data(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    data = cursor.fetchall()
    st.write(f"Table: {table_name}")
    for row in data:
        st.write(row)

# Function to create a new table
# def create_table():
#     table_name = st.text_input("Enter the name of the new table:")
#     if st.button("Create Table") and table_name:
#         query = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
#         cursor.execute(query)
#         st.success(f"Table '{table_name}' created successfully.")

# Function to delete a table
def delete_table():
    table_name = st.text_input("Enter the name of the table to delete:")
    if st.button("Delete Table") and table_name:
        query = f"DROP TABLE {table_name}"
        cursor.execute(query)
        st.warning(f"Table '{table_name}' deleted.")

# Function to add a new row to a table
def add_row(table_name, data):
    query = f"INSERT INTO {table_name} (name) VALUES (%s)"
    cursor.execute(query, (data,))
    connection.commit()
    st.success("Row added successfully.")

# Function to delete a row from a table
def delete_row(table_name, row_id):
    query = f"DELETE FROM {table_name} WHERE id = %s"
    cursor.execute(query, (row_id,))
    connection.commit()
    st.warning("Row deleted.")

# Streamlit UI for the Admin section
def admin_section():
    st.write("Choose the Action:")
    admin_action = st.selectbox(
        "Admin Actions",
        ["View Tables", "Delete Table", "View Table Data"],
    )

    if admin_action == "View Tables":
        tables = cursor.execute("SHOW TABLES")
        table_list = [table[0] for table in cursor.fetchall()]
        st.write("Available Tables:")
        for table_name in table_list:
            st.write(table_name)

    # elif admin_action == "Create Table":
    #     create_table()

    elif admin_action == "Delete Table":
        delete_table()

    elif admin_action == "View Table Data":
        table_name = st.selectbox('select table',('student','professor','courses','department','enrollment','interested'))
        if st.button("View Table Data") and table_name:
            display_table_data(table_name)

        if table_name == 'student':
            st.write(f"Table: {table_name}")
            with st.form("Add Row"):
                new_row_id = st.text_input("New Row ID:")
                new_row_fname = st.text_input('New Row First Name:')
                new_row_lname = st.text_input('New Row Last Name:')
                new_row_age = st.text_input('New Row Age:')
                new_row_gender = st.text_input('New Row Gender:')
                if st.form_submit_button("Add Row"):
                    add = 'insert into student values (%s,%s,%s,%s,%s)'
                    cursor.execute(add,(new_row_id,new_row_fname,new_row_lname,new_row_age,new_row_gender))
                    cursor.execute('Commit')
                    # add_row(table_name, new_row_id)

            with st.form("Delete Row"):
                row_id = st.number_input("Row ID to delete:")
                if st.form_submit_button("Delete Row"):
                    delete_row(table_name, row_id)

        elif table_name == 'professor':
            st.write(f"Table: {table_name}")
            with st.form("Add Row"):
                new_row_id = st.text_input("New Row ID:")
                new_row_fname = st.text_input('New Row First Name:')
                new_row_lname = st.text_input('New Row Last Name:')
                new_row_dept = st.text_input('New Row Department:')
                if st.form_submit_button("Add Row"):
                    add = 'insert into student values (%s,%s,%s,%s)'
                    cursor.execute(add,(new_row_id,new_row_fname,new_row_lname,new_row_dept))
                    cursor.execute('Commit')
                    # add_row(table_name, new_row_id)

            with st.form("Delete Row"):
                row_id = st.number_input("Row ID to delete:")
                if st.form_submit_button("Delete Row"):
                    delete_row(table_name, row_id)

        elif table_name == 'courses':
            st.write(f"Table: {table_name}")
            with st.form("Add Row"):
                new_row_id = st.text_input("New Row ID:")
                new_row_name = st.text_input('New Row Course Name:')
                new_row_code = st.text_input('New Row Course Code :')
                
                if st.form_submit_button("Add Row"):
                    add = 'insert into student values (%s,%s,%s)'
                    cursor.execute(add,(new_row_id,new_row_name,new_row_code))
                    cursor.execute('Commit')
                    # add_row(table_name, new_row_id)

            with st.form("Delete Row"):
                row_id = st.number_input("Row ID to delete:")
                if st.form_submit_button("Delete Row"):
                    delete_row(table_name, row_id)

        elif table_name == 'department':
            st.write(f"Table: {table_name}")
            with st.form("Add Row"):
                new_row_id = st.text_input("New Row ID:")
                new_row_name = st.text_input('New Row Department Name:')
                
                if st.form_submit_button("Add Row"):
                    add = 'insert into student values (%s,%s)'
                    cursor.execute(add,(new_row_id,new_row_name))
                    cursor.execute('Commit')
                    # add_row(table_name, new_row_id)

            with st.form("Delete Row"):
                row_id = st.number_input("Row ID to delete:")
                if st.form_submit_button("Delete Row"):
                    delete_row(table_name, row_id)

        elif table_name == 'enrollment':
            st.write(f"Table: {table_name}")
            with st.form("Add Row"):
                new_row_id = st.text_input("New Row ID:")
                new_row_name = st.text_input('New Row Student ID (From the Exisitng Student):')
                new_row_course = st.text_input('New Row Course ID (From the Existing Course)')
                new_row_date = st.date_input('Date:')
                
                if st.form_submit_button("Add Row"):
                    add = 'insert into student values (%s,%s,%s,%s)'
                    cursor.execute(add,(new_row_id,new_row_name,new_row_course,new_row_date))
                    cursor.execute('Commit')
                    # add_row(table_name, new_row_id)

            with st.form("Delete Row"):
                row_id = st.number_input("Row ID to delete:")
                if st.form_submit_button("Delete Row"):
                    delete_row(table_name, row_id)




if selected == 'Admin':
    admin_username = st.text_input('Enter the Username:')
    admin_password = st.text_input('Enter your password', type='password')
    
    if admin_password == 'webdatabase' and admin_username == 'webdatabase':
            st.write('ACCESS GRANTED')
            admin_section()

    else:
            st.write('ACCESS DENIED')


elif selected == 'Student':
    stu_id = st.text_input('Enter your Student ID :')
    stu_name = st.text_input('Enter your First Name:')
    stu_lname = st.text_input('Enter your Last Name:')
    stu_age = st.text_input('Enter your Age:')
    stu_gender = st.text_input('Enter your Gender:')
    stu_btn = st.button('Submit')
    if stu_btn:
        st.markdown(f'''
        ID ={stu_id}
        First Name = {stu_name}
        Last Name = {stu_lname}
        Age = {stu_age}
        Gender = {stu_gender}
        '''
        )
        stu_insert = "insert into student (ID,Firstname,Lastname,Age,Gender) values (%s,%s,%s,%s,%s)"
        cursor.execute(stu_insert,(stu_id,stu_name,stu_lname,stu_age,stu_gender))
        cursor.execute('commit')  

elif selected == 'Professor':
    prf_id = st.text_input('Enter your Professor ID:')
    prf_name = st.text_input('Enter your First Name:')
    prf_lname = st.text_input('Enter Your Last Name:')
    prf_dept = st.text_input('Enter your Department:')
    prf_btn = st.button('Submit')
    if prf_btn :
        st.markdown(f'''
        ID ={prf_id}
        First Name = {prf_name}
        Last Name = {prf_lname}
        Department = {prf_dept}'''
        )
        stf_insert = "insert into professor (ID,Firstname,Lastname,Department) values(%s,%s,%s,%s)"
        cursor.execute(stf_insert,(prf_id,prf_name,prf_lname,prf_dept))
        cursor.execute('commit')  
                
elif selected == 'Department':
    dept = st.button(label='Get Departments')
    # create = st.button(label='Create Department')
    if dept:
        values = 'select * from department'
        cursor.execute(values)
        res3 = cursor.fetchall()
        for i in res3:
            st.write(i)
    # elif create:
    #     dept_id = st.text_input('Enter the ID of Department:')
    #     dept_name = st.text_input('Enter the Department Name:')
    #     dept_btn = st.button(label='Submit')
    #     if dept_btn:
    #         val = 'insert into department values(%s,%s)'
    #         cursor.execute(val,(dept_id,dept_name))
    #         cursor.execute('commit')

elif selected == 'Courses':
    view = st.button(label='Get Courses')
    # cou = st.button(label='Create Course')
    if view:
        courses = 'select * from courses'
        cursor.execute(courses)
        res4 = cursor.fetchall()
        for i in res4:
            st.write(i)
    # elif cou:
    #     cou_id = st.text_input('Enter the Course ID:')
    #     cou_name = st.text_input('Enter the Course Name:')
    #     cou_code = st.text_input('Enter the Course Code:')
    #     cou_btn = st.button(label='Submit')
    #     if cou_btn:
    #         cour = 'insert into courses values(%s,%s,%s)'
    #         cursor.execute(cour,(cou_id,cou_name,cou_code))
    #         cursor.execute('commit')

elif selected == 'Interested?':
        id = st.text_input('Enter Your Name:')
        student_qlf = st.text_input('Enter Your Current Year or Qualification:')
        phone = st.text_input('Enter Your Phone Number:')
        address = st.text_input('Enter Your Address')
        email = st.text_input('Enter Your Email')
        btn = st.button(label='Submit')
        if btn:
            enrolled = 'insert into interested values (%s,%s,%s,%s,%s)'
            cursor.execute(enrolled,(id,student_qlf,phone,address,email))
            cursor.execute('commit')

elif selected == 'Contact':
    number = '8884081591'
    email = 'talhaamaan49@gmail.com'
    st.write('Phone:',number)
    st.write('Email:',email)