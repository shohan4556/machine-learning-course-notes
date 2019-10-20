def ReadFromLog():
    file = open("orderLog.txt","r")
    logList = []
    for l in file:
        logList.append(l.strip())
    
    file.close()
    return logList
    
#main function     
main()
