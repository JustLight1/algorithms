def wave(s):
    wave_list = []
    for i in range(len(s)):
        if s[i].isalpha():
            wave_variant = s[:i] + s[i].upper() + s[i+1:]
            wave_list.append(wave_variant)

    return wave_list