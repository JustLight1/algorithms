def decompressRLElist(nums):
    res = []
    for i in range(len(nums)):
        b, c = [nums[2*i], nums[2*(i+1)]]
    print(b, c)


decompressRLElist([1,2,3,4])