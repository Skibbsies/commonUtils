def FormatText(text, formatType = 'bold', printText = False):
    FORMAT_DICT = {
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'dark_cyan': '\033[36m',
        'blue': '\033[94m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'red': '\033[91m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }


    try:
        text = str(text)
        formatType = formatType.lower()
    except:
        print('TextFormatting: Could not format text!')
        return text


    for x, y in FORMAT_DICT.items():
        if x == formatType:
            text = y + text + FORMAT_DICT['end']

            if printText == True:
                print(text)
                return text
            else:
                return text


ft = Ft = fT = FT = FormatText
