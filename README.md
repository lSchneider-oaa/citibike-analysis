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
The first iteration on computing the average distance per ride was the most obvious: I used pandas to create a dataframe from the merged csv File. Then I cleaned the dataframe from all rows with some empty entries. Next I added the distance_km column by using the star and end coordinates of each row and the geodesic method. With the mean method I was able to compute the average of all those distance entries. Already on the first run I became aware that my implementation was very inefficient as it took multiple minutes. Even though the computing power of my machine is limited and the file is of medium to large size with around 2.3 million rows that seemed to take way to long. Therefore, I did some research to improve the implementation. 

### Iteration 2: Swifter
As I initially assumed that adding the new distance_km entries to the dataframe was the bottleneck I thought about some solution to improve that process. My first idea was paralellizing the process. Swifter seemed like an appropriate tool. After some testing I quickly realized that my implementation became even worse.

### Iteration 3: Parallelized

### Iteration 4: Parallelized using Chunks

### Iteration 5: Parallelized using Dask

### Iteration 6: Swifter

### Iteration 6: Numpy

### Iteration 7: Numpy & Pyarrow

### Iteration 8: Numpy & Usecols

### Iteration 9: Numpy, Pyarrow & Usecols

## Notebook specifications
