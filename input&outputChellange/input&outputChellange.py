inputs  = open("string.txt" , "rt")
outputs = open("string_output.txt" , "wt")

print("Reading Files.........")

result = ""
for index, line in enumerate(inputs):
    if index == 0 or index == 2:
        result += " " + line.strip()  

    else:
        result += " " + line.strip().lower()
        
print(result , file= outputs)

inputs.close()
outputs.close()

