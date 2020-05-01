succesful_move_counter = 0
total_move_counter = 0
succesful_diveded_total = 0
#list of succesful x and y coordinates [x, y, x, y, x, y...]
succesful_Moves=[]
length_of_list_before_adding = 0
# recursioncounter
n = 1
# X-cord, Y-cord, number of moves
def chance_of_succesful(x,y,k):
    #checks if coordinate is on board of 8x8, returns True
    def valid_Move(possible_x,possible_y):
        if 0<=possible_x <=8 and 0<=possible_y <=8:
            return True
        else:
            return False
    #tests all the possible moves by the knight from given coordinates
    def possible_Moves(x,y):
        #all possible moves for a knight
        moves = [[+2, +1], [+2, -1], [-2, -1], [-2, +1], [+1, +2], [+1, -2], [-1, -2], [-1, +2]]
        global succesful_move_counter
        global total_move_counter
        global succesful_diveded_total
        for i in range((len(moves))):
            maybe_x = x + moves[i][0]
            maybe_y = y + moves[i][1]
            #checks if the move was valid
            if valid_Move(maybe_x,maybe_y) == True:
                succesful_Moves.append(maybe_x)
                succesful_Moves.append(maybe_y)
                #counts plus 1 for both succesful and total
                succesful_move_counter += 1
                total_move_counter += 1
            if valid_Move(maybe_x,maybe_y) == False:
                #if move was not valid, only counts plus one total move
                total_move_counter += 1
        #if recursioncounter is less than given value, call multible_Moves agin.
        if n<k:
            multible_Moves()
        #until given value is reached
        if n==k:
            succesful_diveded_total = (succesful_move_counter/total_move_counter)
            return succesful_diveded_total
    #takes succesful moves and runs new possible moves
    def multible_Moves():
        global n
        n += 1
        #skips every other j, since list is made [x, y, x, y, x, y...]
        for j in range(length_of_list_before_adding,len(succesful_Moves),2):
            possible_Moves(succesful_Moves[j],succesful_Moves[j+1])
    possible_Moves(x,y)
    print(succesful_diveded_total)
# X-cord, Y-cord, number of moves
chance_of_succesful(0,0,k=2)