"""
Created on Tue May 16 10:10:15 2023

@author: AMIT THAKUR
Project Title: Driving Behavior Analysis

Description:
Developed a Python project to analyze driving behavior based on various parameters. Implemented a scoring system to evaluate driving performance using different driving data such as speed, acceleration, braking, lane discipline, tailgating, and turn signal usage.


Speed: Speed refers to the rate at which a vehicle is traveling, usually measured in kilometers per hour (km/h) or miles per hour (mph). It indicates how fast or slow the vehicle is moving.

Acceleration: Acceleration measures the rate of change in speed over time. It represents how quickly the vehicle can increase its speed. Positive acceleration means the vehicle is speeding up, while negative acceleration (also known as deceleration or braking) means the vehicle is slowing down.

Braking: Braking is the process of slowing down or stopping a vehicle using the brakes. It is usually measured in the time it takes for a vehicle to come to a complete stop from a specific speed.

Lane Discipline: Lane discipline indicates how well a driver maintains their position within their designated lane on the road. Good lane discipline means staying within the lane without unnecessary lane changes.

Tailgating: Tailgating refers to driving too closely to the vehicle in front, with insufficient distance to react in case of sudden braking or emergencies.

Turn Signal Usage: Turn signal usage measures how frequently a driver uses their vehicle's turn signals when changing lanes or making turns. It indicates how well a driver communicates their intentions to other road users.

Key Contributions:

-Collected and processed driving data for analysis.
-Developed functions to normalize data to a 0-100 scale for fair comparison.
-Implemented the Interquartile Range (IQR) method to handle outliers effectively.
-Designed scoring functions for each driving parameter, weighted based on importance.
-Calculated overall driver scores using the scoring weights and normalized values.
-Technologies Used:
-Python, NumPy, Data Handling, Data Analysis, Scoring Algorithms

Outcome:
The project successfully assessed driving behavior, providing valuable insights for improving road safety and driver performance. The project demonstrates proficiency in Python programming, data handling, and statistical analysis.
"""
import numpy as np

# Sample data for each driving parameter
speed_data = [60, 45, 50, 70, 55]
acceleration_data = [2.5, 1.2, 1.8, 3.0, 1.5]
braking_data = [1.5, 0.8, 1.2, 2.5, 0.9]
# cornering_data = [20, 15, 12, 22, 14]
lane_discipline_data = [2, 1, 1, 3, 1]
tailgating_data = [3, 1, 2, 4, 1]
turn_signal_data = [10, 12, 11, 8, 13]

# Scoring parameters
scoring_weights = {
    "speed": 0.25,
    "acceleration": 0.20,
    "braking": 0.20,
    # "cornering": 0.15,
    "lane_discipline": 0.10,
    "tailgating": 0.15,
    "turn_signal": 0.10
}

# Function to calculate the IQR

# Approach to detect outliers is using the Interquartile 
# Range (IQR) method. The IQR is calculated as the difference between 
# the 75th percentile (Q3) and the 25th percentile (Q1) of the data. 
# Any data points falling below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR are considered outliers.
def calculate_iqr(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    return iqr

# Function to remove outliers using the IQR method
def remove_outliers_iqr(data):
    iqr = calculate_iqr(data)
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

# Function to normalize values to a 0-100 scale
def normalize(values):
    min_value = min(values)
    max_value = max(values)
    return [(value - min_value) / (max_value - min_value) * 100 for value in values]

# Scoring functions with outlier handling
def calculate_speed_score(speed_data):
    filtered_speed_data = remove_outliers_iqr(speed_data)
    normalized_speed_data = normalize(filtered_speed_data)
    return normalized_speed_data

def calculate_acceleration_score(acceleration_data):
    filtered_acceleration_data = remove_outliers_iqr(acceleration_data)
    normalized_acceleration_data = normalize(filtered_acceleration_data)
    return normalized_acceleration_data

def calculate_braking_score(braking_data):
    filtered_braking_data = remove_outliers_iqr(braking_data)
    normalized_braking_data = normalize(filtered_braking_data)
    return normalized_braking_data



def calculate_lane_discipline_score(lane_discipline_data):
    filtered_lane_discipline_data = remove_outliers_iqr(lane_discipline_data)
    normalized_lane_discipline_data = normalize(filtered_lane_discipline_data)
    return normalized_lane_discipline_data

def calculate_tailgating_score(tailgating_data):
    filtered_tailgating_data = remove_outliers_iqr(tailgating_data)
    normalized_tailgating_data = normalize(filtered_tailgating_data)
    return normalized_tailgating_data

def calculate_turn_signal_score(turn_signal_data):
    filtered_turn_signal_data = remove_outliers_iqr(turn_signal_data)
    normalized_turn_signal_data = normalize(filtered_turn_signal_data)
    return normalized_turn_signal_data

# Calculate component scores
speed_scores = calculate_speed_score(speed_data)
acceleration_scores = calculate_acceleration_score(acceleration_data)
braking_scores = calculate_braking_score(braking_data)

lane_discipline_scores = calculate_lane_discipline_score(lane_discipline_data)
tailgating_scores = calculate_tailgating_score(tailgating_data)
turn_signal_scores = calculate_turn_signal_score(turn_signal_data)

# Compute overall driver scores
driver_scores = [
    scoring_weights["speed"] * speed_score +
    scoring_weights["acceleration"] * acceleration_score +
    scoring_weights["braking"] * braking_score +
    scoring_weights["lane_discipline"] * lane_discipline_score +
    scoring_weights["tailgating"] * tailgating_score +
    scoring_weights["turn_signal"] * turn_signal_score
    for speed_score, acceleration_score, braking_score, lane_discipline_score, tailgating_score, turn_signal_score in zip(
        speed_scores, acceleration_scores, braking_scores, lane_discipline_scores, tailgating_scores, turn_signal_scores
    )
]

print("Driver Scores:", driver_scores)
