import random
import threading
import time

agent = threading.Semaphore() #3 smokers wait on agent
tobacco = threading.Semaphore() #for signaling smoker with tobacco 
paper = threading.Semaphore()#for signaling smoker with paper
match = threading.Semaphore()# for signaling smoker with match
syn = threading.Semaphore()# for synchronization for all threads

agent.acquire()#agent=0
tobacco.acquire()#tobacco=0
paper.acquire()#paper=0
match.acquire()#match=0

def Agent():
    while True:
        
        syn.acquire()#syn=0
        time.sleep(1)
     
        ingredients = ('Tobacco', 'Paper', 'Matches')#ingredient initialization 
        ingredient_1 = random.choice(ingredients)# selecting ingredient1
        ingredient_2 = ingredient_1
        ingredient_3 = ingredient_2

        while (ingredient_2 == ingredient_1):
            ingredient_2 = random.choice(ingredients)# selecting ingredient2
 
        while ((ingredient_3 == ingredient_1) | (ingredient_3 == ingredient_2)):
            ingredient_3 = random.choice(ingredients)
            
        print ("Agent selects",ingredient_1, "and", ingredient_2, "and supplies them to the Smoker having", ingredient_3,".\n")
        time.sleep(1)
        
        agent.release()#agent+1
        time.sleep(1)
            
        agent.release()#agent+1
        time.sleep(1)
            
        agent.release()#agent+1
        time.sleep(1)
        
        if ingredient_3 == 'Tobacco':
            tobacco.release()#tobacco+1
            time.sleep(1)
                       
        elif ingredient_3 == 'Paper':
            paper.release()#paper+1
            time.sleep(1)
            
        else:
            match.release()#paper+1
            time.sleep(1)
        
def smoker_with_tobacco():
    while True:
        
        agent.acquire()#agent-1
        time.sleep(1)
        
        tobacco.acquire()#tobacco-1
        time.sleep(1)
        
        print ("Smoker having Tobacco picks up the resources.\n")
        time.sleep(1)
        
        print ("Smoker having Tobacco starts making cigarette.\n")
        time.sleep(1)
        
        print ("Smoker having Tobacco is smoking now.\n")
        time.sleep(1)  
        
        print ("Smoker having Tobacco now signals the Agent to select next ingredient.\n","\n","\n")
        time.sleep(1)
        
        syn.release()#syn+1
        time.sleep(1)

def smoker_with_paper():
    while True:
        
        agent.acquire()#agent-1
        time.sleep(1)
        
        paper.acquire()#paper-1
        time.sleep(1)
        
        print ("Smoker having Paper picks up the resources.\n")
        time.sleep(1)
        
        print ("Smoker having Paper starts making cigarette.\n")
        time.sleep(1)
        
        print ("Smoker having Paper is smoking now.\n")
        time.sleep(1)
        
        print ("Smoker having Paper now signals the Agent to select next ingredient.\n,","\n","\n")
        time.sleep(1)
        
        syn.release()#syn+1
        time.sleep(1)

        
def smoker_with_matches():
    while True:
        
        agent.acquire()#agent-1
        time.sleep(1)
        
        match.acquire()#match-1
        time.sleep(1)
        
        print ("Smoker having Matches picks up the resources.\n")
        time.sleep(1)
        
        print ("Smoker having Matches starts making cigarette.\n")
        time.sleep(1)
        
        print ("Smoker having Matches is smoking now.\n")
        time.sleep(1)
        
        print ("Smoker having Matches now signals the Agent to select next ingredient.\n","\n","\n")
        time.sleep(1)
        
        syn.release()#syn+1
        time.sleep(1)
        
t1 = threading.Thread(target=Agent).start()#thread1
t2 = threading.Thread(target=smoker_with_tobacco).start()#thread2
t3 = threading.Thread(target=smoker_with_paper).start()#thread3
t4 = threading.Thread(target=smoker_with_matches).start()#thread4
