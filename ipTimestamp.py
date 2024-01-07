def IpTimeStamp(filename):
    try:
        #putting the correct file path
        fileDirectory = open(filename,'r') #1
        #fileRead=fileDirectory.read()

        #create a hash map 
        ipTime={} #1

        #loop through each line and split each line by
        with open('logs.txt') as log_file:
            for line in log_file: # n
                
                #split string by space
                newLine = line.split(" ")
                
                # print (newLine[0]+":"+ newLine[3] +":"+ newLine[4] ),

                #add items to hash map
                ipTime.update({newLine[0] : f'{newLine[3]} " "{newLine[4]}'})

        #access the map
        print(ipTime)   
        #close the file 
        fileDirectory.close()

        #write the logs in a new file
        newLogFiles=open('time.txt','a')
        #write 
        newLogFiles.write(f'{ipTime}')

        #close the file
        newLogFiles.close()

        

    except Exception as e:
        print(e)


IpTimeStamp("los.txt")