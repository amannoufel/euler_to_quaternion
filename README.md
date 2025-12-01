# Euler to Quaternion Converter

This project contains a Python script to convert Euler angles (Roll, Pitch, Yaw) to Quaternions and vice versa. It handles edge cases such as Gimbal lock.

## Files

- `euler_quaternion_converter.py`: The main script containing the conversion functions and example usage.

## Prerequisites

- Python 3.x

## How to Run

1.  Open a terminal.
2.  Navigate to the directory containing the script.
3.  Run the script using python:

    ```bash
    python3 euler_quaternion_converter.py
    ```

## Implementation Details

### Euler to Quaternion

The script uses the standard conversion formula for the Z-Y-X rotation sequence (Yaw, then Pitch, then Roll).

### Quaternion to Euler

The script converts a quaternion $(w, x, y, z)$ back to Euler angles.

**Edge Case Handling (Gimbal Lock):**
When the pitch angle approaches $\pm 90^\circ$ ($\pm \pi/2$ radians), a singularity known as Gimbal lock occurs. In this state, the roll and yaw axes align, losing one degree of freedom. The script detects this condition (when `sin(pitch)` is close to $\pm 1$) and clamps the pitch to $\pm 90^\circ$ to avoid mathematical errors.

## Usage

You can import the functions into your own project:

```python
from euler_quaternion_converter import euler_to_quaternion, quaternion_to_euler
import math

# Convert Euler to Quaternion
w, x, y, z = euler_to_quaternion(0.1, 0.2, 0.3)

# Convert Quaternion to Euler
roll, pitch, yaw = quaternion_to_euler(w, x, y, z)
```
# euler_to_quaternion
