from data_module import (
    display_dataset_preview,
    display_reading_visualisation,
    display_writing_visualisation,
    display_averages,
)

def main_menu():
    while True:
        print("\n=== Data Viewer Interface ===")
        print("1. View dataset")
        print("2. View reading visualisation")
        print("3. View writing visualisation")
        print("4. View averages")
        print("5. Exit")

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
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()