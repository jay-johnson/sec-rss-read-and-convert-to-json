HEADER_COLOR        = '\033[95m'
BLUE_COLOR          = '\033[94m'
GREEN_COLOR         = '\033[92m'
WARNING_COLOR       = '\033[93m'
FAIL_COLOR          = '\033[91m'
END_COLOR           = '\033[0m'


def announcement_print(msg):
    print "" + WARNING_COLOR + str(msg) + END_COLOR
    return None
# end of announcement_print


def green_print(msg):
    print "" + GREEN_COLOR + str(msg) + END_COLOR
    return None
# end of green_print


def red_print(msg):
    print "" + FAIL_COLOR + str(msg) + END_COLOR
    return None
# end of red_print

