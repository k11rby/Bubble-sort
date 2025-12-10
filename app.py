import gradio as gr
import numpy as np

def bubbleSort(list_str):
    # Convert string to list
    list_str = list_str.strip('[]')
    numbers = [int(x.strip()) for x in list_str.split(',') if x.strip()]
    
    steps = []  # Store the current steps
    lenList = len(numbers)
    
    # Make a copy for step tracking
    current_step = numbers.copy()
    
    
    for i in range(lenList - 1):
        steps.append(f"\n Pass {i+1} through the list ")
        
        for j in range(0, lenList - i - 1):
            steps.append(f"  Compare {current_step[j]} and {current_step[j+1]}")
            
            if current_step[j] > current_step[j + 1]:
                # Swap
                current_step[j], current_step[j + 1] = current_step[j + 1], current_step[j]
                steps.append(f"  ✓ Since {current_step[j + 1]} is greater than {current_step[j]} These 2 are swapped \n: {current_step}")
            else:
                steps.append(f"  ✗ Since {current_step[j]} is less than {current_step[j + 1]} no swap is needed \n: {current_step}")
    
    steps.append(f"\nFinal sorted array: {current_step}")
    
    # Return all steps as a formatted string
    return "\n".join(steps)

def NumberGenerator():
    numbers = np.random.randint(1, 100, size=5)
    return str(numbers.tolist())

with gr.Blocks() as demo:
    gr.Markdown("# Bubble Sort Visualizer")
    gr.Markdown("Bubble sort works by comparing adjacent numbers; if the number to the right is less than the number to its left, the numbers will swap. The process keeps happening, bubbling the larger numbers to the end of the list until all the numbers are sorted")
    gr.Markdown("# Try it for yourself !")
    gr.Markdown("Generate an array or make your own")
    with gr.Row():
        generate_button = gr.Button("Generate Random Array", variant="primary")
        sort_button = gr.Button("Sort Array", variant="secondary")
    
    input_array = gr.Textbox(label="Initial array", lines=2)
    
    with gr.Row():
        output_steps = gr.Textbox(label="Sorting Steps", lines=20)
    
    # Connect buttons
    generate_button.click(fn=NumberGenerator, inputs=[], outputs=input_array)
    sort_button.click(fn=bubbleSort, inputs=input_array, outputs=output_steps)

demo.launch()
