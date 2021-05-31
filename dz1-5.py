pceed=int(input('whats companys proceed - '))
cst=int(input('whats companys costs - '))
if pceed>cst:
    print('profit!')
    print('rent='+f"{(pceed-cst)/pceed:.2f}")
    n=int(input('how much staff - '))
    pfStaff=(pceed-cst)/n
    print('profit per staff = '+ f"{pfStaff:.2f}")
else:print('lesion:(')
#в цикле не прописан вариант, когда выручка=издержкам. но, наверное,это тоже убыток =)