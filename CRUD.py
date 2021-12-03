student = []

def show_data_student():
    print(student)

def insert_data_student():
    total_new_data = int(input("Input total of the new data : "))
    for i in range(total_new_data):
        new_data = input(f"Enter student's name (data {i+1}): ")
        student.append(new_data)
    return student

def delete_data_student():
    for (i,item) in enumerate(student):
        print(i, '-->', item)
    del_data = int(input("Input index data you'd like to delete : "))
    student.pop(del_data)
    return student

def edit_data_student():
    for (i,item) in enumerate(student):
        print(i, '-->', item)
    index_edit = int(input("Input index data you'd like to edit : "))
    student[index_edit] = input("input new name : ")
    return student

def main():
    while True:
        print('\n')
        print("---------------Menu---------------")
        print("[1]  Show Data")
        print("[2]  Insert Data")
        print("[3]  Edit Data")
        print("[4]  Delete Data")
        print("[5]  Exit")
        print("----------------------------------")

        opsi_menu = input("Please input your menu [1/2/3/4/5]: ")

        if opsi_menu == '1':
            show_data_student()
        elif opsi_menu == '2':
            insert_data_student()
        elif opsi_menu == '3':
            edit_data_student()
        elif opsi_menu == '4':
            delete_data_student()
        elif opsi_menu == '5':
            print('Thank you for using CRUD \n Have a nice day!')
            break
        else:
            print("Please input correctly.")

main()