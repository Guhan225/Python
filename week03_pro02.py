def count_frequency(lst):
    Freq_dict={}
    for item in lst:
        if item in Freq_dict:
            Freq_dict[item]+=1
        else:
            Freq_dict[item]=1
    return Freq_dict
sample_list=['apple','banana','apple','orange','apple','banana']
print("Frequency count:",count_frequency(sample_list))