from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):

	@abstractmethod
	def process(self, data: Any) -> str:
		pass

	@abstractmethod
	def validate(self, data: Any) -> bool:
		pass

	def format_output(self, result: str) -> str:
		return f"Output: {result}"






class NumericProcessor(DataProcessor):

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







class TextProcessor(DataProcessor):


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








class LogProcessor(DataProcessor):


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
    
    data = [
		[1, 2, 3, 4, 5],
		"Hello Nexus World",
		"ERROR: Connection timeout",
	]
    
    processors = [
		NumericProcessor(),
		TextProcessor(),
		LogProcessor(),
	]
    
    init_head = [
		"Initializing Numeric Processor...",
		"Initializing Text Processor...",
		"Initializing Log Processor...",
	]
    
    message = [
		"Validation: Numeric data verified",
		"Validation: Text data verified",
		"Validation: Log entry verified",
	]


    for i in range(len(processors)):
        print(init_head[i])
        print(f'Processing data: {data[i]}')
        try:
            output = processors[i].process(data[i])
            print(message[i])
            print(processors[i].format_output(output))
        except ValueError as err:
            print(f"Validation failed: {err}")
        
        print()

    

    print("\n=== Polymorphic Processing Demo ===\n")
    
    data_test = [
		[1, 2, 3],
		"hello world!",
		"info: System ready",
	]
    
    print("Processing multiple data types through same interface...")
    for i in range(len(processors)):
        print(f'Result {i+1}: {processors[i].process(data_test[i])}')
    
    print("\nFoundation systems online. Nexus ready for advanced streams.")

    


if __name__ == "__main__":
	main()