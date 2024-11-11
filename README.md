# Customer Information Extractor

This project uses OpenAI's GPT-4 Vision model to extract customer information from images and compile it into an Excel spreadsheet. It's particularly useful for digitizing customer information from business cards, forms, or any documents containing customer details.

## Features

- Extracts customer information from images including:
  - Name
  - Phone Number
  - Mobile Number
  - Email
  - Complete Address (Street, City, ZIP, State, Country)
  - Geolocation (Latitude, Longitude)
- Processes multiple images in batch
- Outputs data to an organized Excel spreadsheet
- Supports multiple image formats (PNG, JPG, JPEG)

## Prerequisites

- Python 3.7+
- OpenAI API key
- Required Python packages:
  - openai
  - Pillow (PIL)
  - pandas
  - openpyxl

## Installation

1. Clone the repository: 