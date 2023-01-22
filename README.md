# whatday

whatday is a Python application for determining the weekday of a given date.

## Installation

As a standalone script you do not need to install the application. Simply download the script and run it, after
installing the dependencies and activating the environment.

```bash
conda env update -f environment.yml
```

To update the dependencies, run the following command:

```bash
conda env update -f environment.yml --prune
```

To activate the environment, run the following command:

```bash
conda activate whatday
```

## Usage

Either specify the year, month and day as positional arguments or use the optional arguments. Per default the current
date is used. If one argument stays unspecified, the current date's is used for that argument.

```bash
python3 whatday.py [-h] [-Y YEAR] [-m MONTH] [-d DAY] YEAR MONTH DAY
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GPL-3.0-or-later](https://choosealicense.com/licenses/gpl-3.0/)
