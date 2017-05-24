#S.McDonald 11/8/2016
#sum_of_numbers
#show the contents of the file and compute the total

def main():
    try:
        #open the file numbers.txt
        #input
        #myfile is a file object
        myfile = open('numbers.txt', 'r') #open the file for reading

        #open the file for writing
        my_out_file = open('my_sum.txt', 'w')

        total = 0

        #compute total
        for line in myfile:
            total = total + int(line)
            print(line, end="")
            
        #write to an output file
        my_out_file.write(str(total) + '\n')

        #close both files
        myfile.close()
        my_out_file.close()
        
    except FileNotFoundError:
        print("ERROR: FILE DOES NOT EXIST! CHECK FILE LOCATION!")

    except PermissionError:
        print("ERROR: FILE CANNOT BE CREATED IN THIS DIRECTORY! CHOOSE A DIFFERENT ONE!")

    except:
        print("ERROR: AN ERROR HAS OCCURED!")

    else:
        print("\ntotal is: ", total)


#call the main function
main()
