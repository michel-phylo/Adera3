import os
import subprocess

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the notebook paths and names
notebook_paths = {
    1: ("Adera_CNV_data_20_TYPES_27_JUNE_CNN_COMPLETE.ipynb", "General analysis using CNN"),
    2: ("Adera_CNV_data_20_TYPES_27_JUNE_RELU_COMPLETE.ipynb", "General analysis using RELU"),
    3: ("Adera_MAKARIOUS_f_specific+parameters+CNV1.ipynb", "Female specific cancer"),
    4: ("Adera_MAKARIOUS_BRAIN+CNV1.ipynb", "Brain cancer"),
    5: ("Adera_MAKARIOUS_exec+system+CNV1.ipynb", "Excretory system cancer"),
    6: ("Copy of dera_MAKARIOUS_2 TYPES+Digestive+system+CNV1.ipynb", "Digestive system cancer"),
    7: ("notatnika Adera_MAKARIOUS+Godly_Male.ipynb", "Male specific cancer")
}

def run_notebook(choice):
    notebook_path, notebook_name = notebook_paths.get(choice)
    notebook_full_path = os.path.join(script_dir, notebook_path)
    print(notebook_full_path)
    if os.path.isfile(notebook_full_path):
        print(f"Running {notebook_name}...")
        subprocess.run(["py", "-m", "notebook",notebook_full_path])
    else:
        print(f"Error: The specified notebook '{notebook_path}' does not exist.")

def main():
    print("Select a notebook to run:")
    for key, value in notebook_paths.items():
        print(f"{key}: {value[1]}")

    choice = int(input("Enter your choice (1-7): "))
    try:
        if choice in notebook_paths.keys():
            run_notebook(choice)
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    while True:
        main()
