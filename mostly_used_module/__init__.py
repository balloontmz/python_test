def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    len_s = len(s)

    if len_s == 0:
        return ''
    if len_s == 1:
        return s
    if s == s[::-1]:
        return s

    tmp_r = s[0]

    """
    'aba' -> 'a b a'
     012      01234
    """
    for i in range((2 * len_s) - 1):
        if i % 2 == 0:
            index = i // 2
            tmp_s = s[index]

            index_l = index - 1
            index_r = index + 1

        else:
            tmp_s = ''
            index_l = (i - 1) // 2
            index_r = (i + 1) // 2

        while index_l >= 0 and index_r < len_s and s[index_l] == s[index_r]:
            tmp_s = '{}{}{}'.format(s[index_l], tmp_s, s[index_r])
            index_l -= 1
            index_r += 1

        if len(tmp_s) > len(tmp_r):
            tmp_r = tmp_s

    return tmp_r


print(longestPalindrome('bnanans'))
print('a')