# input_taker.py

import sys


def get_input(prompt: str, option: list) -> str:
    """A function for take input from user"""
    while True:
        try:
            user_input = input(f"{prompt}: ").strip()

            if not user_input:
                print("Input can't be empty! Please try again")
                continue

            if user_input not in option:
                print("Input not in option! Please try again!")
                continue

            return user_input
        except (KeyboardInterrupt, EOFError):
            print("\nSystem interrupted by user!")
            sys.exit(0)

        except Exception as e:
            print(f"\nError: {e}")
            sys.exit(0)

def get_temperature_input(prompt: str) -> float:
    """A function for take temperature input"""
    while True:
        try:
            user_input = input(f"{prompt}: ").strip()

            if not user_input:
                print("Input can't be empty! Please try again")
                continue
                
            user_input = float(user_input)
            
            return user_input
            
        except ValueError:
            print("Input is not a number! Please enter a valid number")
            continue 
            
        except (KeyboardInterrupt, EOFError):
            print("\nSystem interrupted by user!")
            sys.exit(0)

        except Exception as e:
            print(f"\nError: {e}")
            sys.exit(0)