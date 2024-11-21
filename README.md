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
```bash
git clone https://github.com/yourusername/customer-information-extractor.git
cd customer-information-extractor
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up your configuration:
   - Copy `config.template.py` to `config.py`
   - Add your OpenAI API key to `config.py`

```python
OPENAI_API_KEY = "your-api-key-here"
```

## Usage

1. Place your images in the `images` folder
2. Run the script:
```bash
python extract.py
```
3. Find the extracted data in `customer_info.xlsx`

## Sample Output

### Excel File Structure (customer_info.xlsx)

The script generates an Excel file with the following columns:

| Name | Phone Number | Mobile Number | Email | Street | Street Number | City | ZIP Code | State | Country | Latitude | Longitude |
|------|--------------|---------------|-------|--------|---------------|------|----------|-------|---------|-----------|-----------|
| John Smith | +1-555-0123 | +1-555-4567 | john.smith@example.com | Oak Avenue | 123 | Springfield | 12345 | IL | USA | 39.78373 | -89.65014 |
| Sarah Johnson | +1-555-8901 | +1-555-2345 | sarah.j@example.com | Maple Street | 456 | Chicago | 60601 | IL | USA | 41.87819 | -87.62979 |
| Michael Brown | +1-555-6789 | +1-555-9012 | m.brown@example.com | Pine Road | 789 | Boston | 02108 | MA | USA | 42.35843 | -71.05977 |

### JSON Output Format

For each processed image, the script extracts information in this JSON structure:

```json
{
    "Name": "John Smith",
    "Phone Number": "+1-555-0123",
    "Mobile Number": "+1-555-4567",
    "Email": "john.smith@example.com",
    "Street": "Oak Avenue",
    "Street Number": "123",
    "City": "Springfield",
    "ZIP Code": "12345",
    "State": "IL",
    "Country": "USA",
    "Latitude": "39.78373",
    "Longitude": "-89.65014"
}
```

## File Structure

```
customer-information-extractor/
├── extract.py           # Main script for processing images
├── config.py           # Configuration file with API key (not tracked)
├── config.template.py  # Template for configuration
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── images/            # Input images folder
│   ├── card1.jpg
│   ├── card2.png
│   └── ...
└── customer_info.xlsx # Generated output file
```

## How It Works

1. **Image Processing**: 
   - Images are loaded from the `images` folder
   - Each image is converted to base64 format
   - Supported formats: JPG, JPEG, PNG

2. **API Processing**:
   - Images are sent to OpenAI's GPT-4 Vision model
   - The model analyzes the image content
   - Information is extracted in a structured JSON format

3. **Data Compilation**:
   - JSON responses are parsed and validated
   - Data is compiled into a pandas DataFrame
   - Final output is saved as an Excel spreadsheet

## Error Handling

The script includes comprehensive error handling for:

### Image Processing Errors
```python
try:
    with Image.open(image_path) as img:
        # Image processing
except Exception as e:
    print(f"Error processing image {image_path}: {str(e)}")
```

### JSON Parsing Errors
```python
try:
    customer_info = json.loads(json_str)
except json.JSONDecodeError as e:
    print(f"JSON parsing error: {str(e)}")
```

### Excel File Creation Errors
```python
try:
    df.to_excel('customer_info.xlsx', index=False)
except Exception as e:
    print(f"Excel file creation error: {str(e)}")
```

## Common Issues and Solutions

1. **API Key Error**
   ```
   Error: OpenAI API key not found
   Solution: Ensure your API key is correctly set in config.py
   ```

2. **Image Format Error**
   ```
   Error: Unable to process image
   Solution: Ensure images are in JPG, JPEG, or PNG format
   ```

3. **Excel File Access Error**
   ```
   Error: Permission denied when creating Excel file
   Solution: Close customer_info.xlsx if it's open in another program
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Security Notes

- Never commit your `config.py` file containing your API key
- Keep your API key secure and rotate it periodically
- Monitor your API usage to prevent unexpected charges

## Version History

- v1.0.0 (Initial Release)
  - Basic image processing functionality
  - Excel output generation
  - Multi-image batch processing

## Support

If you encounter any issues or have questions, please:
1. Check the Common Issues section above
2. Open an issue in the GitHub repository
3. Provide sample images (if possible) when reporting issues

## Acknowledgments

- OpenAI for providing the GPT-4 Vision API
- Contributors and maintainers of the dependent Python packages
```

The updated README now includes:
- More detailed sample output section with both Excel and JSON formats
- Code examples for error handling
- Expanded troubleshooting section
- Better organized file structure
- Support section
- More comprehensive documentation of the workflow

