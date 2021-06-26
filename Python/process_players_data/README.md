# Process FIFA© 2017 players data using Python
Using Python, you must find the best players, the most 
expensive ones and what are their nationalities.

## Answer the following questions: 

**Q1.** How many unique nationalities (column `nationality`) exist on the file?

**Q2.** How many unique clubs (column `club`) exist on the file?

**Q3.** List the full name of the first 20 players on the column  `full_name`.

**Q4.** Who are the top 10 players who made more money (use the columns `full_name` and `eur_wage`)?

**Q5.** Who are the 10 oldest players?

**Q6.** Count how many players have the same age. To do this, create a dictionary where the keys are the age
and the values are the counter.

*All questions refer to the file `data.csv`.* 

## Requirements

Use Python 3.6 (or newer) and the pip package manager.

You **CANNOT** use Pandas or NumPy to solve this challenge.

To run the validation tests, install Pytest (in the 
requirements):

```sh
pip install -r requirements.txt
```

And run the tests:

```sh
pytest test_main.py
```

## Details

More details can be found in comments in the file _main.py_
