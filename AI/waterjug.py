def WaterJug(jug1_cap,jug2_cap,target):
    jug1 = 0
    jug2 = 0

    while True:

        jug1 = jug1_cap
        
        if jug1==target:
            print(f"Jug 1 :-{jug1}  Jug 2 :- {jug2}")
            return True
        
        while jug2<jug2_cap and jug1>0:
            jug2+=1
            jug1-=1

            if jug2==target:
                print(f"Jug 1 :-{jug1}  Jug 2 :- {jug2}")
                return True
        
        if jug2==jug2_cap:
            jug2=0
        
        if jug2==target:
            print(f"Jug 1 :-{jug1}  Jug 2 :- {jug2}")
            return True

        if jug1==0:
            return False
water_jug_problem = WaterJug(4, 3, 2)