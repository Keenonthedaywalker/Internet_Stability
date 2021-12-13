import network_stability
import datetime

net = network_stability.NetworkTest()

while True:
    # Run connectivity test.

    # Runs a 30 minute test.
    net.connection_test_interval(hours=0.5)
    # Exports the results to a csv file and names it based on the time.
    net.export_connection_results(f'{datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")}_connection.csv')
    net.report_connection(f'{datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")}_connection.png')

    # Run speed test.
    
    # Does the same as the code above, but only with the internet's speed.
    net.speed_test_interval(minutes=30)
    net.export_speed_results(f'{datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")}_speed.csv')
    net.report_speed(f'{datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")}_speed.png')
