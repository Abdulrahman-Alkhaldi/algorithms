# Process Selection Script

## Overview
This script selects processes based on their duration and value, constrained by a given time limit. It features three algorithms: Naive, Greedy, and Modified Greedy.

## Requirements
- Python 3.x

## Usage
1. **Run the Script**: Execute the script in a Python environment.
2. **Input Data**: Enter processes in the format `P1, duration1, value1, ...` followed by the time limit `T`.
3. **Output**: Results for each method are displayed, showing selected processes, total value, duration, and algorithm running time.

## Algorithms
- **Naive**: Evaluates all combinations to find the highest value within the time limit.
- **Greedy**: Selects processes based on the highest value-to-time ratio.
- **Modified Greedy**: Prioritizes processes with a higher value and shorter duration, using a modified value-to-time ratio.

## Example Input
```plaintext
Enter processes P: 1,2,10,2,3,15,3,1,7
Enter time limit T: 4
