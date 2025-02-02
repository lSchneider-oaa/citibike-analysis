import subprocess
import time
import re
import statistics

scripts = [
    'C:/Users/Leon/Coding/Citi Bike/distance_analysis.py',
    'C:/Users/Leon/Coding/Citi Bike/distance_analysis_swifter.py',
    'C:/Users/Leon/Coding/Citi Bike/distance_analysis_parallelized.py',
    'C:/Users/Leon/Coding/Citi Bike/distance_analysis_parallelized_dask.py',
    'C:/Users/Leon/Coding/Citi Bike/distance_analysis_parallelized_chunks.py',
    'C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy.py',
    'C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy_usecols.py',
    'C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy_pyarrow.py',
    'C:/Users/Leon/Coding/Citi Bike/distance_analysis_numpy_pyarrow_usecols.py'
]

# Regex patterns to extract timing results from each script's output
patterns = {
    'read_time': re.compile(r'CSV read time: (\d+\.\d+) seconds'),
    'distance_time': re.compile(r'Distance calculation time: (\d+\.\d+) seconds'),
    'average_time': re.compile(r'Average distance calculation time: (\d+\.\d+) seconds'),
    'whole_time': re.compile(r'Total computation time: (\d+\.\d+) seconds')
}

# Number of runs per script
runs_per_script = 5

# Store results
results = {script: {'read_time': [], 'distance_time': [], 'average_time': [], 'whole_time': []} for script in scripts}

# Run each script multiple times
for script in scripts:
    print(f"Running benchmark for {script}...")

    for run in range(runs_per_script):
        start_time = time.time()
        try:
            # Run the script and capture output
            output = subprocess.check_output(['python', script], text=True)
            print(f"Run {run + 1}: Completed in {time.time() - start_time:.2f} seconds")

            # Extract timing data from the output
            for phase, pattern in patterns.items():
                match = pattern.search(output)
                if match:
                    results[script][phase].append(float(match.group(1)))

        except subprocess.CalledProcessError as e:
            print(f"Error running {script}: {e}")

# Calculate and print average times
print("\n--- Benchmark Results ---")
for script, times in results.items():
    print(f"\nResults for {script}:")
    for phase, values in times.items():
        if values:
            avg_time = statistics.mean(values)
            print(f"  Average {phase.replace('_', ' ')}: {avg_time:.2f} seconds (over {len(values)} runs)")
        else:
            print(f"  No data for {phase}")
