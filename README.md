# MM2 Offset Validation Summary Tool
The MM2 Offset Validation Summary tool can be used to provide a summary (pivot table) of the CSV output file generated in the previous steps. To run the summary tool, you simply need to have Python >= 3.7 installed and run the following commands:

## Step 1) Clone the repo and install dependencies:

```commandline
git clone https://github.com/bruno-faria-aiven/mm2-offset-validation-summary.git
cd mm2-offset-validation-summary/
pip install -r requirements.txt
```

## Step 2) Build the package:

```commandline
python -m build
```
This will create a dist/ directory containing .tar.gz and .whl files.

## Step 3) Install the package locally:

```commandline
pip install .
```
This command installs your package in the current environment.

## Step 4) Run the Package from the Command Line

After installing the package, you can run your application using the command defined in pyproject.toml:
```commandline
run_offset_validation_summary <CSV_file_PATH>
```
This will execute the main() function from my_python_app/main.py and print the DataFrame as defined in the script. 

