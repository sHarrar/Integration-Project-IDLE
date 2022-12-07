def main(grade=None):
    """

    :return:
    """
    # Sean Harrar
    # NBA2k Calculating stat averages over a certain number of games

    # integration project starts under this line

    # Calculating points average for first 5 games
    game1_points = 27
    game2_points = 15
    game3_points = 10
    game4_points = 30
    game5_points = 25
    total_games = 5
    total_points = (game1_points + game2_points + game3_points + game4_points + game5_points)
    point_average = (total_points / total_games)
    print("Point Average: ", format(point_average, ".2f"), sep='')

    # Calculating rebounds average for first 5 games
    game1_reb = 11
    game2_reb = 7
    game3_reb = 17
    game4_reb = 22
    game5_reb = 5
    total_rebounds = (game1_reb + game2_reb + game3_reb + game4_reb + game5_reb)
    rebound_average = (total_rebounds / total_games)
    print("Rebound Average: ", format(rebound_average, ".2f"), sep='')

    # Calculating assists average for first 5 games
    game1_assists = 6
    game2_assists = 0
    game3_assists = 15
    game4_assists = 4
    game5_assists = 8
    total_assists = (game1_assists + game2_assists + game3_assists + game4_assists + game5_assists)
    assists_average = (total_assists / total_games)
    print("Assist Average: ", format(assists_average, ".2f"), sep='')

    # Calculating steals average for first 5 games
    game1_steals = 6
    game2_steals = 3
    game3_steals = 0
    game4_steals = 4
    game5_steals = 5
    total_steals = (game1_steals + game2_steals + game3_steals + game4_steals + game5_steals)
    steals_average = (total_steals / total_games)
    print("Steals Average: ", format(steals_average, ".2f"), sep='')

    # Calculating blocks average for first 5 games
    game1_blocks = 5
    game2_blocks = 0
    game3_blocks = 13
    game4_blocks = 1
    game5_blocks = 3
    total_blocks = (game1_blocks + game2_blocks + game3_blocks + game4_blocks + game5_blocks)
    blocks_average = (total_blocks / total_games)
    print("Blocks Average: ", format(blocks_average, ".2f"), sep='')

    # Sprint 1
    # Required Elements

    # print function greeting
    print("Hello!")
    # formatting print() output with sep= arguments
    totalCost = 100
    print("Total cost: $", format(totalCost, "0.2f"), sep='')
    # formatting print() output with end= arguments
    totalCost = 200
    print("Total cost: $", format(totalCost, "0.2f"))
    # input function
    (input("Enter a number"))
    # basic calculations
    # Multiplication
    print(5 * 3)
    # Division
    print(12 / 6)
    # Addition
    print(5 + 10)
    # Subtraction
    print(10 - 5)
    # Exponents
    print(2 ** 4)
    # Floor Division
    print(13 // 2)
    # Modulus
    print(7 % 2)

    # Sprint 2 required elements

    # shortcut operator
    x = 5
    y = 10
    x += y
    # if statement #>= operator
    value = 100
    if value >= 100:
        print("Correct!")
    # != operator
    value = 100
    if value != 100:
        print("Incorrect")
    # if else statement
    score = 700
    if score >= 700:
        print("New High Score!")
    else:
        print("Try Again")
    # elif statement #== operator
    good_input = False

    while not good_input:

        try:
            grade = int(input("Enter your grade"))
            if grade == 100:
                print("Perfect!")
            elif grade >= 60:
                print("Good Enough")
            else:
                print("Fail")

            good_input = True

        except ValueError:

            print("Error. Must be a whole number.")

    # Boolean Operators
    a = True
    b = False
    print(a and b)
    print(a or b)
    print(not a)
    print(not b)
    # While Loop
    color = input("Enter your favorite color: ")
    t = 0
    while t < 5:
        print(color)
        t += 1
    # For Loop #in #range
    color = input("Enter your favorite color: ")
    for t in range(5):
        print(color)
    # Function
    import math

    def calculate_area(radius):
        """

        :param radius:
        :return:
        """
        return math.pi * radius * radius

    def calculateDiameter(radius):
        """

        :param radius:
        :return:
        """
        return 2.0 * radius

    radius = int(input("Enter the radius: "))
    area = calculate_area(radius)
    diameter = calculateDiameter(radius)
    print(area)
    print(diameter)


main()
