# **This Project is used to make preprocessing on 4 different datasets using various methods**

## **The first dataset link:**

[fitness-exercises-using-bfp-and-bmi](https://www.kaggle.com/datasets/mustafa20635/fitness-exercises-using-bfp-and-bmi?select=final_dataset_BFP+.csv)

## The second dataset link:

[fitness-tracker-dataset](https://www.kaggle.com/datasets/nadeemajeedch/fitness-tracker-dataset)

## The Third dataset link:

[workout-and-fitness-tracker-data](https://www.kaggle.com/datasets/adilshamim8/workout-and-fitness-tracker-data)

## The Fourth dataset link:

[bmi-data](https://www.kaggle.com/datasets/freego1/bmi-data)

# Preprocessing

## First dataset

### Removing the unwanted columns

### Switching the positions of some columns so it fits the order of other datasets

### Rename columns so we can prevent naming conventions

### Adding BMI Category column

## Second dataset

### Keeping only the columns that we need for calculating the labels

### Filiing the null values using mean

### Calculating the BMI and Adding it in a column

### Rename columns so we can prevent naming conventions

### Adding BMI Category column

## Third dataset

### Removing some rows because we couldn't fill them in a logical way

### Rename columns so we can prevent naming conventions

### Changing the values from cm to meter to insure accurecy of calculations

### Calculating the BMI and Adding it in a column

### Adding BMI Category column

## Fourth dataset

### Switch the position of some columns to match the other data sets

### Changing the values from Inches to meters and from pounds to Kg to insure Accurecy of calculations

### Rename columns to prevent naming conventions

### Filling null values using mean

### Calculating the BMI and Adding it in a column

### Adding BMI Category column

## After the preprocessing and merging:

The data will have 41730 rows and 6 columns the label columns are the last two [ 'BMI' , 'BMI Category' ]

##### Note: The gender column might have "Other" as a value in it. It means that the person didn't want to say they gender
