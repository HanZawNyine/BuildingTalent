towerA = [0,1,2,3]
towerB = [0,]
towerC = [0,]
print(f'TowerA : {towerA}')
print(f'TowerB : {towerB}')
print(f'TowerC : {towerC}')
while True:
     popValue = input("pop value : ").lower()
     addValuetoTower = input("Tower value : ").lower()
     if popValue == 'a':
        pushValue = towerA.pop()
     elif popValue == 'b':
         pushValue =towerB.pop()
     elif popValue == 'c':
         pushValue =towerC.pop()

     if addValuetoTower == "a":
        if towerA[-1]< pushValue:
            towerA.append(pushValue)
        # else:
        #     print("Cannnot change !")
            #retryValuetoTower  =  input("Retry Tower value : ").lower()
     elif addValuetoTower == 'b':
        if towerB[-1] < pushValue:
            towerB.append(pushValue)
        # else:
        #     print("Cannnot change !")
        #     retryValuetoTower = input("Retry Tower value : ").lower()
     elif addValuetoTower == 'c':
        print("C add value")
        print(towerC[-1],pushValue)
        if towerC[-1] < pushValue:
            towerC.append(pushValue)

     if towerC == [0,1,2,3]:
         print('*' * 100)
         print("Congrat!")
         print('*'*100)
         print(f'TowerA : {towerA}')
         print(f'TowerB : {towerB}')
         print(f'TowerC : {towerC}')
         print(f'push Value : {pushValue}')
         break
     print(f'TowerA : {towerA}')
     print(f'TowerB : {towerB}')
     print(f'TowerC : {towerC}')
     print(f'push Value : {pushValue}')

