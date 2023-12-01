
file_path = 'input_doc.txt'  

digits=[]
with open(file_path, 'r') as file:
    lines = file.readlines()
    
    for i in lines:
        nums=[]
        for char in i:
            if char.isdigit(): #store all the digits
                nums.append(char)
        # merge first and last digit:
        merged_dig = str(nums[0]+nums[-1])
        digits.append(int(merged_dig))
       
    print(sum(digits))
    
    



