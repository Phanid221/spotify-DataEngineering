# Spotify - End to End DataEngineering Project - AWS
## Project Overview:
* This project focuses on implementing a robust data pipeline and analytics solution for Spotify data using AWS services. Data is collected from the Spotify API and stored in AWS S3 as the primary storage. The pipeline utilizes AWS Lambda for preprocessing, where views are generated, and the data is transformed and organized into a star schema for improved analysis and understanding.
* The transformed data is then stored in a different folder in S3, creating a clean and structured dataset. AWS Athena is used to query the processed data directly from S3, enabling efficient analysis. Finally, Amazon QuickSight is leveraged to visualize insights and derive meaningful analytics from the data, showcasing trends and patterns within the Spotify dataset.

## Key Technologies:

* Spotify API: Data collection source
* AWS S3: Data storage and organization
* AWS Lambda: Data preprocessing and transformation
* AWS Athena: Query execution and analysis
* Amazon QuickSight: Data visualization
This project demonstrates the integration of cloud services to automate and streamline data processing, enhance analytical capabilities, and deliver actionable insights.
