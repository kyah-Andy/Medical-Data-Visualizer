import unittest
import medical_data_visualizer
import matplotlib as mpl


class MedicalDataVisualizerTestCase(unittest.TestCase):

    def test_cat_plot(self):
        fig = medical_data_visualizer.draw_cat_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)

    def test_heat_map(self):
        fig = medical_data_visualizer.draw_heat_map()
        self.assertIsInstance(fig, mpl.figure.Figure)


if __name__ == "__main__":
    unittest.main()