import subprocess

# Define the Wi-Fi adapter name
adapter = 'wlan0'

try:
    # Disable power management
    subprocess.call(['sudo', 'iwconfig', adapter, 'power', 'off'])

    # Set transmit power to maximum
    subprocess.call(['sudo', 'iwconfig', adapter, 'txpower', '15'])

    # Set the Wi-Fi adapter to use the 802.11n standard
    subprocess.call(['sudo', 'iwconfig', adapter, 'mode', '11n'])

    # Enable Wi-Fi roaming aggressiveness
    subprocess.call(['sudo', 'iwconfig', adapter, 'roaming', 'aggressive'])

    # Disable Wi-Fi power save mode
    subprocess.call(['sudo', 'iwconfig', adapter, 'power', 'off'])

    print('Wi-Fi optimization complete!')
except Exception as e:
    print('An error occurred during Wi-Fi optimization:', e)
