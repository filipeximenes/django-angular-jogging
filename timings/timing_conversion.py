

def from_seconds_to_formated(total_secs):
    hours = total_secs / 3600
    minutes = (total_secs % 3600) / 60
    seconds = ((total_secs % 3600) % 60)

    return '%s:%s:%s' % (hours, minutes, seconds)


def from_formated_to_seconds(formated):
    splits = formated.split(':')

    if len(splits) < 2:
        return False

    seconds = int(splits.pop())
    minutes = int(splits.pop())
    try:
        hours = int(splits.pop())
    except:
        hours = 0

    return (hours * 3600) + (minutes * 60) + seconds
