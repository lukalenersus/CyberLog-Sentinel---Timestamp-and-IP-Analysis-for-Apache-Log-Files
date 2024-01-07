with open("output_file", 'w') as outfile:
    for i in range(1,23):
        dict1 = {}  # use a dictionary to map values from the inital file
        with open("split_i", 'r') as split:
            next(split) #skip the header
            line_list = line.split(delimiter)
            for line in split:
                dict1[line_list[whatever_key_u_use_as_id]] = line_list

            compare_dict = {}
            for f in folders:
                with open("each folder", 'r') as comp:
                    next(comp) #skip the header
                    for cline in comp:
                        cparts = cline.split('delimiter')
                        compare_dict[cparts[whatever_key_u_use_as_id]] = cparts
            for key in dict1:
                if key in compare_dict:
                    outfile.write("write your data")
outfile.close()