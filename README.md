# SOC-Triage-System

## Project Overview
-  The goal of this system is to enhance incident response by identifying suspicious activity within system and application logs. It functions by:
1. Detecting threats and analyzing events in real-time.
2. Classifying events by severity level to rank incidents based on priority.
3. Prioritizing response efforts to ensure critical threats are addressed first.

## System Architecture
-  The system is divided into four primary components:
1. Input/Data: Reading raw system, application, and network logs from public datasets or generated sources.
2. Preprocessing & Parsing: Using Python and Pandas to normalize   timestamps and sort data by IP, User ID, or timeframe.
3. Incident Scoring & Triage: Evaluating events based on severity.
4. Output & Reporting: Producing a ranked incidents table and a summary of security metrics.

## Features & Techniques
-  Rule-based & Anomaly Detection: Identifies patterns such as brute-force or failed logins
-  Data Visualization: Uses Matplotlib and Seaborn to graph event frequency and severity.
-  Triage Effectiveness: Automatically moves the most severe incidents to the top of the analyst's queue.

## Tools
-  Python 3.x 
-  Pandas (for data manipulation) 
-  Matplotlib/Seaborn (for visualization)
-  Use SOC-Faker to generate simulated logs, network traffic, and employee data.

## Team Members (Team 1)
1. Thomas Peaslee
2. Ella Connolly
3. Alexandra Valle
4. Dakota Bowers
5. Alex Cline
