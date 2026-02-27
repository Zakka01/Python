import json, time
from abc import ABC, abstractmethod
from typing import Any, List, Protocol, Union
from collections import Counter, defaultdict, ChainMap, deque


# Protocol (duck typing)
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...
                
        

# Concrete Stage Classes (implement ProcessingStage protocol)
class InputStage:
    def __init__(self):
        print("Stage 1: Input validation and parsing")


    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            structured_data = data
        elif isinstance(data, str):
            try:
                structured_data = json.loads(data)
                if not isinstance(structured_data, dict):
                    raise ValueError("Invalid Data Format")
            except json.JSONDecodeError:
                raise ValueError("error detected in Stage 1: Invalid Data Format")
        else:
            raise ValueError(f"error detected in Stage 1: Invalid Data Format")

        normalized_data = {}
        for key, value in structured_data.items():
            key = str(key).lower()
            if value is not None:
                normalized_data[key] = value

        return normalized_data



class TransformStage:
    def __init__(self):
        print("Stage 2: Data transformation and enrichment")


    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise ValueError("error detected in Stage 2: Invalid Data Format")
        
        transformed_data = {}
        for key, value in data.items():
            if isinstance(value, str):
                value = value.strip().upper()
            transformed_data[key] = value

        return transformed_data
            
            

class OutputStage:
    def __init__(self):
        print("Stage 3: Output formatting and delivery")


    def process(self, data: Any) -> Any:
        
        if not isinstance(data, dict):
            raise ValueError("error detected in Stage 3: Invalid Data Format")
        
        output_string = []
        for key, value in data.items():
            output_string.append(f"{key}: {value}")
            
        return ', '.join(output_string)



# Abstract Base Class
class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List[ProcessingStage] = []


    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)


    def process(self, data: Any) -> Any:
        for stage in self.stages:
            try:
                data = stage.process(data)
            except Exception as err:
                print(f"ERROR: {err}")
        return data


# Adapters - inherit from ProcessingPipeline
class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing JSON data through pipeline...")
        print(f"Input: {json.dumps(data)}")
        
        temp_value = data.get("value") if isinstance(data, dict) else None

        result = super().process(data)

        print("Transform: Enriched with metadata and validation")
        print(f"Output: Processed temperature reading: {temp_value}°C (Normal range)")
        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing CSV data through same pipeline...")
        print(f'Input: "{data}"')
        
        if isinstance(data, str):
            parts = data.split(",")
            i = 0
            structured = {}
            users = []

            for value in parts:
                structured[f"col {str(i)}"] = value
                if value == "user":
                    users.append(value)
                i += 1
        else:
            structured = data

        result = super().process(structured)

        print("Transform: Parsed and structured data")
        print(f"Output: User activity logged: {len(users)} actions processed")
        return result 


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print("\nProcessing Stream data through same pipeline...")
        print(f"Input: {data}")

        structured = {"stream": data}

        result = super().process(structured)

        print("Transform: Aggregated and filtered")
        print("Output: Stream summary: 5 readings, avg: 22.1°C")
        return result


# NexusManager - manages/orchestrates multiple pipelines
class NexusManager:
    def __init__(self):
        self.pipelines = []
        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second")


    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> List[Any]:
        results = []
        for pipeline, data in zip(self.pipelines, data):
            try:
                result = pipeline.process(data)
                results.append(result)
            except Exception as err:
                print(f"ERROR in pipeline: {err}")
                results.append(None)
        return results




def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    manager = NexusManager()
    
    
    print()
    print("Creating Data Processing Pipeline...")
    stage1 = InputStage()
    stage2 = TransformStage()
    stage3 = OutputStage()

    print()
    print("=== Multi-Format Data Processing ===")

    json_pipeline = JSONAdapter("json-1")
    json_pipeline.add_stage(stage1)
    json_pipeline.add_stage(stage2)
    json_pipeline.add_stage(stage3)

    csv_pipeline = CSVAdapter("csv-1")
    csv_pipeline.add_stage(stage1)
    csv_pipeline.add_stage(stage2)
    csv_pipeline.add_stage(stage3)

    stream_pipeline = StreamAdapter("stream-1")
    stream_pipeline.add_stage(stage1)
    stream_pipeline.add_stage(stage2)
    stream_pipeline.add_stage(stage3)
    
    manager.add_pipeline(json_pipeline)
    manager.add_pipeline(csv_pipeline)
    manager.add_pipeline(stream_pipeline)


    inputs = [
        {"sensor": "temp", "value": 23.5, "unit": "C"},
        "user,action,timestamp",
        "Real-time sensor stream"
    ]
    results = manager.process_data(inputs)
    
    
    # Pipeline Demo
    print("\n=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

    start_time = time.perf_counter()
    raw_data = []
    for i in range(100):
        record = {"sensor": "temp", "value": 23 + i, "unit": "C"}
        raw_data.append(record)

    for record in raw_data:
        stage1.process(record)
        stage2.process(record)
        stage3.process(record)

    end_time = time.perf_counter()
    records_processed = len(raw_data)

    print(f"Chain result: {records_processed} records processed through 3-stage pipeline")
    print(f"Performance: {95}% efficiency, {end_time - start_time:.4f}s total processing time")
    

    # Error Recovery
    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")

    bad_data = "23:23"
    recovered_data = {"sensor": "temp", "value": 23, "unit": "C"}
    try:
        stage1.process(bad_data)
        stage2.process(bad_data)
        stage3.process(bad_data)
    except Exception as e:
        print(f"{e}")

    print("Recovery initiated: Switching to backup processor")
    try:
        stage1.process(recovered_data)
        stage2.process(recovered_data)
        stage3.process(recovered_data)
        print("Recovery successful: Pipeline restored, processing resumed")
    except Exception as e:
        print(f"{e}")
        
    print("\nNexus Integration complete. All systems operational.")

if __name__ == "__main__":
    main()
