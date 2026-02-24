from abc import ABC, abstractmethod
from typing import Any

# Parent Class
class DataProcessor(ABC):

	@abstractmethod
	def process(self, data: Any) -> str:
		pass

	@abstractmethod
	def validate(self, data: Any) -> bool:
		pass
	
	def format_output(self, result: str) -> str:
		return f"Output: {result}"


# Child Class inherit from the Parent
class NumericProcessor(DataProcessor):
	def __init__(self):
		print("Initializing Numeric Processor...")

	def validate(self, data: Any) -> bool:
		if isinstance(data, (int, float)):
			return True
		elif isinstance(data, str):
			return False
		else:	
			for d in data:
				if not isinstance(d, (int, float)):
					return False
			return True

	def process(self, data: Any) -> str:
		print(f"Processing data: {data}")
		if not self.validate(data):
			try:
				raise ValueError("Invalid Numeric Data")
			except Exception as err:
				return f"validation: {err}"
				
		else:
			print("Validation: Numeric data verified")
			if isinstance(data, (int, float)):
				data_list = [data]
			else:
				data_list = data
			n_len = len(data_list)
			n_sum = sum(data_list)
			n_avg = n_sum / n_len

		result = f"Processed {n_len} numeric values, sum={n_sum}, avg={n_avg}"
		return self.format_output(result)

	def format_output(self, result: str) -> str:
		return f"Output: {result}"


# Child Class inherit from the Parent
class TextProcessor(DataProcessor):
	def validate(self, data: Any) -> bool:
		pass

	def process(self, data: Any) -> str :
		pass

	def format_output(self, result: str) -> str:
		pass


# Child Class inherit from the Parent
class LogProcessor(DataProcessor):
	def validate(self, data: Any) -> bool:
		pass

	def process(self, data: Any) -> str :
		pass

	def format_output(self, result: str) -> str:
		pass

def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    
    numeric_processor = NumericProcessor()
    print(numeric_processor.process([1, 2, 3, 4, 5]))


if __name__ == "__main__":
	main()