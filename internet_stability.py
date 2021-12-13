import network_stability
import datetime

net = network_stability.NetworkTest()

while True:
    # Run connectivity test.

    net.connection_test_interval(hours=0.5)
    net.export_connection_results(f'{datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")}_connection.csv')
    net.report_connection(f'{datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")}_connection.png')

    # Run speed test.

    net.speed_test_interval(minutes=30)
    net.export_speed_results(f'{datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")}_speed.csv')
    net.report_speed(f'{datetime.datetime.now().strftime("%y_%m_%d-%H_%M_%S")}_speed.png')




"""import network_stability

net = network_stability.NetworkTest()

run_number = 0
save_name1 = "connection" + str(run_number)
save_name2 = "speed" + str(run_number)

while True:
    # Run connectivity test.

    net.connection_test_interval(hours=0.1)
    net.export_connection_results(save_name1 + '.csv')
    net.report_connection(save_name1 + '.png')

    # Run speed test.

    net.speed_test_interval(minutes=10)
    net.export_speed_results(save_name2 + '.csv')
    net.report_speed(save_name2 + '.png')

    run_number += 1"""