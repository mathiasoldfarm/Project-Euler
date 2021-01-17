def get_next_day(day):
  if day == "monday":
    return "tuesday"
  if day == "tuesday":
    return "wedensday"
  if day == "wedensday":
    return "thursday"
  if day == "thursday":
    return "friday"
  if day == "friday":
    return "saturday"
  if day == "saturday":
    return "sunday"
  if day == "sunday":
    return "monday"
  raise Exception(f"Wrong day: {day}")

def iterate_days(f, t, start_day, ret_sundays=True, ret_end_weekday=False):
  f = f.split(".")
  t = t.split(".")
  from_day = int(f[0])
  from_month = int(f[1])
  from_year = int(f[2])
  to_day = int(t[0])
  to_month = int(t[1])
  to_year = int(t[2])

  counter = 0
  sundays = 0
  while( ( from_day, from_month, from_year ) != ( to_day, to_month, to_year ) ):
    if ( from_day == 1 and start_day == "sunday" ):
      sundays += 1
    if (
      from_month in [1,3,5,7,8,10] and from_day == 31
    ) or (
      from_month in [4,6,9,11] and from_day == 30
    ) or (
      from_month == 2 and from_year % 4 == 0 and from_year % 400 == 0 and from_day == 29
    ) or (
      from_month == 2 and from_day == 28
    ):
      from_day = 1
      from_month += 1
    elif (
      from_month == 12 and from_day == 31
    ):
      from_day = 1
      from_month = 1
      from_year += 1
    else:
      from_day += 1
    counter += 1
    start_day = get_next_day(start_day)

  if ret_sundays:
    return sundays
  if ret_end_weekday:
    return start_day

start_date = iterate_days("1.1.1900", "1.1.1901", "monday", ret_sundays=False, ret_end_weekday=True)
sundays = iterate_days("1.1.1901", "31.12.2000", start_date)
print(sundays)