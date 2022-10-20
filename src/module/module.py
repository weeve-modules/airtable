"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from .params import PARAMS
from pyairtable import Table

log = getLogger("module")

table = Table(PARAMS['API_KEY'], PARAMS['BASE_ID'], PARAMS['TABLE'])

def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Writing to Airtable ...")

    try:
        if type(received_data) is list:
            for data in received_data:
                table.create(data)
        else:
            table.create(received_data)

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
