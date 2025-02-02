PS C:\Users\Leon\Coding\Citi Bike> & "C:/Program Files/Python313/python.exe" "c:/Users/Leon/Coding/Citi Bike/benchmarking_distance.py"
Running benchmark for C:/Users/Leon/Coding/Citi Bike/distance_analysis.py...
C:\Users\Leon\Coding\Citi Bike\distance_analysis.py:8: DtypeWarning: Columns (7) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv')
Run 1: Completed in 133.02 seconds
C:\Users\Leon\Coding\Citi Bike\distance_analysis.py:8: DtypeWarning: Columns (7) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv')
Run 2: Completed in 132.96 seconds
C:\Users\Leon\Coding\Citi Bike\distance_analysis.py:8: DtypeWarning: Columns (7) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv')
Run 3: Completed in 132.91 seconds
C:\Users\Leon\Coding\Citi Bike\distance_analysis.py:8: DtypeWarning: Columns (7) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv')
Run 4: Completed in 133.17 seconds
C:\Users\Leon\Coding\Citi Bike\distance_analysis.py:8: DtypeWarning: Columns (7) have mixed types. Specify dtype option on import or set low_memory=False.
  df = pd.read_csv('C:/Users/Leon/Coding/Citi Bike/202412-citibike-tripdata_total.csv')
Run 5: Completed in 133.49 seconds
Running benchmark for C:/Users/Leon/Coding/Citi Bike/distance_analysis_swifter.py...
Pandas Apply: 100%|█████████████████████████████████████████████████████████████████████████████████████| 2310795/2310795 [02:15<00:00, 17112.91it/s]
Run 1: Completed in 143.40 seconds
Pandas Apply: 100%|█████████████████████████████████████████████████████████████████████████████████████| 2310795/2310795 [02:15<00:00, 17116.07it/s]
Run 2: Completed in 143.29 seconds
Pandas Apply: 100%|█████████████████████████████████████████████████████████████████████████████████████| 2310795/2310795 [02:15<00:00, 17078.62it/s]
Run 3: Completed in 143.57 seconds
Pandas Apply: 100%|█████████████████████████████████████████████████████████████████████████████████████| 2310795/2310795 [02:15<00:00, 17030.90it/s]
Run 4: Completed in 144.01 seconds
Pandas Apply: 100%|█████████████████████████████████████████████████████████████████████████████████████| 2310795/2310795 [02:15<00:00, 17115.75it/s]
Run 5: Completed in 143.40 seconds
Running benchmark for C:/Users/Leon/Coding/Citi Bike/distance_analysis_parallelized.py...
Run 1: Completed in 10.50 seconds
Run 2: Completed in 10.47 seconds
Run 3: Completed in 10.45 seconds
Run 4: Completed in 10.60 seconds
Run 5: Completed in 10.46 seconds
Running benchmark for C:/Users/Leon/Coding/Citi Bike/distance_analysis_parallelized_dask.py...
Run 1: Completed in 14.95 seconds
Run 2: Completed in 15.69 seconds
Run 3: Completed in 14.97 seconds
Run 4: Completed in 14.89 seconds
Run 5: Completed in 14.93 seconds
Running benchmark for C:/Users/Leon/Coding/Citi Bike/distance_analysis_parallelized_chunks.py...
Run 1: Completed in 5.28 seconds
Run 2: Completed in 5.24 seconds
Run 3: Completed in 5.17 seconds
Run 4: Completed in 5.29 seconds
Run 5: Completed in 5.24 seconds
Running benchmark for C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy.py...
Run 1: Completed in 7.21 seconds
Run 2: Completed in 7.09 seconds
Run 3: Completed in 7.19 seconds
Run 4: Completed in 7.10 seconds
Run 5: Completed in 7.06 seconds
Running benchmark for C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy_usecols.py...
Run 1: Completed in 2.30 seconds
Run 2: Completed in 2.32 seconds
Run 3: Completed in 2.34 seconds
Run 4: Completed in 2.33 seconds
Run 5: Completed in 2.33 seconds
Running benchmark for C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy_pyarrow.py...
Run 1: Completed in 1.94 seconds
Run 2: Completed in 1.94 seconds
Run 3: Completed in 1.93 seconds
Run 4: Completed in 1.95 seconds
Run 5: Completed in 1.96 seconds
Running benchmark for C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy_pyarrow_usecols.py...
Run 1: Completed in 0.82 seconds
Run 2: Completed in 0.88 seconds
Run 3: Completed in 0.84 seconds
Run 4: Completed in 0.82 seconds
Run 5: Completed in 0.86 seconds

--- Benchmark Results ---

Results for C:/Users/Leon/Coding/Citi Bike/distance_analysis.py:
  Average read time: 4.04 seconds (over 5 runs)
  Average distance time: 127.66 seconds (over 5 runs)
  Average average time: 0.00 seconds (over 5 runs)
  Average whole time: 132.27 seconds (over 5 runs)

Results for C:/Users/Leon/Coding/Citi Bike/distance_analysis_swifter.py:
  Average read time: 6.21 seconds (over 5 runs)
  Average distance time: 135.58 seconds (over 5 runs)
  Average average time: 0.00 seconds (over 5 runs)
  Average whole time: 142.02 seconds (over 5 runs)

Results for C:/Users/Leon/Coding/Citi Bike/distance_analysis_parallelized.py:
  Average read time: 6.44 seconds (over 5 runs)
  Average distance time: 1.22 seconds (over 5 runs)
  Average average time: 0.00 seconds (over 5 runs)
  Average whole time: 9.65 seconds (over 5 runs)

Results for C:/Users/Leon/Coding/Citi Bike/distance_analysis_parallelized_dask.py:
  Average read time: 0.01 seconds (over 5 runs)
  Average distance time: 0.01 seconds (over 5 runs)
  Average average time: 13.97 seconds (over 5 runs)
  Average whole time: 14.00 seconds (over 5 runs)

Results for C:/Users/Leon/Coding/Citi Bike/distance_analysis_parallelized_chunks.py:
  No data for read_time
  No data for distance_time
  Average average time: 0.00 seconds (over 5 runs)
  Average whole time: 4.79 seconds (over 5 runs)

Results for C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy.py:
  Average read time: 6.50 seconds (over 5 runs)
  Average distance time: 0.10 seconds (over 5 runs)
  Average average time: 0.00 seconds (over 5 runs)
  Average whole time: 6.61 seconds (over 5 runs)

Results for C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy_usecols.py:
  Average read time: 1.76 seconds (over 5 runs)
  Average distance time: 0.11 seconds (over 5 runs)
  Average average time: 0.00 seconds (over 5 runs)
  Average whole time: 1.88 seconds (over 5 runs)

Results for C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy_pyarrow.py:
  Average read time: 1.32 seconds (over 5 runs)
  Average distance time: 0.11 seconds (over 5 runs)
  Average average time: 0.00 seconds (over 5 runs)
  Average whole time: 1.43 seconds (over 5 runs)

Results for C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy_pyarrow_usecols.py:
  Average read time: 0.23 seconds (over 5 runs)
  Average distance time: 0.11 seconds (over 5 runs)
  Average average time: 0.00 seconds (over 5 runs)
  Average whole time: 0.36 seconds (over 5 runs)
