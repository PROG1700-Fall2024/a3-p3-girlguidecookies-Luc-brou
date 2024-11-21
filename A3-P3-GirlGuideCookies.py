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

    for i in range(NumGuides):
        print(GuideNames[i])
        if GuidesBoxes[i] 
        if GuidesBoxes[i] > int(RoundAvgBoxes):
            print(f"\n{GuideNames[i]} win the super seller badge!")
        
    
    
    
    
    
    # #if max(GuideNames):
    #     print(f"\n{max(GuideNames)} wins a trip to the Girl Guide Jamboree!")
    # #elif GuidesBoxes > int(RoundAvgBoxes):
    #     print(f"\n{GuideNames > int(RoundAvgBoxes)} win the super seller badge!")
    # elif GuidesBoxes == 0:
    #     print(f"{GuideNames} win nothing.")
    # else:
    #     print(f"{GuideNames} get the left over cookies.")

    # print(f"{counter} gets a prize!")
        




    # #for counter in range(NumGuides): 
    #     #if (max(GuidesBoxes)):
    #        # print(f"\n{max(GuideNames)} wins a trip to the Girl Guide Jamboree!")
    #     #elif GuidesBoxes[counter] > RoundAvgBoxes:
    #        # print(f"{GuideNames, GuidesBoxes} win super seller badge") 
    #        # found = True
    #     #elif GuidesBoxes == 0:
    #        # print(f"{GuideNames} won nothing")



    # # YOUR CODE ENDS HERE

main()