# type: ignore

import psutil
import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)  
        mem_percent = psutil.virtual_memory().percent
        cpu_cores = psutil.cpu_count()  
        
        message = None
        if cpu_percent > 80 or mem_percent > 80:
            message = "High CPU or memory utilization detected!"

        uptime_seconds = time.time() - psutil.boot_time()
        print(cpu_percent)
        print(cpu_cores)
        print(mem_percent)
        print(uptime_seconds)
        
        return render_template(
            "index.html", 
            cpu_percent=cpu_percent, 
            mem_percent=mem_percent, 
            message=message, 
            uptime=uptime_seconds,
            cpu_cores=cpu_cores
        )
    except Exception as e:
        print(e)
        return "Error loading dashboard", 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)