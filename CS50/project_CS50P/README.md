# Project: Conversion helper
#### Video Demo:  <https://youtu.be/IO_zma6vevQ>
#### Description: This a program to help user convert time, temperature, length and weight

This project is designed to help people convert time, temperature, length and weight in our daily lives.

#### Time conversion
The first area is time conversion. It concludes 3 parts.
##### 1. 12-hour to 24-hour
The first one is 12-hour clock to 24-hour clock. Sometinmes we need convert time from time in AM/PM to 24-hour-clock, if we can use a auto converter, life may be a little easier. The usage is to input like "5 AM to 9 PM", caseignored and spacesignored, but "to" is required.
##### 2. Calculate time from a date to another
The second one is to calculate total time(minutes) from a specific date to another given date. The format of input shoule be "YYYY-MM-DD" or just "today", caseignored. Then the total time in minutes will be given.
##### 3. Calculate a future or past date
This part is to calculate a future or past date. We may use it in a siutation such as when we want to know how much time we have before the due date or how many days have passed since a special date. The format of the first input here is "YYYY-MM-DD" or just "today", the second input should be a number.

#### Temperature conversion
The second area is temperature conversion. It conculdes 2 parts.
##### 1. Fahrenheit to Degree Celsius
The first one converts temperature from fahrenheit to celsius, where the formula is "celsius = (fahrenheit - 32) * 5 / 9". The format of input here should be a float number.
##### 2. Degree Celsius to Fahrenheit
The seconde one converts temperature from celsius to fahrenheit, where the formula is "fahrenheit = celsius * 9 / 5 + 32". The format of input here should be a float number.

#### Length conversion
The third area is length conversion. It conculdes 6 parts.
- Foot to Inch
- Inch to Foot
- Mile to Meter
- Meter to Mile
- Centimeter to Inch
- Inch to Centimeter

The first two parts convert foot to inch or vice, where the formula is "1 foot = 12 * inch". The format of input here should be a float number. The second two parts convert btween mile and meter, where the formula is "1 mile = 1609.344 * meter", it also needs user input a float number. The last two convert between centimeter and inch, where "1 inch = 2.54 * centimeter", the program prompts user for a float number.

#### Weight conversion
The fourth and last area is weight conversion. It conculdes 6 parts.
- Pound to Ounce
- Ounce to Pound
- Ounce to Gram
- Gram to Ounce
- Gram to Pound
- Pound to Gram

The first two parts convert pound to ounce or vice, where the formula is "1 pound = 16 * ounce". We need to input an number here. The second two parts convert btween ounce and gram, where the formula is "1 ounce = 28.3495 * gram", it also needs user input a float number. The last two convert between gram and pound, where "1 pound = 453.592 * gram", the program prompts user for a float number, too.
