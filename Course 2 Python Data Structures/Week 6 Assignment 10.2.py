name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


d=dict()

for line in handle:
    if not line.startswith("From "): 
        continue
    else:    
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1

lst=list()        
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print (value,count)

# =============================================================================
# Another Example
# =============================================================================

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
open_file=open(name)

file_dict={}
for line in open_file :
    line=line.rstrip()
    if line.startswith("From ") : 
            words=line.split()
            time=words[5]
            hours=time[:2]
            file_dict[hours]=file_dict.get(hours,0)+1
            
for k,v in sorted (file_dict.items()) :
    print(k,v)
