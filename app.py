import streamlit as st
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Current timestamp
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# Auto-refresh every 2 seconds
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# FizzBuzz logic
if count == 0:
    st.write("Count is zero")
else:
    output = ""
    if count % 3 == 0:
        output += "Fizz"
    if count % 5 == 0:
        output += "Buzz"
    if output == "":
        output = f"Count: {count}"
    st.write(output)

# Show last updated timestamp
st.write(f"Last updated at: {timestamp}")

# Display attendance CSV
try:
    df = pd.read_csv(f"Attendance/Attendance_{date}.csv")
    st.dataframe(df.style.highlight_max(axis=0))
except FileNotFoundError:
    st.warning(f"No attendance file found for {date}")
