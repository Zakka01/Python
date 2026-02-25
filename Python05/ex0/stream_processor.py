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
		if not self.validate(data):
			raise ValueError("Invalid Numeric Data")
		else:
			if isinstance(data, (int, float)):
				data_list = [data]
			else:
				data_list = data
			n_len = len(data_list)
			n_sum = sum(data_list)
			n_avg = n_sum / n_len

		return f"Processed {n_len} numeric values, sum={n_sum}, avg={n_avg}"

	def format_output(self, result: str) -> str:
		return f"Output: {result}"


# Child Class inherit from the Parent
class TextProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Text Processor...")


    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, (list, tuple, set)):
            return all(isinstance(d, str) for d in data)
        return False


    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid Text Data")

        if isinstance(data, str):
            full_text = data
        else:
            full_text = " ".join(data)

        char_count = len(full_text)
        word_count = len(full_text.split())

        return f"Processed text: {char_count} characters, {word_count} words"


    def format_output(self, result: str) -> str:
        return f"Output: {result}"


# Child Class inherit from the Parent
class LogProcessor(DataProcessor):
	def __init__(self):
		print("Initializing Log Processor...")


	def validate(self, data: Any) -> bool:
		if not isinstance(data, str):
			return False
		if ":" not in data:
			return False
		return True


	def process(self, data: Any) -> str:
		if not self.validate(data):
			raise ValueError("Invalid Log Data")

		level, message = data.split(":", 1)
		level = level.strip().upper()
		message = message.strip()

		if level == "ERROR":
			result = f"[ALERT] {level} level detected: {message}"
		elif level == "WARNING":
			result = f"[WARNING] {level} level detected: {message}"
		elif level == "INFO":
			result = f"[INFO] {level} level detected: {message}"
		else:
			result = f"[UNKNOWN] {level} level detected: {message}"

		return result


	def format_output(self, result: str) -> str:
		return f"Output: {result}"



def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    
    num_data = [1, 2, 3, 4, 5]
    numeric_processor = NumericProcessor()
    print(f'Processing data: {num_data}')
    
    try:
        output = numeric_processor.process(num_data)
        print("Validation: Numeric data verified")
        print(numeric_processor.format_output(output))
    except ValueError as err:
        print(f"Validation failed: {err}")
    
    
    
    print()
    
    
    txt_data = "Hello Nexus World"
    text_processor = TextProcessor()
    print(f'Processing data: "{txt_data}"')
	
    try:
        output = text_processor.process(txt_data)
        print("Validation: Text data verified")
        print(text_processor.format_output(output))
    except ValueError as err:
        print(f"Validation failed: {err}")
        
    
    
    
    print()
    
    
    log_data = "ERROR: Connection timeout"
    log_processor = LogProcessor()
    print(f'Processing data: "{log_data}"')
    
    try:
        output = log_processor.process(log_data)
        print("Validation: Log entry verified")
        print(log_processor.format_output(output))
    except ValueError as err:
        print(f"Validation failed: {err}")

    
    print("\n=== Polymorphic Processing Demo ===\n")
    
    print("Processing multiple data types through same interface...")
    print(f'Result 1: {numeric_processor.process([1, 2, 3])}')
    print(f'Result 2: {text_processor.process("hello world")}')
    print(f'Result 3: {log_processor.process("info: System ready")}')
    
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")

    


if __name__ == "__main__":
	main()