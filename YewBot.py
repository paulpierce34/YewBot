import time
import pyautogui
import cv2


pyautogui.FAILSAFE = True ## This enables you to cancel by moving your mouse to any corner of the screen. Alternatively, hold CTRL+C to cancel



## returns back from Falador bank to Yew tree
def returnbackBank():
    time.sleep(3)
    count = 0
    topCompass = pyautogui.locateOnScreen("compass.png", confidence=0.4)
    print ('Returning back to Yew woodcutting location')
    if (topCompass):
        while (count < 1):
            pyautogui.moveTo(topCompass, duration=1) ## brings cursor to the top compass minimap thingy
            pyautogui.move(60, 120) ## moves cursor on the x axis away from the compass
            pyautogui.click()
            time.sleep(25)
            pyautogui.click()
            time.sleep(10)
            pyautogui.move(50, -10)
            pyautogui.click()
            time.sleep(10)
            
            treelogo = pyautogui.locateOnScreen("treelogo.png", confidence=0.60)
            if (treelogo):
                centeroflogo = pyautogui.center(treelogo)
                pyautogui.moveTo(centeroflogo, duration=1)
                pyautogui.click()
            count += 1
        
        time.sleep(10)    
        yewTrees()    
    else:
        print('damn cant find top compass... adjust confidence level in script for topCompass variable')
        time.sleep(5)

## Tries to detect bank teller in falador village
def detectBankTeller(): 
    #bankteller = pyautogui.locateOnScreen("bankteller3.png", confidence=0.35)
    fullinventory = pyautogui.locateOnScreen("fullinventory.png", confidence=0.8)
    alltellers = ["bankteller_fal.png", "bankteller_fal2.png"]
                    # detect bankteller
    #print ('Looking for bank teller')
    for teller in alltellers:
        bankteller = pyautogui.locateOnScreen(teller, confidence=0.50)
        if (bankteller):
            count1 = 0
            while (count1 < 2):
                count1 += 1
                print('I see the bankteller now!')
                #centerofteller = pyautogui.center(bankteller)
                pyautogui.moveTo(bankteller, duration=1)
                pyautogui.click()  ## This click should open up bank
                bankinventory = pyautogui.locateOnScreen("bankinventory.png", confidence=0.5) ##  .6 works pretty well
                time.sleep(5)
                # detect if the bank is open
                if (bankinventory):
                    print ('Detected bank inventory opened up')
                    pyautogui.moveTo(fullinventory, duration=1)
                    pyautogui.move(20, 50)
                    pyautogui.click(button='right')
                    pyautogui.move(0, 80)
                    pyautogui.click()
                    returnbackBank() ## call a return back function
                else:
                    time.sleep(2)
                    count2 = 0
                    while (count2 < 2):
                        try:
                            count2 += 1
                            bankinventory = pyautogui.locateOnScreen("bankinventory.png", confidence=0.5)
                            if (bankinventory):
                                print ('Detected bank inventory opened up')
                                pyautogui.moveTo(fullinventory, duration=1)
                                pyautogui.move(20, 50)
                                pyautogui.click(button='right')
                                pyautogui.move(0, 80)
                                pyautogui.click()
                                returnbackBank()
                        except:
                            print ('Did not detect inventory...')
                                    



## Runs to bank from Yew tree
def yewBankRun():
    count = 0
    topCompass = pyautogui.locateOnScreen("compass.png", confidence=0.4)
    fullinventory = pyautogui.locateOnScreen("fullinventory.png", confidence=0.8)
    allbanks = ["east_fal_bank.png"] ## put more bank minimap screenshots here if you have issues with accuracy
    print ('Executing bank run script...')
    if (topCompass):
        while (count < 2):
            for bankpic in allbanks:
                try:
                    banklocation = pyautogui.locateOnScreen(bankpic, confidence=0.40) ## .37 worked alright
                except:
                    continue
                if (banklocation):
                    print(f'Sweet! I see the bank.. Moving to {bankpic}')
                    pyautogui.moveTo(banklocation, duration=1)
                    pyautogui.click()
                    time.sleep(16)
                    detectBankTeller() ## Try to detect bank teller
                else:
                    #print ("Unable to detect bank location. Sleeping and retrying.")
                    detectBankTeller()
                    time.sleep(3)
                    
                #If we've already moved near the bank, and we still can't detect it, lets trace our steps backwards a little and try to get close enough to detect bank
                if (count == 1):
                    #print ('Adjusting minimap direction to see the bank')
                    pyautogui.move(0, 35)
                    pyautogui.move(-135, -90)
                    pyautogui.click()
                    count += 1
                    if (banklocation):
                        print(f'True...... I see the bank.. Moving to {bankpic}')
                        pyautogui.moveTo(banklocation, duration=1)
                        pyautogui.click()
                        time.sleep(29)
                        detectBankTeller() ## Try to detect bank teller
                    else:
                        print ("Unable to detect bank location. Sleeping and retrying.")
                        detectBankTeller()
                        time.sleep(3)    
                
                ## This moves to the bank area from woodcutting area
                if (count < 1):
                    print ('Moving towards bank...')
                    pyautogui.moveTo(topCompass, duration=1)
                    pyautogui.click()
                    pyautogui.move(50, 30)
                    pyautogui.click()
                    time.sleep(25) ## Sleep timer is so high to account for people that have to walk
                    print ('Adjusting cursor upwards..')
                    pyautogui.move(15, -10)
                    pyautogui.click()
                    time.sleep(14)
                    pyautogui.click()
                    time.sleep(11)
                    count += 1
                    detectBankTeller()
                
    else:
        print('damn cant find...')
        time.sleep(5)







## Looks for nearest Yew tree to cut until inventory is full, and then calls the yewBankRun() function
def yewTrees():
    allTrees = ["yew.png", "yew2.png", "yew3.png", "yew4.png", "yew5.png", "yew6.png", "yew7.png", "yew8.png", "yew9.png", "yew10.png"]
    count = 0
    while (1==1):
        print ("Looking for the nearest Yew tree....")
        for treepic in allTrees:
            fullinventory = pyautogui.locateOnScreen("fullinventory.png", confidence=0.85)
            if (fullinventory):
                    print ('Full inventory detected.')
                    yewBankRun()
                    break
            #print(f"Looking for {treepic}") ## Uncomment if you want to print which .png file you're looking for at the moment
            treelocation = pyautogui.locateOnScreen(treepic, confidence=0.32) ## Adjust confidence level of images (Valid entries: 0-1)
            if (treelocation):
                #fullinventory = pyautogui.locateOnScreen("fullinventory.png", confidence=0.8)
                #print (f"{treelocation}")
                print (f"Found {treepic}!")
                centeroftree = pyautogui.center(treelocation)
                pyautogui.moveTo(centeroftree, duration=1)
                pyautogui.click()
                time.sleep(25)
                del treelocation ## clear variable so it doesn't remember the location of the previous successful tree
                ## Break out of for loop so we restart the process and begin searching for first pic in array
                break
            else:
                #print("None found, searching and waiting for more.. moving eventually")
                time.sleep(1) ## sleep 1 sec in between looking for trees to account for trees that respawn, so as to not spam the user with 'looking for yew trees' messages
                if (count > 3):
                    #pyautogui.moveTo(treelocation, duration=1)
                    #pyautogui.click()
                    count = 0
                count += 1
                try:
                    if (fullinventory):
                        #print('Full inventory... waiting 3 times')
                        yewBankRun()
                except:
                        continue     


try:
    yewTrees()
except KeyboardInterrupt:
    print ("CTRL + C detected. Exiting script.")
    exit(0)
