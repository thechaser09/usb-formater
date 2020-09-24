f = open("drive.txt", "w")
a = input("disk:");
a2 = input("volume:");
f.write(a)
f.close();
f = open("formating.txt", "w")
f.write("select volume " + a2 + "\nformat fs=ntfs quick")
f.close()




