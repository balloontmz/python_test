# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'

import random

WINDOWS = """
*************************************************\n
you choice   * machine choice * has win * count *\n
*************************************************\n
{you_choice}*{machine_choice}*   {has_win}     *  {count}  *\n
{input_1}
"""

CHOICE = {
    "1": "     石头      ",
    "2": "     剪刀      ",
    "3": "     布       ",
}
HAS_WIN = dict((("1", "2"), ("2", "3"), ("3", "1")))
SEED = "123"

CYCLE_INDEX = 5

count = 0
msg = ""
you_choice = ""
machine_choice = ""
has_win = ""

while count < CYCLE_INDEX:
    input_param = WINDOWS.format(you_choice=CHOICE[you_choice] if you_choice in ["1", "2", "3"] else " "*14,
                                 machine_choice=CHOICE[machine_choice] if machine_choice in ["1", "2", "3"] else " "*14,
                                 has_win=has_win,
                                 count=count,
                                 input_1="INPUT:(请输入1.石头2.剪刀3.布)") + msg
    you_choice = input(input_param)
    machine_choice = random.choice(SEED)
    if you_choice in ["1", "2", "3"]:
        msg = ""
        if HAS_WIN[you_choice] == machine_choice:
            has_win = "是"
            count += 1
        else:
            has_win = "否"
    else:
        msg = "输入有误，请重新输入\n"

print(WINDOWS.format(you_choice=CHOICE[you_choice] if you_choice in ["1", "2", "3"] else "",
                     machine_choice=CHOICE[machine_choice] if machine_choice in ["1", "2", "3"] else "",
                     has_win=has_win,
                     count=count,
                     input_1="你已经赢了{counts}次，游戏结束".format(counts=CYCLE_INDEX)))
