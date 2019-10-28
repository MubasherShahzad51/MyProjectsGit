from pip._vendor.distlib.compat import raw_input

marks = raw_input('Enter your Obtain marks:')
outof = raw_input('Enter Out of marks:')
marks = int(marks)
outof = int(outof)
per = marks * 100 / outof
print('Your Percentage is: ' + str(per))
