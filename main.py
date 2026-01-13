import argparse
import sys
from src.workflow.execute_workflow import run_workflow

def main():
    parser = argparse.ArgumentParser(description="Medium Article Generator Agent")
    parser.add_argument("topic", nargs="?", help="The topic to research and write about")
    
    args = parser.parse_args()
    
    if not args.topic:
        print("Please provide a topic.")
        print("Usage: python main.py \"Your Topic Here\"")
        sys.exit(1)
        
    print(f"Starting research on: {args.topic}")
    run_workflow(args.topic)

if __name__ == "__main__":
    main()