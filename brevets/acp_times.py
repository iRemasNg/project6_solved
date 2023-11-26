"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described https://rusa.org/pages/rulesForRiders
and https://rusa.org/pages/acp-brevet-control-times-calculator

You MUST provide the following two functions
with the specified signatures. Otherwise, we will not
be able to run our automated test-cases for grading.
You must keep these signatures even if you don't use
all the same arguments. Arguments are explained in the
docstring.
"""
import arrow


def open_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:
    """

    :param control_dist_km:  A number. The control distance in kilometers.
    :param brevet_dist_km: A number. The nominal distance of the brevet
        in kilometers, which must be one of 200, 300, 400, 600, or 1000
        (the only official ACP brevet distances).
    :param brevet_start_time: An ISO 8601 format date-time string indicating
        the official start date and time of the brevet.
    :return: An ISO 8601 format date string indicating the control open time.
        This will be in the same time zone as the brevet start time.
    """
    return arrow.now().isoformat()


def close_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:
    """
    Args:
    :param control_dist_km: A number. The control distance in kilometers.
    :parma brevet_dist_km: A number. The nominal distance of the brevet
        in kilometers, which must be one of 200, 300, 400, 600, or 1000
        (the only official ACP brevet distances).
    :param brevet_start_time: An ISO 8601 format date-time string indicating
        the official start time of the brevet.
    :return: An ISO 8601 format date string indicating the control close time.
        This will be in the same time zone as the brevet start time.
    """
    return arrow.now().isoformat()
