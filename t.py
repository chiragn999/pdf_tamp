import os
import time

# Path to the file/directory
path = r"C:\Users\chira\Desktop\iimjobs_Sneha_Raosaheb_Patil (1).pdf"


# Both the variables would contain time
# elapsed since EPOCH in float
ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)

# Converting the time in seconds to a timestamp
c_ti = time.ctime(ti_c)
m_ti = time.ctime(ti_m)

print(f"The file located at the path {path} \
was created at {c_ti} and was "
	f"last modified at {m_ti}")
