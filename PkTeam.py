def scoring(baller, batter):
    scoring_menu()


def scoring_menu():
    print('\n\n')
    print("--------------------------------"
          "Press O for Out"
          "Press B for Boundary"
          "Press N for No Ball"
          "Press D for Dot Ball"
          "Press W for Wide Ball")
    user_input = str(input('What happened on this Ball: '))
    return user_input
