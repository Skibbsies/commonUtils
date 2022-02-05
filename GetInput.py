def GetInput(text = '', mode = str):
    try:
        user_input = input('\n' + text + '\n' + '$ ')
    except:
        print(f'Unable to concatenate string with given text: {text}')
        user_input = input('\n' + 'SAMPLE_TEXT' + '\n' + '$ ')

    current_mode = type(user_input)
    
    try:
        user_input = mode(user_input)
    except:
        print('\ngetInput: Cannot explicitly convert input to ' + str(mode) + ' in GetInput()\n')
        current_mode(user_input)
    
    return user_input


gi = Gi = gI = GI = GetInput
