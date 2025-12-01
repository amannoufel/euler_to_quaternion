import math

def euler_to_quaternion(roll, pitch, yaw):
    """
    Convert Euler angles (roll, pitch, yaw) to Quaternion (w, x, y, z).
    
    Args:
        roll (float): Rotation around x-axis in radians.
        pitch (float): Rotation around y-axis in radians.
        yaw (float): Rotation around z-axis in radians.
        
    Returns:
        tuple: (w, x, y, z) representing the quaternion.
    """
    
    # Abbreviations for the various angular functions
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return w, x, y, z

def quaternion_to_euler(w, x, y, z):
    """
    Convert Quaternion (w, x, y, z) to Euler angles (roll, pitch, yaw).
    
    Args:
        w, x, y, z (float): Components of the quaternion.
        
    Returns:
        tuple: (roll, pitch, yaw) in radians.
    """
    
    # Pitch (y-axis rotation)
    sinp = 2 * (w * y - z * x)
    if abs(sinp) >= 0.99999:
        # Gimbal lock case: use 90 degrees if out of range
        pitch = math.copysign(math.pi / 2, sinp)
        
        # When pitch is +/- 90 degrees, roll and yaw are ambiguous.
        # We set roll to 0 and calculate yaw.
        # For pitch = +90, yaw = -2 * atan2(x, w)
        # For pitch = -90, yaw = +2 * atan2(x, w)
        
        if sinp > 0:
             roll = 0
             yaw = -2 * math.atan2(x, w)
        else:
             roll = 0
             yaw = 2 * math.atan2(x, w)
             
    else:
        pitch = math.asin(sinp)
        
        # Roll (x-axis rotation)
        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = math.atan2(sinr_cosp, cosr_cosp)

        # Yaw (z-axis rotation)
        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = math.atan2(siny_cosp, cosy_cosp)

    return roll, pitch, yaw

def main():
    print("Euler to Quaternion and Vice Versa Converter")
    print("--------------------------------------------")
    
    # Example 1: Identity
    r, p, y = 0, 0, 0
    print(f"\nInput Euler (rad): Roll={r}, Pitch={p}, Yaw={y}")
    q = euler_to_quaternion(r, p, y)
    print(f"Quaternion: w={q[0]:.4f}, x={q[1]:.4f}, y={q[2]:.4f}, z={q[3]:.4f}")
    e = quaternion_to_euler(*q)
    print(f"Recovered Euler: Roll={e[0]:.4f}, Pitch={e[1]:.4f}, Yaw={e[2]:.4f}")

    # Example 2: 90 degrees yaw
    r, p, y = 0, 0, math.pi/2
    print(f"\nInput Euler (rad): Roll={r}, Pitch={p}, Yaw={y:.4f}")
    q = euler_to_quaternion(r, p, y)
    print(f"Quaternion: w={q[0]:.4f}, x={q[1]:.4f}, y={q[2]:.4f}, z={q[3]:.4f}")
    e = quaternion_to_euler(*q)
    print(f"Recovered Euler: Roll={e[0]:.4f}, Pitch={e[1]:.4f}, Yaw={e[2]:.4f}")

    # Example 3: Gimbal Lock case (Pitch = 90 degrees)
    # When pitch is 90 degrees, roll and yaw become ambiguous. 
    # The system typically resolves this by setting one to 0.
    r, p, y = 0, math.pi/2, 0
    print(f"\nInput Euler (rad): Roll={r}, Pitch={p:.4f}, Yaw={y}")
    q = euler_to_quaternion(r, p, y)
    print(f"Quaternion: w={q[0]:.4f}, x={q[1]:.4f}, y={q[2]:.4f}, z={q[3]:.4f}")
    e = quaternion_to_euler(*q)
    print(f"Recovered Euler: Roll={e[0]:.4f}, Pitch={e[1]:.4f}, Yaw={e[2]:.4f}")
    
    # Example 4: Random values
    r, p, y = 0.5, -0.2, 1.0
    print(f"\nInput Euler (rad): Roll={r}, Pitch={p}, Yaw={y}")
    q = euler_to_quaternion(r, p, y)
    print(f"Quaternion: w={q[0]:.4f}, x={q[1]:.4f}, y={q[2]:.4f}, z={q[3]:.4f}")
    e = quaternion_to_euler(*q)
    print(f"Recovered Euler: Roll={e[0]:.4f}, Pitch={e[1]:.4f}, Yaw={e[2]:.4f}")

if __name__ == "__main__":
    main()
