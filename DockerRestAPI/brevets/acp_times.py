
import arrow

CLOSE = [(1000, 11.428), (600, 15), (400, 15), (200, 15), (0, 15)]
OPEN = [(1000, 28), (600, 30), (400, 32), (200, 34), (0, 34)]


def open_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:

    total_time = 0
    if control_dist_km > brevet_dist_km * 1.2 or control_dist_km < 0:
        return "invalid"
    if (control_dist_km >= 200 and control_dist_km <= 240 ) and brevet_dist_km == 200:
        opening_time = arrow.get(brevet_start_time).shift(hours=5, minutes=53)
        return opening_time.isoformat()
    elif (control_dist_km >= 300 and control_dist_km <= 360 ) and brevet_dist_km == 300:
        opening_time = arrow.get(brevet_start_time).shift(hours=9)
        return opening_time.isoformat()
    elif (control_dist_km >= 400 and control_dist_km <= 480 ) and brevet_dist_km == 400:
        opening_time = arrow.get(brevet_start_time).shift(hours=12, minutes=8)
        return opening_time.isoformat()
    elif (control_dist_km >= 600 and control_dist_km <= 720 ) and brevet_dist_km == 600:
        opening_time = arrow.get(brevet_start_time).shift(hours=18, minutes=48)
        return opening_time.isoformat()
    elif (control_dist_km >= 1000 and control_dist_km <= 1200 ) and brevet_dist_km == 1000:
        opening_time = arrow.get(brevet_start_time).shift(hours=33, minutes=5)
        return opening_time.isoformat()
    else:
        for i in range(len(OPEN)):
         if control_dist_km >= OPEN[i][0]:
            km = control_dist_km - OPEN[i][0]
            time = km / OPEN[i-1][1]
            total_time += time
            control_dist_km -= km
	        
        brevet_start_time = arrow.get(brevet_start_time)
        hours = int(total_time)
        minutes = round(60 * (total_time - hours))
        opening_time = brevet_start_time.shift(hours=hours, minutes=minutes)
	
        return opening_time.isoformat()




def close_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:
    total_time = 0
    if control_dist_km > brevet_dist_km * 1.2 or control_dist_km < 0:
        return "invalid"
    if control_dist_km < 60:
        closing_time = arrow.get(brevet_start_time).shift(hours=control_dist_km / 20 + 1)
        return closing_time.isoformat()
    elif (control_dist_km >= 200 and control_dist_km <= 240 ) and brevet_dist_km == 200:
        closing_time = arrow.get(brevet_start_time).shift(hours=13, minutes=30)
        return closing_time.isoformat()
    elif (control_dist_km >= 300 and control_dist_km <= 360 ) and brevet_dist_km == 300:
        closing_time = arrow.get(brevet_start_time).shift(hours=20)
        return closing_time.isoformat()
    elif (control_dist_km >= 400 and control_dist_km <= 480 ) and brevet_dist_km == 400:
        closing_time = arrow.get(brevet_start_time).shift(hours=27)
        return closing_time.isoformat()
    elif (control_dist_km >= 600 and control_dist_km <= 720 ) and brevet_dist_km == 600:
        closing_time = arrow.get(brevet_start_time).shift(hours=40)
        return closing_time.isoformat()
    elif (control_dist_km >= 1000 and control_dist_km <= 1200 ) and brevet_dist_km == 1000:
        closing_time = arrow.get(brevet_start_time).shift(hours=75)
        return closing_time.isoformat()
    else:
        for i in range(len(CLOSE)):
            if control_dist_km >= CLOSE[i][0]:
                km = control_dist_km - CLOSE[i][0]
                time = km / CLOSE[i-1][1]
                total_time += time
                control_dist_km -= km

        brevet_start_time = arrow.get(brevet_start_time)
        hours = int(total_time)
        minutes = round(60 * (total_time - hours))
        closing_time = brevet_start_time.shift(hours=hours, minutes=minutes)

        return closing_time.isoformat()
