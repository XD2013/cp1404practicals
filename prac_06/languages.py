"""CP1404/CP5632 Practical - Languages"""

from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
print(python)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


filed = [ruby, python, visual_basic]
print(f"The dynamically typed languages are:")
for i in filed:
    if i.is_dynamic():
        print(i.field)


