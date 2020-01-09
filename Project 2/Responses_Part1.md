1. 4 devices (192.168.1.10, 192.168.1.11, 192.168.1.12, 192.168.1.13) which are slaves. The master is: 192.168.1.1
2.
 - 192.168.1.10 = 3 registers: Register 0, Register 1, Register 2
 - 192.168.1.11 = 3 registers: Register 0, Register 1, Register 2
 - 192.168.1.12 = 3 registers: Register 0, Register 1, Register 2
 - 192.168.1.13 = 3 registers: Register 0, Register 1, Register 2
3. Read holding registers (3), Write Single Register (6), Write Multiple Coils (15)
4. **Note**: My answers for question 4 are based on the following assumptions: a register is being used to record / set the temperature given that a register can store a 16 bit value. A coil can store a single bit and generally used as a means to signify on / off. Therefore the coil would be a better used for turning a valve on / off. The second assumption I am making is that even though the question states 'provide the modbus address', per the modbus specification, there is no such thing as a 'modbus address'. Therefore, per this thread: https://piazza.com/class/ixly0oavrku1gx?cid=108 I have been told that a 'modbus address' is what is referred to in the modbus specification as a 'register reference' or 'register address'
 - **Answer**: PLC (IP address) address that is written to for recording the temperature set point: 192.168.1.12. The 'modbus address', 'reference number' or 'register reference' is: 10
 - **Answer**: PLC (IP address) address that is written to for controlling valves: 192.168.1.11. The 'modbus address', 'reference number' or 'register reference' is: 0
