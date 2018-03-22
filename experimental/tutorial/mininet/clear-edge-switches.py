import os
os.system('ovs-ofctl -O OpenFlow13 del-flows s'+str(input_switch+1))
os.system('ovs-ofctl -O OpenFlow13 del-flows s'+str(output_switch+1))