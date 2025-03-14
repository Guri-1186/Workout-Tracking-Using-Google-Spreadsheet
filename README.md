# Exercise Tracking App

This Python script allows users to track their workouts by logging exercises, duration, and calories burned. It integrates with the **Nutritionix API** to analyze exercise details and stores the data in a **Google Sheet** via the **Sheety API**. Additionally, environment variables are used to keep sensitive information secure.

## Features

- User inputs the exercise they performed.
- The **Nutritionix API** processes the input and returns workout details.
- Data is logged to a **Google Sheet** using the **Sheety API**.
- Environment variables are used for API keys and authentication.

## Technologies Used

- **Python**
- **Requests Library** (for API calls)
- **dotenv** (for environment variable management)
- **Nutritionix API**
- **Sheety API**

## Prerequisites

Before running the script, make sure you have:

- Python installed (3.x recommended)
- Required dependencies installed (`requests`, `dotenv`)
