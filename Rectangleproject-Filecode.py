import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("rectangle_area_calculator.log"),
        logging.StreamHandler()
    ]
)

def get_rectangle_input(rect_num: int) -> float:
    """
    Prompts the user for the dimensions (length and width) of a rectangle and calculates its area.

    Args:
        rect_num (int): The rectangle number (1 or 2) to differentiate between the inputs.

    Returns:
        float: The area of the rectangle.
    
    Raises:
        ValueError: If the user provides invalid input for length or width.
    """
    while True:
        try:
            length = float(input(f'Enter length for Rectangle_{rect_num}: '))
            width = float(input(f'Enter width for Rectangle_{rect_num}: '))

            if length <= 0 or width <= 0:
                raise ValueError("Length and width must be positive numbers.")

            area = length * width
            logging.info(f"Rectangle_{rect_num} area calculated: {area}")
            return area
        except ValueError as e:
            logging.error(f"Invalid input for Rectangle_{rect_num}: {e}")
            print(f"Please enter valid positive numbers for Rectangle_{rect_num}.")

def compare_areas(area_1: float, area_2: float):
    """
    Compares the areas of two rectangles and prints which one has the greatest area.

    Args:
        area_1 (float): The area of the first rectangle.
        area_2 (float): The area of the second rectangle.
    """
    if area_1 > area_2:
        print(f'Rectangle 1 has the greatest area at {area_1} square units.')
    elif area_2 > area_1:
        print(f'Rectangle 2 has the greatest area at {area_2} square units.')
    else:
        print(f'Both Rectangle 1 and Rectangle 2 have the same area of {area_1} square units.')

def main():
    """
    Main function to orchestrate the process of calculating and comparing rectangle areas.
    """
    try:
        area_1 = get_rectangle_input(1)
        area_2 = get_rectangle_input(2)

        compare_areas(area_1, area_2)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
