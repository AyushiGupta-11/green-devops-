from codecarbon import EmissionsTracker

tracker = EmissionsTracker()

tracker.start()

# Simulated workload
for i in range(10000000):
    x = i * i

tracker.stop()