import unittest
import numpy as np
import torch
from torch.autograd import gradcheck
from src.torch_model import MyReLU


class ReluTest(unittest.TestCase):
    def setUp(self):
        self.relu = MyReLU.apply

    def test_relu_values_x_leqz(self):
        tin_leqz = torch.linspace(-10, 0, 300)
        tout_leqz = list(self.relu(tin_leqz))

        for x in tout_leqz:
            self.assertEqual(x, 0)

    def test_relu_values_x0(self):
        tin_eqz = torch.zeros(5, dtype=torch.long)
        tout_eqz = list(self.relu(tin_eqz))

        for x in tout_eqz:
            self.assertEqual(x, 0)

    def test_relu_values_x_geqz(self):
        tin_geqz = torch.tensor(np.linspace(0.001, 10, 300))
        tout_geqz = list(self.relu(tin_geqz))
        test_geqz = list(tin_geqz)

        for ii in range(len(tout_geqz)):
            self.assertEqual(tout_geqz[ii], test_geqz[ii])

    def test_drelu_values(self):
        tin = torch.randn(20, 20, dtype=torch.double, requires_grad=True)

        self.assertTrue(gradcheck(self.relu, tin, eps=1e-6, atol=1e-4))


if __name__ == "__main__":
    unittest.main(verbosity=2)
