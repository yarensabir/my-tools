def label_selector(path1, path2, fileCount, classCount, indeks):
    counter = 0
    for i in range(fileCount+1,1,-1):
        try: 
            file =  path1 + str(i) + ".txt" 
            lines = open(file).readlines()
            for line in lines:
                text, *_ = line.split(" ") 
                for j in range(0,classCount): 
                    if text == str(indeks):
                        counter = counter + 1
                        if counter < 1001:
                            dosya = path2 + str(i) + ".txt"
                            with open(dosya, 'a') as f:
                                f.write(line)
                            break                  
        except Exception:
            print("exception")