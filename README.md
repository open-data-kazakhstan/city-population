# Population of Cities in Kazakhstan 2022

## Installation

To begin using the project, follow the steps below:

1. Clone the repository:
    ```shell
    $ git clone https://github.com/your-username/city-population.git
    ```

2. Create and activate a virtual environment:
    ```bash
    pip install venv
    python -m venv /path/to/localrepo
    cd /path/to/localrepo
    Scripts/activate  # For Windows users
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script (data transformation):
    ```bash
    python scripts/transform.py
    ```

## Data

Population data is sourced from [stat.gov](https://stat.gov).

- `archive/source.xlsx`: Raw data of population of Kazakhstan as of January 1, 2023.
- `data/city_population.csv`: Cleaned version containing cities with more than 45,000 population.

## Scripts

- `package.py`: Used to create or update the datapackage.json file containing metadata about the dataset.
- `transform.py`: Used to convert the source.xlsx file to a CSV format for easier processing.

## License

The dataset is available under the appropriate license terms from [stat.gov](https://stat.gov).

