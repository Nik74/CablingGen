# Auxiliary function that reads file and returns values from the specified "column" number num

def read_file(file, num):
    result = []

    for k in file:
        f = open(k, 'r')

        flag = False

        if f:
            for line in f:
                if flag:
                    material = ''

                    count = 0

                    for i in line:
                        if count == num:
                            if i != ';':
                                if i != '"':
                                    material += i
                            else:
                                break

                        if i == ';':
                            count += 1

                    if material not in result:
                        result.append(material)

                flag = True

        f.close()

    return result
