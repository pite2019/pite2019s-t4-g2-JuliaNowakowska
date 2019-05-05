class Matrix:
	def __init__ (self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.matrix = self.blank_matrix()
	
	def blank_matrix(self):
		matrix = []
		for x in range(self.rows):
			matrix.append([])
		return matrix
		
	def add_elements(self):
		for x in range (self.rows):
			for y in range(self.columns):
				element = int(input("Input element to the matrice.\t"))
				self.matrix[x].append(element)
				
	def show_elements(self):
		for element in self.matrix:
			print(element)
	
	def addsub(self, class2):
		choice = input("Type A for addition and S for substraction\t")
		if (self.rows == class2.rows and self.columns == class2.columns):
			class3 = Matrix(self.rows, self.columns)
			for x in range(self.rows):
				for y in range(self.columns):
					if (choice.upper() == 'A'):
						element = self.matrix[x][y] + class2.matrix[x][y]
					elif (choice.upper() == 'S'):
						element = self.matrix[x][y] - class2.matrix[x][y]
					else:
						break
					class3.matrix[x].append(element)
			return class3
		else:
			print("Error!\n")
	
	def multMatNumb(self, number):
		for y in range(self.rows):
			for x in range(self.columns):
				self.matrix[x][y] *= number

	def multiplication(self, class2):
		if(self.columns == class2.rows):
			result = Matrix(self.rows, class2.columns)
			for y in range(self.rows):
				for x in range(class2.columns):
					val = 0
					for i in range(class2.rows):
							val += self.matrix[y][i] * class2.matrix[i][x]
					result.matrix[y].append(val)
			return result
		else:
			print("Error!\n")
			
	def transpose(self):
		transposed = Matrix(self.columns, self.rows)
		for x in range(transposed.rows):
			for y in range(transposed.columns):
				transposed.matrix[y].append(self.matrix[x][y])
		return transposed
			
