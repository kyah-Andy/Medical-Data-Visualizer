import medical_data_visualizer
from unittest import main

# Run unit tests automatically
main(module='test_module', exit=False)

# Run and generate plots (optional)
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()