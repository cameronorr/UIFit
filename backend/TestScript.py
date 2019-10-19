from Measurements import Measurements

front = "tucked1.jpg"
bent = "tucked2.jpg"
back = "tucked3.jpg"

error = 6
inches = 76+error

m = Measurements(inches, front, bent, back)

print(m.shoulder_width)
print(m.right_shoulder_elbow)
print(m.right_elbow_wrist)
print(m.left_shoulder_elbow )
print(m.left_elbow_wrist )
print(m.right_shoulder_wrist )
print(m.left_shoulder_wrist )
print(m.shoulder_hip)
print(m.right_hip_ankle )
print(m.left_hip_ankle )
print(m.right_hip_knee )
print(m.left_hip_knee )
print(m.hip_ankle_max )
print(m.chest_point)

shirt_height = 29.875
shoulder_length = 18.875
sleeve_length = 32.5