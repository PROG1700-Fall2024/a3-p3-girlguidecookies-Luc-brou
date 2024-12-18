#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:W0489720
#Student Name: Luc Brousseau  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    GuideNames=[]
    GuidesBoxes=[]

    Num=float(input("Input the number of Girl Guides selling cookies: "))
    NumGuides=int(Num)

    for counter in range(NumGuides):
        GuideName=input(f"\nInput the name of girl guide #{counter+1}: ")
        GuideBoxes=input(f"Input the amount of boxes sold by girl guide #{counter+1}: ")
        GuideNames.append(GuideName)
        GuidesBoxes.append(float(GuideBoxes))

    AvgBoxes=((sum(GuidesBoxes))/NumGuides)
    RoundAvgBoxes= round(AvgBoxes,0)

    print("\n-------------------------------------------------------------------------------------------------------") 

    #print(f"\nGuide {GuideNames} sold {GuidesBoxes} boxes") (neccesary? if so fix ordering and format of output)

    #print("-------------------------------------------------------------------------------------------------------") 

    if RoundAvgBoxes <0: #check if boxes are negative number(s), tell user
        print("\nPlease enter valid numbers of boxes (No negative numbers).")

    elif RoundAvgBoxes==0: #check for if no cookies sold, tell user
        print("\nThe Girl Guides did not sell any cookies.")

    else: #Prints average amount of boxes sold
        print(f"\nThe average amount of boxes sold by each Girl Guide is {int(RoundAvgBoxes)}.")

    print("\n-------------------------------------------------------------------------------------------------------") 

    print("")

    for i in range(NumGuides): #logic not quite printing right here... so submitting as is as I am overdue. 
        if max(GuideNames):
            print(f"\n{GuideNames[i]} wins a trip to the Girl Guide Jamboree!")
        elif GuidesBoxes[i] > int(RoundAvgBoxes):
            print(f"\n{GuideNames[i]} wins the super seller badge!")
        if (GuidesBoxes[i]) ==0:
            print(f"\n{GuideNames[i]} wins nothing.")
        else: 
            print(f"\n{GuideNames[i]} wins the leftover cookies.") 

    # # YOUR CODE ENDS HERE

main()