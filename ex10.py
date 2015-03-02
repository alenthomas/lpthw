# Declared 3 strings
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

#fourth string is declared using """
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#print the four strings
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#  a simple while loop in to animate/simulate a loading symbol
while True:
    for i in ["/", "-", "|", "\\","|"]:
        print "%s\r" %i,
