#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Modbus TestKit: Implementation of Modbus protocol in python

 (C)2009 - Luc Jean - luc.jean@gmail.com
 (C)2009 - Apidev - http://www.apidev.fr

 This is distributed under GNU LGPL license, see license.txt
"""

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp


def main():
    """main"""
    logger = modbus_tk.utils.create_logger("console")

    try:
        #Connect to the slave
        master = modbus_tcp.TcpMaster()
        master.set_timeout(5.0)
        logger.info("connected")


        logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 0, 4))
        logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 4, output_value=[54]))
        logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 5, output_value=[54]))
        logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 6, output_value=[54]))
	      logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 7, output_value=[54]))
        logger.info(master.execute(1, cst.READ_INPUT_REGISTERS, 0, 4))


    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())

if __name__ == "__main__":
    main()
