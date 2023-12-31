# Self Study - Deddy Corbuzier ETL Project

## introduction
The Deddy Corbuzier ETL Project aims to automate the process of extracting video data from the Deddy Corbuzier YouTube channel with youtube data API and then saving it in CSV and JSON file formats. Simultaneously, the project uploads the raw data to a MongoDB server and uploads the transfomed data to posgresql database. By doing this, it simplifies the data retrieval process for analysis and insights.

![Diagram](./diagram.jpg)

## Features
- Extract video data from the "Deddy Corbuzier" YouTube channel with youtube data API.
- Save extracted data in the following formats:
    - DeddyVideo.csv: A CSV file containing video information.
    - DeddyVideo.json: A JSON file containing video information.
- Upload raw data to a MongoDB server for further analysis and storage.
- Upload transformed data to a PostgreSQL server for further analysis and storage.
