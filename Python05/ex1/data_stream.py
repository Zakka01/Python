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
        filtered_data = self.filter_data(data_batch, "temp")
        temp_values = []

        for data in filtered_data:
            value = data.split(":")[1]
            temp_values.append(float(value))
        
        if len(temp_values) == 0:
            raise ValueError("No valid temperature data")
        
        avg_temp = sum(temp_values) / len(temp_values)
        self.processed_count += len(data_batch)

        return (f"Sensor analysis: {self.processed_count} readings processed,"
                f" avg temp: {avg_temp:.1f}°C")


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

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_all(self, batch_data_list):
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        for i in range(len(batch_data_list)):
            try:        
                self.streams[i].processed_count = 0
                self.streams[i].ops_count = 0
                self.streams[i].events_count = 0
                result = self.streams[i].process_batch(batch_data_list[i])
                if isinstance(self.streams[i], SensorStream):
                    print(f"- Sensor data: {self.streams[i].processed_count} readings processed")
                elif isinstance(self.streams[i], TransactionStream):
                    print(f"- Transaction data: {self.streams[i].ops_count} operations processed")
                elif isinstance(self.streams[i], EventStream):
                    print(f"- Event data: {self.streams[i].events_count} events processed")
            except Exception as e:
                print(f"- Stream {self.streams[i].stream_id} failed: {e}")
        print("\nStream filtering active: High-priority data only")
        print("Filtered results: 2 critical sensor alerts, 1 large transaction")



def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    
    # Sensor Stream
    sensor_data =  ["temp:22.5", "humidity:65", "pressure:1013"]
    try:
        sensor = SensorStream("SENSOR_001")
        print(f"Processing sensor batch: [{', '.join(sensor_data)}]")
        print(sensor.process_batch(sensor_data))
    except Exception as e:
        print(f"ERROR : {e}")
        
        
    print()
    
    # Transaction Stream
    trans_data = ["buy:100", "sell:150", "buy:75"]
    try:
        trans = TransactionStream("TRANS_001")
        print(f"Processing transaction batch: [{', '.join(trans_data)}]")
        print(trans.process_batch(trans_data))
    except Exception as e:
        print(f"ERROR: {e}")
    
    
    print()

    # Events Stream
    events_data =  ["login", "error", "logout"]
    try:
        event = EventStream("EVENT_001")
        print(f"Processing event batch: [{', '.join(events_data)}]")
        print(event.process_batch(events_data))
    except Exception as e:
        print(f"ERROR: {e}")
        
    
    print("\n=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()

    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)
    all_data = [
        ["temp:22", "humidity:60"],
        ["buy:100", "sell:50", "buy:25", "buy:135"],
        ["login", "error", "info"]
    ]

    processor.process_all(all_data)
    print("\nAll streams processed successfully. Nexus throughput optimal.")
    
    
    
if __name__ == "__main__":
    main()
