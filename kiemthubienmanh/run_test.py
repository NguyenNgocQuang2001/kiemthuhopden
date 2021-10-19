import subprocess

for i in range(1, 26) :
	process = subprocess.Popen("pytest test" + str(i) + ".py", stdout = subprocess.PIPE)
	output = process.communicate()[0]
	result = output.decode()
	print("test case " + str(i) + ": ", end = " ")
	if result.find("passed") != -1 :
		print("PASSED !!!")
	else :
		pos = result.find("assert")
		while result[pos] != ' ' :
			pos += 1
		pos += 1
		a = ""
		b = ""
		while result[pos] != ' ' :
			a = a + result[pos]
			pos += 1
		pos += 4
		while result[pos] != '\n' :
			b = b + result[pos]
			pos += 1
		if a == "tong" :
			id = result.find("assert")
			pos = result.find("assert", id + 1)
			while result[pos] != ' ' :
				pos += 1
			pos += 1
			a = ""
			b = ""
			while result[pos] != ' ' :
				a = a + result[pos]
				pos += 1
			pos += 4
			while result[pos] != '\n' :
				b = b + result[pos]
				pos += 1
		print("Expected : " + b + ", Find : " + a + " => FAILED !!!")