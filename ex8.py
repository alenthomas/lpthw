# declaring variable with a string of %r
formatter = "%r %r %r %r"

# prints formatter with output 1 2 3 4
print formatter % (1, 2, 3, 4)
# prints one two three four
print formatter % ("one", "two", "three", "four")
# prints true false false and true
print formatter % (True, False, False, True)
#prints %r %r %r %r four times
print formatter % (formatter, formatter, formatter, formatter)
# prints four strings
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
