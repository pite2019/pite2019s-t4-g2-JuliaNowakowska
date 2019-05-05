from matrix import Matrix
import time

def main():
	
	matrix1 = Matrix(2, 3)
	matrix1.add_elements()
	matrix1.show_elements()
	print("\n")
	
	matrix2 = Matrix(3, 2)
	matrix2.add_elements()
	matrix2.show_elements()
	print("\n")
	
	
	matrix3 = matrix1.addsub(matrix2)
	try:
		matrix3.show_elements()
		print("\n")
	except AttributeError:
		pass
		
	result = matrix1.multiplication(matrix2)
	try:
		print("Result of multiplication: ")
		result.show_elements()
		print("\n")
	except AttributeError:
		pass
		
	transposed = result.transpose()
	print("Result of transposition: ")
	transposed.show_elements()
	
	time.sleep(10)

if __name__ == "__main__":
	main()
