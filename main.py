from data_module import (
    display_dataset_preview,
    display_reading_visualisation,
    display_writing_visualisation,
    display_averages,
    search_data,
    update_data_entry,
    save_changes
)

def main_menu():
    while True:
        print("\n=== Data Viewer Interface ===")
        print("1. View dataset")
        print("2. View reading visualisation")
        print("3. View writing visualisation")
        print("4. View averages")
        print("5. Search or filter data")
        print("6. Update a data entry")
        print("7. Save changes")
        print("8. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            display_dataset_preview()
        elif choice == '2':
            display_reading_visualisation()
        elif choice == '3':
            display_writing_visualisation()
        elif choice == '4':
            display_averages()
        elif choice == '5':
            search_data()
        elif choice == '6':
            update_data_entry()
        elif choice == '7':
            save_changes()
            print("Changes saved.")
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 8.")

if __name__ == "__main__":
    main_menu()