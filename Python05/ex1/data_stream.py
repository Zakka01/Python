from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "total": 0
        }


class SensorStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"
        self.processed_count = 0
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {stream_id}, Type: {self.stream_type}")


    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing sensor batch: [{', '.join(data_batch)}]")

        filtered_data = self.filter_data(data_batch, "temp")
        temp_values = []

        # split get values and store them
        for data in filtered_data:
            try:
                value = data.split(":")[1]
                temp_values.append(float(value))
            except Exception as err:
                print(f"ERROR: {err}")
        
        # check if no value match the criteria
        if len(temp_values) == 0:
            raise ValueError("No valid temperature data")
        
        # do operations 
        avg_temp = sum(temp_values) / len(temp_values)
        
        # how many items this stream has processed
        self.processed_count += len(data_batch)

        result = (f"Sensor analysis: {self.processed_count} readings processed, "
                  f"avg temp: {avg_temp:.1f}°C")
        return result

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        
        filtered_data = []
        for data in data_batch:
            if isinstance(data, str) and data.startswith(f"{criteria}:"):
                filtered_data.append(data)
            
        return filtered_data
        

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.stream_type = "Financial Data"
        self.ops_count = 0
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing transaction batch: [{', '.join(data_batch)}]")

        filtered_data = self.filter_data(data_batch)
        buy_total = 0
        sell_total = 0

        for data in filtered_data:
            action, value = data.split(":")
            value = float(value)
            if action == "buy":
                buy_total += value
            elif action == "sell":
                sell_total += value
        net_flow = buy_total - sell_total

        self.ops_count += len(data_batch)

        result = (f"Transaction analysis: {self.ops_count} operations, net flow: {net_flow:+.0f} units")
        return result

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        filtered_data = []
        for data in data_batch:
            if isinstance(data, str):
                filtered_data.append(data)
        return filtered_data 

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.ops_count
        }


class EventStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id)
        self.stream_type = "System Events"
        self.events_count = 0
        print("Initializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: {self.stream_type}")
        

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing event batch: [{', '.join(data_batch)}]")
        
        filtered_data = self.filter_data(data_batch, "error")
        self.events_count += len(data_batch)

        result = (f"Event analysis: {self.events_count} events, {len(filtered_data)} error detected")
        return result


    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        
        filtered_data = []
        for data in data_batch:
            if isinstance(data, str) and data == criteria:
                filtered_data.append(data)
        return filtered_data


    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "events_count": self.events_count
        }


class StreamProcessor:
    def __init__(self):
        self.streams = []
        
    def process_batch(self, batch_data):
        print("Batch Results:")

        for i in range(len(self.streams)):
            stream = self.streams[i]
            data = batch_data[i]

            result = stream.process(data)
            return ("- " + result)

def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    
    # Sensor Stream
    sensor_data =  ["temp:22.5", "humidity:65", "pressure:1013"]
    try:
        sensor = SensorStream("SENSOR_001")
        print(sensor.process_batch(sensor_data))
    except Exception as e:
        print(f"ERROR : {e}")
        
        
    print()
    
    # Transaction Stream
    trans_data = ["buy:100", "sell:150", "buy:75"]
    try:
        trans = TransactionStream("TRANS_001")
        print(trans.process_batch(trans_data))
    except Exception as e:
        print(f"ERROR: {e}")
    
    
    print()

    # Events Stream
    events_data =  ["login", "error", "logout"]
    try:
        event = EventStream("EVENT_001")
        print(event.process_batch(events_data))
    except Exception as e:
        print(f"ERROR: {e}")
        
    
    print()
    print("=== Polymorphic Stream Processing ===")
    
    print("Processing mixed stream types through unified interface...\n")
    streams = [
        SensorStream("S001"),
        TransactionStream("T001"),
        EventStream("E001")
    ]
    
    batch_data = [
        ["temp:22", "humidity:60"],
        ["buy:100", "sell:50", "buy:30", "sell:10"],
        ["login", "logout", "error"]
    ]
    
    print(StreamProcessor())
    
    
    
if __name__ == "__main__":
    main()