import sys
with open(sys.argv[1],'r') as f:
    input_list=[]
    for line in f:
        line=int(line.strip())
        input_list.append(line)
    print(input_list)
    output_list=[]
    for i in input_list:
        if i%2!=0:
            output_list.append(i)
    print(output_list)


with open(sys.argv[2],'w') as f1:
    for j in output_list:

        f1.write(str(j)+"\n")

    f1.close()