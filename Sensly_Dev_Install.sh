#!/bin/bash

chmod u+x i2c_setup.sh Uart_enable.sh Update.sh 
./i2c_setup.sh
pip install plotly
./Uart_enable.sh