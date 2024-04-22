from pyo import *

inputs, outputs = pa_get_devices_infos()
print('- Inputs (Microphone Like Devices) :\n-----------------------------------------------------------------------')
for index in sorted(inputs.keys()):
    print('  \nDevice index:', index)
    for key in ['name']:
        print('    %s:' % key, inputs[index][key])
print('\n\n- Outputs (Speaker Like Devices) :\n-----------------------------------------------------------------------')
for index in sorted(outputs.keys()):
    print('  \nDevice index:', index)
    for key in ['name']:
        print('    %s:' % key, outputs[index][key])