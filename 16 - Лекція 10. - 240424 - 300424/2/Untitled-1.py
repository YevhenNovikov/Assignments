with open('file1.txt', 'w') as file:
    file.write("Lorem ipsum dolor sit amet, consectetur adipiscing \
               elit, sed do eiusmod tempor incididunt ut labore et \
               dolore magna aliqua. Ut enim ad minim veniam, quis \
               nostrud exercitation ullamco laboris nisi ut aliquip \
               ex ea commodo consequat. Duis aute irure dolor in \
               reprehenderit in voluptate velit esse cillum dolore \
               eu fugiat nulla pariatur. Excepteur sint occaecat \
               cupidatat non proident, sunt in culpa qui officia \
               deserunt mollit anim id est laborum")

with open('file1.txt', 'r') as file1:
    text = file1.read()

with open('file2.txt', 'w') as file2:
    file2.write(text.upper())
