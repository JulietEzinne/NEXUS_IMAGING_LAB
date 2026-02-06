# Nexus Imaging Lab: Clinical Logic Exercise
patient_name = "NK"
modality = "X-Ray"
base_kv = 60
thickness_cm = 18

# Logic: Calculate kV based on body part thickness (The 2kV per cm rule)
final_kv = base_kv + (thickness_cm * 2)

# Safety Check: Flag if kV exceeds standard diagnostic limits
if final_kv > 120:
    status = "⚠️ WARNING: High Exposure"
else:
    status = "✅ Normal Exposure Range"

print(f"Analysis for {patient_name}:")
print(f"Target kV: {final_kv}")
print(f"Safety Status: {status}")
