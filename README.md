# citibike-analysis
This repository contains an in-depth analysis and diverse visualizations of the Citi Bike Rides in New York City in December 2024.


## Data

This project uses data from the **[Citi Bike Trip Data](https://citibikenyc.com/system-data)**. You can download the dataset directly from their website or just click **[here](https://s3.amazonaws.com/tripdata/202412-citibike-tripdata.zip)**.

I played around with using sqlite3 to use SQL and also analyzed it using just pandas. In both cases I used combine_csv.py in file-processing to combine the three csv into one large file.

To replicate the analysis: -> I have to adjust this.
1. Download the dataset from the link above.
2. Place the file(s) in the `data/` folder of this repository (create the folder if it doesn’t exist).

**Note**: The dataset is not included in this repository due to size constraints.

For startes I wanted to get an onverview over the data. I ran df.info() to get an understanding for the columns, used dropna() to get rid of faulty rows and printed to number of distinct entries in the relevant columns.

## Ride Distance Analysis

The first question that popped into my mind was the average ride distance using the bikes. For startes I decided to go with the straight-line distance to minimize complexity. Still, with my first implementation I ran into a computation time of over three minutes. Due to some optimization steps I was able to get the whole thing running in less then one second. I will outline the steps and progress in the following.

### Iteration 1: Using geopy.distance

### Iteration 2:

### Iteration 3:

### Iteration 4:

### Iteration 5:

## Notebook specifications
