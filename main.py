import math

def position_to_stand(total_soldiers) -> int:
    # if total soldiers is a power of 2, we directly return the starting position
    if math.log(total_soldiers, 2) == int(math.log(total_soldiers, 2)):
        winning_position = 1
    else:
        # finding the nearest power power of 2
        nearest_power_of_2 = int(math.log(n, 2))
        # finding the remaining numbers
        diff = total_soldiers - (2**nearest_power_of_2)
        # winning position is (2*l + 1)
        winning_position = (2*diff) + 1
        if winning_position > total_soldiers:
            winning_position = winning_position%total_soldiers

    return winning_position
    



if __name__ == '__main__':
    # taking the total soldiers input here to be able to use this value for functions created later.
    total_soldiers = int(input("Enter the total number of soldiers: "))
    winning_position = position_to_stand(total_soldiers)
    print("The winning position is: ", winning_position)