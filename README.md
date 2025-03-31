# Graphical Abstract Visualizer for Radiation Biology Experiments

Spring 2024 | NBISC

This repository contains a data visualization pipeline developed to support the generation of publication-ready graphical abstracts for radiation biology experiments. Developed in conjunction with the NASA Biological Institutional Scientific Capability (NBISC) and UC Berkeley, the tool converts structured Excel metadata into a rich, interpretable Gantt chart-style visual summary of experimental timelines.

## Overview
This tool automates the transformation of preclinical radiation experiment metadata into intuitive visual timelines, aiding in communication, comparison, and documentation of experimental conditions. It is particularly useful for projects requiring clear visualization of irradiation schedules, subject grouping, treatment timelines, and recovery windows.

## Key Features
Supports custom Excel data input (compatible with formats used by Dynan Lab)

Visualizes key timepoints, including:

- Date of Birth (DOB)

- Irradiation Date

- Termination Date (Initial and Final)

- Encodes metadata such as gender, beam type, dose, treatment status, and group

- Annotations are included to denote treatment and control markers

- Interactive and publication-ready output built using Plotly

## Inputs & Outputs

The script expects an Excel file with the following fields, located in the Dynan Si-28 sheet (or user-specified equivalent):

- Gender

- Group

- Beam

- Dose

- DOB

- Irradiation Date

- Termination Date Initial

- Termination Date Final

- Treatment

- Subjects

- Order (used to define Y-axis sort order)

Ensure all dates are formatted correctly and categorical variables are consistent across rows.

## Installation
To install necessary dependencies:
```
pip install pandas plotly numpy 
```
Download your file of interest from SLIMS, then pass it through the Graphical Abstract Visualizer as an .xslx file. 


### Notebook

### Visual Encoding Guide
The tool uses color, opacity, labels, and annotations to encode various experimental attributes. Below is a summary of the encoding scheme used:

| Attribute |  Encoding Style  | Example |
| --------- | ---------------- | ------- |
| Gender    |    Base color    | Blue (Male), Coral (Female) |
| Beam Type	| Opacity	| High opacity for Silicon, 20% opacity for Controls |
| Treatment | Left-aligned block color | Sage Green (Treated, NR+), Burnt Orange (Untreated, NR−) |
| Group	| Y-axis sorting |	Based on Order column |
| Subjects	| Label	 | Displayed in chart text |
| Dose | Label	| Displayed in chart text |
| DOB to Irradiation | Gray pre-bars	| Visualizes lifespan before experiment start |

The legend and hover tooltips are automatically generated and synced across components.

### Sample Output
A graphical abstract will be rendered with the following layout:

<img width="1497" alt="image" src="https://github.com/user-attachments/assets/a243eb8f-8e86-454f-8983-b05ea7c25e22" />


## Customization

The script can be modified for other studies by:

- Changing the Excel sheet name or file path

- Adjusting how categorical variables (e.g., Treatment, Beam) are defined or grouped

- Extending annotations to include additional metadata (e.g., genotype, cage ID)

- Color maps and opacity rules are modular and can be updated in the assign_color() and assign_treatment_color() functions within the script.

## License
This code is licensed under the NASA License. Attribution is appreciated when used in publications or presentations.

## Acknowledgments
Developed as part of the NBISC (NASA Biological Institutional Scientific Collections) initiative.  Special thanks to the Dynan Lab for the support and validation of the data structure.

