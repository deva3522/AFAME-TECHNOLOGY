import pandas as pd

file_path = '/Users/dv/Downloads/HR Data.csv'
hr_data = pd.read_csv(file_path)

hr_data_cleaned = hr_data.drop(columns=['EmployeeCount', 'StandardHours', 'EmployeeNumber'])

hr_data_cleaned.rename(columns={
    'Attrition': 'EmployeeAttrition',
    'BusinessTravel': 'TravelFrequency',
    'DailyRate': 'DailySalary',
    'DistanceFromHome': 'CommuteDistance',
    'Education': 'EducationLevel',
    'EducationField': 'FieldOfEducation',
    'JobRole': 'Position',
    'MonthlyIncome': 'MonthlySalary',
    'NumCompaniesWorked': 'CompaniesWorked',
    'WorkLifeBalance': 'WorkLifeBalanceRating'
}, inplace=True)

hr_data_cleaned.drop_duplicates(inplace=True)

for col in hr_data_cleaned.select_dtypes(include=['object']).columns:
    hr_data_cleaned[col] = hr_data_cleaned[col].str.strip()

hr_data_cleaned.dropna(inplace=True)

cleaned_file_path = '/Users/dv/Desktop/HR Data Cleaned.csv'
hr_data_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to: {cleaned_file_path}")
