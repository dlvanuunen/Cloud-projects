
# pip install caldav
import caldav
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import os
from dotenv import load_dotenv
load_dotenv()

# Calendar Service
url = os.getenv("CAL_PROVIDER")
username = os.getenv("CAL_USERNAME")
password = os.getenv("CAL_PASSWORD")

# Timezone
user_tz = os.getenv("USER_TZ")
tz_info = ZoneInfo(user_tz)


def get_calendar():
    client = caldav.DAVClient(
        url=url,
        username=username,
        password=password,
        auth_type="basic",
    )
    calendar = client.calendar(
        url=f"{url}{username}/Calendar/{os.getenv("CAL_ID")}/"
    )

    return calendar


def get_events(calendar):
        events = calendar.search(
        start=datetime.now(),
        end=datetime.now() + timedelta(days=7),
        event=True,
        expand=True,)

        return events



def fetch_events():
    calendar = get_calendar()
    events = get_events(calendar)
    json = format_events(events)
    
    return json





def format_events(events):

    events_list = []    
    for e in events:

        c = e.icalendar_component


        summary = str(c.get("SUMMARY", "(no title)"))
        location = str(c["LOCATION"]) if "LOCATION" in c else None
        starttime = c["DTSTART"].dt
        endtime = getattr(c.get("DTEND"), "dt", None)
        all_day = not isinstance(starttime, datetime)

        if all_day:
            if endtime is not None:
                endtime = endtime - timedelta(days=1)   # all-day end is exclusive, make it inclusive
        else:
            if starttime.tzinfo is not None:
                starttime = starttime.astimezone(tz_info).replace(tzinfo=None)
            if endtime is not None and endtime.tzinfo is not None:
                endtime = endtime.astimezone(tz_info).replace(tzinfo=None)

        # 2. Then build the dict
        event_dict = {
            "title": summary,
            "start": starttime.isoformat(),
            "end": endtime.isoformat() if endtime else None,
            "all_day": all_day,
            "location": location,
        }
        events_list.append(event_dict)
            

    event_amount= len(events)
    json = {"user_tz":user_tz,
    "count":event_amount,
    "events":events_list       
    }

    return json      









if __name__ == "__main__":
    calendar = get_calendar()
    events = get_events(calendar)
    json = format_events(events)
    print(json)

    

