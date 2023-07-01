import psutil
import time


# Function to calculate network bandwidth
def get_bandwidth():
    network_info = psutil.net_io_counters(pernic=True)
    time.sleep(1)  # Delay to calculate the difference in network stats
    network_info_updated = psutil.net_io_counters(pernic=True)

    # Calculate the difference in network stats
    stats = {}
    for interface in network_info:
        if interface in network_info_updated:
            stats[interface] = {
                'bytes_sent': network_info_updated[interface].bytes_sent - network_info[interface].bytes_sent,
                'bytes_received': network_info_updated[interface].bytes_recv - network_info[interface].bytes_recv
            }

    return stats


# Continuously monitor network bandwidth
while True:
    bandwidth_stats = get_bandwidth()
    for interface, stats in bandwidth_stats.items():
        bytes_sent = stats['bytes_sent']
        bytes_received = stats['bytes_received']

        print(f"Interface: {interface}")
        print(f"Bytes Sent: {bytes_sent}")
        print(f"Bytes Received: {bytes_received}")
        print("")

    # Wait for a specific time interval before measuring bandwidth again
    time.sleep(5)
