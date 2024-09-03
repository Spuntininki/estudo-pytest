input_list = generated_list
    output_list = sum_double(input_list)
    for index, element in enumerate(input_list):
        print(element * 2)
        print(output_list[index])
        assert element * 2 == output_list[index]