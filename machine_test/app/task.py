# tasks.py

import speedtest
from celery import shared_task

@shared_task
def check_internet_speed():
    st = speedtest.Speedtest()
    # Run the speed test
    download_speed = st.download() / 10**6  
    upload_speed = st.upload() / 10**6 
    # Print the results (for testing purposes)
    print(f"Download Speed: {download_speed} Mbps")
    print(f"Upload Speed: {upload_speed} Mbps")
    
    #pip install speedtest-cli

