import clipboard

# Accept user input
my_string=input("Enter text: ")

# Copy first 4000 characters to clipboard to paste into Twitter
clipboard.set(my_string[0:4000])
