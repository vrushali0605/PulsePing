import time

def run_worker():
    print("PulsePing Worker Running...")

    while True:
        print("Worker heartbeat... (ready for monitoring tasks)")
        time.sleep(60)  # runs every minute for now

if __name__ == "__main__":
    run_worker()